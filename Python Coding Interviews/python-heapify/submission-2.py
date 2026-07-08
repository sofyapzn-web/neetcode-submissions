import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    h =[]
    heapq.heapify(strings)
    while strings :
        h.append(heapq.heappop(strings))


def heapify_integers(integers: List[int]) -> List[int]:
    l = []
    heapq.heapify(integers)
    while integers :
        l.append(heapq.heappop(integers))
    
def heap_sort(nums: List[int]) -> List[int]:
    h = []
    heapq.heapify(nums)
    



# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
