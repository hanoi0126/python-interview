
from typing import List


def order_even_first_odd_last_v1(numbers: List[int]) -> None:
    even_list, odd_list = [], []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    numbers[:] = even_list + odd_list


def order_even_first_odd_last_v2(numbers: List[int]) -> None:
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7]
    order_even_first_odd_last_v2(numbers)
    print(numbers)