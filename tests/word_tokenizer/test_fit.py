from konoha import WordTokenizer


def test_fit():
    documents = [
        '私は猫である',
        '私は猫ではない'
    ]

    vocabulary = {'私', 'は', '猫', 'で', 'ある', 'は', 'ない'}
    tk = WordTokenizer('mecab')

    tk.fit(documents)
    assert set(tk.vocabulary) == vocabulary
