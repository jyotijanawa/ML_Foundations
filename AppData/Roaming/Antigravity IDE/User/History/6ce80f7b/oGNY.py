def find_largest_number(nums):
    if not nums:
        return None

    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


if __name__ == "__main__":
    print("--- Running Placement Practice Code ---")

    test_list = [12, 45, 2, 89, 23, 6]
    result = find_largest_number(test_list)

    print(f"Input List: {test_list}")
    print(f"Largest Number is: {result}")
    print("---------------------------------------")