import random

def main():
    lst = amount_and_element()
    rdm(lst)

def rdm(lst):

    output = random.choice(lst)
    print(f" -> {output}!")


def amount_and_element():
    lst = []
    amt = int(input("YourChoice : "))
    for i in range(0, amt):
        ele = (input())

        lst.append(ele)

    return lst


main()
