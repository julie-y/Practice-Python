#take the first few consenants and move to the end of the word
#then add ay to the end of the word

#if a word starts with a vowal, then add yay
original = input ('Please type in your sentence: ').strip().lower()
#split sentence into words
words = original.split()  #words=['this', 'is', 'pig', 'latin']
new_words=[] #make a blank list

#see if it starts with vowal
for word in words:
    if word[0] in 'aeiou':
        new_word = word+'yay'
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos =vowel_pos+1
            else:
                break
        first=word[vowel_pos :]
        second=word[:vowel_pos]
        new_c_word = first + second+'ay'
        new_words.append(new_c_word)
new_words =' '.join(new_words)   #stick words together # join.() can be used join list words together                        
print(new_words)









