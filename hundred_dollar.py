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
	for s in fin:
		if getWordValue(s) == 100:
			fout.write(s)
	fin.close()
	fout.close()

if __name__ == "__main__":
	getHundredDollarWords()













