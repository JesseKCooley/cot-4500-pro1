def ApproximationAlgorithm(value, tolerance):
    iter = 0
    diff = 0.0
    x = value
    while( diff >= tolerance):
            
        print(iter + ' : ' + x)
        iter+=1
        y = x
        x = (x / 2.0) + (1.0 / x)

        diff = abs( x - y)

    print('\nConvergence after '+iter+' iterations')
    
def BisectionMethod(func, a,b, tolerance, max):
    i = 0
    while( abs(b-a)> tolerance and i < max):
        i+=1
        p = (a+b)/2.0

        if ( (func(a) < 0 and func(p)>0) or ( (func(a) > 0 and func(p) < 0) ) ):
            b = p
        else:
            a = p

    return i #number of iterations taken
    
def FixedPointIteration(func, p0, tolerance, max):
    i = 1
    while (i <= max):
        p = func(p0)
        if (abs(p-p0) < tolerance):
            print(p +'\nSUCCESS')
            return
        i +=1
        p0 = p
    print("FAILURE")

def NewtonRaphson(func,funcPrime, pPrev, tolerance, max):
    i=1
    while(i <= max):
        if (funcPrime(pPrev) != 0):
            pNext = pPrev - func(pPrev)/funcPrime(pPrev)
            if (abs(pNext-pPrev) < tolerance):
                #print(pNext + '\nSUCCESS')
                return i
            i += 1
            pPrev = pNext
        else:
            print('FAILURE: DERIVATIVE IS ZERO')
            return
        
    print('FAILURE: MAX ITERATIONS EXCEEDED')



def binary_to_double_precision_float(binary_str):
        # Ensure the binary string is 64 bits
    binary_str = binary_str.ljust(64, '0')

        # Extract sign, exponent, and mantissa
    sign = int(binary_str[0], 2)
    exponent = int(binary_str[1:12], 2)
    mantissa = int(binary_str[12:], 2)

        # Calculate
    sign_multiplier = (-1) ** sign
    decimal_value = sign_multiplier * (1 + mantissa / (2 ** 52)) * (2 ** (exponent - 1023))

        #enforce digits
    return decimal_value         

def calculate_series(x, max_terms, error_threshold):
    result = 0.0

    for k in range(1, max_terms + 1):
        #the series in question
        term = ((-1) ** k) * ((x ** k) / (k ** 3))
        result += term

        # Check if the absolute value of the current term is below the error threshold
        if abs(term) < error_threshold:
            break

    return result, k