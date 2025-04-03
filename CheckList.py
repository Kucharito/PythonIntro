list1=[10,20,30,40,10]

def check_list(list1):
    if list1[0]==list1[-1]:
        print("Prvky na prvom a poslednom indexe sa rovnaju")
        return True
    else:
        return False

print(check_list(list1))

