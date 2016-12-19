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
    # <---------------------------Move me to the end of the recent working area!!!!!!!
    # read column for column chronological and then remove -1 from the string. return the result.

    return encrypted

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
    col0 = [None] * 6
    col1 = [None] * 6
    col2 = [None] * 6
    col3 = [None] * 6
    col4 = [None] * 6
    col5 = [None] * 6
    master = [col0, col1, col2, col3, col4, col5]
    adfgvx = "adfgvx"
    secret = encryptedMessage
    secretLength = len(encryptedMessage)
    truth = []
    i = 0
    col_S = 0; row_S = 0;
    for row in range(0, 6, 1):
        for col in range(0, 6, 1):
            master[col][row] = keyUsing36char[i]
            i += 1




    # read bigrams and decode
    i = 0; temp=[None,None]
    # we could increase performance by remember earlier results during decoding.
    while i < secretLength:
        temp[0] = secret[i]
        i += 1
        if i < secretLength:
            temp[1] = secret[i]
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
