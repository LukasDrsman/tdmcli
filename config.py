from colors import *

# Terminal escapes as defined in colors.
# To overwrite color from defines, change the
# escape code in one of the variables and uncomment it:

# black     = '\033[30m'
# red       = '\033[31m'
# green     = '\033[32m'
# yellow    = '\033[33m'
# blue      = '\033[34m'
# violet    = '\033[35m'
# beige     = '\033[36m'
# white     = '\033[37m'
# grey      = '\033[90m'
# none      = ''
# underline = '\033[4m'
# end       = '\033[0m'

# task state flags configuration
flags = [
    # id, symbol, symbol color, text color, overwrite deadline color, commands (short, long), priority index
    ("n", "□ ", violet, white, False, ("uc", "uncheck"), 1),
    ("d", "✔ ", green, grey, True, ("cc", "check"), 0),
    ("i", "⚡", yellow, yellow, False, ("i", "important"), 2)
]

# default flag on creation
defflag = "n"

# path to default file and folder containing todolists
deffile = "~/.tdmcli/todo.tdff"
defpath = "~/.tdmcli/"
# write on exit
writeonexit = True

# prompt configuration
prompt = green + "▶ " + end
# datetime format
dateformat = "%H:%M %a %d %b"
# linenumber format
lnnumf = black + "%2d  " + end
