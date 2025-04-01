from typing import List, Tuple

def quicksort(arr: List[int], partition: str ="first") -> int:
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
    if len(arr) <= 1:
        return 0