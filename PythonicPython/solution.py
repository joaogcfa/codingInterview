from typing import List, Set, Dict, Tuple


def print_indices_and_elements(elements) -> None:
    for index, values in enumerate(elements):
        print(index, values)


def get_even_numbers_between(start: int, end: int) -> List[int]:
    lista = [e for e in range(start, end+1) if e % 2 == 0]
    return lista


def get_char_set_from(s: str) -> Set[str]:
    sete = {char for char in s if s.isalpha()}
    return sete


def get_perfect_squares_between(start: int, end: int) -> Dict[int, int]:
    dic = {num: num**(1/2)
           for num in range(start, end + 1) if num**(1/2) % 1 == 0}
    return dic


def filter_even_from(numbers: List[int]) -> List[int]:
    lista = [e for e in numbers if e % 2 == 0]
    return lista


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1


def transform_multiples_of_5(numbers: List[int]) -> List[int]:
    return [n if n % 2 == 0 else -1 for n in numbers if n % 5 == 0]


def str_lengths(strings: List[str]) -> List[int]:
    return [len(string) for string in strings]


def get_fibonacci_type(version: int) -> str:
    if version == 1:
        return "<class 'generator'>"
    elif version == 2:
        return "<class 'list'>"


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return 'Generator functions are a special kind of function that return a lazy iterator. This lazy iterator is the main difference from a generator to a normal funcition, since a normal function that would return a list would return all the values at once, while a generator function would return one value at a time, and only when it is needed. Moreover, a generator function can be used to create an infinite sequence of values, while a normal function would return a list with a finite number of values, since lazy iterators are not stored in memory.'


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        # You can add more code here if you need


def my_avg(e1: float, e2: float, *others: Tuple[float]) -> float:
    return -1


def keys_with_different_value() -> List[int]:
    return []


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        # You should add code here and remove the break
        break

    if numbers:
        # You should add code here
        pass


def append_range(start: int, end: int, step: int = 1, to: List[int] = []):
    # You may add code here

    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10


def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value == None


print(get_even_numbers_between(1, 6))
