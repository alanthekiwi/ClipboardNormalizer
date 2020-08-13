# clipboardNormalizer.py

"""
	A super-simple and silly python program that normalizes content in your clipboard if there's foriegn characters.
	I originally made it so that I can copy-paste stuff from the Discord Bot DankMemer's economy system which uses foreign characters instead of spaces to discourage copy pasting.
	
	This program is super useless for anything besides that, or so I think. Congratulations if you can find a proper use case.
"""

from pyperclip import copy, paste
from unidecode import unidecode
from time import sleep 

CHECK_DELAY = 1  # in seconds

def has_unicode_content(string):
	for char in string:
		if ord(char) > 127: return True
	return False

last_string = ''
while True:
	sleep(CHECK_DELAY)
	clipboard = paste()
	
	# Avoid further computing if content matches last normalized content or null.
	if not clipboard or clipboard == last_string: continue
	
	if has_unicode_content(clipboard):
		normalized = unidecode(clipboard)
		if normalized != clipboard:
			copy(normalized)
			last_string = normalized