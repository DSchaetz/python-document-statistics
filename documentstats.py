###################################################################################
# Python Document Statistics
# Analyzes text files to calculate total word count
# and identify the 10 most frequently occurring words.
###################################################################################
import sys
import string

def readFile(filename):

	#Opening text file to read the contents.
	with open(filename, 'r') as file:
		contents = file.read()
	return contents

def wordCount(contents):

	#Stop-words to be ignored in the word count.
	stopWords = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but',
             'by', 'for', 'from', 'had', 'has', 'have', 'he',
             'her', 'his', 'how', 'i', 'in', 'is', 'it', 'its',
             'me', 'my', 'not', 'of', 'on', 'or', 'our', 'she',
             'that', 'the', 'their', 'them', 'there', 'they',
             'this', 'to', 'was', 'we', 'were', 'what', 'when',
             'where', 'which', 'who', 'will', 'with', 'you', 'your',
	     'all', 'some', 'if', 'do', 'into', 'upon', 'one']

	#Splitting words to lowercase to eliminate same word differences, as well as punctuation.
	contents = contents.translate(str.maketrans('', '', string.punctuation))
	words = contents.lower().split()
	#Adding total amount of words in the file.
	print("Total Word Count:", len(words))

	#Creating a dictionary to each words and the count.
	wordCountDict = {}

	#Counting the amount of words that appear with ignored stop-words.
	for word in words:
		if word not in stopWords:
			if word in wordCountDict:
				wordCountDict[word] += 1
			else:
				wordCountDict[word] = 1
	return wordCountDict

def topTenWords(wordCountDict):

	#Sorting the dictionary numerically by the word count
	sortedWords = sorted(wordCountDict.items(), key=lambda item: item[1], reverse=True)

	#Top ten words with the counts of each
	print("Top 10 Words:")
	for word, count in sortedWords[:10]:
		print(word, count)

def main():
		if len(sys.argv) < 2:
			print("Usage: python documentstats.py filename.txt")
			sys.exit(1)

		filename = sys.argv[1]

		contents = readFile(filename)

		wordCountDict = wordCount(contents)

		topTenWords(wordCountDict)

if __name__ == '__main__':
		main()
    