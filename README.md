Where Counting Sort algorythm doesn't perform well:
1. Large Range of Elements: If the range of elements in the array is very large compared to the number of elements, Counting Sort requires a large amount of memory to store the counting array, which can make it impractical.
2. Non-integer Data: Counting Sort is designed for sorting integer data. It doesn't work directly with non-integer data or data with floating-point values.
3. Sparse Data: If the data is sparse (i.e., there are many gaps between the elements), Counting Sort may waste memory and time allocating and processing empty slots in the counting array.