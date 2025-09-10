from collections import Counter
import re

# Toy corpus
corpus = ["low", "low", "low", "low", "low",
          "lowest", "lowest",
          "newer", "newer", "newer", "newer", "newer", "newer",
          "wider", "wider", "wider",
          "new", "new"]

# 1️⃣ Preprocess: add end-of-word marker '_' and split into chars
corpus_chars = [' '.join(list(word) + ['_']) for word in corpus]

def get_stats(corpus_list):
    """Count adjacent symbol pairs (bigrams) across the corpus"""
    pairs = Counter()
    for word in corpus_list:
        symbols = word.split()
        for i in range(len(symbols)-1):
            pair = (symbols[i], symbols[i+1])
            pairs[pair] += 1
    return pairs

def merge_pair(corpus_list, pair_to_merge):
    """Merge the most frequent pair in corpus"""
    merged_corpus = []
    pattern = re.escape(' '.join(pair_to_merge))
    repl = ''.join(pair_to_merge)
    for word in corpus_list:
        new_word = re.sub(pattern, repl, word)
        merged_corpus.append(new_word)
    return merged_corpus

# Mini-BPE: perform 5 merges
num_merges = 5
for step in range(num_merges):
    pairs = get_stats(corpus_chars)
    if not pairs:
        break
    best_pair = pairs.most_common(1)[0][0]
    print(f"Step {step+1} - Most frequent pair: {best_pair}, Corpus size: {len(set(''.join(corpus_chars)))}")
    corpus_chars = merge_pair(corpus_chars, best_pair)

print("\nFinal corpus with subwords:")
print(corpus_chars)

# 2️⃣ Segment specific words
def segment_word(word, merges):
    # Start with chars + _
    chars = list(word) + ['_']
    word_seq = chars
    for merge in merges:
        pattern = re.escape(' '.join(merge))
        repl = ''.join(merge)
        word_seq_str = ' '.join(word_seq)
        word_seq_str = re.sub(pattern, repl, word_seq_str)
        word_seq = word_seq_str.split()
    return word_seq

# List of merges from BPE
corpus_temp = [' '.join(list(w)+['_']) for w in corpus]
merges_list = []
for step in range(num_merges):
    pairs = get_stats(corpus_temp)
    if not pairs:
        break
    best_pair = pairs.most_common(1)[0][0]
    merges_list.append(best_pair)
    corpus_temp = merge_pair(corpus_temp, best_pair)

words_to_segment = ["new", "newer", "lowest", "widest", "newestest"]
print("\nSubword segmentation:")
for w in words_to_segment:
    seg = segment_word(w, merges_list)
    print(f"{w} -> {seg}")
