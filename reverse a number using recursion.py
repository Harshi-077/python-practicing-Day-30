def reverse_number(n, rev=0):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit

    return reverse_number(n // 10, rev)


n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))