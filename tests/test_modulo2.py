import pytest
from progetto.modulo2 import processa_dati, leggi_da_file

def test_processa_dati():
    risultato = processa_dati(leggi_da_file("dati/test.json"))
    assert risultato == [1, 3, 4, 6]
