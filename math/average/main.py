# Find mean, mode, median

def mean(nums: list) -> float:
    if not nums:
        raise ValueError("List is empty")
    return sum(nums) / len(nums)

def median(nums: list) -> float:
    sorted_list = sorted(nums)
    length = len(sorted_list)
    mid_index = length >> 1
    return (
        (sorted_list[mid_index] + sorted_list[mid_index - 1]) / 2
        if length % 2 == 0
        else sorted_list[mid_index]
    )

def mode(nums: list) -> list:
    result = list()
    for x in nums:
        result.append(nums.count(x))
    if not result:
        return []
    y = max(result)
    result = {nums[i] for i, value in enumerate(result) if value == y}
    return sorted(result)

if __name__ == "__main__":
    numbers = [2, 4, 5, 5, 6, 8, 9]

    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")