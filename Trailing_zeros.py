def factorial( n):
        if n == 0 or n == 1:
            return 1 
        return n * factorial(n-1)

n = 7 ; num = factorial(n) ; cnt = 0 
while num >= 0:

    rem = num%10 
    if rem == 0:
        cnt += 1    
    else:
        print(cnt) 
        break 
            
    num = num//10 

# The above approach takes too much time when the input number is too loong , 
# so it fails a testcase when the input is too long. 
# so , we came up with new approach 

# think about a number 10  , 
# how 10 is formed with multiply of 5*2, how many 5's are there in 10 , just 1 , how many trailing zeros are 1 
# similiar to 100 , how many 5's are there, 20 + how 5's are there in 20, 4 is therre , total 24 
#trailing zeros are 24 

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        ans = 0 
        while n > 0:

            n = n // 5 
            ans += n 
        
        return ans 
    

obj = Solution() 
print(obj.trailingZeroes(100)) 

# T.C : O(logn) 
# S.C: o(1) 

# For simple understanding
# Here , 5! have 1 0's , 10! have 2 0's , then if the guy gives a num , ask how many zero present in num, just cal how many 5's are there, 
# you'll get the answer 

# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5,040
# 8! = 40,320
# 9! = 362,880
# 10! = 3,628,800
