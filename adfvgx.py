def adfgvx_encryption(keyUsing36char, clearTextUsingTheKeyForCoding):
    '''

    :param keyUsing36char: must include 0 to 9 and a to z and shuffle it. Send it as "string"
    :param clearTextUsingTheKeyForCoding:  send it as ['s','c','r','e','t']
    :return: encryptet message
    '''
    secret = clearTextUsingTheKeyForCoding
    key = keyUsing36char
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
    print master
    # use key char by char and decode, read col first then row.
    i = 0
    for i in  range(secretLength):
        for row in range(6):
            for col in range(6):
                if( master[col][row] == secret[i]):
                    encrypted.insert(0, adfgvx[col])
                    encrypted.insert(0, adfgvx[row])
    encrypted.reverse()
    return encrypted