def isprime(num): 
    for i in range(2, int(int(num)**0.5)+1): 
        if int(num) % i == 0: 
            return 
    
    if len(num) == n:
        print(num) 
        return 

    for j in secon: 
        isprime(num+j) 

n = int(input()) 
         
first = ['2', '3', '5', '7'] 
secon = ['1', '3', '7', '9'] 
for k in first: isprime(k)