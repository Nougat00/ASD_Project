import random
import sys
import time


def rndGenerator(amount, scope):
    rndTable = []
    for i in range(0, amount):
        rndTable.append(random.randrange(1, scope))
    return rndTable


def part(table, p, r):
    x = table[r]
    i = p - 1
    for j in range(p, r):
        if (table[j] <= x):
            i += 1
            swap = table[i]
            table[i] = table[j]
            table[j] = swap
    swap = table[i + 1]
    table[i + 1] = table[r]
    table[r] = swap
    return i + 1


def qs(table, p, r):
    if (p < r):
        q = part(table, p, r)
        qs(table, p, q - 1)
        qs(table, q + 1, r)
    return table


def heapify(table, n, i):
    lar = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and table[i] < table[l]:
        lar = l

    if r < n and table[lar] < table[r]:
        lar = r

    if lar != i:
        table[i], table[lar] = table[lar], table[i]

        heapify(table, n, lar)


def heapSort(table):
    n = len(table)

    for i in range(n // 2 - 1, -1, -1):
        heapify(table, n, i)

    for i in range(n - 1, 0, -1):
        table[i], table[0] = table[0], table[i]
        heapify(table, i, 0)

    return table


def insertionSort(table):
    for i in range(1, len(table)):
        key = table[i]
        j = i - 1
        while j >= 0 and key < table[j]:
            table[j + 1] = table[j]
            j -= 1
        table[j + 1] = key
    return table


def mergeSort(table):
    if len(table) > 1:
        mid = len(table) // 2
        L = table[:mid]
        R = table[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                table[k] = L[i]
                i += 1
            else:
                table[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            table[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            table[k] = R[j]
            j += 1
            k += 1
    return table


sys.setrecursionlimit(999999999)



print("---------------HeapSort---------------\n")
table = rndGenerator(100000, 100000)
heap_time = time.time()
table = heapSort(table)
heap_time_stop = time.time()
print(f"Time for random numbers in heap sort {heap_time_stop - heap_time} Seconds")
heap_time = time.time()
table = heapSort(table)
heap_time_stop = time.time()
print(f"Time for sorted numbers in heap sort {heap_time_stop - heap_time} Seconds")
table.reverse()
heap_time = time.time()
table = heapSort(table)
heap_time_stop = time.time()
print(f"Time for reversed numbers in heap sort {heap_time_stop - heap_time} Seconds")

print("\n---------------QuickSort---------------\n")

table = rndGenerator(100000, 100000)
qs_time = time.time()
table = qs(table, 0, len(table) - 1)
qs_time_stop = time.time()
print(f"Time for random numbers in quicksort {qs_time_stop - qs_time} Seconds")

# print(f"Time for sorted numbers in quicksort {qs_time_stop - qs_time} Seconds")
# qs_time = time.time()
# #table = qs(table, 0, len(table) - 1)
# qs_time_stop = time.time()

# table.reverse()
# qs_time = time.time()
# table = qs(table, 0, len(table) - 1)
# qs_time_stop=time.time()
#
# print(f"{qs_time_stop-qs_time} Seconds")

print("\n---------------InsertSort---------------\n")

table = rndGenerator(100000, 100000)
in_time = time.time()
table = insertionSort(table)
in_time_stop = time.time()
print(f"Time for random numbers in insertsort {in_time_stop - in_time} Seconds")
in_time = time.time()
table = insertionSort(table)
in_time_stop = time.time()
print(f"Time for sorted numbers in insertsort {in_time_stop - in_time} Seconds")
table.reverse()
in_time = time.time()
table = insertionSort(table)
in_time_stop = time.time()
print(f"Time for reversed numbers in insertsort {in_time_stop - in_time} Seconds")


print("\n---------------MergeSort---------------\n")
table = rndGenerator(100000, 100000)
mrg_time = time.time()
table = mergeSort(table)
mrg_time_stop = time.time()
print(f"Time for random numbers in mergeSort {mrg_time_stop - mrg_time} Seconds")
mrg_time = time.time()
table = mergeSort(table)
mrg_time_stop = time.time()
print(f"Time for sorted numbers in mergeSort {mrg_time_stop - mrg_time} Seconds")
table.reverse()
mrg_time = time.time()
table = mergeSort(table)
mrg_time_stop = time.time()
print(f"Time for reversed numbers in mergeSort {mrg_time_stop - mrg_time} Seconds")