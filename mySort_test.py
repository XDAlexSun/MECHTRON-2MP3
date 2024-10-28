import time
import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer

lib_path = "/home/alex/MECHTRON2MP3/Assignment2/libmysort.so"
mySortLib = ctypes.CDLL(lib_path)

#Importing sorting algorithms
mySortLib.bubbleSort.argtypes = [ndpointer(ctypes.c_int, flags="C_CONTIGUOUS"), ctypes.c_int]
mySortLib.bubbleSort.restype = None

mySortLib.insertionSort.argtypes = [ndpointer(ctypes.c_int, flags="C_CONTIGUOUS"), ctypes.c_int]
mySortLib.insertionSort.restype = None

mySortLib.mergeSort.argtypes = [ndpointer(ctypes.c_int, flags="C_CONTIGUOUS"), ctypes.c_int]
mySortLib.mergeSort.restype = None

mySortLib.heapSort.argtypes = [ndpointer(ctypes.c_int, flags="C_CONTIGUOUS"), ctypes.c_int]
mySortLib.heapSort.restype = None

mySortLib.countingSort.argtypes = [ndpointer(ctypes.c_int, flags="C_CONTIGUOUS"), ctypes.c_int]
mySortLib.countingSort.restype = None

#creating small and large test cases
arr0 = np.array([64, -134, -5, 0, 25, 12, 22, 11, 90], dtype=np.int32)
print("Original small array:", arr0)
arr = np.random.choice(np.arange(-1000000, 1000000, dtype=np.int32), size=500000, replace=False)
print("Original large array:", arr)

# #Bubble Sort Test
# n = len(arr0)
# arr_copy0 = np.copy(arr0)
# mySortLib.bubbleSort(arr_copy0, n)
# print("Small sorted array using Bubble Sort:", arr0)

# arr_copy = np.copy(arr)
# n = len(arr)
# start = time.time()
# mySortLib.bubbleSort(arr_copy, n)
# end = time.time()
# print("Large sorted array using Bubble Sort:", arr_copy)
# print(f"Time to convert: {end - start} seconds")

#Insertion Sort Test
n = len(arr0)
arr_copy0 = np.copy(arr0)
mySortLib.insertionSort(arr_copy0, n)
print("Small sorted array using Insertion Sort:", arr0)

arr_copy = np.copy(arr)
n = len(arr)
start = time.time()
mySortLib.insertionSort(arr_copy, n)
end = time.time()
print("Large sorted array using Insertion Sort:", arr_copy)
print(f"Time to convert: {end - start} seconds")

# #Merge Sort Test
# n = len(arr0)
# arr_copy0 = np.copy(arr0)
# mySortLib.mergeSort(arr_copy0, 0, n)
# print("Small sorted array using Merge Sort:", arr0)

# arr_copy = np.copy(arr)
# n = len(arr)
# start = time.time()
# mySortLib.mergeSort(arr_copy, 0, n)
# end = time.time()
# print("Large sorted array using Merge Sort:", arr_copy)
# print(f"Time to convert: {end - start} seconds")

# #Heap Sort Test
# n = len(arr0)
# arr_copy0 = np.copy(arr0)
# mySortLib.heapSort(arr_copy0, n)
# print("Small sorted array using Heap Sort:", arr0)

# arr_copy = np.copy(arr)
# n = len(arr)
# start = time.time()
# mySortLib.heapSort(arr_copy, n)
# end = time.time()
# print("Large sorted array using Heap Sort:", arr_copy)
# print(f"Time to convert: {end - start} seconds")

# #Counting Sort Test
# n = len(arr0)
# arr_copy0 = np.copy(arr0)
# mySortLib.countingSort(arr_copy0, n)
# print("Small sorted array using Heap Sort:", arr0)

# arr_copy = np.copy(arr)
# n = len(arr)
# start = time.time()
# mySortLib.countingSort(arr_copy, n)
# end = time.time()
# print("Large sorted array using Counting Sort:", arr_copy)
# print(f"Time to convert: {end - start} seconds")

# #Built In Sort
# arr_copy0 = np.copy(arr0)
# n = len(arr0)
# sorted_arr = sorted(arr_copy0)
# print("Small sorted array using built-in sort:", arr0)

# arr_copy = np.copy(arr)
# n = len(arr)
# start = time.time()
# sorted_arr = sorted(arr_copy) 
# end = time.time()

# print("Large sorted array using Counting Sort:", arr_copy)
# print("Time taken by built-in sort:", end - start, "seconds")

# #Numpy Sort
# arr_copy0 = np.copy(arr0)
# n = len(arr0)
# sorted_arr = np.sort(arr_copy0)
# print("Small sorted array using numpy sort:", arr0)

# arr_copy = np.copy(arr)
# n = len(arr)
# start = time.time()
# sorted_arr = np.sort(arr_copy) 
# end = time.time()

# print("Large sorted array using Numpy Sort:", arr_copy)
# print("Time taken by built-in sort:", end - start, "seconds")