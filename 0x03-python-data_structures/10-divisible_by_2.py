#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    return [x % 2 == 0 for x in my_list]
