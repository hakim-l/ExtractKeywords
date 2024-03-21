from src.input_pipeline import TextFilePipeline
from src.keyword_extractor import KeyWordsExtractor
import argparse
import pathlib
import os

CURDIR= pathlib.Path(__file__).resolve().parent

def load_data(file_dir: str)-> str:
    pipeline= TextFilePipeline()
    return pipeline.load_data(file_dir)

def get_keywords(doc: str)-> list:
    keywords_extractor= KeyWordsExtractor()
    return keywords_extractor.extract_keywords(doc)

if __name__=='__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument('--file_dir',
                        type=str,
                        default= os.path.join(CURDIR,
                                              'data',
                                              'input_text.txt'
                                              )
                        )

    args= parser.parse_args()

    doc= load_data(args.file_dir)
    keywords= get_keywords(doc)
    print(keywords)
