def prettify_text(text):
    text = text.replace('True', 'Yes')
    text = text.replace('False', 'No')
    text = text.replace('None', 'Unknown')
    return text
