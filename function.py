'''
funtion to compare two test marks and return the higher one


'''

# function to compare 2 test marks.
def tests(test1, test2):
#test if both test marks are equal
	if test1 == test2:
# if they are the same, return any of them		
		
		return test1
	else:
# I f not equal, return the second test mark 		
		return test2
# Here, we are asking the user to fill in the marks for test one and test two.
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
Function to calculate final coursework marks.
'''
def courseWrk(cswork):
# Here, we re evoking the tests function to get one test mark.
	testsMark = tests(test1,test2)
# Calculate the average of coursework and test mark
	avgtestsCswork = (cswork + testsMark)/2
# Calculate 40% of the average
	fnltestsCswork = avgtestsCswork * (40/100)
# print a seperate line
	print('..............................')
# Display the final coursework marks.
	print('your final coursework marks is: ', fnltestsCswork)
# Print another seperate line
	print('..............................')
# Asking the user to enter their coursework mark 
cswork = int(input('Please enter your course work Marks: '))
# Call thw function to calculate and display final result.
courseWrk(cswork)