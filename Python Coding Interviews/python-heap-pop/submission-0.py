import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    l = []
    for _ in range(len(heap)):
        h = heapq.heappop(heap)
        l.append(h)
    return l


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
