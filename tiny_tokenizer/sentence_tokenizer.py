import re


class SentenceTokenizer:
    PERIOD = '。'
    PERIOD_SPECIAL = '__PERIOD__'

    def __init__(self):
        pass

    @staticmethod
    def conv_period(item):
        return item.group(0).replace(SentenceTokenizer.PERIOD, '__PERIOD__')

    def tokenize(self, document):
        """
        Divide a raw document into sentences.
        :param document: a raw document
        :type document: str
        :return: list of sentences
        :rtype list[str]
        """
        pattern = r'（.*?）'
        pattern = re.compile(pattern)
        document = re.sub(pattern, self.conv_period, document)

        pattern = r'「.*?」'
        pattern = re.compile(pattern)
        document = re.sub(pattern, self.conv_period, document)

        result = []
        for line in document.split('\n'):
            line = line.rstrip()
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            line = line.replace('。', '。\n')
            sentences = line.split('\n')

            for sentence in sentences:
                if not sentence:
                    continue

                period_special = SentenceTokenizer.PERIOD_SPECIAL
                period = SentenceTokenizer.PERIOD
                sentence = sentence.replace(period_special, period)
                result.append(sentence)

        return result
