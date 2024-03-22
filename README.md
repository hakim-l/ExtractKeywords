# Intro
To complete the task, I utilized pretrained deep learning model.
For the assignment, I used multi-qa-mpnet-base-dot-v1 sentence transformer through sentence-transformer and keybert library.

The multi-qa-mpnet-base-dot-v1 model is part of the sentence-transformers library. It serves as a powerful tool for semantic search, mapping sentences and paragraphs to a 768-dimensional dense vector space. Here are some key details about this model:
Purpose: Designed specifically for semantic search.
Training Data: Trained on an impressive 215 million (question, answer) pairs from diverse sources.
Vector Space Dimension: The model maps text to a 768-dimensional vector space.

# Instruction
1. Install the required packages with following command\
`
pip install -r requirements.txt
`

2. Prepare the input text data by save it to data/input_text.txt
3. To get keywords run following command\
`
python main.py
`
