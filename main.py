import argparse
from font_parser import FontParser


def parse_unicode_from_ttf(ttf_path, csv_file, doc_file):
    font_parser = FontParser(ttf_path, csv_file, doc_file)
    font_parser.parse_unicode()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--ttf', required=True, help='Path to the image')
    ap.add_argument('-a', '--csv', required=True, help='Path to the output csv')
    ap.add_argument('-b', '--doc', required=True, help='Path to the document file')
    args = vars(ap.parse_args())
    ttf_path = args['ttf']
    csv_file = args['csv']
    doc_file = args['doc']
    parse_unicode_from_ttf(ttf_path, csv_file, doc_file)