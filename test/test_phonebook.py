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
        tamanho_lista_esperado = phoneBook.entries.__len__()
        nomes_esperados = phoneBook.entries.keys()

        # Act
        result = phoneBook.get_names()

        #Assert
        assert result.__len__() == tamanho_lista_esperado
        assert result == nomes_esperados

    def test_get_numbers(self):
        #Setup
        phoneBook = Phonebook()
        nome_valido = "Will"
        num_valido = "12"
        phoneBook.add(nome_valido, num_valido)
        tamanho_lista_esperado = phoneBook.entries.__len__()
        numeros_esperados = phoneBook.entries.values()

        # Act
        result = phoneBook.get_numbers()

        #Assert
        assert result.__len__() == tamanho_lista_esperado
        print()
        print(numeros_esperados)
        print(result)
        assert result == numeros_esperados

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


    #TDD Aqui :)
    #
    #
    #
    def test_change_number_nome_valido_numero_valido(self):  #Caso de sucesso
        #Setup
        phoneBook = Phonebook()
        nome_valido = "Alice"
        phoneBook.add(nome_valido, "81999999999")
        novo_numero = "819999"
        result_esperado = "Usuario alterado"

        #Act
        result = phoneBook.change_number(nome_valido, novo_numero)


        #Asserts
        assert result == result_esperado
        assert phoneBook.entries.get(nome_valido) == novo_numero

    def test_change_number_nome_invalido_numero_valido(self): #Caso para quando o nome não existir
        #Setup
        phoneBook = Phonebook()
        nome_invalido = "Joao"
        novo_numero = "999999999"
        result_esperado = "Usuario nao alterado"

        #Act
        result = phoneBook.change_number(nome_invalido, novo_numero)

        #Asserts
        assert result == result_esperado

    def test_change_number_nome_valido_numero_invalido(self): #Caso para quando o número for invalido
        #Setup
        phoneBook = Phonebook()
        nome_valido = "Alice"
        numero_valido = "81999999999"
        phoneBook.add(nome_valido, numero_valido)

        novo_numero = "0"
        result_esperado = "Usuario nao alterado"

        #Act
        result = phoneBook.change_number(nome_valido, novo_numero)

        #Asserts
        assert result == result_esperado