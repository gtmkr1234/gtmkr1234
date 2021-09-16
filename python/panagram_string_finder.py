input_string = input("Enter the string: ")
for i in range(97,123)and(65,91) :
    if chr(i) not in input_string:
        print("String is not panagram...")
        break
else :
    print("String is panagram...")
    