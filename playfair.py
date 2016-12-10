# Encryption
ciphertxt= []
clearTxt = ['j','a','g','a','t','e','r']
nyckel = "skitgubbegillarfarskfisk"
nyckelLen = len(nyckel)
#Create 2D list. Enter key with removed duplicate letters, row by row across columns
col1=[None] *5
col2=[None] *5
col3=[None] *5
col4=[None] *5
col5=[None] *5
tmp = [col1,col2,col3,col4,col5] # currently good enough without list copies in main list.
row=0
col=0
for read in nyckel:

    if tmp[0].count(read) + tmp[1].count(read) + tmp[2].count(read) + tmp[3].count(read) + tmp[4].count(read) == 0:

        tmp[col][row]= read
        col = (col + 1) % 5
        if col == 0:
            row = (row + 1) % 5
    else:
        sc = tmp[0].count(read) + tmp[1].count(read) + tmp[2].count(read) + tmp[3].count(read) + tmp[4].count(read) == 0




#append the rest of the letters in chronologically order
english = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z','y']

for read in english:

    if tmp[0].count(read) + tmp[1].count(read) + tmp[2].count(read) + tmp[3].count(read) + tmp[4].count(read) == 0:

        tmp[col][row] = read
        col = (col + 1) % 5
        if col == 0:
            row = (row + 1) % 5


# create bigrams of clear text. no bigram using samme letter allowed insert junk letter 'n' between

length = len(clearTxt)

previous = None; second = 0; junk = 'n'
for read in clearTxt:
    if previous == read:
        clearTxt.insert(second, junk)
        second +=1
        previous=junk
        continue
    previous = read
    second += 1

length = len(clearTxt)
if length % 2 == 1:
    clearTxt.append(junk)


# read two letters from cleartext, use 2D list applie rules. Append result in ouput list
listlength = len(clearTxt)
A = 0; rowFor0 = 0; colFor0  = 0; rowFor1 = 0; colFor1  = 0
temp = ['.','.']
while A < listlength:
    temp[0] = clearTxt[A]
    A += 1
    if A < listlength:
        temp[1] = clearTxt[A]
        A += 1
    for row in range(5):
        for col in range(5):
            if tmp[col][row] == temp[0]:
                rowFor0 = row
                colFor0 = col
            elif tmp[col][row] == temp[1]:
                rowFor1 = row
                colFor1 = col
    if rowFor0 == rowFor1:
        #read in order, row/col index 0 goeas first
        ciphertxt.insert(0, tmp[(colFor0 + 1)%5][rowFor0])
        ciphertxt.insert(0, tmp[(colFor1 + 1) % 5][rowFor1])

    elif colFor1 == colFor0:
        # read in order, row/col index 0 goeas first
        ciphertxt.insert(0, tmp[colFor0][(rowFor0 + 1)%5])
        ciphertxt.insert(0, tmp[colFor1][(rowFor1 + 1)%5])
    else:
        if colFor0 > colFor1:
            # read in order, row/col index 0 goeas first
            colDiff = abs(colFor0 - colFor1)
            ciphertxt.insert(0, tmp[(colFor0 - colDiff ) % 5][rowFor0])
            ciphertxt.insert(0, tmp[(colFor1 + colDiff) % 5][rowFor1])
        elif colFor0 < colFor1:
            # read in order, row/col index 0 goeas first
            colDiff = abs(colFor0 - colFor1)
            ciphertxt.insert(0, tmp[(colFor0 + colDiff) % 5][rowFor0])
            ciphertxt.insert(0, tmp[(colFor1 - colDiff) % 5][rowFor1])



print "Cipher text: ",ciphertxt


#reads 2D list with row by row across all the columns.
row = 0; col = 0
output= []
for row in range(5):
    for col in range(5):
        read = tmp[col][row]
        if read != None:
            output.append(read,)
#print output


