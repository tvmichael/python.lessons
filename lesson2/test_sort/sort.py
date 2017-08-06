# sort list

# функція сортування числового списку
#1
def my_sort_v1(slist):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist)-1):
            if slist[i] > slist[i+1]:
                slist[i], slist[i+1] = slist[i+1], slist[i]
                was_swap = True
    return slist

#2
#https://ru.wikibooks.org/wiki/%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8_%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0/%D0%91%D1%8B%D1%81%D1%82%D1%80%D0%B0%D1%8F#Python
def my_sort_v2(slist):
    if len(slist) <= 1:
        return  slist
    base_elem = slist[0]
    less_then = [elem for elem in slist if elem <  base_elem]
    large_then = [elem for elem in slist if elem > base_elem]
    return my_sort_v2(less_then) + [base_elem] + my_sort_v2(large_then)

#3
def my_sort(slist):
    return sorted(slist)

# TEST --------------------------------
# підключаємо бібліотеку для тестування
import unittest

# створюємо тестуючий клас
class MyListTest(unittest.TestCase):
    def test_normal(self):
        res = my_sort([4, 5, 9, 1, 6, 8, 2, 8, 4])
        self.assertEqual(res, [1, 2, 4, 4, 5, 6, 8, 8, 9])

    def test_single(self):
        res = my_sort([7])
        self.assertEqual(res, [7])

    def test_empty(self):
        res = my_sort([])
        self.assertEqual(res, [])

    def test_negative(self):
        res = my_sort([4, -5, 9, 1, 6, -8, 2, 4])
        self.assertEqual(res, [-8, -5, 1, 2, 4, 4, 6, 9])

    def test_abc(self):
        res = my_sort(['e', 'l', 'c', 'r', 'a', 'b'])
        self.assertEqual(res, ['a', 'b', 'c', 'e', 'l', 'r'])


# якщо запускаємося з консолі
if __name__ == '__main__':
    unittest.main()

#print(my_sort([4, 5, 9, 1, 6, 8, 2, 8, 4]))
#print(my_sort([7]))
#print(my_sort([]))
#print(my_sort([4, -5, 9, 1, 6, -8, 2, 4]))