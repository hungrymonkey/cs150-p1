""" Pylint told me I should add an doc String"""

def sanitize_input( var_i ):
    if all( 0 <= i <= 1 for i in var_i[:-1]) is False:
       return False
    return True


def check_config( var_i ):
    inital_config = var_i(len(var_i)-1)
    if len(var_i) - 1 <= inital_config:
       return False
    return sum( var_i[:-1]) == 0

