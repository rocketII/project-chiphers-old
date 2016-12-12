# encoding: utf-8
#implement them in order
#Priority   text
# 1         make one cipher work at the time
# 2
# Do not use this old ciphers with important secrets. They are old and can be forced open using math just a moment of days or weeks.
#Thinking what are they? Just read wikipedia or search for them on the internet.
import playfair
import adfvgx
import tilfid
import dubbleTranspose
print"------------------------------------"
print "Demo playfair, remember i = j"
print"------------------------------------"
clearTxt = ['j','a','g','a','t','e','r']
print "My secret: ",clearTxt
nyckel = "skitgubbegillarfarskfisk"
encrypted1 = playfair.playfair_encrypt(clearTxt,nyckel,'n')
print "My encrypted secret: ",encrypted1

secret =playfair.playfair_decryption(encrypted1,nyckel,'n')
print "My secret revealed: ",secret
print"------------------------------------"
print "Demo ADFVGX"
print"------------------------------------"
key= "0n1o2p3q4a5b6c7d8e9rstuvwxyzfghjiklm"
print "key length: ",len(key)
secretStuff = ['i','c','a','n','d','r','i','n','k','m','i','l','k']
length = len(secretStuff)
print "secret: ",secretStuff
encryptStuff = adfvgx.adfgvx_encryption(key, secretStuff)
print "encrypted secret: ",encryptStuff
revealed = adfvgx.adfgvx_decryption(key, encryptStuff)
print "Decrypted message: " , revealed
print"------------------------------------"
print "Demo Tilfid"
print"------------------------------------"
#Bug001: works using length 3 and 6 not 9 though
#length affects how many operations needed before changing row, fixed problem with duplicating if statement.
#Bug002: After length eleven it dosen't work.
swane = ['b', 'u', 'r', 'k', 'a', 'r', 'a', 'k', 'e', 'g', 'e'] # when above 11 we get bug 002
print "Secret message:       ", swane," length: ", len(swane)
cloud = tilfid.tilfid_encryption(swane)
print "Encrypted message     ", cloud
print "Decrypted encryption: ",tilfid.tilfid_decryption(cloud)
print"------------------------------------"
print "Demo Dubble Transpose"
print"------------------------------------"
passwd = "abcdefghijk"
key = "ab"
print "From passwd=",passwd," and key=",key
print "We get encrypted code: ",dubbleTranspose.dubbleTransposse_encryption(key, passwd)
dubbleTranspose.dubbleTransposse_decryption()
print"------------------------------------"
