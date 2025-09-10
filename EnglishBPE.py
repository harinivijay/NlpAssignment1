from collections import Counter
import re

# -----------------------------
# 1 Corpus
# -----------------------------
paragraph = """The quick brown fox jumps over the lazy dog. 
Dogs are often very quick and clever. 
A fox is sly and fast. 
Some dogs jump higher than others. 
The clever fox outsmarts the lazy dogs easily.""".lower().replace('\n', ' ')

corpus_words = paragraph.split()

# Add end-of-word marker _
corpus_chars = [' '.join(list(word) + ['_']) for word in corpus_words]

# -----------------------------
# 2️Functions for BPE
# -----------------------------
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

# -----------------------------
# 3️Learn BPE merges (30 steps)
# -----------------------------
num_merges = 30
merges_list = []

for step in range(num_merges):
    pairs = get_stats(corpus_chars)
    if not pairs:
        break
    best_pair = pairs.most_common(1)[0][0]
    merges_list.append(best_pair)
    corpus_chars = merge_pair(corpus_chars, best_pair)
    print(f"Step {step+1}: Most frequent pair {best_pair} | Vocabulary size: {len(set(''.join(corpus_chars)))}")

print("\nFinal corpus after 30 merges:")
print(corpus_chars)

# -----------------------------
# 4️Segment words using learned merges
# -----------------------------
def segment_word(word, merges):
    chars = list(word) + ['_']
    word_seq = chars
    for merge in merges:
        pattern = re.escape(' '.join(merge))
        repl = ''.join(merge)
        word_seq_str = ' '.join(word_seq)
        word_seq_str = re.sub(pattern, repl, word_seq_str)
        word_seq = word_seq_str.split()
    return word_seq

words_to_segment = ["fox", "dogs", "outsmarts", "clever", "higher"]
print("\nSubword segmentation:")
for w in words_to_segment:
    seg = segment_word(w.lower(), merges_list)
    print(f"{w} -> {seg}")

# -----------------------------
# 5️Top 5 merges and 5 longest tokens
# -----------------------------
pair_counts = get_stats(corpus_chars)
top_5_merges = pair_counts.most_common(5)
print("\nTop 5 merges after training:")
for pair, count in top_5_merges:
    print(f"{pair} : {count}")

# Longest subword tokens
all_tokens = set(''.join(corpus_chars).split())
longest_tokens = sorted(all_tokens, key=lambda x: len(x), reverse=True)[:5]
print("\n5 longest subword tokens:")
print(longest_tokens)
