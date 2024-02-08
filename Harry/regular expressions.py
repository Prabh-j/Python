#regexr.com
import re
pattern = r'[A-Z]ome' #it is used to find pattern from the data
words = ''' The most important words a man can say are, "I will do better." These are not the most important words any man can say. I am a man, and they are what I 
needed to say. The ancient code of the Knights Radiant says "journey before destination." Some may call it a simple platitude, but it is far more. A journey will 
have pain and failure. It is not only the steps forward that we must accept. It is the stumbles. the trials. The knowledge that we will fail. That we hurt those 
around us. But if we stop, if we accept the person we are when we fall, the journey ends. That failure becomes our destination. To love the journey is to accept 
no such end. I have found, through painful experience, that the most important step a person can take is always the next  one. I'm certain some will feel threatened 
by this record. Some few may feel liberated. Most will simply feel that it should not exist. I needed to write it anyway. '''

matches = re.search(pattern, words) #search will give first occurance of data
print(matches)
print(dir(matches))

print('-------------')

matche = re.finditer(pattern, words) #it will give all occurance of data
for match in matche:
    print(match)
    print(words[match.span()[0]:match.span()[1]])

