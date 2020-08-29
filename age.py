# Input (yes/no) for having been driving or not first
# Then input your age to tell if legal

driving = input('Have you been driving before? ')
if driving != 'yes' and driving != 'no':
	print('Please input yes/no')
	raise SystemExit

age = input('How old are you? ')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('Congratulations! You have a driving license')
	else:
		print('Wow, how have you been driving before?')
elif driving == 'no':
	if age >= 18:
		print('Fine, you can get a driving license when you pass through the test.')
	else:
		print('Be patient! you can get a driving license in several years.')
 