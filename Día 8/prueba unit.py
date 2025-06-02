import unittest
import archivo1
#voy a probar el metodo en la clase de abajo
class probar_archivo1(unittest.TestCase):
    def test_mayusculas(self):
        palabra = 'hola'
        resultado = archivo1.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'HOLA')

if __name__=='__main__':
    unittest.main()