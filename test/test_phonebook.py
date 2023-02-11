from src.phonebook import Phonebook
class TestPhonebook:

    def test_add_nome_valido_numero_valido(self):
        #Setup
        phoneBook = Phonebook()
        nome_valido = "Willams"
        num_valido = "8198770767"
        resul_esperado = "Numero adicionado"

        #Act
        result = phoneBook.add(nome_valido, num_valido)

        #Asserts
        assert result == resul_esperado
        assert phoneBook.entries.keys().__contains__(nome_valido)
        assert phoneBook.entries.get(nome_valido) == num_valido

    def test_add_nome_com_hashtag_numero_valido(self):
        #Setup
        phoneBook = Phonebook()
        nome_invalido = "#Willams#"
        num_valido = "81999999999"
        lista_antes = phoneBook.entries
        resul_esperado = "Nome invalido"

        #Act
        result = phoneBook.add(nome_invalido, num_valido)

        #Asserts
        assert result == resul_esperado
        assert phoneBook.entries.__len__() == lista_antes.__len__()

    def test_add_nome_com_arroba_numero_valido(self):
        #Setup
        phoneBook = Phonebook()
        nome_invalido = "@Willams@"
        num_valido = "81999999999"
        lista_antes = phoneBook.entries
        resul_esperado = "Nome invalido"

        #Act
        result = phoneBook.add(nome_invalido, num_valido)

        #Asserts
        assert result == resul_esperado
        assert phoneBook.entries.__len__() == lista_antes.__len__()

    def test_add_nome_com_exclamacao_numero_valido(self):
        #Setup
        phoneBook = Phonebook()
        nome_invalido = "!Willams"
        num_valido = "81999999999"
        lista_antes = phoneBook.entries
        resul_esperado = "Nome invalido"

        #Act
        result = phoneBook.add(nome_invalido, num_valido)

        #Asserts
        assert result == resul_esperado
        assert phoneBook.entries.__len__() == lista_antes.__len__()

    def test_add_nome_com_cifrao_numero_valido(self):
        # Setup
        phoneBook = Phonebook()
        nome_invalido = "$Willams$"
        num_valido = "81999999999"
        lista_antes = phoneBook.entries
        resul_esperado = "Nome invalido"

        # Act
        result = phoneBook.add(nome_invalido, num_valido)

        # Asserts
        assert result == resul_esperado
        assert phoneBook.entries.__len__() == lista_antes.__len__()

    def test_add_nome_com_porcentagem_numero_valido(self):
        # Setup
        phoneBook = Phonebook()
        nome_invalido = "Will%"
        num_valido = "81999999999"
        lista_antes = phoneBook.entries
        resul_esperado = "Nome invalido"

        # Act
        result = phoneBook.add(nome_invalido, num_valido)

        # Asserts
        assert result == resul_esperado
        assert phoneBook.entries.__len__() == lista_antes.__len__()

    def test_add_nome_valido_numero_invalido(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "Will"
        num_invalido = "12"
        lista_antes = phoneBook.entries
        resul_esperado = "Numero invalido"

        # Act
        result = phoneBook.add(nome_valido, num_invalido)

        # Asserts
        assert result == resul_esperado
        assert phoneBook.entries.__len__() == lista_antes.__len__()

    def test_lookup_nome_valido(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)

        # Act
        result = phoneBook.lookup(nome_valido)

        # Asserts
        assert result == num_valido

    def test_lookup_nome_invalido_com_hashtag(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "#Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        resul_esperado = "Nome invalido"

        # Act
        result = phoneBook.lookup(nome_valido)

        # Asserts
        assert result == resul_esperado

    def test_lookup_nome_invalido_com_arroba(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "@Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        resul_esperado = "Nome invalido"

        # Act
        result = phoneBook.lookup(nome_valido)

        # Asserts
        assert result == resul_esperado

    def test_lookup_nome_invalido_com_exclamacao(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "!Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        resul_esperado = "Nome invalido"

        # Act
        result = phoneBook.lookup(nome_valido)

        # Asserts
        assert result == resul_esperado

    def test_lookup_nome_invalido_com_cifrao(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "$Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        resul_esperado = "Nome invalido"

        # Act
        result = phoneBook.lookup(nome_valido)

        # Asserts
        assert result == resul_esperado

    def test_lookup_nome_invalido_com_porcentagem(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "Will%"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        resul_esperado = "Nome invalido"

        # Act
        result = phoneBook.lookup(nome_valido)

        # Asserts
        assert result == resul_esperado

    def test_get_names(self):
        #Setup
        phoneBook = Phonebook()
        nome_valido = "Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        tamanho_lista_esperado = 2

        # Act
        result = phoneBook.get_names()

        #Assert
        assert result.__len__() == tamanho_lista_esperado
        assert result.__contains__(nome_valido)

    def test_get_numbers(self):
        #Setup
        phoneBook = Phonebook()
        nome_valido = "Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        tamanho_lista_esperado = 2

        # Act
        result = phoneBook.get_numbers()

        #Assert
        assert result.__len__() == tamanho_lista_esperado

    def test_clear(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        tamanho_lista_esperado = 0
        resul_esperado = "phonebook limpado"

        # Act
        result = phoneBook.clear()

        # Assert
        assert result == resul_esperado
        assert phoneBook.entries.__len__() == tamanho_lista_esperado

    def test_search_nome_valido(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "Will"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)

        # Act
        result = phoneBook.search(nome_valido)

        # Assert
        assert result.__contains__(nome_valido)

    def test_get_phonebook_sorted(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "Alice"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        lista_esperada = phoneBook.entries

        # Act
        result = phoneBook.get_phonebook_sorted()

        # Assert
        assert result == lista_esperada

    def test_get_phonebook_reverse(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "Alice"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        lista_esperada = sorted(phoneBook.entries, key=phoneBook.entries.get, reverse=True)


        # Act
        result = phoneBook.get_phonebook_reverse()

        # Assert
        print(lista_esperada)

    def test_delete(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido = "Alice"
        num_valido = "81999999999"
        phoneBook.add(nome_valido, num_valido)
        resul_esperado = 'Numero deletado'
        tamanho_lista_esperado = 1

        # Act
        result = phoneBook.delete(nome_valido)

        #Assert
        assert resul_esperado == result
        assert phoneBook.entries.__len__() == tamanho_lista_esperado