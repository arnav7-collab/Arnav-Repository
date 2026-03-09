r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []
sum = 0

print("Enter matrix elements:")
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)
    sum += sum(row)

print("Sum of matrix elements =", sum)
