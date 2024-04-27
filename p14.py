numbers=[10,20,30,40,50]
square_numbers=[]
 
 
for num in numbers:
    square_numbers.append(num*num)
print(square_numbers)

numbers=[10,20,30,40,50]
square_numbers=[num*num for num in numbers]
print(square_numbers)
    
even_numbers=[num for num in range(1,10) if num%2==0]
print(even_numbers)

word="shreya"
vowels="aeiou"
result=[char for char in word if char in vowels]
print(result)