def threeDivisors(limit: int) -> list[int]:
    print(limit)
    nums = []
    
    for i in range(1, limit+1):
        count = 1
        for j in range(1, (i//2)+1):
            if i % j == 0:
                count += 1
        if count >= 3:
            nums.append(i)
        
    return nums


if __name__ == "__main__":
    n = 10000
    print(threeDivisors(n))