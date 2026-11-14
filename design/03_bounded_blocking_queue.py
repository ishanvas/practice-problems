"""LeetCode 1188. Design Bounded Blocking Queue (Medium) - Concurrency (Condition / Semaphore)
https://leetcode.com/problems/design-bounded-blocking-queue/

Build a thread-safe FIFO queue with a fixed capacity.

  enqueue(element)  add element at the back. If the queue is full, wait
                    until there is room.
  dequeue()         remove and return the front element. If the queue is
                    empty, wait until there is one.
  size()            return how many elements are in the queue.

Several producer and consumer threads call it at the same time. Use the
threading module (Lock + Condition, or Semaphores). Don't busy-wait.

Constraints: 1 <= capacity <= 30, 1 <= threads <= 8.

Testing note: each case runs one scenario. A result of "TIMEOUT" means a
thread was still stuck after 2 seconds, so something waited forever.
"""

import threading
import time

from testkit import run


class BoundedBlockingQueue:

    def __init__(self, capacity: int):
        # TODO: your code here
        pass

    def enqueue(self, element: int) -> None:
        raise NotImplementedError

    def dequeue(self) -> int:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError


def _start(fn):
    t = threading.Thread(target=fn, daemon=True)
    t.start()
    return t


def _finished(threads, timeout=2.0):
    end = time.time() + timeout
    for t in threads:
        t.join(max(0.0, end - time.time()))
    return not any(t.is_alive() for t in threads)


def scenario(name: str):
    if name == "single thread":
        q = BoundedBlockingQueue(2)
        q.enqueue(1)
        q.enqueue(2)
        return [q.size(), q.dequeue(), q.dequeue(), q.size()]

    if name == "dequeue waits":
        q, got = BoundedBlockingQueue(1), []
        t = _start(lambda: got.append(q.dequeue()))
        time.sleep(0.2)
        waiting = t.is_alive()
        q.enqueue(7)
        return [waiting, got] if _finished([t]) else "TIMEOUT"

    if name == "enqueue waits":
        q = BoundedBlockingQueue(1)
        q.enqueue(1)
        t = _start(lambda: q.enqueue(2))
        time.sleep(0.2)
        waiting, size_when_full = t.is_alive(), q.size()
        first = q.dequeue()
        if not _finished([t]):
            return "TIMEOUT"
        return [waiting, size_when_full, first, q.dequeue()]

    if name == "fifo order":
        q, got = BoundedBlockingQueue(2), []
        producer = _start(lambda: [q.enqueue(i) for i in range(200)])
        consumer = _start(lambda: [got.append(q.dequeue()) for _ in range(200)])
        return got == list(range(200)) if _finished([producer, consumer]) else "TIMEOUT"

    if name == "many threads":
        q, got, lock = BoundedBlockingQueue(3), [], threading.Lock()
        over_capacity = []

        def produce(start):
            for i in range(start, start + 250):
                q.enqueue(i)
                if q.size() > 3:
                    over_capacity.append(True)

        def consume():
            for _ in range(250):
                x = q.dequeue()
                with lock:
                    got.append(x)

        threads = [_start(lambda s=s: produce(s)) for s in range(0, 1000, 250)]
        threads += [_start(consume) for _ in range(4)]
        if not _finished(threads, timeout=5.0):
            return "TIMEOUT"
        return [sorted(got) == list(range(1000)), not over_capacity, q.size()]

    raise ValueError(name)


if __name__ == "__main__":
    run(scenario, [
        (("single thread",), [2, 1, 2, 0], "basic FIFO with size()"),
        (("dequeue waits",), [True, [7]], "dequeue on empty waits for an enqueue"),
        (("enqueue waits",), [True, 1, 1, 2], "enqueue on full waits for a dequeue"),
        (("fifo order",), True, "one producer + one consumer keeps order"),
        (("many threads",), [True, True, 0], "4 producers + 4 consumers: nothing lost, never over capacity"),
    ])
