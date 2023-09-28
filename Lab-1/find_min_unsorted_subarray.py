def find_min_unsorted_subarray_n(arr, is_reversed=False):
    if is_reversed:
        r_start_unsorted = len(arr) - 1
        for j in range(len(arr) - 1, 0, -1):
            if arr[j] > arr[j - 1]:
                r_start_unsorted = j
                break

        r_end_unsorted = 0
        for i in range(1, r_start_unsorted):
            if arr[i] < arr[i + 1]:
                r_end_unsorted = i
                break

        if r_end_unsorted == len(arr) - 1:
            return -1, -1

        r_min_unsorted_index = r_start_unsorted
        r_max_unsorted_index = r_end_unsorted

        for k in range(r_start_unsorted, r_end_unsorted + 1, -1):
            if arr[k] >= arr[k - 1]:
                r_max_unsorted_index = k - 1 if arr[r_max_unsorted_index] > arr[k - 1] else r_max_unsorted_index
            else:
                r_min_unsorted_index = k - 1 if arr[r_min_unsorted_index] < arr[k - 1] else r_min_unsorted_index

        r_last_unsorted_subarray_index = 0
        for i in range(r_max_unsorted_index, len(arr) - 1):
            if arr[r_max_unsorted_index] < arr[i]:
                r_last_unsorted_subarray_index = i

        r_first_unsorted_subarray_index = 0
        for i in range(r_min_unsorted_index, 0, -1):
            if arr[r_min_unsorted_index] > arr[i]:
                r_first_unsorted_subarray_index = i

        return r_first_unsorted_subarray_index, r_last_unsorted_subarray_index

    start_unsorted = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            start_unsorted = i
            break

    end_unsorted = len(arr) - 1
    for j in range(len(arr) - 1, start_unsorted, -1):
        if arr[j] < arr[j - 1]:
            end_unsorted = j
            break

    if start_unsorted == 0 and end_unsorted == len(arr) - 1:
        return -1, -1

    min_unsorted_index = end_unsorted
    max_unsorted_index = start_unsorted

    for k in range(end_unsorted, start_unsorted + 1, -1):
        if arr[k] >= arr[k - 1]:
            min_unsorted_index = k - 1 if arr[min_unsorted_index] > arr[k - 1] else min_unsorted_index
            max_unsorted_index = k if arr[max_unsorted_index] < arr[k] else max_unsorted_index
        else:
            max_unsorted_index = k - 1 if arr[max_unsorted_index] < arr[k - 1] else max_unsorted_index
            min_unsorted_index = k if arr[min_unsorted_index] > arr[k] else min_unsorted_index

    last_unsorted_subarray_index = 0
    if (max_unsorted_index == len(arr) - 1):
        last_unsorted_subarray_index = len(arr) - 1
    else:
        for i in range(max_unsorted_index, len(arr)):
            if arr[max_unsorted_index] > arr[i]:
                last_unsorted_subarray_index = i

    first_unsorted_subarray_index = 0
    for i in range(min_unsorted_index, 0, -1):
        if arr[min_unsorted_index] < arr[i]:
            first_unsorted_subarray_index = i

    return first_unsorted_subarray_index, last_unsorted_subarray_index
