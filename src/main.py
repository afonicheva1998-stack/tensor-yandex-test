def reverse_string(s: str) -> str:
    return s[::-1]


def main():
    text = input("Введите строку: ")
    print("Результат:", reverse_string(text))


if __name__ == "__main__":
    main()
