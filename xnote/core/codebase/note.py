import random, string
import pickle
from xnote.core.constants import *

class Note:
    title: str
    description: str
    content: str
    id: str


    def __init__(self, title : str, description : str, content : str):
        if len(title) <= MAX_TITLE_LENGTH and len(description) <= MAX_DESC_LENGTH and len(content) <= MAX_CONTENT_LENGTH:
            self.title = title
            self.description = description
            self.content = content
            self.id = ''.join([random.choice(string.ascii_letters
                + string.digits) for n in range(24)])
        
        else:
            print("Error: One of the fields is larger than what it should be.\n")
            print("Here are the max length for each field:",
                f"Title: {MAX_TITLE_LENGTH}", f"Description: {MAX_DESC_LENGTH}", f"Content: {MAX_CONTENT_LENGTH}", sep='\n')

            # Prevents this note from being created.
            exit(-1)

    def __str__(self):
        return f'Title: {self.title}\nDescription: {self.description}\nContent: {self.content}\nID: {self.id}]'


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