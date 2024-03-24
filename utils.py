from langchain.text_splitter import TokenTextSplitter
from sentence_transformers import SentenceTransformer


def text_split(text):
    """This function makes chunks of the text

    Args:
        text (str): text to split into chunks

    Returns:
        texts: a list with equal-sized chunks
    """
    text_splitter = TokenTextSplitter(
        encoding_name="gpt2", chunk_size=250, chunk_overlap=10
    )
    texts = text_splitter.split_text(text)

    texts = list(map(lambda x: x.replace("\n", " "), texts))

    return texts


def embedding(texts):
    """This function receives a list of texts and returns the embeddings

    Args:
        texts (list[str]): The texts to encode

    Returns:
        embedding_list: a list with the vectors
    """
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    embedding_list = model.encode(texts)
    return embedding_list
