import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    msg = input().rstrip()
    cnt = [0] * 26
    
    for s in msg:
        if 3 in cnt:
            check = cnt.index(3)
            if s != chr(check + ord('A')):
                break
            cnt[check] = 0
        else:
            cnt[ord(s)-ord('A')] += 1
    if 3 in cnt:
        print("FAKE")
    else:
        print("OK")
