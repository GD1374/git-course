import os


def welcome():
    print('-------------')
    print('Developer: Mahdi Malekifard')
    print('status: junior')
    print('-------------')


def clean_screen():
    os.system('cls')


def get_input():
    my_list = []
    while True:
        nums_for_list = int(input('Enter a number: '))
        if nums_for_list == 0:
            break
        my_list.append(nums_for_list)
        print(my_list)
    return my_list


def calc_max_number(a_list):
    max_num = 0
    for num in a_list:
        if num > max_num:
            max_num = num
    return f'The Max Number is : -- {max_num} --'


def run():
    clean_screen()
    welcome()
    print(calc_max_number(get_input()))


if __name__ == "__main__":
    run()
