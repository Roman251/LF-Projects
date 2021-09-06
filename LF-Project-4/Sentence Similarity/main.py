import models

raw_input = input("Enter the sentence you want the similarity score for : ")

print()

print("Seperate each sentence by a comma.")
corpus = [input("Enter the list of sentences you want to check the similarity score against : ")]

print()

print("TFIDF : Vectorizer")
print("Tansformer : BERT Transformen")
print("Compare : BERT/Vectorizer")

choice = input("Which model would you like to use?\n")

if choice == 'TFIDF':
    models.vectorizer(raw_input, corpus)

elif choice == 'Transformer':
    models.transformer_similarity(raw_input, corpus)

elif choice == 'Compare':
    print('###########TfidfVectorizer###########')
    models.vectorizer(raw_input, corpus)

    print()

    print('###########BERT###########')
    models.transformer_similarity(raw_input, corpus)

else:
    print("No model found for {}".format(choice))