import json

def leggi_da_file(filepath):
    """Questa funzione legge dati JSON da un file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    
def processa_dati(dati:list) -> list:

    """
    Questa funzione dovrebbe processare una lista di dizionari.
    Implementa la logica per filtrare i dizionari che hanno una chiave 'attivo'
    con valore True e restituire una nuova lista contenente solo i valori
    della chiave 'id' di questi dizionari.
    """
    
    lista_risultati = []

    for diz in dati:
        if diz["attivo"] == True:
            lista_risultati.append(diz["id"])
    
    return lista_risultati
    

if __name__ == "__main__":
    dizionario = leggi_da_file("dati/test.json")
    attivi = processa_dati(dizionario)
    print(attivi)
    
