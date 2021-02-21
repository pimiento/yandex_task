#!/usr/bin/env python3

# 1.
def left_anti(a: list, b: list) -> list:
    sa = set(a) # O(N_alogN_a)
    sb = set(b) # O(N_blogN_b)
    result = list(sa - sb) # O(N_a)
    return result # O((N_a+N_b)log(N_a+N_b)) -> O(NlogN)

assert left_anti([1, 2, 3, None], [None]) == [1, 2, 3]
assert left_anti([], [1, 2, 3]) == []


# 2.

def remove_zeroes(arr: list) -> list:
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    return arr[:count]

assert remove_zeroes([1, 0, 2, 4, 0, 6]) == [1, 2, 4, 6]
assert remove_zeroes([0]) == []
assert remove_zeroes([1, 2, 3]) == [1, 2, 3]
assert remove_zeroes([]) == []
assert remove_zeroes([None, 0, 0.0]) == [None]
