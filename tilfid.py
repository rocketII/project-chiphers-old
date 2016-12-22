# code by rocketII on github. use on your own risk.
#! /path/to/python
# Bug 002:list with eleven or more characters dosen't work
def tilfid_encryption (secret_stuff):
    '''
    Encrypt your message with tilfid cipher
    :param secret_stuff: enter text string "secret stuff"
    :return: encrypted stuff
    '''
    secret = secret_stuff
    secretLength = len(secret_stuff)
    # helper = ['1','2','3']
    encrypted_tmp = []
    for n in range(secretLength):
        encrypted_tmp.append([None, None, None])
    encrypted = []
    # Using coordinates layer,row, col
    # Make sure that booth recipient and sender got the same layers like below. Modify when required.
    layer1 = [['a', 'k', 'g'], ['l', 'r', 't'], ['x', 'm', 'n']]
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
    #print "Encoded as: ",encrypted_tmp

    # read row by row, trigram gets encoded and saved.
    
    #rowByrow = [None] * secretLength
    trigram = [None] * 3   # trgigram = [layer, col, row] *3
    ci =0;ri = 0; j = 0
    #print "          lay,row,col:"
    for round in range(secretLength): # bug here?  Yes row didn't change when required. now fixed?
            trigram[0] = encrypted_tmp[ci][ri] # insert layer   :
            ci = (ci + 1) % secretLength
            if ci == 0:
                ri = (ri + 1) % 3
            trigram[1] = encrypted_tmp[ci][ri] #insert row      :
            ci = (ci + 1) % secretLength
            if ci == 0:
                ri = (ri + 1) % 3
            trigram[2] = encrypted_tmp[ci][ri] #insert col      :
            ci = (ci + 1) % secretLength
            if ci == 0:
                ri = (ri + 1) % 3

            #print "Trigram: ",trigram
            #                        layer        col         row
            encrypted.append(master[trigram[0]][trigram[2]][trigram[1]]) # expected type but got None, when using list length over 11

    del secret, secretLength, ci, ri ,trigram ,master
    return encrypted

def tilfid_decryption(encryption_text):
    '''
    Decrypt Tilfid encryption message, make sure that the layers are the same as sender's, also make sure
    that coordinates are working as layer, row, col otherwise change the code.
    :param encryption_text: Enter the secret phrase as list ['s','e','c','r','e','t']
    :return: secret message as list
    '''
    # Using coordinates layer,row, col
    # Make sure that booth recipient and sender got the same layers like below. Modify when required.

    layer1 = [['a', 'k', 'g'], ['l', 'r', 't'], ['x', 'm', 'n']]
    layer2 = [['q', 'w', 'm'], ['!', 'o', 'e'], ['u', 's', 'z']]
    layer3 = [['i', 'f', 'v'], ['j', 'p', 'd'], ['b', 'h', 'c']]
    master = [layer1, layer2, layer3]
    message =[]
    phrase = encryption_text
    phraseLength = len(phrase)
    decrypted_tmp = []
    for w in range(phraseLength):
        decrypted_tmp.append([None,None,None]) # [layer, col, row]


    # letter by letter read and encode using master and secret
    r=0; c = 0
    for round in range(phraseLength):
        for layer in range(3):
            for col in range(3):
                for row in range(3):
                    # sorry this is totally quadratic time complexity x^4... when there's time I should make it better, hashtable or something
                    if master[layer][col][row] == phrase[round]: # bug here?
                        # print "Master: ", master[layer][col][row]
                        decrypted_tmp[c][r] = layer
                        c = (c + 1) % phraseLength
                        if c == 0:
                            r = (r + 1) % 3
                        decrypted_tmp[c][r] = row
                        c = (c + 1) % phraseLength
                        if c == 0:
                            r = (r + 1) % 3
                        decrypted_tmp[c][r] = col
                        c = (c + 1) % phraseLength
                        if c == 0:
                            r = (r + 1) % 3
    # read column by column and decode
    tmp = [None, None, None]; o = 0; p = 0
    for round in range(phraseLength): # bug 002 here?
                    tmp[0] = decrypted_tmp[o][p]
                    p = (p + 1) % 3
                    if p % 3 == 0:
                        o = (o + 1) % phraseLength
                    tmp[1] = decrypted_tmp[o][p]
                    p = (p + 1) % 3
                    if p % 3 == 0:
                        o = (o + 1) % phraseLength
                    tmp[2] = decrypted_tmp[o][p]
                    p = (p + 1) % 3
                    if p % 3 == 0:
                        o = (o + 1) % phraseLength
                    message.append(master[tmp[0]][tmp[2]][tmp[1]])  # expected type but got None instead over length +11
    return message
