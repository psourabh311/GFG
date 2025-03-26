from typing import List
class Solution:
    def lcmAndGcd(self, a : int, b : int):
        if a<b:
            a,b = b,a
        lcm = 1
        for i in range(1,b+1):
            if (a*i)% b==0 :
                lcm = a*i
                break
                
        gcd_val=1
        for i in range(1,b+1):
             if a%i==0 and b%i==0:
                gcd_val = i
        return [lcm,gcd_val]
