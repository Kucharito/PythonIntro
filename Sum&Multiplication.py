def product_function(number1,number2):
    product=number1*number2
    if (product)>1000:
        print("Súčet čísel je väčší ako 1000")
        print("Súčet čísel je: ", number1+number2)
        return number1+number2
    else:
        print("Súčet čísel je menší ako 1000")
        print("Súčin čísel je: ", number1*number2)
        return number1*number2

if __name__ == "__main__":
    for i in range(3):
        number1 = int(input("Zadaj si cislo number1\n"))
        number2 = int(input("Zadaj si cislo number2\n"))
        product_function(number1, number2)

