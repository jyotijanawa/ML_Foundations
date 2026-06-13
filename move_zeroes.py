def move_zeroes(nums):
    last_non_zero_pos = 0

    for current_pos in range(len(nums)):
        if nums[current_pos] != 0:
            nums[last_non_zero_pos], nums[current_pos] = nums[current_pos], nums[last_non_zero_pos]
            last_non_zero_pos += 1

    return nums


if __name__ == "__main__":
    print("--- Running Placement Practice Code ---")

    test_array1 = [0, 1, 0, 3, 12]
    test_array2 = [4, 0, 0, 9, 0, 1, 2]

    print(f"Original 1: [0, 1, 0, 3, 12]     -> Result: {move_zeroes(test_array1)}")
    print(f"Original 2: [4, 0, 0, 9, 0, 1, 2] -> Result: {move_zeroes(test_array2)}")
    print("---------------------------------------")