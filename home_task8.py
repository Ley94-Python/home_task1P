n = int(input("Ведите длину шоколадки:"))
m = int(input("Ведите ширину шоколадки:"))
k = int(input("Ведите размер куска, который хотите отломить:"))
if k < m*n and (k % m == 0 or k % n == 0):
    print("Yes")
else:
    print("No")