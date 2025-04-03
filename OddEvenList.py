list1=[10,20,25,30,35]
list2=[40,45,60,75,90]

def odd_even_list(list1, list2):
    list3=[]
    for i in list1:
        if i%2!=0:
            list3.append(i)

    for i in list2:
        if i%2==0:
            list3.append(i)
    return list3

print("Result list",odd_even_list(list1, list2))