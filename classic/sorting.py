def bubble(xs):
    for i,x1 in enumerate(xs[:-1]):
        for j, x2 in enumerate(xs[i+1:]):
            j = i + 1 + j
            if xs[j] < xs[i]:
                tmp = xs[i]
                xs[i] = xs[j]
                xs[j] = tmp
    return xs

def merge(xs):
    def combine(a,b):
        ptrA = [0] # stupid hack for how Python scopes parent variables
        ptrB = [0]
        def assignPtr():
            if ptrA[0] >= len(a):
                result = b[ptrB[0]]
                ptrB[0] += 1
            elif ptrB[0] >= len(b):
                result = a[ptrA[0]]
                ptrA[0] += 1
            elif a[ptrA[0]] < b[ptrB[0]]:
                result = a[ptrA[0]]
                ptrA[0] += 1
            else: # b[ptrB] < a[ptrA]
                result = b[ptrB[0]]
                ptrB[0] += 1
            return result
        itr = xrange(len(a)+len(b))
        return [assignPtr() for i in itr]

    def ms(x):
        if len(x) < 2:
            return x
        sortedA = ms(x[:len(x)/2])
        sortedB = ms(x[len(x)/2:])
        return combine(sortedA, sortedB)
    return combine(ms(xs[:len(xs)/2]), ms(xs[len(xs)/2:]))

print bubble([4,2,3,1])
print merge([4,2,3,1])
