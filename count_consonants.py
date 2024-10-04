def count_consonants(string: str) -> int:
    vowels = ("a", "e", "i", "o", "u")
    if not string:
        return 0
    if string[0] not in vowels:
        return 1 + count_consonants(string[1:])
    return count_consonants(string[1:])


print(count_consonants('aeiomd'))