#
# Ejemplos de propiedades de relaciones, 
# en Python 3.x
#
# Receta basica (usando idle3):
# 1) En idle3 open this file.
# 2) Run Module (F5) of this file.
# 3) Eventualmente en la ventana interactiva ejecutar comandos.
#
from bitmat import bitmat
import predicados

def test_predicados():
     
    # define matriz test A1
    A1 = bitmat([[1,1,0],
                 [1,1,0],
                 [0,0,0]])
    print ('matriz test A1')
    print (A1)
     
    # define matriz test A2
    A2 = bitmat([[1,1,0],
                 [1,1,0],
                 [0,0,1]])
    print ('matriz test A2')
    print (A2)
     
    # define matriz test A3
    A3 = bitmat([[1,1,0],
                 [1,1,1],
                 [0,0,1]])
    print ('matriz test A3')
    print (A3)
     
    # define matriz test A4
    A4 = bitmat([[1,0,0],
                 [0,1,0],
                 [0,0,1]])
    print ('matriz test A4')
    print (A4)
     
    # define matriz test A5
    A5 = bitmat([[1,1,0],
                 [1,0,1],
                 [0,0,0]])
    print ('matriz test A5')
    print (A5)
     
    # define matriz test A6
    A6 = bitmat([[1,1,0],
                 [0,1,0],
                 [0,0,0]])
    print ('matriz test A6')
    print (A6)
     
    # define matriz test A7
    A7 = bitmat([[0,1,0],
                 [0,0,0],
                 [0,0,0]])
    print ('matriz test A7')
    print (A7)

    # define matriz test A8
    A8 = bitmat([[1,0,0],
                 [0,1,0],
                 [0,0,0]])
    print ('matriz test A8')
    print (A8)
    
    # define matriz test A9
    A9 = bitmat([[1,1,0],
                 [0,1,0],
                 [0,0,1]])
    print ('matriz test A9')
    print (A9)
   
    # define matriz test B
    # B = bitmat(3)
    # B[0,2] = B[1,1] = B[2,0] = 1
    # print ('matriz B')
    # print (B)

    # tests en la A1
    assert predicados.es_reflexiva     (A1) == False
    assert predicados.es_simetrica     (A1) == True
    assert predicados.es_antisimetrica (A1) == False
    assert predicados.es_transitiva    (A1) == True
    assert predicados.es_relacion_de_equivalencia (A1) == False
    assert predicados.es_relacion_de_orden        (A1) == False

    # tests en la A2
    assert predicados.es_reflexiva     (A2) == True
    assert predicados.es_simetrica     (A2) == True
    assert predicados.es_antisimetrica (A2) == False
    assert predicados.es_transitiva    (A2) == True
    assert predicados.es_relacion_de_equivalencia (A2) == True
    assert predicados.es_relacion_de_orden        (A2) == False

    # tests en la A3
    assert predicados.es_reflexiva     (A3) == True
    assert predicados.es_simetrica     (A3) == False
    assert predicados.es_antisimetrica (A3) == False
    assert predicados.es_transitiva    (A3) == False
    assert predicados.es_relacion_de_equivalencia (A3) == False
    assert predicados.es_relacion_de_orden        (A3) == False

    # tests en la A4
    assert predicados.es_reflexiva     (A4) == True
    assert predicados.es_simetrica     (A4) == True
    assert predicados.es_antisimetrica (A4) == True
    assert predicados.es_transitiva    (A4) == True
    assert predicados.es_relacion_de_equivalencia (A4) == True
    assert predicados.es_relacion_de_orden        (A4) == True

    # tests en la A5
    assert predicados.es_reflexiva     (A5) == False
    assert predicados.es_simetrica     (A5) == False
    assert predicados.es_antisimetrica (A5) == False
    assert predicados.es_transitiva    (A5) == False
    assert predicados.es_relacion_de_equivalencia (A5) == False
    assert predicados.es_relacion_de_orden        (A5) == False

    # tests en la A6
    assert predicados.es_reflexiva     (A6) == False
    assert predicados.es_simetrica     (A6) == False
    assert predicados.es_antisimetrica (A6) == True
    assert predicados.es_transitiva    (A6) == True
    assert predicados.es_relacion_de_equivalencia (A6) == False
    assert predicados.es_relacion_de_orden        (A6) == False

    # tests en la A7
    assert predicados.es_reflexiva     (A7) == False
    assert predicados.es_simetrica     (A7) == False
    assert predicados.es_antisimetrica (A7) == True
    assert predicados.es_transitiva    (A7) == True 
    assert predicados.es_relacion_de_equivalencia (A7) == False
    assert predicados.es_relacion_de_orden        (A7) == False

    # tests en la A8
    assert predicados.es_reflexiva     (A8) == False
    assert predicados.es_simetrica     (A8) == True
    assert predicados.es_antisimetrica (A8) == True
    assert predicados.es_transitiva    (A8) == True 
    assert predicados.es_relacion_de_equivalencia (A8) == False
    assert predicados.es_relacion_de_orden        (A8) == False

    # tests en la A9
    assert predicados.es_reflexiva     (A9) == True 
    assert predicados.es_simetrica     (A9) == False
    assert predicados.es_antisimetrica (A9) == True 
    assert predicados.es_transitiva    (A9) == True 
    assert predicados.es_relacion_de_equivalencia (A9) == False
    assert predicados.es_relacion_de_orden        (A9) == True 

if __name__ == '__main__':
    test_predicados()

# end
