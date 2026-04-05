n = int(input())
arr = list(map(int, input().split()))
move_count = 0

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    move_count += (i - (j + 1))

print(' '.join(map(str, arr)))
print(move_count)
