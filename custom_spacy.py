import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load("en_core_web_md")

ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    {"label": "PERSON", "pattern": [{"POS": "PROPN"}]},
    {"label": "PERSON", "pattern": [{"POS": "PROPN"}, {"POS": "PROPN"}]},
    {"label": "PERSON", "pattern": [{"POS": "PROPN"}, {"POS": "PROPN"}, {"POS": "PROPN"}]},
    {"label": "PERSON", "pattern": [{"POS": "PROPN"}, {"POS": "PROPN"}, {"POS": "PROPN"}, {"POS": "PROPN"}]},
    {"label": "PERSON", "pattern": [{"TEXT": {"REGEX": "^[A-Za-z]\."}}, {"POS": "PROPN"}]},
]

ruler.add_patterns(patterns)
nlp.to_disk("./custom_en_model")
print("Custom spaCy model created successfully at ./custom_en_model")