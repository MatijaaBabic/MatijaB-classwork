def sum_even(n):
    if n > 0:
        n = n + sum_even(n-2)
    return n
x = int(input("Please input an even number: "))
if x % 2 == 0:
    print(sum_even(x))
else:
    x = int(input("Error: Please input an even number: "))
    print(sum_even(x))


