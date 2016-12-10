
'''
def obo ():
    print "test this is obo!"
    return

def setKey(key):
    "Insert a key containing only the english letters."
    holder = key
    return 1
'''


nyckel = "skitgubbegillarfarskfisk"
nyckelLen = len(nyckel)
print "length: ", len(nyckel)
#remove duplicates
col1=[None] *5
col2=[None] *5
col3=[None] *5
col4=[None] *5
col5=[None] *5
tmp = [col1,col2,col3,col4,col5]
row=0
col=0
tmp
for read in nyckel:
    print read," occours: ",tmp.count(read)
    if tmp.count(read) == 0:
        print read," is unique in nyckel"
        tmp[row][col]= read
    col = (col + 1) % 5
    if col == 0:
        row = (row + 1) % 5
print "Results: ",tmp
