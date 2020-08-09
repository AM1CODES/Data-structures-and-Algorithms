def quicksort(arr):
    n = len(arr)
    
    if n < 2:
        return arr
    
    pivot = arr[n//2]
    items_g = []
    items_l = []
    same = []
    for i in arr:
        if i > pivot:
            items_g.append(i)
        elif i < pivot:
            items_l.append(i)
        else:
            same.append(i)
            
    return quicksort(items_l) + same + quicksort(items_g)

if __name__ == "__main__":
    arr = []
    size = int(input("Enter the size of the list:"))
    for i in range(0,size):
        print("ENTER YOUR NUMBER:")
        ele = int(input())
        arr.append(ele)
    arr = quicksort(arr)
    print("Sorted array is:",arr)