def insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        val = arr[i]
        while arr[i-1] > val and i>0:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            i = i-1
            
if __name__ == "__main__":
    arr = []
    size = int(input("Enter the size of the list:"))
    for i in range(0,size):
        print("ENTER YOUR NUMBER:")
        ele = int(input())
        arr.append(ele)
    insertionsort(arr)
    print("Sorted array is:",arr)