def deb ():
    print "deb goes meh!"
    return

def dubbleTransposse_encryption(): # (key, secret):
    '''
    takes key and secret creates cipher text and encrypt it too then it returns the result
    :param key:
    :param secret:
    :return:
    '''
    #calc nr of filled rows, nr of empty row slots and nr of col.
    keyHold = "abc" #key
    keyLength = len(keyHold)
    cache = "aaaaaaaa" # secret
    cacheLength = len(cache)
    Fullrows = cacheLength / keyLength
    nrOfEmptySpaces = (keyLength -(cacheLength % keyLength))
    # Generate empty 2D list with n rows and m col.
    master = [[None]]
    for i in range(keyLength):
        master
    master
    print master

    # Fill 2D list with elements row by row. When empty string apply the rest of empty spaces

    # Sort the 2D list columns chronological with a as the lowest at the left side.

    # Read col for col where we skip 'special char None or -1' into the encryption list/string and return result

    return 0

def dubbleTransposse_decryption(): # (key, encrypted_text)
    # calc nr of filled rows, nr of empty row slots and nr of col.

    # Generate empty 2D list with n rows and m col. (calc nr of rows, keylength == nrOfCol)

    # Mark the loweest row elements from the lowest right col

    # sort the cols alphabetically

    # Read the elements into the 2D list and jump empty spaces.

    #swap cols so that the col headers match the key

    # read row by row into Decypted string and return it.

    return
