#implement them in order
#Priority   text
# 1         make one cipher work at the time
# 2
# Do not use this old ciphers with important secrets. They are old and can be forced open using math just a moment of days or weeks.
import playfair
import adfvgx
import tilfid
import dubbleTranspose
clearTxt = ['j','a','g','a','t','e','r']
print clearTxt
nyckel = "skitgubbegillarfarskfisk"
encrypted1 = playfair.playfair_encrypt(clearTxt,nyckel,'n')
print encrypted1

secret =playfair.playfair_decryption(encrypted1,nyckel,'n')
print secret
