def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome ignoring spaces and case."""
    normalized = ''.join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


if __name__ == '__main__':
    user_input = input('Enter text or number: ').strip()
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')
