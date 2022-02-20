def dec(func):
    def question():
        func()
        while True:
            x = input("repeat? (Yes/No) ").lower()
            if x == "yes":
                func()
            elif x == "no":
                exit_task()
                break
            else:
                print("Enter yes or no")
    return question


def my_task():
    print("My task".center(34))
    for i in range(len(lst)):
        print(i + 1, lst[i])
    x = input("Please, enter number (1, 2, 3, 4, 5, 6, 7, 8, 9, 0) ")
    meny[x]()


@dec
def add_task():
    l = input("Please enter a new task ")
    lst.append(l)
    # my_task()


# def correct_numer():
#     while True:
#         if x in "12345":
#             break
#         else:
#             print("Enter correct number")
#             x = input()


def exit_task():
    print("Main menu".center(34))
    task = ["1. List all task",
            "2. Add task",
            "3. change task",
            "4. delete task",
            "5. Find word",
            "6. Complete the task",
            "7: Show completed task",
            "8: Show incomplete task",
            "9. Exit"]
    for row in task:
        print(row)
    x = input("Please, enter number (1, 2, 3, 4, 5, 6, 7, 8, 9, 0) ")
    meny[x]()


def buy_buy():
    write()
    print("Goodbye".center(34))


@dec
def change_task():
    x1 = input("enter number tasks ")
    x11 = int(x1)
    x2 = input("Enter a new task ")
    lst[x11-1] = x2



@dec
def delete_task():
    x3 = list(map(int, input("What task  do you want to delete? ").split()))
    for i in x3:
        lst.pop(i - 1)


@dec
def find_word():
    w = input("Enter word ")
    for i in range(len(lst)):
        if w in lst[i]:
            print(lst[i])


@dec
def complete_the_task():
    x = list(map(int, input("enter the numbers of completed tasks ").split()))
    for i in x:
        lst[i - 1] = "+" + lst[i-1].upper()
        lst_1.append(lst[i - 1])


def show_completed_task():
    print("My completed task".center(34))
    for i in range(len(lst_1)):
        print(i + 1, lst_1[i])
    x = input("Please, enter number (1, 2, 3, 4, 5, 6, 7, 8, 9, 0) ")
    meny[x]()


def show_incomplete_task():
    print("My incomplete task".center(34))
    k = 0
    for row in lst:
        if row not in lst_1:
            k += 1
            print(k, row)
    x = input("Please, enter number (1, 2, 3, 4, 5, 6, 7, 8, 9, 0) ")
    meny[x]()


def write():
    with open("my_task.txt", "w") as file:
        file.write("My task:".center(34))
        file.write(" \n")
        for row in lst:
            file.write(row + '\n')
        file.write("My completed task:".center(34))
        file.write(" \n")
        for row_1 in lst_1:
            file.write(row_1 + '\n')


lst_1 = []
lst_2 = []
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
        "9": buy_buy,
        "3": change_task,
        "5": find_word,
        "6": complete_the_task,
        "7": show_completed_task,
        "8": show_incomplete_task,
        "4": delete_task}
exit_task()

