def my_task():
    for i in range(len(lst)):
        print(i + 1, lst[i] )
    x = input("Please, enter number (1, 2, 3, 4, 5, 0) ")
    meny[x]()


def add_task():
    l = input("Please enter a new task ")
    lst.append(l)
    my_task()


# def correct_numer():
#     while True:
#         if x in "12345":
#             break
#         else:
#             print("Enter correct number")
#             x = input()


def exit_task():
    task = ["1. List task",
            "2. Add task",
            "3. change task",
            "4. delete task",
            "5. Exit"]
    for row in task:
        print(row)
    x = input("Please, enter number (1, 2, 3, 4, 5) ")
    meny[x]()


def buy_buy():
    print("Goodbye".center(34))


def change_task():
    x1 = input("enter number tasks ")
    x11 = int(x1)
    x2 = input("Enter a new task ")
    lst[x11-1] = x2
    my_task()


def delete_task():
    x3 = input("What task  do you want to delete? ")
    x33 = int(x3)
    lst.pop(x33 - 1)
    my_task()


a = "Walk the dog"
b = "Take the child to the garden"
c = "Go to football with the child"
d = "Clean the apartment"
e = "Cook dinner"
lst = [a, b, c, d, e]
print("Notebook".center(34))
meny = {"1": my_task,
        "2": add_task,
        "0": exit_task,
        "5": buy_buy,
        "3": change_task,
        "4": delete_task}
exit_task()

