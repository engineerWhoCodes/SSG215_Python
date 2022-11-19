#Checking the availability of items in a set against a particular set and then checking for avialability
authorsLib = {'Fagunwa', 'Achebe', 'Shakespeare', 'Clark', 'Saro Wiwa', 'Ngugi', 'Nwankwo', 'Austen', 'Eliot', 'Hardy', 'Bunyan', 'Tutuola', 'Delano', 'Ulasi', 'Odunjo', 'Yinka', 'Tho' }
myList = {'Olabode', 'Yuppie', 'Adamu', 'Tho', 'Adichie', 'Achebe', 'Soyinka', 'Nwanko', 'Bronte', 'Rakumi', 'Yinka', 'Loto', 'Mu',}
myDict = {}
for auth in myList:
    if auth in authorsLib:
        myDict[auth] = 'Available'
    else:
        myDict[auth] = 'Not available'
    print('The availability list: ', myDict)