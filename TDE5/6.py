def triangular(num):
    i = 1
    while i * (i + 1) * (i + 2) <= num:
        if i * (i + 1) * (i + 2) == num:
            return True
        i += 1
    return False

n = int(input("digite um numero: "))
if triangular(n):
    print("é triangular")
else:
    print("não é triangular")