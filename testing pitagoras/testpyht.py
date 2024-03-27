def hitung_hipotenusa(a, b):
    return (a**2 + b**2) ** 0.5

def test_hitung_hipotenusa():
    # Test case 1: a = 3, b = 4
    a = 3
    b = 4
    hasil = hitung_hipotenusa(a, b)
    assert hasil == 5

    # Test case 2: a = 5, b = 12
    a = 5
    b = 12
    hasil = hitung_hipotenusa(a, b)
    assert hasil == 13

    # Test case 3: a = 8, b = 15
    a = 8
    b = 15
    hasil = hitung_hipotenusa(a, b)
    assert hasil == 17

    # Test case 4: bilangan negatif
    a = -3
    b = 4
    hasil = hitung_hipotenusa(a, b)
    assert hasil == 5

    # Test case 5: hasil nol
    a = 0
    b = 0
    hasil = hitung_hipotenusa(a, b)
    assert hasil == 0

    # Test case 6: a > b
    a = 12
    b = 5
    hasil = hitung_hipotenusa(a, b)
    assert hasil == 13

    # Test case 7: a < b
    a = 5
    b = 12
    hasil = hitung_hipotenusa(a, b)
    assert hasil == 13

