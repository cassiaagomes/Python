from sala import *


class Entry:
    """Uma classe privada utilizada para encapsular os pares chave/valor"""
    __slots__ = ("key", "value")

    def __init__(self, entryKey, entryValue):
        self.key = entryKey
        self.value = entryValue

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class ChainHashTable:
    def __init__(self, size):
        self.size = size
        # inicializa a tabela de dispersão com todos os elementos iguais a None
        self.table = list([] for i in range(self.size))

    def __hash(self, key: str) -> int:
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def put(self, key: int, data: object) -> int:
        '''Insere um par chave/valor na tabela hash.
           Retorna o slot em que o par chave/valor foi inserido'''
        slot = self.__hash(key)
        #print(f'Chave {key} no slot {slot}')

        # verifica se a chave já está no list relativo ao slot
        for entry in self.table[slot]:
            if entry.key == key:
                return -1

        self.table[slot].append(Entry(key, data))
        return slot

    def get(self, key: int):
        '''Obtem o valor associado à chave de busca.'''
        slot = self.__hash(key)
        for entry in self.table[slot]:
            if entry.key == key:
                return entry.value
        return -1

    def __str__(self):
        info = ""
        for items in self.table:
            if items is None:
                continue
            for entry in items:
                info += str(entry)
        return info

    def __len__(self):
        return self.size

    def keys(self):
        """Retorna uma lista de chaves na tabela hash."""
        result = []
        for lst in self.table:
            if lst is not None:
                for entry in lst:
                    result.append(entry.key)
        return result

    def contains(self, key):
        """Retorna True se a tabela hash contém uma entrada com a chave dada."""
        for items in self.table:
            if items is not None:
                for entry in items:
                    if entry.key == key:
                        return True
        return False

    def displayTable(self):
        entrada = -1
        for items in self.table:
            entrada += 1
            print(f'Entrada {entrada:2d}: ', end='')
            if len(items) == 0:
                print(' None')
                continue
            for entry in items:
                print(f'[ {entry.key},{entry.value} ] ', end='')
            print()

    def search(self, key: int):
        """Percorre a tabela hash em busca da chave especificada.
           Retorna 'Thure' se a chave for encontrada, caso contrário, retorna 'None'."""
        slot = self.__hash(key)
        for entry in self.table[slot]:
            if entry.key == key:
                return True
        return False

            
