file = open('passage.txt')
lines = file.readlines()
list_ = []
common_words = ['the', 'a', 'and', 'it', '', 'you', 'to', 'of', 'in', 'is', 'your', 'on', 'that', 'but',
                'if', 'be', 'this', 'we', 'as', 'do', 'for', 'are']
for line in lines:
    line = line.replace('\n', '')
    for sentence in line.split('.'):
        for word in sentence.split(' '):
            if word.lower() not in common_words:
                list_.append(word.lower())
word_count = {}
for word in set(list_):
    word_count[word] = list_.count(word)

word_count = list(word_count.items())
word_count.sort(key = lambda x: x[1], reverse = True)
word_count[:10]