from asyncio import gather

from convert import string_to_float

'''This function takes no parameters because it gets the input from the user and sees if the value is a float using the 
defined function string_to_float in convert.py. If the input from the user is indeed a float, it appends it to user_list 
and returns it to the console'''
def gather_numbers()->list[float]:
    user_list = []
    for i in range(10):
        user_input = input('Enter a number!')
        if string_to_float(user_input) is not None:
            user_list.append(float(user_input))
    print( user_list)
    return user_list

if __name__ == '__main__':
    print(sum(gather_numbers()))