class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        dummy = n
        def digit_product(x):
            prod = 1
            while x > 0:
               prod *= x % 10
               x //= 10
            return prod
             
        while True:
            if digit_product(n) % t == 0:
               return n
            n += 1
        return n    


        