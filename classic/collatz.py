def collatz(n):
    steps = 0
    while n > 1:
        n = n*3 + 1 if n % 2 else n/2
        steps = steps + 1
    print "Steps:",steps

collatz(3)
