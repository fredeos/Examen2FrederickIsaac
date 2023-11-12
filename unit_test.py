import unittest

from Examen2 import MiClase

class Pruebas_MiClase(unittest.TestCase):
    instancia = MiClase(5, 90, 4, ["Sleepwalker", "Midnight City", "Set fire to the rain"], [0.3 , 0.6 , 0.2])

    def test_ObtenerValencia(self):
        self.assertEqual(self.instancia.ObtieneValencia(136), 2) # 1era prueba del metodo
        self.assertEqual(self.instancia.ObtieneValencia(245), 1) # 2nd prueba del metodo

    def test_DivisibleTempo(self):
        self.assertEqual(self.instancia.DivisibleTempo(3), [1,3]) # 1era prueba del metodo
        self.assertEqual(self.instancia.DivisibleTempo(9), [1,3,9]) #2nd prueba del metodo

    def test_ObtieneMasBailable(self):
        self.assertEqual(self.instancia.ObtieneMasBailable(self.instancia.listaBailabilidad), 0.6) # 1era prueba del metodo
        self.assertGreater(self.instancia.ObtieneMasBailable([7,81,2000]), 1000) # 2nd prueba del metodo

    def test_VerfificaListaCanciones(self):
        self.assertEqual(self.instancia.VerificaListaCanciones(self.instancia.listaCanciones), True) # 1era prueba del metodo
        self.assertEqual(self.instancia.VerificaListaCanciones(["Cancion1", None, "Cancion3"]), False) # 2da prueba del metodo
    
    def test_Encuentra(self):
        self.assertEqual(self.instancia.Encuentra([1,2,3,4],3),True) # 1era prueba del metodo
        self.assertEqual(self.instancia.Encuentra([1,2,3,4],7),False) # 2da prueba del metodo
    def test_ObtenerPares(self):
        self.assertEqual(self.instancia.ObtienePares(136), 1) # 1era prueba del metodo
        self.assertEqual(self.instancia.ObtienePares(245), 1) # 2nd prueba del metodo


if __name__ == "__main__":
    unittest.main()