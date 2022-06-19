
metin = "enes"
sifrelenen = ""
for i in metin:

    sifrelenen = sifrelenen + chr(ord(i) * 2 )
    print(sifrelenen)
print(metin, " = >", sifrelenen)