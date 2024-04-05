import types


class FlatIterator:

    def __init__(self, list_of_list):

        self.list_of_list = list_of_list

    def __iter__(self):

        self.list_num = 0

        self.num_in_list = -1
        return self

    def __next__(self):

        self.num_in_list += 1

        if self.num_in_list == len(self.list_of_list[self.list_num]):

            self.list_num += 1

            self.num_in_list = 0

            if self.list_num == len(self.list_of_list):
                raise StopIteration

        item = self.list_of_list[self.list_num][self.num_in_list]
        return item


def test_1(lists):

    list_of_lists_1 = lists
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



def flat_generator(list_of_lists):

    for list_in_list in list_of_lists:

        for data_in_list in list_in_list:

            yield data_in_list



def test_2(lists):

    list_of_lists_1 = lists
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':


    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(f'Вызываем итератор ********************************')
    for item in FlatIterator(list_of_lists_1):
        print(item)


    print()
    flat_list_iter = [item for item in FlatIterator(list_of_lists_1)]
    print('list comprehension  по итератору *****************')
    print(flat_list_iter)


    test_1(list_of_lists_1)
    print()


    print(f'Вызываем генератор ********************************')
    for item in flat_generator(list_of_lists_1):
        print(item)


    print()
    flat_list_gen = [x for x in flat_generator(list_of_lists_1)]
    print('list comprehension  по генератору *****************')
    print(flat_list_gen)


    test_2(list_of_lists_1)
