'''
Author: Georges Hassana
12/19/2018

Description:
	The goal of this question is to write a software library that 
	accepts 2 version string as input and returns whether one is 
	greater than, equal, or less than the other. 

Example: 
“1.2” is greater than “1.1”.

Output:
“1.2” is greater than “1.1”.
'''

def compareVersions(version1, version2):
	'''
	The function takes as two inputs version1 and version2
	and return the version1 greater than version2 or
	version1 less than version2 or version1 and version2 are equal
	'''
	#split by the character "."
	sp_version1 = version1.split(".")
	sp_version2 = version2.split(".")
	# Get the length of the string
	l1 = len(sp_version1)
	l2 = len(sp_version2)
	if l1 > l2:
		sp_version1 += ['0' for _ in range(l1 - l2 )]
	elif(l1 < l2):
		sp_version2 += ['0' for _ in range(l2 - l1 )]

	index = 0
	while index < l1:
		if int(sp_version1[index]) > int(sp_version2[index]):
			return "version 1 is greater than version 2"
		elif int(sp_version1[index]) < int(sp_version2[index]):
			return "version 1 is less than version 2"
		else:
			index +=1
	
	return "version 1 and version 2 are equal"

#Test
if __name__ == '__main__':
	print(compareVersions("7.3.2.1","7.2.8.1"))
	print(compareVersions("24.0","114.1.0"))
	print(compareVersions("05.0","5.0.0"))



	


 

