vowels = ['a', 'e', 'i', 'o', 'u']
#a = 'a'
#e = 'e'
#i = 'i'
#o = 'o'
#u = 'u'

length = len(vowels)

vowcount = 0

for count in range(0, 10):
    word = input('Input a word: ')
   
    word = word.lower()
    word = word.strip(" ")
   
    for i in range (0, length - 1):
       
        if vowels[i] in word:
            vowcount += 1
       
        else:
            continue
   
   
print(vowcount)  
