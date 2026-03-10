

print(len('banana')*7)



greet = 'Hello Bob'

print(greet.upper())



data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

# 6.5

text = "X-DSPAM-Confidence:    0.8475"

pos = text.find('0')

print(float(text[pos:pos+6]))

