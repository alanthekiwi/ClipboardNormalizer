# ClipboardNormalizer

 A super-simple and silly python program that normalizes content in your clipboard if there's foriegn characters in it. I originally made it so that I can cheat a certain Discord Bot's economy system which gives you stuff to type. You can't copy-paste it cause the text content uses zero width unicode characters to discourage such activity. Butt, this program allows you to do so!
 
 This program is super useless for anything besides that, or so I think. Congratulations if you can find a proper use case.

## Requirements

- [Python](https://www.python.org/) 3.7 or above.
- [unidecode](https://pypi.org/project/Unidecode/) (normalizing the unicode)
- [pyperclip](https://pypi.org/project/pyperclip/) (clipboard functions)

### Notes

This program was written specifically to run on Windows platforms. I have not tested this on other platforms. It should work though, maybe.

### Extra

If you're on windows, you can rename the `.py` extension to `.pyw` to hide the console because this application is meant to be a headless one.

If you're planning to freeze the source to an executable. I'd recommend [PyInstaller](https://www.pyinstaller.org/).
Run the following command for the best results:
`pyinstaller clipboardNormalizer.py --onefile --noconsole`

### Todos

- Maybe some additional features to make it useful? Not too sure, this was a silly program anyway.

License
----

MIT License
