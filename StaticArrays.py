"""
StaticArrays.py is a practice for basic functionalities of Arrays like traversal, deletion, insertion, replacement
"""
# Static Arrays

# function to delete complete array
def delete_arr(arr, length):
    """
    arr: array
    length: length of the array
    """
    if length > 0:
        #deletion/ replacing the value by 0
        print('Deletion')
        for i in range(len(arr1)):
            arr1[i] = 0
    return arr
# function to delete middle element of an array
def delete_middle(arr, length):
    """
    arr: array
    length: length of the array
    """
    middle_index = length // 2   
    print('deleting the middle element')
    for i in (middle_index+1, length-1):
        arr[i-1] = arr[i]
    # remove the last element as the array has been moved
    arr.pop()
    return arr

# function to insert at the end of the array
def insert_end(arr, value, length, capacity):
    """
    arr: array
    value: value to be inserted
    length: length of array
    capacity: max capacity of the array
    """    
    if length < capacity:
        arr[length] = value
        length += 1
    else:
        print("Cannot insert: array is at full capacity.")
    return arr, length

# inserting at the i'th index
def insert(arr, value, index, length):
    arr.append(None)
    # Shift elements to the right
    for i in range(length, index, -1):
        arr[i] = arr[i - 1]
    
    arr[index] = value

    return arr

# initialization
arr1 = [1,2,3]
# Read
print('arr1: ', arr1)
print('arr1[0]', arr1[0])

#traversing through the array
print('Traversal')
for value in arr1:
    print(value)

for i in range(len(arr1)):
    print(arr1[i])

# deletion/ replacement

arr1 = delete_arr(arr1, len(arr1))
print('arr1', arr1)

arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = delete_middle(arr2, len(arr2))
print('arr2:', arr2)

# Insertion
arr3 = [1, 2, 3, 4, 5, None]
current_length = 5  # Current length of the array (excluding None)
capacity = len(arr3)  # Capacity of the array

arr3, current_length = insert_end(arr3, 100, current_length, capacity)
print('arr3:', arr3)

arr4 = [1,2,3,4,5]
arr4 = insert(arr4,100,2,len(arr4))
print('arr4:',arr4)

