def remove_chars(input_string, n):
    if n > len(input_string):
        print("Number of characters to remove is greater than the length of the string.")
        return None
    else:
        print(input_string[n:])

if __name__ == "__main__":
    input_string= input("Input your string ")
    number_of_chars=int(input("Input number of chars to remove "))
    remove_chars(input_string, number_of_chars)
