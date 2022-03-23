from heap import Heap


class TestHeap:
    def test_sift_down_1(self):
        heap = Heap()
        heap._data = [4, 3, 3]
        heap._sift_down(0)
        assert heap._data == [4, 3, 3]

    def test_sift_down_2(self):
        heap = Heap()
        heap._data = [2, 3, 4]
        heap._sift_down(0)
        assert heap._data == [4, 3, 2]

    def test_sift_down_3(self):
        heap = Heap()
        heap._data = [10, 2, 8, 4, 5, 0]
        heap._sift_down(1)
        assert heap._data == [10, 5, 8, 4, 2, 0]

    def test_sift_down_4(self):
        heap = Heap()
        heap._data = [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
        heap._sift_down(0)
        assert heap._data == [10, 8, 9, 4, 7, 6, 5, 0, 3, 2, 1, 0, -1]

    def test_sift_down_5(self):
        heap = Heap()
        heap._data = [20, 1, 10, 9, 8, 7, 6, 4, 5, 3, 2]
        heap._sift_down(1)
        assert heap._data == [20, 9, 10, 5, 8, 7, 6, 4, 1, 3, 2]

    def test_sift_up_1(self):
        heap = Heap()
        heap._data = [3, 2, 4]
        heap._sift_up(2)
        assert heap._data == [4, 2, 3]

    def test_sift_up_2(self):
        heap = Heap()
        heap._data = [4, 5, 2]
        heap._sift_up(0)
        assert heap._data == [4, 5, 2]

    def test_sift_up_3(self):
        heap = Heap()
        heap._data = [4, 5, 2]
        heap._sift_up(2)
        assert heap._data == [4, 5, 2]

    def test_sift_up_4(self):
        heap = Heap()
        heap._data = [5, 4, 3, 2, 1, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8]
        heap._sift_up(5)
        assert heap._data == [10, 4, 5, 2, 1, 3,
                              0, -1, -2, -3, -4, -5, -6, -7, -8]

    def test_sift_up_5(self):
        heap = Heap()
        heap._data = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10]
        heap._sift_up(10)
        assert heap._data == [10, 9, 7, 6, 8, 4, 3, 2, 1, 0, 5]

    def test_add_el_1(self):
        heap = Heap()
        heap._data = [3, 2, 1]
        heap.add_el(0)
        assert heap._data == [3, 2, 1, 0]

    def test_add_el_2(self):
        heap = Heap()
        heap._data = [3, 2, 1]
        heap.add_el(4)
        assert heap._data == [4, 3, 1, 2]

    def test_add_el_3(self):
        heap = Heap()
        heap._data = [5, 3, 2, 1]
        heap.add_el(4)
        assert heap._data == [5, 4, 2, 1, 3]

    def test_add_el_4(self):
        heap = Heap()
        heap._data = [8, 7, 5, 4, 3, 2]
        heap.add_el(6)
        assert heap._data == [8, 7, 6, 4, 3, 2, 5]

    def test_add_el_5(self):
        heap = Heap()
        heap._data = [8, 5, 7, 4, 3, 2, 1]
        heap.add_el(6)
        assert heap._data == [8, 6, 7, 5, 3, 2, 1, 4]

    def test_pop_el_1(self):
        heap = Heap()
        heap._data = [4, 3, 2, 1]
        heap.pop_el(0)
        assert heap._data == [3, 1, 2]

    def test_pop_el_2(self):
        heap = Heap()
        heap._data = [4, 3, 2, 1]
        heap.pop_el(1)
        assert heap._data == [4, 1, 2]

    def test_pop_el_3(self):
        heap = Heap()
        heap._data = [-1, -2, -3, -4]
        heap.pop_el(3)
        assert heap._data == [-1, -2, -3]

    def test_pop_el_4(self):
        heap = Heap()
        heap._data = [8, 7, 6, 5, 4, 3, 2]
        heap.pop_el(1)
        assert heap._data == [8, 5, 6, 2, 4, 3]

    def test_pop_el_5(self):
        heap = Heap()
        heap._data = list(range(20, 2, -1))
        heap.pop_el(2)
        assert heap._data == [20, 19, 15, 17, 16, 9,
                              14, 13, 12, 11, 10, 3, 8, 7, 6, 5, 4]

    def test_pop_el_6(self):
        heap = Heap()
        heap._data = [20, 19, 11, 18, 17, 10,
                      9, 16, 15, 14, 13, 8, 7, 6, 5, 12]
        heap.pop_el(len(heap._data)-2)
        assert heap._data == [20, 19, 12, 18, 17,
                              10, 11, 16, 15, 14, 13, 8, 7, 6, 9]

    def test_get_max_1(self):
        heap = Heap()
        heap._data = [4, 3, 2, 1]
        m = heap.get_max()
        assert m == 4
        assert heap._data == [4, 3, 2, 1]

    def test_get_max_2(self):
        heap = Heap()
        heap._data = [5, 3, 2, 1]
        m = heap.get_max(True)
        assert m == 5
        assert heap._data == [3, 1, 2]

    def check_heap_validity(self, heap: Heap):
        for i in range(len(heap._data)):
            child_1, child_2 = i*2+1, i*2+2
            if child_1 < len(heap._data) and heap._data[child_1] > heap._data[i]:
                return False
            if child_2 < len(heap._data) and heap._data[child_2] > heap._data[i]:
                return False
        return True

    def test_chek_heap_1(self):
        heap = Heap()
        heap._data = [2, 3, 1]
        assert self.check_heap_validity(heap) == False

    def test_create_heap_1(self):
        heap = Heap([3, 4, 5])
        assert self.check_heap_validity(heap)

    def test_create_heap_2(self):
        heap = Heap([1, 3, 2])
        assert self.check_heap_validity(heap)

    def test_create_heap_3(self):
        heap = Heap([3, 2, 1, 4, 7, 5])
        assert self.check_heap_validity(heap)

    def test_create_heap_4(self):
        heap = Heap([9, 8, 10, 1, 23, 7, 15])
        assert self.check_heap_validity(heap)
