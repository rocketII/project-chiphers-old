# encoding: utf-8
def deb ():
    print ".deb files goes meh! So dependant"
    return

def dubbleTransposse_encryption(key, secret):
    '''
    takes key and secret creates cipher text and encrypt it too then it returns the result
    :param key:
    :param secret: the use of char -1 is strictly forbidden!
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
def dubbleTransposse_decryption(): # (key, encrypted_text)
    # calc nr of filled rows, nr of empty row slots and nr of col.

    # Generate empty 2D list with n rows and m col. (calc nr of rows, keylength == nrOfCol)

    # Mark the loweest row elements from the lowest right col

    # sort the cols alphabetically

    # Read the elements into the 2D list and jump empty spaces.

    #swap cols so that the col headers match the key

    # read row by row into Decypted string and return it.

    return
