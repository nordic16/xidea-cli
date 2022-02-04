import pickle


def retrieve_notes(path: str) -> []:
    """Retrieves a list of notes from the desired file."""
    notes = []

    try:
        with open(path, 'rb') as f:
            # If the file isn't empty.
            if f.readlines():
                f.seek(0)
                notes = pickle.load(f)
                
    
    except FileNotFoundError: # Creates the file if it doesn't exist.
        open(path, 'x')

    return notes


def write_notes(path: str, notes: []):
    """Writes all notes to the desired file."""
    with open(path, 'wb') as f:
        pickle.dump(obj=notes, file=f)