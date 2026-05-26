def normalize_text(text: str) -> str:
    """Return normalized text for anagram comparison."""
    return ''.join(sorted(text.replace(' ', '').lower()))


def is_anagram(first: str, second: str) -> bool:
    """Return True if the two strings are anagrams."""
    return normalize_text(first) == normalize_text(second)


if __name__ == '__main__':
    first_string = input('Enter the first string: ').strip()
    second_string = input('Enter the second string: ').strip()

    if is_anagram(first_string, second_string):
        print(f'"{first_string}" and "{second_string}" are anagrams.')
    else:
        print(f'"{first_string}" and "{second_string}" are not anagrams.')
