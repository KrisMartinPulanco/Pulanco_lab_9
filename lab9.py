num_of_rows=int(input("Enter the numbers of rows"))
num = 1
for row in range (1, num_of_rows + 1):
    for column in range(1, row + 1):  
        print(num, end=" ") 
        num = num + 1
    print()
