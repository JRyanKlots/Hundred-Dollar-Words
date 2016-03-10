"""
This program was created by John Ryan Klots (jrk254@cornell.edu) 
in order to demonstrate an application of programming to 
problem solving. The specific problem in this case is 
that of finding english words whose 'value' is 1 dollar.
The value of a word corresponds to the sum of the values of its letters.

a = 1 cent,
b = 2 cents,
c = 3 cents,
.
.
.
z = 26 cents

The list of possible words (corresponding to wordsEn.txt) are from:
http://www-01.sil.org/linguistics/wordlists/english/

"""

letter_value = "abcdefghijklmnopqrstuvwxyz"

def getLetterValue(c):
	return letter_value.find(c) + 1

def getWordValue(s):
	sum = 0
	for c in s:
		sum += getLetterValue(c)
	return sum

def getHundredDollarWords():
	fin = open("wordsEn.txt")
	fout = open("hundred.txt", "w")
	num_dollar = 0
	num_total = 0
	for s in fin:
		if getWordValue(s) == 100:
			fout.write(s)
			num_dollar += 1
		num_total += 1
	fin.close()
	fout.close()
	print str(num_dollar) + " out of " + str(num_total) + " words are worth a dollar."
	print "Open 'hundred.txt' to see them!"

if __name__ == "__main__":
	getHundredDollarWords()
