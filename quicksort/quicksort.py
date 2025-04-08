from typing import List, Tuple

def quicksort(arr: List[int], partition: str ="first") -> List[int]:
    """
    Sorts a given array and computes the number of comparisons, then returns the number of comparisons.
    
    Partitions based on one of three choices: first element, last element, or median-of-three.

    Args:   
        arr (List[int]): A list of integers to be sorted
        partition (str): The partitioning strategy to use. Can be 'first', 'last', or 'median'.
                         Default is 'first'.

    Returns:
        int: the number of comparisons used to sort the list
    """

    # Returns the index of the pivot based on the given scheme
    def partition_scheme(to_partition: List[int]) -> int:
        match partition:
            # Returns the index of the last position
            case "last":
                return len(to_partition) - 1
            
            # Returns the index of the median value of the first, middle, and last indices
            case "median":
                mid_index = (len(to_partition) + 1) // 2

                possible_elems = [(to_partition[0], 0),
                                  (to_partition[mid_index], mid_index),
                                  (to_partition[-1], len(to_partition) -1)]
                return sorted(possible_elems)[1][1]
            
            # Otherwise returns the index 0
            case _:
                return 0

    # Perform the recursive sorting operations and counts the number of comparisons
    def quicksort_helper(arr: List[int]) -> Tuple[List[int], int]:

        # Base case
        if len(arr) <= 1:
            return arr, 0
        
        # Initialize swapping and comparison pointers, pivot and number of iterations
        i = 0
        j = 1
        pivot_index = partition_scheme(arr)
        pivot = arr[pivot_index]
        stop = len(arr)

        # Swap the pivot to the first position of the array
        arr[0], arr[pivot_index] = arr[pivot_index], arr[0]

        # Perform swaps if arr[j] is less than the pivot
        while j < stop:
            if arr[j] <= pivot:
               i += 1
               arr[i], arr[j] = arr[j], arr[i]
            j += 1
        
        # Put the pivot value in the right spot
        arr[0], arr[i] = arr[i], arr[0]

        # Sort the subarrays to the left and right of the pivot
        left_arr = arr[0:i]
        right_arr = arr[i+1:]
        sorted_left, left_sum = quicksort_helper(left_arr)
        sorted_right, right_sum = quicksort_helper(right_arr)

        return sorted_left + [pivot] + sorted_right, (len(arr) - 1 + left_sum + right_sum)
    
    return quicksort_helper(arr)