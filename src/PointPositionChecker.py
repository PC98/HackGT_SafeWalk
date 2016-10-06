R =  0.00001
def makeLine(checkX, checkY, givenX1, givenY1, givenX2, givenY2):
	line3 = [givenX2 - givenX1, givenY2 - givenY1, givenY1**2 + givenX1**2 - givenY1*givenY2 - givenX1*givenX2]
	line4 = [givenX2 - givenX1, givenY2 - givenY1, -givenY2**2 - givenX2**2 + givenY1*givenY2 + givenX1*givenX2]
	line1 = [givenY1 - givenY2, givenX2 - givenX1, -givenY1*givenX2 + givenX1*givenY2 + R]
	line2 = [givenY1 - givenY2, givenX2 - givenX1, -givenY1*givenX2 + givenX1*givenY2 - R]
	tmp1 = sign(line1, checkX, checkY) * sign(line2, checkX, checkY)
	if(tmp1 == 0):
		return True
	elif(tmp1 < 0):
		tmp2 = sign(line3, checkX, checkY) * sign(line4, checkX, checkY)
		if tmp2 <= 0:
			return True
		elif((checkX - givenX1)**2 + (checkY - givenY1)**2 - R**2 <=0 or (checkX - givenX2)**2 + (checkY - givenY2)**2 - R**2 <= 0) :
			return True
		else:
			return False
	else:
		return False
def sign(line, checkX, checkY):
	value = checkX * line[0] + checkY * line[1] + line[2]
	return value
