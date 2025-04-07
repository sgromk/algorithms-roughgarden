from typing import List

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
                first_elem = to_partition[0]
                middle_elem = to_partition[len(to_partition) // 2]
                last_elem = to_partition[-1]
                middle_val = sorted([first_elem, middle_elem, last_elem])[1]
                return to_partition.index(middle_val)
            
            # Otherwise returns the index 0
            case _:
                return 0

    # Perform the recursive sorting operations
    def quicksort_helper(arr: List[int]) -> List[int]:

        # Base case
        if len(arr) <= 1:
            return arr
        
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
        sorted_left = quicksort_helper(arr[0:i])
        sorted_right = quicksort_helper(arr[i+1:])

        return sorted_left + [pivot] + sorted_right
    
    return quicksort_helper(arr)