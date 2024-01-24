#answer
# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

count = dict()

# 각 숫자가 몇 번씩 나왔는지를
# hashmap에 기록해줍니다.
for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

ans = 0
# 배열을 앞에서부터 순회하며 쌍을 만들어줍니다. (2개 합을 순회하면서 구하고, diff는 hash map을 이용한다.)
for i in range(n):
    count[arr[i]] -= 1  # 사용한 수는 제외
    for j in range(i): #인덱스가, (1,0)(2,0)(2,1)... 이런식으로 순회 해야 중복 x
        diff = k - arr[i] - arr[j] # 인덱스값으로 접근하므로 가지수는 diff의 갯수 만큼
        if diff in count:
            ans += count[diff]
            # print(diff, arr[i], arr[j])
            # print()

print(ans)