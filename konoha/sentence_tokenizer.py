import re
from typing import List


class SentenceTokenizer:
    """Simple Rule-based Sentence Splitter.
    """

    PERIOD = "。"
    PERIOD_SPECIAL = "__PERIOD__"

    PATTERNS = [
        r"（.*?）",
        r"「.*?」",
    ]

    @staticmethod
    def conv_period(item) -> str:
        return item.group(0).replace(
            SentenceTokenizer.PERIOD, SentenceTokenizer.PERIOD_SPECIAL
        )

    def tokenize(self, document) -> List[str]:
        """
        Divide a raw document into sentences.
        :param document: a raw document
        :type document: str
        :return: list of sentences
        :rtype list[str]
        """

        for pattern in SentenceTokenizer.PATTERNS:
            pattern = re.compile(pattern)  # type: ignore
            document = re.sub(pattern, self.conv_period, document)

        result = []
        for line in document.split("\n"):
            line = line.rstrip()
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            line = line.replace("。", "。\n")
            sentences = line.split("\n")

            for sentence in sentences:
                if not sentence:
                    continue

                period_special = SentenceTokenizer.PERIOD_SPECIAL
                period = SentenceTokenizer.PERIOD
                sentence = sentence.replace(period_special, period)
                result.append(sentence)

        return result
