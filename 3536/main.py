"""isPrime_large"""
def main():
    """isPrime_large"""
    number = int(input())
    if number < 2:
        is_prime = False
    elif number in (2, 3):
        is_prime = True
    elif not number % 2 or not number % 3:
        is_prime = False
    else:
        is_prime = True
        i = 5
        while i * i <= number:
            if not number % i or not number % (i + 2):
                is_prime = False
                break
            i += 6

    print("YES" if is_prime else "NO")

main()
