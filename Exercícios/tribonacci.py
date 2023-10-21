signature = [1, 1]

def tribonacci(sig, n):
    if len(sig) < 3:
        for i in range(3 - len(sig)):
            sig.append(0)
    elif len(sig) > 3:
        sig = [sig[0], sig[1], sig[2]]
    if n == 0:
        return []
    if n < 3:
        arr = []
        for i in range(n):
            arr.append(sig[i])
        return arr
    for i in range(n - 3):
        total = sig[i] + sig[i + 1] + sig[i + 2]
        sig.append(total)
    return sig

print(tribonacci(signature, 1))

# for i in range(15):
#     n = signature[i] + signature[i + 1] + signature[i + 2]
#     signature.append(n)

# print(signature)