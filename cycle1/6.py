def bubble_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


n=int(input("enter the no of numbers"))
a=[]
for i in range(0,n):
    c=int(input("enter the number"))
    a.append(c)
print("unsorted list is")
print(a)
bubble_sort(a)
print("sorted list is")
print(a)