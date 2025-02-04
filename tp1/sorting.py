#!/usr/bin/env python3
import time

def bubble_sort(data):
    """Implementation of Bubble Sort."""
    arr = data[:]  # Make a copy so original isn't modified
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(data):
    """Implementation of Selection Sort."""
    arr = data[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(data):
    """Implementation of Insertion Sort."""
    arr = data[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_sort_time(sort_func, data):
    """Measure execution time of a given sorting function."""
    start_time = time.perf_counter()
    sorted_data = sort_func(data)
    end_time = time.perf_counter()
    return sorted_data, (end_time - start_time)

def main():
    # 1. Read the file listing from the generated text file
    #    Change 'listing.txt' if your file has a different name.
    input_file = "listing.txt"
    
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # 2. Run Bubble Sort, Selection Sort, Insertion Sort and measure time
    for sort_name, func in [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort)
    ]:
        _, duration = measure_sort_time(func, lines)
        print(f"{sort_name} took {duration:.6f} seconds to sort {len(lines)} items.")

if __name__ == "__main__":
    main()
