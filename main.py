import json
import hashlib
from pprint import pprint

class WikipediaLinkIteration:
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'w', encoding='utf8')
        with open('countries.json') as f:
            country = json.load(f)
            list_country = []
            for i in country:
                name = i.get('name')
                list_country.append((name.get('common')).replace(' ', '_'))
            self.a = list_country

    def __iter__(self):
        return self

    def __next__(self):
        if self.a != []:
            link = 'https://en.wikipedia.org/wiki/' + self.a[0]
            self.file.write(self.a[0] + ' - ' + link + '\n')
            (self.a).remove(self.a[0])
            return link
        else:
            self.file.close()
            raise StopIteration


def my_generator(path):
    with open(path, 'r') as f:
        while f.readline() != '':
            a = f.readline()
            mdpass = hashlib.md5(str(a).encode("utf-8")).hexdigest()  # For MD5 hash
            print(mdpass)


if __name__ == '__main__':
    for item in WikipediaLinkIteration('text.txt'):
        pass

    my_generator('text.txt')