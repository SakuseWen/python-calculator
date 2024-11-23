class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")

        if a == 0:
            return 0

        result = 0
        negative = False

        if a < 0:
            negative = not negative
            a = -a

        if b < 0:
            negative = not negative
            b = -b

        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return -result if negative else result
    
    def modulo(self, a, b):
        
        if b == 0:
            raise ValueError("Cannot modulo by zero.")

        if a == 0:
            return 0
        
        remainder = abs(a)
        divisor = abs(b)
        
        while remainder >= divisor:
            remainder = self.subtract(remainder, divisor)
        # Adjust the sign based on the input
        return remainder if a >= 0 else -remainder

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))