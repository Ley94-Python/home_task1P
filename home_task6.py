num = int(input("Введите номер билета: "))
sum_left = 0
sum_right = 0
for i in range(6):
    if i < 3:
        sum_right = sum_right + num // 10 **i % 10
    else:
        sum_left = sum_left + num // 10 **i % 10
if sum_left == sum_right:
    print("Билет - удачный")
else:
    print("Билет - неудачный")


