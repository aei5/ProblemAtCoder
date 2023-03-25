N, M = map(int, input().split())
ans = [0]*N
Ans = 0
for i in range(1,N):
    ans[i] = int(input())
    if ans[i] <= M:
        Ans += ans[i]
print(Ans)
