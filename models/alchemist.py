class Alchemist:
    def __init__(self, name, email, status, id = None):
        self.name = name
        self.email = email
        self.status = status
        self.id = id

    def info(self):
        return f'All items by {self.name}. Order more by {self.email}.'

    
        