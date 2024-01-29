# Usage: 
# py.exe multiclipBoard.pyw save <keyword> - Saves clipboard to keyword.
# py.exe multiclipBoard.pyw delete <keyword> - deletes clipboard to keyword.
# py.exe multiclipBoard.pyw <keyword> - Loads keyword to clipboard.
# py.exe multiclipBoard.pyw list - Loads all keywords to clipboard.
# py.exe multiclipBoard.pyw clear - clears clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# Save clipboard content:the first condition checks if there are exactly three arguments passed to the script.
# The second condition checks if the second argument is the string "save" in lowercase.
# If both conditions are true, the code saves the current clipboard content to the mcbShelf dictionary with the key specified in the third argument (sys.argv[2])

if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# delete specific keyword and its content
if len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == "clear":
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
