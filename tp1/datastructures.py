#!/usr/bin/env python3
import time
import psutil   # For memory usage (you might need: pip install psutil)
from collections import deque

def measure_memory():
    """Returns the memory usage in MB of the current process."""
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)  # Convert bytes to MB

def main():
    # 1. Read the file listing from text file
    input_file = "listing.txt"
    
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # Print an overview
    print(f"Total lines read from file: {len(lines)}")

    # 2. Store content in a hashtable (Python dictionary), stack (list), and queue (deque)
    # -------------------------------------------------------------------
    # (A) HASHTABLE
    # We'll store each line as a key in a dictionary. 
    # If lines can repeat, you might store them as {line: count}, etc.
    
    start_time = time.perf_counter()
    start_mem = measure_memory()
    
    hashtable = {}
    for i, line in enumerate(lines):
        hashtable[line] = i  # store index, or anything else
    
    end_time = time.perf_counter()
    end_mem = measure_memory()
    
    print(f"Hashtable creation took {(end_time - start_time):.6f} seconds.")
    print(f"Memory used for hashtable: {end_mem - start_mem:.6f} MB.\n")

    # (B) STACK (using a Python list)
    
    start_time = time.perf_counter()
    start_mem = measure_memory()
    
    stack = []
    for line in lines:
        stack.append(line)  # push
    
    end_time = time.perf_counter()
    end_mem = measure_memory()
    
    print(f"Stack creation (push all) took {(end_time - start_time):.6f} seconds.")
    print(f"Memory used for stack: {end_mem - start_mem:.6f} MB.\n")

    # (C) QUEUE (using collections.deque for efficiency)
    
    start_time = time.perf_counter()
    start_mem = measure_memory()
    
    queue = deque()
    for line in lines:
        queue.append(line)  # enqueue
    
    end_time = time.perf_counter()
    end_mem = measure_memory()
    
    print(f"Queue creation (enqueue all) took {(end_time - start_time):.6f} seconds.")
    print(f"Memory used for queue: {end_mem - start_mem:.6f} MB.\n")

    # 3. Retrieve the names of the files in positions 1, 100, 1000, 5000, and last for each structure
    #    Note: We'll assume 1-based indexing as typically stated in tasks, so be mindful for 0-based Python indexing.
    positions = [1, 100, 1000, 5000, len(lines)]
    print("Retrieving elements from these positions:", positions, "\n")

    # Retrieve from Stack
    # For a Python list used as a stack, we can do direct indexing, but that’s not typically how stacks are used.
    # We'll just show we *can* index them. 
    # If the requested position doesn't exist, handle it gracefully.
    for pos in positions:
        if pos <= len(stack):
            print(f"Stack position {pos}: {stack[pos-1]}")
        else:
            print(f"Stack position {pos} out of range!")
    print()

    # Retrieve from Queue (again, direct indexing possible with a deque, but not as cheap for large indexes)
    # In real queue usage, you'd pop from the left or right. We'll just show indexing as an example.
    queue_list = list(queue)  # Convert to list for direct indexing
    for pos in positions:
        if pos <= len(queue_list):
            print(f"Queue position {pos}: {queue_list[pos-1]}")
        else:
            print(f"Queue position {pos} out of range!")
    print()

    # Retrieve from Hashtable
    # Hashtables typically don’t store in a specific "position" sense. We can do a naive approach:
    # e.g. just convert keys to a list and index. 
    # But this won't match the original line order unless we used an OrderedDict or just store lines in a list. 
    # We'll demonstrate a direct approach:
    hashtable_keys = list(hashtable.keys())
    for pos in positions:
        if pos <= len(hashtable_keys):
            print(f"Hashtable position {pos}: {hashtable_keys[pos-1]}")
        else:
            print(f"Hashtable position {pos} out of range!")
    print()

    # 4. Measure & record execution time + memory used for removal and insertion
    #    The teacher indicated "perform the addition and removal of items". Let’s demonstrate a small example.

    # Example: removing 10 items from each data structure, measuring time & memory
    # (A) Stack removal (pop from the end)
    start_time = time.perf_counter()
    start_mem = measure_memory()


    for _ in range(10):
        if stack:
            stack.pop()
    end_time = time.perf_counter()
    end_mem = measure_memory()
    print(f"Stack pop(10) took {(end_time - start_time):.6f} seconds, memory change: {end_mem - start_mem:.6f} MB.")

    # (B) Queue removal (popleft)
    start_time = time.perf_counter()
    start_mem = measure_memory()
    for _ in range(10):
        if queue:
            queue.popleft()
    end_time = time.perf_counter()
    end_mem = measure_memory()
    print(f"Queue popleft(10) took {(end_time - start_time):.6f} seconds, memory change: {end_mem - start_mem:.6f} MB.")

    # (C) Hashtable removal
    # We'll remove 10 items from the dictionary if we can (just some keys)
    # For demonstration, we remove from the front of 'hashtable_keys'.
    start_time = time.perf_counter()
    start_mem = measure_memory()
    to_remove = hashtable_keys[:10]
    for key in to_remove:
        if key in hashtable:
            del hashtable[key]
    end_time = time.perf_counter()
    end_mem = measure_memory()
    print(f"Hashtable removal of 10 items took {(end_time - start_time):.6f} seconds, memory change: {end_mem - start_mem:.6f} MB.\n")

    # Example: adding new items to each data structure
    # We'll just create some dummy lines, e.g. ["new_file1", "new_file2", ...]
    new_lines = [f"new_file{i}" for i in range(10)]

    # (A) Stack insertion
    start_time = time.perf_counter()
    start_mem = measure_memory()
    for line in new_lines:
        stack.append(line)
    end_time = time.perf_counter()
    end_mem = measure_memory()
    print(f"Stack push(10) took {(end_time - start_time):.6f} seconds, memory change: {end_mem - start_mem:.6f} MB.")

    # (B) Queue insertion
    start_time = time.perf_counter()
    start_mem = measure_memory()
    for line in new_lines:
        queue.append(line)
    end_time = time.perf_counter()
    end_mem = measure_memory()
    print(f"Queue enqueue(10) took {(end_time - start_time):.6f} seconds, memory change: {end_mem - start_mem:.6f} MB.")

    # (C) Hashtable insertion
    start_time = time.perf_counter()
    start_mem = measure_memory()
    for i, line in enumerate(new_lines):
        hashtable[line] = i + 999999  # Some arbitrary data
    end_time = time.perf_counter()
    end_mem = measure_memory()
    print(f"Hashtable insertion of 10 new items took {(end_time - start_time):.6f} seconds, memory change: {end_mem - start_mem:.6f} MB.\n")

if __name__ == "__main__":
    main()
