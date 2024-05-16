# Where it doesn't perform well:
# 1. Large Range of Elements: If the range of elements in the array is very large compared to the number of elements,
# Counting Sort requires a large amount of memory to store the counting array, which can make it impractical.
# 2. Non-integer Data: Counting Sort is designed for sorting integer data. It doesn't work directly with non-integer
# data or data with floating-point values.
# 3. Sparse Data: If the data is sparse (i.e., there are many gaps between the elements), Counting Sort may waste
# memory and time allocating and processing empty slots in the counting array.

def custom_counting_sort(array):
    # Find the maximum element in the array
    max_element = max(array)

    # Create a counting array to store the count of each element
    count = [0] * (max_element + 1)

    # Count the occurrences of each element
    for num in array:
        count[num] += 1

    # Update the count array to store the position of each element in the sorted array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create a new array to store the sorted elements
    sorted_array = [0] * len(array)

    # Place each element in its correct position in the sorted array
    for num in array:
        sorted_array[count[num] - 1] = num
        count[num] -= 1

    return sorted_array


# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = custom_counting_sort(arr)
print("Sorted array:", sorted_arr)