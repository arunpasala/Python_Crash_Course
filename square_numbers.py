squares =[]
for value in range(1,11):
    square=value**2
    squares.append(square)  
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
minimum_value=min(digits)
maximum_value=max(digits)       
sum_of_digits=sum(digits)
print(f"Minimum value:{minimum_value}")
print(f"Maximum value:{maximum_value}") 
print(f"Sum of digits:{sum_of_digits}")