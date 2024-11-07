import sys

l1=[]

print(f'Initial_size: {sys.getsizeof(l1)}')

for i in range(0, 17):
    l1.append(i)
    print(f'{i} ---> {sys.getsizeof(l1)}')
