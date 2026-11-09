from bisect import bisect
import random

def bsearch(arr, target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = left + (right -left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def check(arr, target): 
    i = bisect(arr, target)
    if i > 0 and arr[i-1] == target:
        return i - 1
    return -1

arr = sorted(random.sample(range(1, 100), 10))
target = random.randint(1, 100)
result = bsearch(arr, target)
if result != -1:
    print(f"array: {arr}\ntarget: {target}\nElement found at index: {result}")
else:
    print(f"array: {arr}\ntarget: {target}\nElement not found in the array.")
if result == check(arr, target):
    print("The result is correct.")
else:
    print("The result is incorrect.")
