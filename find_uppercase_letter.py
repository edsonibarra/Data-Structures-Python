def find_uppercase_recursively(string: str) -> str:
    def _find(string: str):
        if not string:
            return "Not Found"
        if string[0].isupper():
            return string[0]
        return _find(string[1:])
    return _find(string)


def find_uppercase_iteratevely(string: str) -> str:
    for c in string:
        if c.isupper():
            return c
    return "Not found"

def main():
    str_1 = "lucidProgramming"
    str_2 = "LucidProgramming"
    str_3 = "lucidprogramming"
    
    print("Recursively")
    print(find_uppercase_recursively(str_1))
    print(find_uppercase_recursively(str_2))
    print(find_uppercase_recursively(str_3))

    print("Iterative")
    print(find_uppercase_iteratevely(str_1))
    print(find_uppercase_iteratevely(str_2))
    print(find_uppercase_iteratevely(str_3))


if __name__ == "__main__":
    main()
