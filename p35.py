numbers = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    numbers.append(num)
sum_negative=0
sum_pos_even=0
sum_pos_odd=0
sum=0
for i in numbers:
    if i<0:
        sum_negative+=i
    elif num%2==0:
        sum_pos_even+=i
    else:
        sum_pos_odd+=i
print("Su