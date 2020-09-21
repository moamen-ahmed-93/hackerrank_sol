

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s=n
        for i in range(1,n):
            if n%i == 0:
                s+=i
        return s
       

