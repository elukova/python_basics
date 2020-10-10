
my_list = [3, 5, 3, 3, 2]
print("Rating list: ", my_list)
user_answer = input("Do you want to expand the rating list? Press 'y' or 'n' ")
while user_answer != "n":
    my_list = sorted(my_list)
    new = float(input("Enter a number: "))
    my_list.append(new)
    my_list.sort(reverse=True)
    print("Rating list: ", my_list)
    user_answer = input("Do you want to expand the list more? Press 'y' or 'n' ")
