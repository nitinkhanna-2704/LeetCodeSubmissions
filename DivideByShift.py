

class Solution(object):

'''
Object ot declare division operation based on repeated subtraction.
'''
    def divide(object , dividend, divisor):
    '''
    Divide operations for numbers between (-2**31 -1 , 2**31 -1)
    '''
        if(dividend == 1<<31 and divisor == -1):
            return 2**31 -1
        elif(dividend == -1<<31 and divisor == -1):
            return  2**31 -1

        if dividend >=0 and divisor >= 0:
            sign = True

        elif dividend < 0 and divisor < 0:
            sign = True

        else:
            sign = False


        abs_dvnd, abs_div = abs(dividend), abs(divisor)
        q = 0

        while abs_dvnd >= abs_div:
            shift = 0

            while abs_dvnd >= (abs_div << (shift)):
                shift += 1

            q += 1 << (shift-1)

            abs_dvnd -= abs_div << (shift - 1)



        return q if sign is True else -q
