# Install Indic NLP if not already installed
# pip install indic-nlp-library
import os
from itertools import zip_longest

from indicnlp.tokenize import indic_tokenize

INDIC_RESOURCES_PATH = "/Users/harinismac/Documents/Masters/Fall 2025/NLP/indic_nlp_resources"
os.environ['INDIC_NLP_RESOURCES'] = INDIC_RESOURCES_PATH
# Text paragraph
text = "தமிழ்நாட்டில் பள்ளிகள், கல்லூரிகள் செப்டம்பர் 11 அன்று மூடல். இது மார்ட்டியர் எமனுவேல் சேகரனின் 68வது நினைவு நாளையொட்டி ஏற்பாடு செய்யப்பட்டுள்ளது. அனைத்து மாணவர்களும் அந்த நாளில் பள்ளி மற்றும் கல்லூரிக்கு செல்ல வேண்டியில்லை. அரசு அதிகாரிகள், ஆசிரியர்கள் மற்றும் மாணவர்கள் அனைவரும் நினைவூட்டல் நிகழ்ச்சிகளில் கலந்து கொள்வார்கள்."

# Tokenize using Indic NLP
tokens_tool = indic_tokenize.trivial_tokenize(text, lang='ta')

# Manually corrected tokens
tokens_manual = ["தமிழ்நாட்டில்","பள்ளிகள்",",","கல்லூரிகள்","செப்டம்பர்","11","அன்று","மூடல்",".",
                 "இது","மார்ட்டியர்","எமனுவேல்","சேகரனின்","68வது","நினைவு","நாளையொட்டி","ஏற்பாடு","செய்யப்பட்டுள்ளது",".",
                 "அனைத்து","மாணவர்களும்","அந்த","நாளில்","பள்ளி","மற்றும்","கல்லூரிக்கு","செல்ல","வேண்டியில்லை",".",
                 "அரசு","அதிகாரிகள்",",","ஆசிரியர்கள்","மற்றும்","மாணவர்கள்","அனைவரும்","நினைவூட்டல்","நிகழ்ச்சிகளில்","கலந்துகொள்வார்கள்","."]

# Compare outputs
print('Mismatched tokens are as follows:')

for t_manual, t_tool in zip_longest(tokens_manual, tokens_tool, fillvalue="<MISSING>"):
    if t_manual != t_tool:
        print(f" Manual: '{t_manual}' | Tool: '{t_tool}'")
