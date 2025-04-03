def divisible_by_five(list):
    if len(list) == 0:
        return False
    else:
        for i in list:
            if i %5==0:
                print(i)


if __name__ == "__main__":
    list = [10, 20, 33, 46, 55]
    divisible_by_five(list)
