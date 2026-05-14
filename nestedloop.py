#nested loop=The "inner loop" will finish all its iterations before finishing one iteration of the "outer loop"

rows=int(input("Enter no.of rows:"))
columns=int(input("Enter no.of columns:"))
symbol=input("Enter a symbol to use:")
for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()


