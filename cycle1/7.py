def absent_digits(n):
    # Create a set containing all possible digits (0 to 9).
    all_nums = set(range(10))  # Using range(10) to include 0 to 9

    # Convert the list 'n' to a set of integers.
    n = set(n)

    # Find the difference between the set of all_nums and the set 'n' to get absent digits.
    absent = all_nums - n

    # Sort the result to get a list of absent digits.
    absent = sorted(absent)

    # Print the list of absent digits instead of returning it.
    print(absent)

a=[]
for i in range(0,10):
    c=int(input("enter the digit of number"))
    a.append(c)
print(a)
# Test the 'absent_digits' function with a given list.
absent_digits(a)
