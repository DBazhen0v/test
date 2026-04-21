def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        less = [i for i in arr[1:] if i < arr[0]]
        more = [i for i in arr[1:] if i >= arr[0]]
        return quicksort(less) + [arr[0]] + quicksort(more)

a = list(map(int, input().split()))
print(quicksort)