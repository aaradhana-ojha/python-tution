def armstrong(n):
    
    num_str = str(n)
    
    num_len = len(num_str)
   
    sum_of_powers = 0
    
    
    for digit in num_str:
        
        sum_of_powers += int(digit) ** num_len
    
    
    if sum_of_powers == n:
        return True
    else:
        return False

print(armstrong(153))  # 1^3 + 5^3 + 3^3 = 153
print(armstrong(123))  
