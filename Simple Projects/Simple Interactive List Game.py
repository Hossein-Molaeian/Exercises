lst = [0, 1, 2]


def user_index():
    check = True
    while check:
        result = input("Choose an index to replace its content (0,1,2): ")
        if (result in ['0', '1', '2']) and (result.isdigit()):
            check = False
            return result
        else:
            print("Sorry that's not a correct index, try again.")


def user_content():
    result2 = input(
        "What do you want to replace your index's content with: ")
    lst[int(user_index())] = result2
    return lst


def playing():
    check2 = True
    while check2:
        result3 = input("Do you want to play again? (Y/N): ")
        if result3 in ["Y", "y"]:
            print(user_content())
        elif result3 in ["N", "n"]:
            check2 = False
        else:
            print("Sorry I don't understand, please enter y or n: ")


print(user_content())
playing()
