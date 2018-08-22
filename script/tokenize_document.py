import sys
import json
import tqdm
import pathlib


if __name__ == '__main__':
    sys.path.append('./')
    from src.word_tokenizer import WordTokenizer
    from src.sentence_tokenizer import SentenceTokenizer
    wikipextractor_dir = pathlib.Path('data/jawiki')
    sentence_tokenizer = SentenceTokenizer()
    word_tokenizer = WordTokenizer('KyTea')
    wakati_fpath = 'data/jawiki-20180801-pages-articles.txt'

    wakati_file = open(wakati_fpath, 'w')
    json_fpath_list = list(wikipextractor_dir.glob('*/wiki_*'))

    for json_fpath in tqdm.tqdm(json_fpath_list):
        for json_str in open(json_fpath):

            try:
                json_object = json.loads(json_str)
                document = json_object['text']

                for sentence in sentence_tokenizer.tokenize(document):
                    print(word_tokenizer.tokenize(sentence), file=wakati_file)

            except Exception as e:
                print(e, file=sys.stderr)

    wakati_file.close()
