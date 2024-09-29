x = int(input("Enter x: "))

left = 1
right = 7

while left < right:
    mid = (left + right) // 2
    if x > mid:
        left = mid + 1
    else:
        right = mid

res = left
print(res)
