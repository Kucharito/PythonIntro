def reverse_order_number(digits):
    reversed_digits = ' '.join(str(digits)[::-1])
    return reversed_digits

if __name__ == "__main__":
    print(reverse_order_number(123456))