# README

**Student Name:** Harini Vijayakumar  
**700#:** 700775210 

## ToolComparison
This program compares **manual tokenization** with a **tool tokenizer**.  
- Input: Text paragraph in Tamil language and manual tokens.  
- Output: Differences between manual and tool tokens.  
- Shows which words are split differently.  

## Mini-BPE
This program implements a **mini BPE learner**.  
- Input: Small corpus of words.  
- Learns BPE merges step by step.  
- Outputs: Merged corpus, top frequent pairs, segmented words.  
- Can handle rare and unseen words using subwords.  

## EnglishBPE
This program trains **BPE on an English paragraph**.  
- Input: Short paragraph of text.  
- Learns 30 merges (or more for longer text).  
- Outputs: Top 5 merges, 5 longest subword tokens, and segmentation of selected words.  
- Demonstrates how subwords capture prefixes, suffixes, stems, and whole words.
