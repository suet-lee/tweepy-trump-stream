import re

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def findPhrase(needle, haystack):
	if re.search(needle, haystack, re.IGNORECASE):
		return True
	else:
		return False

def countPhrase(phrase, string):
	count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(phrase), string))
	return count
