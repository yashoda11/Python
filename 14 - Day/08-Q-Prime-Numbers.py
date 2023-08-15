# 8. Create a nested loop to find and print prime numbers from 2 to 20.
# Expected Input: None
# Expected Output: 2 3 5 7 11 13 17 19

for num in range(2, 21):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")