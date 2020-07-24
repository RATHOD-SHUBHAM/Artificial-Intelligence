#Todo : Shubham Shankar
# Student ID : 1001761068


from bayseian import bayesian
from sys import argv

givenValue = False
observations = []
query = []

for i in argv:
        if i == "given":
                givenValue = True
        query.append(i)
        if givenValue:
                observations.append(i)

bnet = bayesian()

if query:
	numerator = bnet.nextValues(bnet.getValue(query))
	if observations:
		denominator = bnet.nextValues(bnet.getValue(observations))
	else:
		denominator = 1
	print ("The probability is : %.10f" % (numerator/denominator))
else:
	print ("Invalid query string")