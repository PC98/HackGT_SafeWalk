from math import sqrt

R = 0.00025  # Constant value.


def make_line(checkX, checkY, givenX1, givenY1, givenX2, givenY2):
    # Initializing a series of constants
    diff_X2_X1 = givenX2 - givenX1
    diff_Y2_Y1 = givenY2 - givenY1
    tmp_C_1 = givenY1 * givenY2 + givenX1 * givenX2
    tmp_C_2 = -givenY1 * givenX2 + givenX1 * givenY2
    tmp_C_3 = R * sqrt(diff_X2_X1 ** 2 + diff_Y2_Y1 ** 2)

    # Computing the coefficients of straight lines of form Ax + By + C = 0
    line1 = [-diff_Y2_Y1, diff_X2_X1, tmp_C_2 + tmp_C_3]
    line2 = [-diff_Y2_Y1, diff_X2_X1, tmp_C_2 - tmp_C_3]
    line3 = [diff_X2_X1, diff_Y2_Y1, givenY1 ** 2 + givenX1 ** 2 - tmp_C_1]
    line4 = [diff_X2_X1, diff_Y2_Y1, -givenY2 ** 2 - givenX2 ** 2 + tmp_C_1]

    sign_check_1 = sign(line1, checkX, checkY) * sign(line2, checkX, checkY)
    if sign_check_1 == 0:
        return True
    elif sign_check_1 < 0:
        sign_check_2 = sign(line3, checkX, checkY) * sign(line4, checkX, checkY)
        if sign_check_2 <= 0:
            return True
        elif ((checkX - givenX1) ** 2 + (checkY - givenY1) ** 2 - R ** 2 <= 0 or (checkX - givenX2) ** 2 + (
                    checkY - givenY2) ** 2 - R ** 2 <= 0):
            return True
    return False

def sign(line, checkX, checkY):
    return checkX * line[0] + checkY * line[1] + line[2]
