from processor import Processor
from validator import Validator

if __name__ == '__main__':

    text1 = "The quick brown fox jumps over the lazy dog"
    text2 = "The lazy dog jumps over the quick brown fox"

    validator = Validator()

    distance = validator.levenshtein_distance(text1, text2)
    score = validator.text_similarity_score(text1, text2)

    print(f"No processor - distance: {distance}, score: {score}")

    processor = Processor()
    validator = Validator(processor=processor.base_text_processor)

    distance = validator.levenshtein_distance(text1, text2)
    score = validator.text_similarity_score(text1, text2)

    print(f"Simple processor - distance: {distance}, score: {score}")

    processor = Processor()
    validator = Validator(processor=processor.stemming_processor)

    distance = validator.levenshtein_distance(text1, text2)
    score = validator.text_similarity_score(text1, text2)

    print(f"Porter stemmer - distance: {distance}, score: {score}")
