import pytest
from python.queue import Queue


def test_enqueue_dequeue():
    q = Queue()
    # Dequeuing empty queue returns None
    assert q.dequeue() is None

    # Enqueue elements
    q.enqueue(1)
    q.enqueue(2)
    assert q.top.value == 1
    assert q.last.value == 2

    # Dequeue first element
    assert q.dequeue() == 1
    assert q.top.value == 2
    assert q.last.value == 2

    # Enqueue another element and continue dequeue
    q.enqueue(3)
    assert q.last.value == 3
    assert q.dequeue() == 2
    assert q.dequeue() == 3

    # Queue should now be empty
    assert q.dequeue() is None
    assert q.top is None
