def fibonacci(n):
    """
    This function generates a list of Fibonacci numbers up to the given number n.

    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers, usually starting with 0 and 1.

    This function uses a while loop to generate the Fibonacci sequence. It starts with 0 and 1 and then in each iteration, it adds the last two numbers in the sequence and adds the sum to the list.

    The function returns the list of Fibonacci numbers.

    :param n: The number up to which the Fibonacci sequence should be generated
    :return: A list of Fibonacci numbers up to n
    """
    a , b = 0 , 1
    
    result = []
    while a <= n:
        result.append(a)
        a , b= b,a+b
    return result

i = int(input("Enter the number: "))
print(fibonacci(i))  # prints the list of Fibonacci numbers up to the given number
# All code is written by me , except comments .
