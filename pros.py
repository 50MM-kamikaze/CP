word1 = "sam"
word2 = "good"
        
result = ''
i = 0 
while i < len(word1) or i <len(word2):
    if i < len(word1):
        result = result + word1[i]
    if i < len(word2):
        result = result + word2[i]
    i+=1
print( result)
