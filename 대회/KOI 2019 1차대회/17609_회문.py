import sys
input = sys.stdin.readline
N = int(input())

def is_palindrome(s, left, right):
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_pseudo_palindrome(s, N):
    left = 0
    right = N-1
    check = True

    while left <= right:
        if s[left] != s[right]:
            check = False
            break
        left += 1
        right -= 1
       
    if check:
        return True
    
    if is_palindrome(s, left, right-1):
        return True

    if is_palindrome(s, left+1, right):
        return True
    
    return False

for i in range(N):
    arr = input()[:-1]
    if is_palindrome(arr, 0, len(arr)-1):
        print(0)
    elif is_pseudo_palindrome(arr, len(arr)):
        print(1)
    else:
        print(2)
