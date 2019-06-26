import unittest
import xenakis

class TestXenakisMethods(unittest.TestCase):
    def test_hmac_security_equal(self):
        a = {'a' : 2}
        a_packed = xenakis.pack(a)
        b = {'a' : 2}
        b_packed = xenakis.pack(b)
        self.assertEqual(xenakis.unpack(a_packed), xenakis.unpack(b_packed))

    def test_hmac_security_diff(self):
        a = {'a' : 2}
        a_packed = xenakis.pack(a)
        a_packed = a_packed[:5] + b'X' + a_packed[6:] # man-in-the-middle
        self.assertRaises(xenakis.InvalidSignature, xenakis.unpack, a_packed)

if __name__ == '__main__':
    unittest.main()
