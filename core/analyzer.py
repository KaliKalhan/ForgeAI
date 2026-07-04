def analyze(text):

    characters = len(text)

    words = len(text.split())

    lines = len(text.splitlines())

    paragraphs = len(
        [p for p in text.split("\n\n") if p.strip()]
    )

    return {
        "characters": characters,
        "words": words,
        "lines": lines,
        "paragraphs": paragraphs,
    }
