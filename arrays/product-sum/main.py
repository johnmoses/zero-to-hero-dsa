""" 
Calculate the product sum of a "special" array which can contain integers or nested
arrays. The product sum is obtained by adding all elements and multiplying by their
respective depths.

For example, in the array [x, y], the product sum is (x + y). In the array [x, [y, z]],
the product sum is x + 2 * (y + z). In the array [x, [y, [z]]],
the product sum is x + 2 * (y + 3z).

Example Input:
arr = [5, 2, [-7, 1], 3, [6, [-13, 8], 4]]
depth = 1
Output: 12
"""

def productSum1(arr, depth=1):
    """
    Calculate product sum of special array with nested elements
    """
    total = 0
    for element in arr:
        if isinstance(element, list):
            total += productSum1(element, depth + 1)
        else:
            total += element
    return total * depth

def productSum2(arr: list[int | list], depth: int) -> int:
    total_sum = 0
    for i in arr:
        total_sum += productSum2(i, depth + 1) if isinstance(i, list) else i
        return total_sum * depth

print(productSum1([5, 2, [-7, 1], 3, [6, [-13, 8], 4]],1))
print(productSum2([5, 2, [-7, 1], 3, [6, [-13, 8], 4]],1))