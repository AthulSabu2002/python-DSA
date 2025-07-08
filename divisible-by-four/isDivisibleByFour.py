def is_divisible_by_four(num: int) -> bool:
    n = len(str(num))
    
    if n == 0:
        return False
    if n == 1:
        return num % 4 == 0
    
    return int(str(num)[-2:]) % 4 == 0

if __name__ == "__main__":
    print(is_divisible_by_four(1098098089009809809809089899898988230))