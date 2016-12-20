# Oops! I only did half of the chipher... fix it soon.
def adfgvx_encryption(keyUsing36char, key24transposing , clearTextUsingTheKeyForCoding):
    '''
    ADFGVX famous old cipher, Need more info read some books ;-)
    :param keyUsing36char: must include 0 to 9 and a to z and shuffle it. Send it as "string"
    :param key24transposing:
    :param clearTextUsingTheKeyForCoding:  send it as ['s','c','r','e','t']
    :return: encryptet message
    '''
    secret = clearTextUsingTheKeyForCoding
    secretLength = len(secret)
    encrypted = []
    adfgvx = "adfgvx"

    # create 6x6 matrix using lists
    col0 = [None] * 6
    col1 = [None] * 6
    col2 = [None] * 6
    col3 = [None] * 6
    col4 = [None] * 6
    col5 = [None] * 6
    master =[col0, col1, col2, col3, col4, col5]
    i =0
    for row in range(0,6,1):
        for col in range(0,6,1):
            master[col][row] = keyUsing36char[i]
            i += 1

    # use key char by char and decode, read row by row.
    i = 0
    for i in  range(secretLength):
        for row in range(6):
            for col in range(6):
                if( master[col][row] == secret[i]):
                    encrypted.insert(0, adfgvx[col])
                    encrypted.insert(0, adfgvx[row])
    encrypted.reverse()  # because above algorithm works backwards.
    # halfway, now purge trash.
    del i, secretLength, secret, master, col0, col1, col2, col3, col4, col5
    # make table with key length as nrOfColumns, calc the nr of slots needed and then calc nr of rows. no empty slots needed.
    # Generate empty 2D list with n rows and m col.
    key = key24transposing
    keylength = len(key)
    encryptedlength = len(encrypted)
    Fullrows = encryptedlength / keylength
    nrOfEmptySpaces = (keylength - (encryptedlength % keylength))
    if nrOfEmptySpaces > 0:
        Fullrows += 1
    numberOfElements = keylength * Fullrows


    masterII = []

    # walksthrough key char by char. and makes columns
    for i in range(keylength):
        masterII.insert(0, [])
    # for every char in the table make the title row filled with key. else fill the table row by row with -1.

    for p in range(keylength):
        masterII[p].append(key[p])
    for j in range((numberOfElements)):
        masterII[(j % keylength)].append('-1')
    del adfgvx, i, j, p
    # Enter the content of "encrypted" row by row.
        # Fill 2D list with elements row by row. When empty string apply the rest of empty spaces
        # the row 0 are only for sorting and column swapping. Never read it as part in encryption message.
    row = 1
    col = 0

    for h in range(encryptedlength):

            if row == 0:
                row = (row % Fullrows) + 1
            masterII[col][row] = encrypted[h] # try dynamic column growth.
            col = (col + 1) % keylength
            if col == 0:
                row = (row % Fullrows) + 1
    # sort the table headers chronological.
    masterII.sort()

    # read column for column chronological and then remove -1 from the string. return the result.
    del h, key24transposing
    row = 1; col = 0; encryptedII = []
    for col in range(keylength):
        for row in range(Fullrows + 1):
            if masterII[col][row] != '-1' and row != 0:
                encryptedII.append(masterII[col][row])
    return encryptedII
'''
read row by row from 2D list but not row 0:
row = 1; col = 0; encryptedII = []
    for row in range(Fullrows + 1):
        for col in range(keylength):
            if masterII[col][row] != '-1' and row != 0:
                encryptedII.append(masterII[col][row])
'''
def adfgvx_decryption(keyUsing36char, key24transposing, encryptedMessage):
    '''
    ADFGVX, decryption
    :param keyUsing36char: must include 0 to 9 and a to z and shuffle it. Send it as "string"
    :param key24transposing:
    :param encryptedMessage: the message length % 2 should be 0. If 1 then it's broken.
    :return: Secret
    '''

    #create chart
    # create 6x6 matrix using lists
    key2 = key24transposing
    key2length = len(key2)

    secret = encryptedMessage
    secretLength = len(encryptedMessage)
    secretII = []
    toBeDecoded = []
    truth = []
    i = 0
    # generate table with row 0 as header, use ciphertext for calc.
    Fullrows = secretLength / key2length
    nrOfEmptySpaces = (key2length - (secretLength % key2length))
    if nrOfEmptySpaces > 0:
        Fullrows += 1
    numberOfElements = key2length * Fullrows
    masterII = []
    # walksthrough key char by char. and makes columns
    for i in range(key2length):
        masterII.insert(0, [])
    # for every char in the table make the title row filled with key. else fill the table row by row with -1.

    for p in range(key2length):
        masterII[p].append(key2[p])
    for j in range((numberOfElements)):
        masterII[(j % key2length)].append('-1')
    # mark empty slots with -2 from the "lists end" (last row last column) and work on last row
    countDown2Boom = key2length - 1
    while nrOfEmptySpaces != 0:
        masterII[ countDown2Boom ][ Fullrows ] = '-2'
        nrOfEmptySpaces -= 1
        countDown2Boom -= 1

    # sort masterII columns by chronological

    masterII.sort()
    del i, j, nrOfEmptySpaces, p, countDown2Boom # purge <3 !
    # read the cipher text and fill masterII column by column
    char = 0
    while char != secretLength  :
        for col in range(key2length):
            for row in range(Fullrows + 1):
                if masterII[col][row] != '-2' and row != 0:
                    masterII[col][row] = secret[char]
                    char += 1
    # <---------------------------Move me to the end of the recent working area!!!!!!!
    # rearrange the columns in order of key

    # swap cols so that the col headers match the key       <------------ works but needs more tests
    # used to swap columns
    tmpCol = [['+']];
    tmp2Col = [['+']]
    for round in range(Fullrows):
        tmpCol[0].append('-')
    for round in range(Fullrows):
        tmp2Col[0].append('-')
# look at range.
    for a in range(key2length):  # range is nrOfCol
        for b in range(key2length):  # range is nrOfCol
            if key2[a] == masterII[b][0]:
                if key2length == 2 and a == 1:
                    continue
                elif key2length == 1:
                    continue
                else:
                    for f in range(Fullrows + 1):  # range depends on nr of rows because f walks throug the rows in the columns. +1 with fullrows covers the header row
                        tmpCol[0][f] = masterII[a][f]
                        tmp2Col[0][f] = masterII[b][f]
                        # copy a col into tmpCol, copy e col into tmp2Col
                        # Now tmpCol overwrite e col
                        masterII[b][f] = tmpCol[0][f]
                        # Now tmp2Col overwrite a col
                        masterII[a][f] = tmp2Col[0][f]

    # read row by row into  toBeDecoded

    for row in range(Fullrows + 1):
        for col in range(key2length):
            if masterII[col][row] != '-1' and row != 0:
                toBeDecoded.append(masterII[col][row])
    toBeDecoded.remove('-2')
    # fill decode table
    col0 = [None] * 6
    col1 = [None] * 6
    col2 = [None] * 6
    col3 = [None] * 6
    col4 = [None] * 6
    col5 = [None] * 6
    master = [col0, col1, col2, col3, col4, col5]
    adfgvx = "adfgvx"
    col_S = 0; row_S = 0; i = 0
    for row in range(0, 6, 1):
        for col in range(0, 6, 1):
            master[col][row] = keyUsing36char[i]
            i += 1


    # read bigrams and decode
    i = 0; temp=[None,None]
    # we could increase performance by remembering earlier results during decoding.
    toBeDecodedLength = len(toBeDecoded)
    while i < toBeDecodedLength:
        temp[0] = toBeDecoded[i]
        i += 1
        if i < toBeDecodedLength:
            temp[1] = toBeDecoded[i]
            i += 1
        j = False
        l = 0
        while j != True :
            if temp[0] == adfgvx[l]:
                col_S = l
                j = True
            l += 1
        j = False
        l = 0
        while j != True:

            if temp[1] == adfgvx[l]:
                row_S = l
                j = True
            l += 1
        truth.append(master[col_S][row_S])

    return truth
