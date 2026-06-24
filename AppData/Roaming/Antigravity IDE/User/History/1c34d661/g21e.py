def reverse_string(word: str) -> str:
    reversed_word = ""
    position = len(word) - 1

    while position >= 0:
        reversed_word = reversed_word + word[position]
        position = position - 1

    return reversed_word


if __name__ == "__main__":
    print("--- Running Placement Practice Code ---")

    input_1 = "python"
    output_1 = reverse_string(input_1)
    print(f"Input: {input_1} | Output: {output_1}")

    input_2 = "college"
    output_2 = reverse_string(input_2)
    print(f"Input: {input_2} | Output: {output_2}")

    print("---------------------------------------")