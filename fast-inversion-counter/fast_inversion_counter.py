from typing import List, Tuple


def fast_inv_count(arr: List[int]) -> int:
    """
    Computes the number of inversions in a given array.

    An inversion is defined as a pair of indices, (i,j) s.t. i < j and arr[i] > arr[j].

    Args:
        arr (List[int]): A list of integers over which we compute the number of inversions

    Returns:
        int: the number of inversions in the list
    """
    
    # Performs the merge-sort based inversion counting
    def fast_inv_helper(inner_arr: List[int]) -> Tuple[List[int], int]:
        arr_len = len(inner_arr)

        # Base case, return same array and no inversions
        if arr_len <= 1:
            return inner_arr, 0
        
        midpoint = len(inner_arr) // 2

        # Sort and count the left and right halves        
        left_arr, sum_left = fast_inv_helper(inner_arr[0:midpoint])
        right_arr, sum_right = fast_inv_helper(inner_arr[midpoint:])

        # Merge and count inversions
        merged_array = []
        inversion_count = 0
        i = 0
        j = 0
        i_max = len(left_arr)
        j_max = len(right_arr)
        merged_length = i_max + j_max

        while len(merged_array) < merged_length:
            curr_i = 0
            curr_j = 0
            
            if i < i_max:
                curr_i = left_arr[i]
            if j < j_max:
                curr_j = right_arr[j]

            if curr_i and (curr_i < curr_j or not curr_j):
                merged_array.append(curr_i)
                i += 1
            elif curr_j:
                merged_array.append(curr_j)
                j += 1
                inversion_count += (i_max - i)

        return merged_array, (inversion_count + sum_left + sum_right)
    
    # Call the helper and discard the sorted array
    final_sorted_array, total_inversions = fast_inv_helper(arr)

    print(total_inversions)
    return total_inversions