def display_styles(text):
    # 1. Normal
    print("Normal:")
    print(text)
    print()

    # 2. Reverse
    print("Reversed:")
    print(text[::-1])
    print()

    # 3. Diagonally normal
    print("Diagonally normal:")
    for i, c in enumerate(text):
        print(" " * i + c)
    print()

    # 4. Diagonally reversed
    print("Diagonally reversed:")
    for i, c in enumerate(text[::-1]):
        print(" " * i + c)
    print()

if __name__ == "__main__":
    word = "banana"
    display_styles(word)