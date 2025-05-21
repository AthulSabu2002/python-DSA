s = input("Enter a string: ")

l, r = 0, len(s) - 1
lst = list(s)

print(lst)

while l < r:
    lst[l], lst[r] = lst[r], lst[l]
    l += 1
    r -= 1

print(''.join(lst))