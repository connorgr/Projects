def closestPairNaive(pts, distanceFn):
    minPair = [-1, 0, 0]
    for i in xrange(len(pts)):
        for j in xrange(len(pts)):
            if i == j:
                continue
            d = distanceFn(pts[i], pts[j])
            if minPair[0] == -1 or minPair[0] > d:
                minPair = [d, i, j]

def euclid(a,b):
    return sqrt(a*a + b*b)

# How can we improve on this? --> kD tree-type divide and conquer
# 1D for now
def closestPair1d(pts, distanceFn):
    if len(pts) == 1:
        return None
    elif len(pts) == 2:
        return DIFF
    elif len(pts) == 3:
        return DIFF
