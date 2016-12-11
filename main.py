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
tilfid.tilfid_encryption("secret")
print"------------------------------------"
