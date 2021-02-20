#'continue' means continue the loop yes but skip this one (x) for example
#but for 'break' it breaks the cycle completely 

for i in range(5):
	if i == 3:
		continue
	elif i == 4:
		break
print (i)