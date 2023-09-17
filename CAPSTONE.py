#implementation of matrices using lists
#entering matrices
#first matrix
print('First matrix')
r=int(input("enter the number of rows:" ))
c=int(input("enter the number of columns:" ))
m1=[]
print('enter the elements rowwise: ')
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    m1.append(a)
print('the entered matrix is: ')
for i in range(r):
    for j in range(c):
        print(m1[i][j],end=' ')
    print()
print('\n')

#second matrix
print('Second matrix')
p=int(input("enter the number of rows:" ))
q=int(input("enter the number of columns:" ))
m2=[]
print('enter the elements rowwise: ')
for i in range(p):
    a=[]
    for j in range(q):
        a.append(int(input()))
    m2.append(a)
print('the entered matrix is: ')
for i in range(p):
    for j in range(q):
        print(m2[i][j],end=' ')
    print()
print('\n')
#choice making
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for exit")
choice=int(input('Enter your choice'))
print('\n')

#addition
if choice==1:
    if r==p and c==q:
        m3=[]
        for i in range(r):
            b=[]
            for j in range(c):
                x=m1[i][j]+m2[i][j]
                b.append(x)
            m3.append(b)
        print("The sum of the matrices is:")
        for i in range(r):
            for j in range(c):
                print(m3[i][j],end=' ')
            print()
    else:
        print('Addition is not possible')
#Subtraction
elif choice==2:
    if r==p and c==q:
        m4=[]
        for i in range(r):
            b=[]
            for j in range(c):
                x=m1[i][j]-m2[i][j]
                b.append(x)
            m4.append(b)
        print("The difference of the matrices is:")
        for i in range(r):
            for j in range(c):
                print(m4[i][j],end=' ')
            print()
    else:
        print('Subtraction is not possible')

#multiplication
elif choice==3:
    if c==p:
        m5=[]
        for i in range(r):
            z=[]
            s=0
            for j in range(q):
                for k in range(c):
                    s+=m1[i][k]*m2[k][j]
                z.append(s)
                s=0
            m5.append(z)
        print("The product of the matrices is:")
        for i in range(r):
            for j in range(q):
                print(m5[i][j],end=' ')
            print()
    else:
        print('Multiplication is not possible')
#exit
elif choice==4:
    print('EXIT')
    exit()
else:
    print('Please enter your choice from the above options')
