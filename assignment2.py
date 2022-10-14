n=int(input("Enter no. of Complex Number you want to store\n"))
list_complex = []
cnt=int(0)
for i in range(n):
    r=input("Enter the real number \n")
    i=input("Enter the imginary number \n")
    list_complex.append(f'{r} + {i}i')
    cnt=cnt+1
print(list_complex)
