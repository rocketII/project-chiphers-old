def tilfid_encryption (secret_Stuff):
    '''
    Encrypt your message with tilfid cipher
    :param secret_Stuff: enter text string "secret stuff"
    :return: encrypted stuff
    '''
    secret = secret_Stuff
    secretLength = len(secret_Stuff)
    helper = ['1','2','3']
    encrypted_tmp = []
    for n in range(secretLength):
        encrypted_tmp.append([None, None, None])
    encrypted = []
    #Using coordinates layer,row, col
    #Make sure that booth recipient and sender got the same layers like below. Modify when required.
    layer1 = [['a','k','g'], ['l','r','t'], ['x','m','n']]
    layer2 = [['q', 'w', 'm'], ['!', 'o', 'e'], ['u', 's', 'z']]
    layer3 = [['i', 'f', 'v'], ['j', 'p', 'd'], ['b', 'h', 'c']]
    master = [layer1, layer2, layer3]

    # letter by letter read and encode using master and secret
    for i in range(secretLength):
        for layer in range(3):
                for col in range(3):
                    for row in range(3):
                        #sorry this is totally quadratic time complexity x^4... when there's time I should make it better, hashtable or something
                        if master[layer][col][row] == secret[i]:
                            encrypted_tmp[i][0] = layer
                            encrypted_tmp[i][1] = row
                            encrypted_tmp[i][2] = col

    # read row by row, trigram gets encoded and saved.
    #rowByrow = [None] * secretLength
    trigram = [None] * 3   # trgigram = [layer, col, row] *3
    ci =0;ri = 0; j = 0
    for round in range(secretLength):
            trigram[0] = encrypted_tmp[ci][ri] # insert layer   : 1
            ci = (ci + 1) % secretLength;
            trigram[1] = encrypted_tmp[ci][ri] #insert row      : 1
            ci = (ci + 1) % secretLength;
            trigram[2] = encrypted_tmp[ci][ri] #insert col      : 1
            ci = (ci + 1) % secretLength
            if ci == 0:
                ri = (ri + 1) % 3
            #                        layer        col         row
            encrypted.append(master[trigram[0]][trigram[2]][trigram[1]])

    del secret, secretLength
    return encrypted