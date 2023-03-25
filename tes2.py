N, A, B = map(int,input().split())
for i in range(1, N + 1):
    if i % A == 0 and i % B== 0:
        print("AB")
    elif i % A == 0:
        print("A")
    elif i % B == 0:
        print("B")
    else:
        print("N")
