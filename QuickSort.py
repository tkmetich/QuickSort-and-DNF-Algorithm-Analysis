import random
from timeit import default_timer as timer
import tracemalloc


def LomutoPartition(A, l, r):
    p = A[l] 
    s = l 
    for i in range(l + 1, r + 1): 
        if A[i] < p:
            s = s + 1
            A[s], A[i] = A[i], A[s]
    A[l], A[s] = A[s], A[l]
    return s

def Quicksort(A, l, r):
    if l < r:
        s = LomutoPartition(A, l, r)
        Quicksort(A, l, s - 1)
        Quicksort(A, s + 1, r)

def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

def quickselect(arr, k, l=0, r=None):
    if r is None:
        r = len(arr) - 1

    if l == r:
        return arr[l]

    s = lomuto_partition(arr, l, r)

    if s == k - 1:
        return arr[s]
    elif s > l + k - 1:
        return quickselect(arr, k, l, s - 1)
    else:
        return quickselect(arr, k - 1 - s, s + 1, r)

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


# Example usage:
# Worst Case
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
    30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
    57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
    85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

#Average Case
B = [57, 55, 76, 76, 45, 50, 87, 1, 17, 36, 68, 39, 40, 45, 88, 15, 92, 31, 42, 0, 34, 39, 29, 98, 52, 5, 80, 5, 15,
    9, 42, 99, 84, 59, 72, 57, 60, 89, 79, 86, 20, 79, 21, 5, 80, 85, 50, 53, 86, 21, 30, 85, 34, 65, 80, 48, 18, 
    34, 62, 3, 100, 56, 59, 7, 71, 88, 44, 18, 26, 64, 61, 52, 6, 65, 41, 53, 43, 67, 48, 4, 69, 44, 80, 33, 3, 98, 
    85, 97, 8, 14, 19, 77, 61, 92, 76, 23, 71, 73, 87, 38] 

#Best Case
C = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93, 1, 7, 13, 19, 26, 32, 38, 44, 51, 57, 63, 69, 76, 82,
    88, 94, 3, 5, 9, 11, 15, 17, 21, 23, 27, 29, 33, 35, 39, 41, 45, 47, 53, 55, 59, 61, 65, 67, 71, 73, 77, 79, 83,
    85, 89, 91, 95, 97, 99, 2, 4, 8, 10, 14, 16, 20, 22, 28, 30, 34, 36, 40, 42, 48, 49, 54, 58, 60, 64, 66, 72, 74,
    78, 80, 86, 92, 96, 98, 100]

# Best Case
D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# Average Case
E = [1, 1, 2, 0, 0, 1, 2, 2, 0, 0, 0, 2, 2, 1, 1, 2, 2, 0, 1, 1, 0, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 2, 1, 1, 2, 1, 1,
    2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 0, 2, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 2, 2, 2, 0, 2, 0, 0, 0, 1, 2,
    0, 2, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 2, 2, 1, 0, 1, 1]

# Worst Case
F = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""testArr = F

print("Test Case: F")
start = timer()
tracemalloc.start()
Quicksort(testArr, 0, len(testArr) - 1)
print("Memory Used (current, Max): ", tracemalloc.get_traced_memory())
tracemalloc.stop()
end = timer()

runtime = end - start
print("Total run time is :", runtime, "\n\n")"""


"""print("Test Case: F")
start = timer()
tracemalloc.start()
result = dutch_national_flag(F)
print("Memory Used (current, Max): ", tracemalloc.get_traced_memory())
tracemalloc.stop()
end = timer()

print(result)

runtime = end - start
print("Total run time is :", runtime, "\n\n")"""


print("Test Case: F")
start = timer()
tracemalloc.start()
result = quickselect(F, 50)
print("Memory Used (current, Max): ", tracemalloc.get_traced_memory())
tracemalloc.stop()
end = timer()

print(result)

runtime = end - start
print("Total run time is :", runtime, "\n\n")