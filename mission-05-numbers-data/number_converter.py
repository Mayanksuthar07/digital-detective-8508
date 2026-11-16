def main():
    try:
        number = int(input("Enter a non-negative decimal integer: "))
    except ValueError:
        print("Please enter a whole number, such as 13.")
        return
    except EOFError:
        print("No input was provided.")
        return

    if number < 0:
        print("Please enter zero or a positive number.")
        return

    print("Binary:", bin(number))
    print("Hexadecimal:", hex(number))


if __name__ == "__main__":
    main()
