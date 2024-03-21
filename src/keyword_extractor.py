from keybert import KeyBERT
from sentence_transformers import SentenceTransformer


class KeyWordsExtractor(object):

    def __init__(self):
        self.sentence_model = SentenceTransformer("multi-qa-mpnet-base-dot-v1")
        self.keyword_model= KeyBERT(model=self.sentence_model)

    def extract_keywords(self, doc: str)->list:
        return self.keyword_model.extract_keywords(doc,
                                                   stop_words='english',
                                                   use_mmr=True,
                                                   diversity=0.8,
                                                   nr_candidates=20,
                                                   keyphrase_ngram_range=(1,5)
                                                   )