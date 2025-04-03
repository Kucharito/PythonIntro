def find_string(input_string, substring):
    count=input_string.count(substring)
    return count

input_string= input("Input your string here: ")
substring= input("Input your substring here: ")
print(substring, "appeared ", find_string(input_string, substring), "times in the string")

