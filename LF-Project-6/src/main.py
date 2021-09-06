import numpy as np
import neattext.functions as nfx
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer('bert-base-nli-mean-tokens')

all_embeddings = np.load('../data/embeddings.npy', allow_pickle=True)

def check_similarity(query, data_frame):

    similarity_score = []

    query = nfx.clean_text(query, stopwords=True, contractions=True, multiple_whitespaces=True, special_char=True)
    query_embedding = model.encode(query)
    
    for val in range(len(data_frame)):
        cos_sim = cosine_similarity([query_embedding], [all_embeddings[val]])
        similarity_score.append(cos_sim)
    
    data_frame['similarity_score'] = similarity_score
    

    return data_frame.sort_values(by=['similarity_score'], ascending=False)