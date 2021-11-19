def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

print("Following is the list of height of students in cms")
arr = [140, 120, 135, 153, 174, 121]
bubbleSort(arr)
print("Sorted array is :")
for i in range(len(arr)):
    print("%d" %arr[i]),
