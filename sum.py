# sum_numbers.py
def sum_numbers(nums):
    """
    Function to calculate the sum of a list of numbers
    """
    if not nums:
        return 0
    total = 0
    for num in nums:
        total += num
    return total

# Example usage
if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    print("Sum of numbers:", sum_numbers(numbers))
