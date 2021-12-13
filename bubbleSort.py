A=[]
for v in range (8):
    A.append(int(input('enter a int number :')))
    print(A)
def bubbleSort(A):
    for passnum in range(len(A)-1,0,-1):
        for i in range(passnum):
            if A[i]>A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp

bubbleSort(A)
print('Sorted Array:')
print (A)
