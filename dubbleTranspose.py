# encoding: utf-8
def deb ():
    print ".deb files goes meh! So dependant"
    return

def dubbleTransposse_encryption(key, secret):   #  Tested enough, but not fool proof, needs to be tested with  different keys and secret
    '''
    takes key and secret creates cipher text and encrypt it too then it returns the result.
    Remember that dubble encryption require this function twice.
    :param key: consist of string or list with 1 dimension. And only unique letter becuase dubblicate one krasches the
                algorithm.
    :param secret: the use of char -1 or -2 is strictly forbidden! If it happens anyway the result should not be trusted
           I trust that the user follows that direction otherwise it's the users fault. Adding the .remove('-2') at the
           begining works bu must be added.
    :return: gibberish whitch require decryption in order to read
    '''
    #calc nr of filled rows, nr of empty row slots and nr of col.

    '''
index :      1-n
 "    -------------------
 0    |  col header     |
 -    -------------------
 1-n  | rows of data    |
      -------------------
       row 0  contain col header used for sorting and arrenging columns.
    '''
    #retrieve and calc
    encyptionList = ['-1']
    keyHold = key # try ->  "ab"
    keyLength = len(keyHold) # makes columns
    cache = secret # try -> "abcdefghijk"
    cacheLength = len(cache)
    Fullrows = cacheLength / keyLength
    nrOfEmptySpaces = (keyLength -(cacheLength % keyLength))
    if nrOfEmptySpaces > 0:
        Fullrows += 1
    numberOfElements = keyLength * Fullrows



    # Generate empty 2D list with n rows and m col.
    master = []
    for i in range(keyLength):
        master.insert(0, [])
    for j in range((numberOfElements+1)):
        if j == 0:
            for p in range(keyLength):
                master[p].append(keyHold[p])
        else:
            master[(j % keyLength)].append('-1')

    #print master

    # Fill 2D list with elements row by row. When empty string apply the rest of empty spaces
    # the row 0 are only for sorting and column swapping. Never read it as part in encryption message.
    row = 1; col = 0
    for h in range(cacheLength):

        if row == 0:
            row = (row % Fullrows) + 1
        master[col][row] = cache[h]
        col = (col + 1) % keyLength
        if col == 0:
            row = (row % Fullrows) + 1

    # Sort the 2D list columns chronological with a as the lowest at the left side.
    master.sort()
    # Read col for col where we skip 'special char None or -1' into the encryption list/string and return result
    row = 1; col = 0
    for e in range(numberOfElements):
        if (master[col][row] != '-1') and row != 0:
            encyptionList.insert(0, master[col][row])
        row = row % Fullrows +1
        if row == 1:
            col = (col + 1) % keyLength
    encyptionList.reverse()
    encyptionList.remove('-1')
    return encyptionList
'''     Ändra kolumner
krav:
    * two identiska tmp columner som motsvarar 2D listans kolumner
    * nrOfRows nrOfCol
for a in range(5):  # range is nrOfCol
    for b in range(5): # range is nrOfCol
        if cheatSheat[a] == TwoD[b][0]:
            for f in range(3): # range depends on nr of rows
                tmpCol[0][f] = TwoD[a][f]
                tmp2Col[0][f] = TwoD[b][f]
                # copy a col into tmpCol, copy e col into tmp2Col
                #Now tmpCol overwrite e col
                TwoD[b][f] = tmpCol[0][f]
                #Now tmp2Col overwrite a col
                TwoD[a][f] = tmp2Col[0][f]
'''
def dubbleTransposse_decryption(key, encrypted_text):   # got problems length on
    '''
    With key and encrypted text we recreate the secret code.
    Remember that dubble encryption require this function twice.
    :param key: text string. And only unique letter becuase dubblicate one krasches the
                algorithm.
    :param encrypted_text:
    :return:
    '''

    # calc nr of filled rows, nr of empty row slots and nr of col.
    decryptionList = ['-1']
    keyHolder = key # default "ab"
    keyLength = len(keyHolder)  # makes columns
    encryptedMessg = encrypted_text  # default ['a','b','c','d','e','f','g','h','i','j','k']
    encryptedMessgLength = len(encryptedMessg)
    Fullrows = encryptedMessgLength / keyLength  # contains soon total rows exkl row 0
    nrOfEmptySpaces = (keyLength - (encryptedMessgLength % keyLength))
    leftover = encryptedMessgLength % keyLength
    if nrOfEmptySpaces > 0 and leftover > 0:
        Fullrows += 1
    numberOfElements = keyLength * Fullrows # includes empty slots
    # Generate empty 2D list with n rows and m col. (calc nr of rows, keylength == nrOfCol)
    master = []
    for i in range(keyLength):
        master.insert(0, [])
    for j in range((numberOfElements + 1)):
        if j == 0:
            for p in range(keyLength):
                master[p].append(keyHolder[p])
        else:
            master[(j % keyLength)].append('-1')
    # Mark the loweest row elements from the lowest right col      <--------------------- untill here it works
    countDown = keyLength - 1
    for mark in range(nrOfEmptySpaces):
        if leftover > 0:
            master[countDown][(Fullrows)] = '-2'
            countDown -= 1
    # sort the cols alphabetically
    master.sort()
    # Read the elements into the 2D list and jump '-2' spaces. column by column
    row = 1;col = 0
    for h in range(encryptedMessgLength): # error writes data

        if master[col][row] == '-2':
            row = (row + 1) % Fullrows
            col = (col + 1) % keyLength
        elif row == 0 : # never write to row 0 and -2 elements
            row += 1
        master[col][row] = encryptedMessg[h]
        row = (row % Fullrows) + 1
        if row == 1:
            col = (col + 1) % keyLength
    # swap cols so that the col headers match the key       <------------ works but needs more tests

    # used to swap columns
    tmpCol = [['+']]; tmp2Col = [['+']]
    for round in range(Fullrows):
        tmpCol[0].append('-')
    for round in range(Fullrows):
        tmp2Col[0].append('-')

    for a in range(keyLength):  # range is nrOfCol
        for b in range(keyLength):  # range is nrOfCol
            if keyHolder[a] == master[b][0]:
                if keyLength == 2 and a == 1:
                    continue
                elif keyLength == 1:
                    continue
                else:
                    for f in range(Fullrows + 1):  # range depends on nr of rows because f walks throug the rows in the columns. +1 with fullrows covers the header row
                        tmpCol[0][f] = master[a][f]
                        tmp2Col[0][f] = master[b][f]
                        # copy a col into tmpCol, copy e col into tmp2Col
                        # Now tmpCol overwrite e col
                        master[b][f] = tmpCol[0][f]
                        # Now tmp2Col overwrite a col
                        master[a][f] = tmp2Col[0][f]
    # read row by row into Decypted string and return it.   <-------- works but need no tests
    row1 = 1;col1 = 0
    for e in range(numberOfElements):
        if (((master[col1][row1] != '-2') and (row1 != 0) ) and col1 < keyLength):
            decryptionList.insert(0, master[col1][row1])
        col1 = ((col1 + 1) % keyLength)
        if col1 == 0:
            row1 = (row1 % Fullrows) + 1
    decryptionList.reverse()
    decryptionList.remove('-1')
    return decryptionList
