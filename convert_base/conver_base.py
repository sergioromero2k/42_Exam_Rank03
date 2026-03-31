#!/usr/bin/env python3

def convert_base(number: str, from_base: int, to_base: int) -> str:
    decimal = int(number, from_base)
    if decimal == 0:
        return '0'
    digits = "0123456789ABCDEF"
    result = ""
    while decimal > 0:
        result = digits[decimal % to_base] + result
        decimal //= to_base
    return result


def main() -> None:
    print(convert_base("ff", 16, 2))
    print(convert_base("10", 2, 10))


if __name__ == "__main__":
    main()
