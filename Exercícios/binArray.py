arr = [1, 1, 0, 1]

def BinArray(arr):
    n = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            n += 2 ** (len(arr) - i - 1)
    return n

print(BinArray(arr))
