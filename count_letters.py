def count_vowels_and_consonants(text):
    vowels_count = 0
    consonants_count = 0

    vowels_set = "aeiouAEIOU"

    for char in text:
        if char.isalpha():
            if char in vowels_set:
                vowels_count += 1
            else:
                consonants_count += 1

    return vowels_count, consonants_count


if __name__ == "__main__":
    print("--- Running Placement Practice Code ---")

    test_word = "placement"
    vowels, consonants = count_vowels_and_consonants(test_word)

    print(f"Input Word: '{test_word}'")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print("---------------------------------------")