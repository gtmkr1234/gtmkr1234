inupt_list = eval(input())
output_list = []
for i in inupt_list :
    if i not in output_list:
        output_list.append(i)
print(output_list)