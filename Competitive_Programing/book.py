
# Arithmetic progression :
# When the distance between two consecutive
# elements are same. Here the distance two consecutive elements is 4.
eg= [3,7,11,15]
solution = (len(eg)*(eg[0]+eg[len(eg)-1]))//2
print(solution)

# Geometric progression :
# When the distance between two consecutive
# elements are same. Here the ratio betwwen two consecutive elements is 1/2.

eg = [3,6,12,24]
k = eg[1]//eg[0] # The ratio betwwen two consecutive elements
solution = ((eg[len(eg)-1]*k) - eg[0])  // (k-1)
print(solution)