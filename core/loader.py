def load_text(filepath):
    """
    Reads a text file and returns its contents.
    """

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
