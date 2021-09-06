from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def jaccard_similarity(query, document):
    query = query.lower().split()
    document = document.lower().split()

    intersection = [word for word in query if word in document]
    union = query + list(set(document) - set(query))
    return len(intersection)/len(union)

def vectorizer(query, corpus=[]):
    
    count_vector = TfidfVectorizer(ngram_range=(1,1))
    
    corpus_vectors = count_vector.fit_transform(corpus)
    query_vector = count_vector.transform([query]).reshape(1, -1)

    similarity_score = []
    for i in range(len(corpus)):
        similarity_score.append(cosine_similarity(query_vector, corpus_vectors[i].reshape(1, -1)[0][0])[0][0])

    for i in range(len(corpus)):
        print("Similarity between '{}' and '{}' is {}".format(query, corpus[i], round(similarity_score[i],2)))

    return None

def transformer_similarity(query, sentences=[]):
    sentences.insert(0, query)
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    sentence_embeddings = model.encode(sentences)
    similarity_scores = cosine_similarity([sentence_embeddings[0]], sentence_embeddings[1:])

    for i in range(len(similarity_scores[0])):
        print("Similarity between '{}' and '{}' is {}".format(sentences[0], sentences[i+1], round(similarity_scores[0][i]),2))

    return None

if __name__ == '__main__':
    
    sentences=['My name is Roman']

    print('###########TfidfVectorizer###########')
    vectorizer('People call me Roman', corpus=sentences)

    print()

    print('###########BERT###########')
    transformer_similarity('People call me Roman', sentences=sentences)
    