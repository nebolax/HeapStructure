class Heap:

    def __init__(self, shuffled_list: list = []):
        '''
            Takes shuffled list as an argument
            and performs permutations to create heap from this list

            Warning! All indexes must be non-negative!
            And check on emptiness by yourself before operations!
        '''
        self._data = shuffled_list
        for i in range(len(self._data)-1, -1, -1):
            self._sift_down(i)

    def _sift_down(self, el_ind: int):
        '''
            Finds the passed element's location in the heap
            and sifts it down to the leaves until the element's
            relative position to his parent and children becomes corect
        '''
        n = len(self._data)
        while True:
            variant, child_1, child_2 = el_ind, el_ind*2 + 1, el_ind*2 + 2

            if child_1 < n and self._data[child_1] > self._data[variant]:
                variant = child_1
            if child_2 < n and self._data[child_2] > self._data[variant]:
                variant = child_2

            if variant == el_ind:
                break
            self._data[variant], self._data[el_ind] = self._data[el_ind], self._data[variant]
            el_ind = variant

    def _sift_up(self, el_ind: int):
        '''
            Finds the passed element's location in the heap
            and sifts it up to the root until the element's
            relative position to his parent and children becomes corect
        '''
        while True:
            if el_ind == 0:
                break

            parent_ind = (el_ind-1) // 2

            if self._data[parent_ind] >= self._data[el_ind]:
                break

            self._data[el_ind], self._data[parent_ind] = self._data[parent_ind], self._data[el_ind]
            el_ind = parent_ind

    def get_max(self, pop=False):
        '''
            Pops (uses pop_el function) current maximum (root) of the heap
        '''
        if pop:
            return self.pop_el(0)
        else:
            return self._data[0]

    def pop_el(self, el_ind: int):
        '''
            Removes the desired element from the heap and returns it
            In fact, replaces the el_ind element with the last leaf (to keep good structure)
            and then for the new value in this node calls sift_up or sift_down
            (depending on whether this element is bigger than it's parent or not)
            At the end returns the initial value of the node
        '''
        if el_ind == len(self._data)-1:
            return self._data.pop()

        original_value = self._data[el_ind]
        self._data[el_ind] = self._data.pop()
        if self._data[el_ind] > original_value:
            self._sift_up(el_ind)
        else:
            self._sift_down(el_ind)

        return original_value

    def add_el(self, new_el: int):
        '''
            Adds this element of the heap keeping structure optimal
            In fact, append element to the first free leaf
            and calls sift_up for this element
        '''
        self._data.append(new_el)
        self._sift_up(len(self._data)-1)

    def isEmpty(self):
        return len(self._data) == 0
