""" 
Geometry
"""
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def area_of_triangle(p1, p2, p3):
    return abs((p1[0] * (p2[1] - p3[1]) + 
                p2[0] * (p3[1] - p1[1]) + 
                p3[0] * (p1[1] - p2[1])) / 2.0)

def convex_hull_graham_scan(points):
    def cross_product(O, A, B):
        return (A[0] - O[0]) * (B[1] - O[1]) - (A[1] - O[1]) * (B[0] - O[0])
    
    points = sorted(set(points))
    
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

print(distance((1, 2), (4, 6)))
print(area_of_triangle((0, 0), (0, 3), (4, 0)))
print(convex_hull_graham_scan([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0)]))