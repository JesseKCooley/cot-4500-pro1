
#import main.assignment_1 as assignment_1
from ..main import assignment_1
#Example function for q6
def example_func(x):
        return ((pow(x,3)) + ( 4 *(pow(x,2)) )- 10)
def examp_funcPrime(x):
        return (3* (pow(x,2)) + (8 *x))

# Binary number to convert
binary_number = "010000000111111010111001"

def test():
        result = assignment_1.binary_to_double_precision_float(binary_number)
        roundResult = round(result,0)
        strResult = '%E' %  (result)
        roundStrResult = '%E' %  (roundResult)
        #answer to q1 (number to 5 digits)
        print(f"{strResult[:6]}\n")
        #answer to q2 (chopped approximation to 3 digits)
        print(f"{strResult[:4]}\n")
        #answer to q4 (rounded approximation to 3 digits)'
        print(f"{roundStrResult[:4]}\n")
        absolute_error = roundResult - result
        relative_error = absolute_error / roundResult
        print(f"Absolute: {absolute_error}\t Relative: {relative_error}\n")
        #problem 5
        error_threshold = 1e-4
        result,terms = assignment_1.calculate_series(1.0,1000,error_threshold)
        print(f'{terms}\n')
        #problem  6
        n = assignment_1.BisectionMethod(example_func,-4,7,0.0001,9999)
        print(f'{n}\n')
        n2 = assignment_1.NewtonRaphson(example_func,examp_funcPrime,-4,0.0001,9999)
        print(f'{n2}\n')
       
test()

