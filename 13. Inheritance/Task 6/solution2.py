class ContactList(list):
    def __init__(self, value=list()):
        self.value = value

    def search_by_name(self, name):
        result = []
        for elem in self.value:
            if name in elem:
                result.append(elem)
        return result

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya'))