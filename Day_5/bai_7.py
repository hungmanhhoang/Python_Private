string = input()

word_dict = {}
for word in string:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1 

print(word_dict)