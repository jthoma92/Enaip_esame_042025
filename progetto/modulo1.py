def funzione_doppio(x):
    """Questa funzione restituisce il doppio del argomento passato alla funzione"""
    # TODO: Implementare la funzione per restituire il doppio di x
    pass

def funzione_quadrato(y):
    """
    Questa funzione dovrebbe prendere un numero e restituire il suo quadrato.
    Completa l'implementazione.
    """
    # TODO: Implementare la funzione per restituire il quadrato di y
    pass

class ClasseParzialmenteImplementata:
    def __init__(self, nome):
        self.nome = nome

    def metodo_esistente(self):
        return f"Ciao, sono {self.nome}!"

    def metodo_da_completare(self, valore:str):
        """
        Questo metodo aggiunge una stringa al self.nome
        """
        return self.nome + valore