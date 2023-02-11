class Phonebook:
    def __init__(self):
        self.entries = {'POLICIA': '190'}
        self.tamanho_minimo_numero = 3

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if self.verify_valid_name(name):
            pass
        else:
            return "Nome invalido"

        if self.verify_valid_number(number):
           pass
        else:
            return "Numero invalido"

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def verify_valid_name(self, name):#Refatoração
        caracteres_invalidos = ['#', '@', '!', '$', '%']
        for item in caracteres_invalidos:
            if item in name:
                return False
        return True

    def verify_valid_number(self, number):     #Refatoração
        if len(number) > self.tamanho_minimo_numero:
            return True
        else:
            return False


    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if self.verify_valid_name(name):
            pass
        else:
            return "Nome invalido"

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name not in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'
