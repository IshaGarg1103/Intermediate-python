points2d=[(1,2),(15,1),(5,-1),(10,4)]
points2d_sorted = sorted(points2d)
print(points2d)
print(points2d_sorted) # it will sort according to the x value

points2d_sorted=sorted(points2d, key= lambda x:x[1])
print(points2d)
print(points2d_sorted) # it will sort according to the y value

def sort_by_y(points2d):
    return sorted(points2d)
print(sort_by_y(points2d))

points2d_sorted = sorted(points2d, key = lambda x: x[0]+x[1])
print(points2d)
print(points2d_sorted) # it will sort according to sums of each tuple

