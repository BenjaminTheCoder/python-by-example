
"""Collatz conjecture / 3n+1 problem."""

from more_itertools import iterate, before_and_after, take

def is_even(x: int) -> bool:
    return x % 2 == 0

def collatz(n: int) -> list[int]:
    assert n > 0, 'n must be a positive integer'
    before, after = before_and_after(
        lambda x: x > 1, 
        iterate(lambda x: x // 2 if is_even(x) else x * 3 + 1, n))
    return list(before) + list(take(1, after))

print(collatz(11))
# [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]



