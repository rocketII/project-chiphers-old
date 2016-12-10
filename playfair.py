
'''
def obo ():
    print "test this is obo!"
    return

def setKey(key):
    "Insert a key containing only the english letters."
    holder = key
    return 1
'''
# Encryption
ciphertxt= []
clearTxt = "goingto"
nyckel = "skitgubbegillarfarskfisk"
nyckelLen = len(nyckel)
print "length: ", len(nyckel)
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
    #print read," occours: ",tmp.count(read)
    if tmp[0].count(read) + tmp[1].count(read) + tmp[2].count(read) + tmp[3].count(read) + tmp[4].count(read) == 0:
        #print read," is unique in nyckel, result: ",tmp.count(read)
        tmp[col][row]= read
        col = (col + 1) % 5
        if col == 0:
            row = (row + 1) % 5
    else:
        sc = tmp[0].count(read) + tmp[1].count(read) + tmp[2].count(read) + tmp[3].count(read) + tmp[4].count(read) == 0
        #print read, " nope!! not unique: ",sc


#print tmp
#append the rest of the letters in chronologically order
english = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z','y']

for read in english:
    print read, " occours: ", tmp.count(read)
    if tmp[0].count(read) + tmp[1].count(read) + tmp[2].count(read) + tmp[3].count(read) + tmp[4].count(read) == 0:
        #print read, " is unique in nyckel, result: ", tmp.count(read)
        tmp[col][row] = read
        col = (col + 1) % 5
        if col == 0:
            row = (row + 1) % 5
    else:
        sc = tmp[0].count(read) + tmp[1].count(read) + tmp[2].count(read) + tmp[3].count(read) + tmp[4].count(read) == 0
        #print read, " nope!! not unique: ", sc

row = 0; col = 0

'''#reads 2D list with row by row across all the columns.
output= []
for row in range(5):
    for col in range(5):
        read = tmp[col][row]
        if read != None:
            output.append(read,)
print output
'''