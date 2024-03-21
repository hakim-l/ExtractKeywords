class TextFilePipeline(object):
    def __init__(self):
        pass

    def load_data(self, file_dir:str)->str:
        with open(file_dir,'r') as infile:
            data= infile.read()
        del infile
        return data