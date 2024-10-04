def calculate_length_rec(string: str, cur_count: int = 0) -> int:
    """
    Get the length of the string passed in recursively. 
    """
    if not string:
        return 0
    return 1 + calculate_length_rec(string[1:])


def main():
    str_1 = "word"
    str_2 = "LucidProgramming"
    print(calculate_length_rec(str_1))
    print(calculate_length_rec(str_2))

if __name__ == "__main__":
    main()
