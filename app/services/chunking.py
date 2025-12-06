def chunk_text(text, max_length=6000):
    chunks = []
    while len(text) > max_length:
        cut = text[:max_length]
        last_period = cut.rfind(".")
        if last_period != -1:
            cut = text[:last_period+1]
        chunks.append(cut)
        text = text[len(cut):]
    chunks.append(text)
    return chunks
