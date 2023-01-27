import csv
from itertools import chain
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode


class FontParser:
    def __init__(self, ttf_file, csv_file, doc_file):
        self.ttf_file = ttf_file
        self.csv_file = csv_file
        self.doc_file = doc_file

    def parse_unicode(self):
        ttf = TTFont(self.ttf_file, 0, verbose=0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1)
        chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)
        ttf_chars = [[hex(c[0]).upper(), chr(c[0])] for c in chars]

        with open(self.csv_file, 'w+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='\\')
            for ttf_char in ttf_chars:
                writer.writerow(ttf_char)

        with open(self.doc_file, 'wt', encoding='utf-8') as f:
            for ttf_char in ttf_chars:
                f.write(ttf_char[1] + '\r\n')
