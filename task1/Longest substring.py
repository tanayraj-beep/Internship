def longest_non_repeating_substring(s: str) -> str:
    """Return the longest substring without repeating characters."""
    start = 0
    best_start = 0
    best_len = 0
    last_seen = {}

    for index, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = index

        current_len = index - start + 1
        if current_len > best_len:
            best_len = current_len
            best_start = start

    return s[best_start:best_start + best_len]


if __name__ == '__main__':
    user_input = input('Enter a string: ').strip()
    longest = longest_non_repeating_substring(user_input)
    print(f'Longest substring without repeating characters: "{longest}"')
    print(f'Length: {len(longest)}')
