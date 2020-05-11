import unittest
import prime_number
import sympy

class PrimesTestCase(unittest.TestCase):
    
    def test_numbers(self):
        a = 11
        result = prime_number.is_prime(a)
        self.assertEqual(result,sympy.isprime(11))
        
if __name__ == '__main__':
    unittest.main()
        
