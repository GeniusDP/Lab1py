
#ввод данных
print("Type in coefficients in format:\n")

print("a1 b1 c1\n")
a1, b1, c1 = input().split()
a1=float(a1)
b1=float(b1)
c1=float(c1)
print("\n")

print("a2 b2 c2\n")
a2, b2, c2 = input().split()
a2=float(a2)
b2=float(b2)
c2=float(c2)

det = a1*b2 - b1*a2 #определитель системы!=0
detX = c1 * b2 - c2 * b1; #определитель для 1-й переменной по формуле Крамера
detY = a1 * c2 - a2 * c1; #определитель для 2-й переменной по формуле Крамера

x = detX / det; #формула Крамера
y = detY / det; #формула Крамера

print("\nAnswer is : \n")
print("x = ", x, "\t", "y = ", y)

