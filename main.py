# # t = {'a':1,'b':2}
# # t['c'] = 3
# # print(t)
# #
#
file = "C:/Users/gansreek/Desktop/test.txt"
count = 0
with open(file,'r') as file:
    content = file.read()
    count = len(content)

    char_count = {}
    for i in content:
        if i.isalpha():
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1

print(count)
print(char_count)
#
#
#
#
#
#
#






# t = {'a':1,'b':2}
# t['c'] = 3
# print(t)
#

file = "C:/Users/gansreek/Desktop/test.txt"
with open(file,'r') as file:
    content = file.read()
    words = content.split()
    # print(words)
    word_count = len(words)
def repeated():
    repeated_words = {}
    for i in words:
        if words.count(i) > 1:
            if i not in repeated_words:
                repeated_words[i] = words.count(i)
    print("Repeated words:", repeated_words)
print("Number of words in the sentence: ", word_count)
repeated()










    # for word, count in repeated_words.items():
    #     print(f"'{word}': {count}")










