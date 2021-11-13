#Traditional way to sum the elements in the list.
# listofNum = [1,2,3,4,5]
# sum = 0
# for i in listofNum:
#     sum = sum + i
# print(sum)

#recursion way of summing up the elements in a list
def list_sum(num_list):
    if len(num_list)== 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
print(list_sum([2,4,5,6,7]))