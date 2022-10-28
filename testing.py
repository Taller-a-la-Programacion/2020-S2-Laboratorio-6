import Laboratorio6;
import pytest;
    
def test_eliminarRepetidos_1():
    assert Laboratorio6.eliminarRepetidos( [12, 78, 12, 0, 5.2, "abc", 0, 12, 5.2, 12] ) == [78, "abc"]
    
def test_eliminarRepetidos_2():
    assert Laboratorio6.eliminarRepetidos( [12, 5.2, 12] ) == [5.2]
    
def test_sumaImparesPares_1():
    assert Laboratorio6.sumaImparesPares([0,2,3,4], [4, 8, 6, 0]) == [13, 14]
    
def test_sumaImparesPares_2():
    assert Laboratorio6.sumaImparesPares([10, 0], [100, 2]) == [110, 2]
    
def test_sumaImparesPares_3():
    assert isinstance(Laboratorio6.sumaImparesPares([1,2], "dos"), str) == isinstance("Error: segundo argumento debe ser entero", str)
    
def test_convertirBase_1():
    assert Laboratorio6.convertirBase([0,0,1,0] , 2, 10) == 2

def test_matriz_1():
    assert Laboratorio6.matrizDiagonalInversa( [[0,0,1,0], [0,0,1,0], [0,0,1,0], [0,0,1,0]]) == [0, 0, 1, 0]
    
def test_matriz_2():
    assert Laboratorio6.matrizDiagonalInversa( [[0,0,1], [0,1,0], [0,0,0]]) == [0, 1, 0]
