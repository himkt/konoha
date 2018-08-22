all: get-wikidump tokenize

get-wikipedia:
	cd data && wget https://dumps.wikimedia.org/jawiki/20180801/jawiki-20180801-pages-articles.xml.bz2
	cd data && WikiExtractor.py jawiki-20180801-pages-articles.xml.bz2 --output jawiki.json --json

tokenize:
	python ./script/tokenize_document.py
