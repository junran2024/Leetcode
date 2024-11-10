
arr = [0,1,2,3,0]

n = len(arr)
left, right, ans = 1, n - 2, 0

while left <= right:
    mid = (left + right) // 2
    if arr[mid] > arr[mid + 1]:
        right = mid - 1
    else:
        left = mid + 1
    
    if left==right: ans=left
    if abs(left-right)==1 and (left>right): ans=left
    if abs(left-right)==1 and (left<right): ans=right

print(ans)

#Letcode: 