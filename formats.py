import json, xml.etree.ElementTree as Tree


def count_descending(x):
    return -x[1]


def load_words_from_json(filename):
    words = []
    with open(filename) as news:
        for every_item in json.load(news)['rss']['channel']['items']:
            words += every_item['description'].split()
    return words


def load_words_from_xml(filename):
    words = []
    with open(filename) as news:
        for item in Tree.parse(news).findall('channel/item/description'):
            words += item.text.split()
    return words


def get_frequent_words(words, wc=10, min_length=6):
    word_count = {}
    for word in words:
        if len(word) > min_length:
            word_count.setdefault(word, 0)
            word_count[word] = word_count[word] + 1
    pair_list = list(word_count.items())
    pair_list.sort(key=count_descending)
    return pair_list[:wc]


def print_words(list):
    for every_element in list:
        print(every_element[0])


print_words(get_frequent_words(load_words_from_xml('news.xml')))
print_words(get_frequent_words(load_words_from_json('news.json')))
