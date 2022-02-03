import random, string

class Note:
    title: str
    description: str
    content: str
    id: str

    def __init__(self, title, description, content):
        self.title = title
        self.description = description
        self.content = content
        self.id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(32)])

    def __str__(self):
        return f'[{self.title}, {self.description}, {self.content}]'

    