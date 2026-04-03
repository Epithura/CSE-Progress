t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    freq = [0] * (m + 1)
    Alpha=[]
    for _ in range(n):
        parts = list(map(int, input().split()))
        s = parts[1:]
        if len(s)==1:
            Alpha.append(s[0])
        for x in s:
            freq[x] += 1
    if any(freq[i] == 0 for i in range(1, m + 1)):
        print("NO")
        continue
    if any(freq[i] >= 3 for i in range(1, m + 1)):
        print("YES")
        continue
    count_ge2 = sum(1 for i in range(1, m + 1) if freq[i] >= 2)
    if n == 2:
        if count_ge2 == m:
            print("YES")  
        else:
            print("NO")
    else:  
        if count_ge2 >= 2:
            print("YES")
        elif count_ge2==1:
            if len(set(Alpha))<len(Alpha):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")