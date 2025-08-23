# Common Two Pointers Problems - Python Example

def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        curr_area = min(height[left], height[right]) * width
        max_area = max(max_area, curr_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

heights = [1,8,6,2,5,4,8,3,7]
print("Max water container area:", max_area(heights))
