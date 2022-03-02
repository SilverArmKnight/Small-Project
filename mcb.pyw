#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Delete keyword from the shelf.
#        py.exe mcb.pyw delete - Delete all keywords from the shelf.
#
#        There will be situations in which <keyword> is "list" or "delete", but
#        I will not be handling it anytime soon.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')      # Create and save to a shelf file.

# Check if it's either save <keyword> or delete <keyword>
if len(sys.argv) == 3:
    # py.exe mcb.pyw <save> keyword.
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # py.exe mcb.pyw delete <keyword>    
    elif sys.argv[1].lower() == 'delete':
        mcbShelf[sys.argv[2]] = ''
    else:
        print("FUCK YOU!")

# Check if it's <keyword>, list or delete.
elif len(sys.argv) == 2:
    # py.exe mcb.pyw <keyword>
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # py.exe mcb.pyw list
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # py.exe mcb.pyw delete
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

mcbShelf.close()