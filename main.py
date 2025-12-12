from stats import get_num_words, letter_count
import sys

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	# print(sys.argv[1])
	book_content = get_book_text(book_path)
	num_word = get_num_words(book_content)
	# print(f"Found {num_word} total words")
	dict_word = letter_count(book_content)
	print(f"Usage: python3 main.py {book_path}")
	print(f""" 
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
		""")
	for i in dict_word:
		print(f"{i}: {dict_word[i]}")
	


main()