def replicate_n_times(arr, n, k):
    b = []
    t = 0

    while t < k:
        i = 0
        while i < n:
            b.append(arr[t])
            i += 1
        t += 1

    print(b)

a = [1, 2, 3, 4]
n = int(input("Times you want to replicate: "))
k = int(input("Size of array: "))
replicate_n_times(a, n, k)
