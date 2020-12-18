# Unit4-05/usr/bin/env python3
# This program was created by Larry Nkengbeza
# This program was created on December 2020
# This program is adding in for loop with conitiue statement.


def main():
    # Input

    user_input = (input("Enter a how many integer which will be added:"))
    user_input2 = (input("Enter a positive integer which will be added:"))
    addition = user_input2+user_input2
    # Process and Output
    while True:
        if user_input > 0:
            print(user_input2)
            if user_input2 > 0:
                print(user_input2)
                if user_input2 > 0:
                    print(user_input2)
                    if user_input2 > 0:
                        print(user_input2)
                        if user_input2 > 0:
                            print(user_input2)
        if user_input2 > 0:
            print(user_input2)
        else:
            continue
    print("The answer is {0}".format(addition))


if __name__ == "__main__":
    main()
