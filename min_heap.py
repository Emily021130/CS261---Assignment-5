# Name: Shuyao Zeng
# OSU Email: zengs@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5
# Due Date: 08/07/2023
# Description:


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """
        self._heap.append(node)
        child_index = self._heap.length() - 1
        parent_index = (child_index - 1) // 2
        while child_index > 0:
            if self._heap[child_index] < self._heap[parent_index]:
                parent_node = self._heap[parent_index]
                child_node = self._heap[child_index]
                self._heap.set_at_index(child_index, parent_node)
                self._heap.set_at_index(parent_index, child_node)
                child_index = parent_index
                parent_index = (child_index - 1) // 2
            else:
                break

    def is_empty(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self._heap.is_empty() is True:
            return True
        else:
            return False

    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self._heap.is_empty() is True:
            raise MinHeapException
        else:
            return self._heap[0]

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self._heap.is_empty() is True:
            raise MinHeapException
        min_value = self._heap[0]
        self._heap.set_at_index(0, self._heap[self._heap.length() - 1])
        self._heap.remove_at_index(self._heap.length() - 1)
        _percolate_down(self._heap, 0)
        return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        new_heap = DynamicArray()
        for index in range(da.length()):
            value = da[index]
            new_heap.append(value)
        self._heap = new_heap
        parent = da.length() // 2 - 1
        while parent >= 0:
            _percolate_down(self._heap, parent)
            parent -= 1

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        self._heap = DynamicArray()

def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    heap = MinHeap()
    heap.build_heap(da)
    parent = da.length() // 2 - 1
    last = da.length() - 1
    for index in range(parent, -1, -1):
        _percolate_down(da, parent)
    while last > 0:
        parent_node = da[0]
        da[0] = da[last]
        da[last] = parent_node
        _percolate_down(da, 0)
        last -= 1


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    left_child = parent * 2 + 1
    right_child = parent * 2 + 2
    min_child = parent
    if left_child <= da.length() - 1 and da[left_child] < da[min_child]:
        min_child = left_child
    if right_child <= da.length() - 1 and da[right_child] < da[min_child]:
        min_child = right_child
    if min_child != parent:
        temp = da[parent]
        da[parent] = da[min_child]
        da[min_child] = temp
        _percolate_down(da, min_child)

def _percolate_down_2(da: DynamicArray, parent: int, last) -> None:
    """
    TODO: Write your implementation
    """
    left_child = parent * 2 + 1
    right_child = parent * 2 + 2
    min_child = parent
    if left_child <= last and da[left_child] < da[min_child]:
        min_child = left_child
    if right_child <= last and da[right_child] < da[min_child]:
        min_child = right_child
    if min_child != parent:
        temp = da[parent]
        da[parent] = da[min_child]
        da[min_child] = temp
        _percolate_down_2(da, min_child, last)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
