from typing import Optional

'''This function takes a string value and sees if that value can become a float by using the float() function.
 If it can't, and gets a value error, it returns None'''
def string_to_float(values:str)->Optional[float]:
    try:
       return float(values)
    except ValueError:
        return None
