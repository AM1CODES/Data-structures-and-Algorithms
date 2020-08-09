def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            

if __name__ == "__main__":
    arr = []
    size = int(input("Enter the size of the list:"))
    for i in range(0,size):
        print("ENTER YOUR NUMBER:")
        ele = int(input())
        arr.append(ele)
    bubblesort(arr)
    print("Sorted array is:",arr)