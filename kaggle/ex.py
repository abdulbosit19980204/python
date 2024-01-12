word_count = []
key_finder = []
keywords = ['casino', 'they']
doc_list = ["The Learn Python Challenge Casino they", "They bought a car", "Casinoville they "]


def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    # >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    # >>> keywords = ['casino', 'they']
    # >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    indxs = {key: [] for key in keywords}
    for i, str_txt in enumerate(doc_list):
        txt_list = str_txt.split()
        txt = [word.strip(',.').lower() for word in txt_list]
        for key in keywords:
            if key.lower() in txt:
                indxs[key].append(i)
    return indxs


# Check your answer

print(multi_word_search(doc_list, keywords))
