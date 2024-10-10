from typing import Callable
from Levenshtein import distance, ratio


class Validator:

    def __init__(self,
                 weights: tuple[int, int, int] = (1, 1, 1),
                 processor: Callable | None = None,
                 score_cutoff: int | float | None = None,
                 score_hint: int | None = None):

        # The weights for the three operations in the form (insertion, deletion, substitution).
        self.__weights = weights

        # A method used to preprocess the strings before comparing them. E.g., Porter stemming algorithm.
        self.__processor = processor

        # For levenshtein_distance it must be an integer indicating the
        # maximum distance between s1 and s2, that is considered as a result.
        # If the distance is bigger than score_cutoff, score_cutoff + 1 is returned instead.
        # For text_similarity_score it is a float between 0 and 1.0.
        # If the score < score_cutoff, 0 is returned instead.
        self.__score_cutoff = score_cutoff

        # Expected distance between s1 and s2. This is used to select a faster implementation.
        # It applies only for levenshtein_distance, but not for text_similarity_score.
        self.__score_hint = score_hint

    def levenshtein_distance(self, text1: str, text2: str) -> int:
        """
        Returns the minimum number of insertions, deletions, and substitutions
        required to change one character sequence into the other.
        :param text1: One character sequence.
        :param text2: The other character sequence.
        :return: Integer that is at most equal to the length of the longer sequence.
        """
        return distance(s1=text1,
                        s2=text2,
                        weights=self.__weights,
                        processor=self.__processor,
                        score_cutoff=self.__score_cutoff,
                        score_hint=self.__score_hint)

    def text_similarity_score(self, text1: str, text2: str) -> float:
        if self.__score_cutoff is None:
            cutoff = 0
        else:
            cutoff = self.__score_cutoff
        return ratio(s1=text1,
                     s2=text2,
                     processor=self.__processor,
                     score_cutoff=cutoff)
