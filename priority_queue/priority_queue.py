import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove_min(self):
        return heapq.heappop(self._queue)[-1]

    def decrease_prio(self, item, priority):
        for i, (p, _, it) in enumerate(self._queue):
            if it == item:
                self._queue[i] = (priority, self._index, item)
                self._index += 1
                heapq.heapify(self._queue)
                break

    def empty(self):
        return not self._queue

    def min_prio(self):
        return self._queue[0][0]
