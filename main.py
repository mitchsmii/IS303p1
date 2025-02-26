# main page that will call the other functons


# imports f1 (dispalyGameIntro) and the global variable sUserName
from displayGameIntro import displayGameIntro
from f2 import Menu
from f3 import fullGame

# calls displayGameIntro (Function 1) to display game into and return sUserName
sUserName = displayGameIntro()
print(sUserName)

# show menu and show what option user chose
sMenuChoice = int(Menu())
print(sMenuChoice)

fullGame()