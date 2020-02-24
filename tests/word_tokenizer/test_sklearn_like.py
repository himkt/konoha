from konoha import WordTokenizer

import pytest


DOCUMENTS = [
    '私は猫である',
    '私は猫ではない'
]
VOCABULARY = {'私', 'は', '猫', 'で', 'ある', 'は', 'ない'}


def test_sklearn_like_interface():
    try:
        tk = WordTokenizer('mecab')
    except ImportError:
        pytest.skip('skip fit/transform test')

    tk.fit(DOCUMENTS)
    assert set(tk.vocabulary) == VOCABULARY

    texts = '私は猫である'
    id_texts = tk.transform(texts)
    assert isinstance(id_texts, list)

    for id_text in id_texts:
        assert isinstance(id_text, list)

    itexts = tk.itransform(id_texts)
    assert texts == ''.join(itexts[0])


def test_tf_options():
    try:
        tk = WordTokenizer('mecab')
    except ImportError:
        pytest.skip('skip fit/transform test')

    tk.fit(DOCUMENTS, min_tf=2)
    assert set(tk.vocabulary) == {'私', 'は', '猫', 'で'}
