# rocketII @ github made this shitty code. Can be used with SMS. :)
# Linux shebang below
#! /path/to/python
# encoding: utf-8

#implement them in prio order
#Priority   text
#1          analysis of known bugs
# Do not use this old ciphers with important secrets. They are old and can be forced open using my friend math and we are talkning a moment of hours or days.
#Thinking what are they? Just read wikipedia or search for them on the internet.

#import shitty libs
import playfair
import adfvgx
import tilfid
import dubbleTranspose


print "@=================================================================================================================@"
print "| Disclaimer: These ciphers are not meant to be used with important data. I take no responsibility for this code. | "
print "@=================================================================================================================@"
print"------------------------------------"
print "Demo playfair, remember i = j"
print"------------------------------------"
#clearTxt = ['j','a','g','a','t','e','r']
clearTxt = ['j','y','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','e','r','a','g','a','t','s']
print "My secret: ",clearTxt
nyckel = "runningaround"
encrypted1 = playfair.playfair_encrypt(clearTxt,nyckel,'n')
print "My encrypted secret: ",encrypted1
secret = playfair.playfair_decryption(encrypted1,nyckel,'n')
print "My secret revealed: ",secret




print"------------------------------------"
print "Demo ADFVGX"
print"------------------------------------"

key= "0n1o2p3q4a5b6c7d8e9rstuvwxyzfghjiklm"
colKey = "shangrile"
print "key length: ",len(key)
secretStuff =  ['i','c','a','n','d','r','i','n','k','m','i','l','k']   # default['i','c','a','n','d','r','i','n','k','m','i','l','k']
length = len(secretStuff)
print "secret: ",secretStuff
encryptStuff = adfvgx.adfgvx_encryption(key, colKey, secretStuff)
print "encrypted secret: ",encryptStuff
revealed = adfvgx.adfgvx_decryption(key, colKey, encryptStuff)
print "Decrypted message: " , revealed




print"------------------------------------"
print "Demo Tilfid"
print"------------------------------------"
#Bug001: works using length 3 and 6 not 9 though
#length affects how many operations needed before changing row, fixed problem with duplicating if statement.
#Bug002: After length eleven it dosen't work.
swane = ['b', 'u', 'r', 'k', 'a', 'r', 'a', 'k', 'e', 'g', 'e'] # when above 11 we get bug 002
print "Secret message:       ", swane
cloud = tilfid.tilfid_encryption(swane)
print "Encrypted message     ", cloud
print "Decrypted encryption: ",tilfid.tilfid_decryption(cloud)



print"------------------------------------"
print "Demo Dubble Transpose"
print"------------------------------------"
passwd = "juliaAbbaRosmarieQwertyBobSimon"   #"abcdefghijk"
key = "bawkeyxzgh"
print "From passwd=",passwd," and key=",key
first = dubbleTranspose.dubbleTransposse_encryption(key, passwd)
cloudMyCloud = dubbleTranspose.dubbleTransposse_encryption(key, first)
print "We get encrypted code1: ",first
print "We get encrypted code2: ",cloudMyCloud
decryptR1 = dubbleTranspose.dubbleTransposse_decryption(key, cloudMyCloud)
decryptR2 = dubbleTranspose.dubbleTransposse_decryption(key, decryptR1)
print "We get decrypted code1: ", decryptR1
print "We get decrypted code2: ", decryptR2
print"------------------------------------"
