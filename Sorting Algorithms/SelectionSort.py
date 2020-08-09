def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
            

if __name__ == "__main__":
    arr = []
    size = int(input("Enter the size of the list:"))
    for i in range(0,size):
        print("ENTER YOUR NUMBER:")
        ele = int(input())
        arr.append(ele)
    selectionsort(arr)
    print("Sorted array is:",arr)