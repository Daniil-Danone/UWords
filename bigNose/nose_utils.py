TEXT = "Сегодня мама мыла раму. Раму мыла мама. А потом она мыла стёкла. Стекло было грязным и она решила помыть его ещё раз, а раму позже"
TEXT = TEXT.replace('.', '')
TEXT = TEXT.replace(',', '')
TEXT = TEXT.replace('-', '')

words = {}


def wordsFrequency(text):
    for i in text.split():
        if i.lower() not in words.keys():
            words[i.lower()] = 1
        else:
            words[i.lower()] += 1


wordsFrequency(TEXT)
print(words)
