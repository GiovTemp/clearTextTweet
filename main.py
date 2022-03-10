# Python program to read JSON
# from a file


import json

# Opening JSON file


print('StopWords Loading......')
stopWords = []
for line in open('stopwords.json', 'rb'):
    stopWords.append(json.loads(line))

tweets = []
print('Im cleaning up the tweets (this may take a while)......')

for line in open('dati.json', 'rb'):
    tweet_dict = json.loads(line)
    n = 0
    while n < len(tweet_dict['spacy']['processed_text']):
        i = 0
        while i < len(stopWords[0]):
            if tweet_dict['spacy']['processed_text'][n].split(' ')[0] == stopWords[0][i]:
                tweet_dict['spacy']['processed_text'].pop(n)
                break
            i += 1
        n += 1
    tweets.append(tweet_dict)

print('Creating New File......')


with open('newData.json', 'w', encoding='utf-8') as f:
    json.dump(tweets, f, ensure_ascii=False)

print('File created successfully !')
