def get_num_words(content):
	splited_content = len(content.split())
	return(splited_content)


def letter_count(content):
	letter_dict = {}
	for i in content.split():
		for j in i.lower():
			letter_dict[j] = letter_dict.get(j, 0) + 1
	return letter_dict