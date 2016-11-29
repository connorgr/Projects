'''
List the Fibonacci sequence up to and including the nth number.
Indexing starts at 1.
'''
def fibonacci(nth):
    sequence = [0, 1]
    if nth > 2:
        for i in xrange(2, nth):
            sequence.append(sequence[i-1]+sequence[i-2])
    print sequence[:nth]

'''
Print the largest Fibonacci number that is less than n
'''
def fibonacciLT(n):
    if n < 0:
        raise ValueError("n must be equal to or greater than 0")
    elif n == 0 or n == 1:
        print n
    else:
        sequence = [0, 1]
        i = 2
        while sequence[-1] < n:
            sequence.append(sequence[i-1]+sequence[i-2])
            i = i + 1
        print sequence[-2]

fibonacci(10)
fibonacciLT(35)
