#!/usr/bin/env python3


def fahrenheit(temp_in_celsius):
    result = (temp_in_celsius * 9 / 5) + 32
    return result


def main():
    for num in range(0, 51):
        print("Result ", num, "=", fahrenheit(num))


main()
