import multiprocessing
import math
import sys
import time

# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorial of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    number=[5000,6000,700,8000]

    start_time=time.time()

    # create a pool of workers processors
    with multiprocessing.Pool() as pool:
        result=pool.map(compute_factorial,number)

    end_time=time.time()
    print(f"Results: {result}")
    print(f"Time taken: {end_time-start_time} seconds")