def remove_duplicates(sequence):
    """Return a new list with duplicates removed without using built-in set() or dict()."""
    result = []
    for item in sequence:
        found = False
        for existing in result:
            if existing == item:
                found = True
                break
        if not found:
            result.append(item)
    return result


if __name__ == '__main__':
    raw_input = input('Enter values separated by spaces: ').strip()
    values = raw_input.split()
    unique_values = remove_duplicates(values)
    print('Unique values:', unique_values)
