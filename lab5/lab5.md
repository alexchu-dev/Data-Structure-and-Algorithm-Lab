# Lab 5 Reflection and Observations

* Alex Chu
* Kenneth Reforma
* Krinskumar Vaghasia

## Heap Insertion

### Picture of heap created with 10 values
![10 value heap](IMG_2675.jpg)

### Pictures of adding 11th value to heap
#### This is the starting state where value 10 is to be added in the existing heap.
![11 value heap 1](IMG_2676.jpg)
#### 10 is added on to the bottom-right most position in the heap.
![11 value heap 2](IMG_2677.jpg)
#### 10 goes up to depth 2 and 49 goes down to depth 3 since 10 is less than 49.
![11 value heap 3](IMG_2679.jpg)
#### 10 goes up to depth 1 and 31 goes down to depth 2 since 10 is less than 31. This is the final MinHeap since 10 is already in its correct position. 
![11 value heap 4](IMG_2680.jpg)

## Heap Removal

### Picture after 1 value was removed from heap
![Alt text](IMG_2681.jpg)

### Picture after 2 value was removed from heap
![Alt text](IMG_2682.jpg)

### Picture after 3 value was removed from heap
![Alt text](IMG_2683.jpg)

### Values removed (in order removed):
> 1, 10, and 22

## Array representation of heap
### Picture of heap
![Alt text](IMG_2683.jpg)

### Array representation of heap
> After the third removal, the heap in array is [31, 49, 82, 69, 79, 777, 97, 107].

## Creating a heap from array
### Photograph of your array and heap
![Alt text](IMG_2685.jpg)

* What number is the first non-leaf node starting from bottom?
> 1
* What index is that node at?
> 4

### Photograph of heap created by Heapify
![Alt text](IMG_2692.jpg)

## HeapSort

Initial questions (do first):
* How many values are in your array? 
> 11
* What is index of last value in array? 
> 10

After doing 1 removal operation:
* What was the first value removed?
> 777
* How does this number compare with others in heap (biggest? smallest?)
> It is the biggest in the heap.
* Look at your heap portion of the array after you did this removal. How many values are in it, what is the index of the bottom right most value in heap?
> 10 values in the heap and the index of the bottom right most value is 9.

After doing 2 removal operations:
Perform another remove from the heap and adjust the array to match
* What was the second value removed and how does it compare with others still in heap?
> The value is 107 and it is the biggest in the heap.
* Look at your heap portion of the array after you did this removal.. how many values are in what is the index of the bottom right most value in heap?
> 9 values in the heap and the index of the bottom right most value is 8.
* Are there any open spots in the array that is not part of the heap and not holding anything useful?
> There are no open spots and every index is being used since the last removed value from the heap is placed on the bottom right most space of the heap portion.

After doing 3 removal opeations:
Perform another remove from the heap and adjust the array to match
* What was the second value removed and how does it compare with others still in heap?
> The value is 97 and it is the biggest in the heap.
* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
> 8 values in the heap and the index of the bottom right most value is 7.
* Are there any open spots in the array that is not part of the heap and not holding anything useful?
> There are no open spots and every index is being used since the last removed value from the heap is placed on the bottom right most space of the heap portion.

## Reflection

This last part is to be completed individually.

Write a short paragraph about what you learned from this lab.
* Discuss what you learned about heaps and heap sort.
* What was the most surprising thing you learned about heaps?


