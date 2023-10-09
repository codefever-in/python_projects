# bubble sort
def bubbleSort(arr):
    n = len(arr)
    
    swapped = False
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
 

# insertion sort
def insertionSort(arr):
    n = len(arr)  
      
    if n <= 1:
        return  
 
    for i in range(1, n):  
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]:  
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = key    


# selection sort
def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
          
            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
