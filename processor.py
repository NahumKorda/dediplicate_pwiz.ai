from porter2stemmer import Porter2Stemmer


class Processor:

    def __init__(self):
        self.__stemmer = Porter2Stemmer()

    @staticmethod
    def base_text_processor(text: str) -> str:
        """
        Simplifies text by replacing line breaks with empty spaces,
        and removing multiple consecutive spaces.
        :param text: A string that is to be simplified.
        :return: Simplified string.
        """
        text = text.replace("\n", " ")
        while "  " in text:
            text = text.replace("  ", " ")
        return text.strip()

    def stemming_processor(self, text: str) -> str:
        text = self.__remove_non_alphanumeric_characters(text)
        text = self.base_text_processor(text)
        retval = list()
        for word in text.split(" "):
            retval.append(self.__stemmer.stem(word))
        return " ".join(retval)

    @staticmethod
    def __remove_non_alphanumeric_characters(text: str) -> str:
        retval = ""
        for c in text:
            if c.isalnum():
                retval += c
            else:
                retval += " "
        return retval
