def check_palindrome(number):
    if number==number[::-1]:
        print("The number is palindrome")
        return True
    else:
        print("The number is not palindrome")
        return False

if __name__ == "__main__":
    number = input("Input your number ")
    check_palindrome(number)