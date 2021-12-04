import re
from typing import List
from typing import Match
from typing import Optional
from typing import Pattern


class SentenceTokenizer:

    PERIOD = "。"
    PERIOD_SPECIAL = "__PERIOD__"

    PATTERNS = [
        re.compile(r"（.*?）"),
        re.compile(r"「.*?」"),
    ]

    def __init__(
        self,
        period: Optional[str] = None,
        patterns: Optional[List[Pattern[str]]] = None,
    ) -> None:

        self._period = period or self.PERIOD
        self._patterns = patterns or self.PATTERNS

    def conv_period(self, item: Match) -> str:
        return item.group(0).replace(self._period, SentenceTokenizer.PERIOD_SPECIAL)

    def tokenize(self, document: str) -> List[str]:
        for pattern in self._patterns:
            document = re.sub(pattern, self.conv_period, document)

        result = []
        for line in document.split("\n"):
            line = line.rstrip()
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            line = line.replace(f"{self._period}", f"{self._period}\n")
            sentences = line.split("\n")

            for sentence in sentences:
                if not sentence:
                    continue

                period_special = SentenceTokenizer.PERIOD_SPECIAL
                sentence = sentence.replace(period_special, self._period)
                result.append(sentence)

        return result
