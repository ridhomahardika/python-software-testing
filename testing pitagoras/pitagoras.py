print("Kalkulator teorema Pythagoras! Hitung sisi-sisi segitiga anda.")
print("Se supaya lebih mudah dipahami, sebutkan sisi b sebagai sisi a biar a² + b² = c².")

while True:
    print("Masukkan nama sisi yang ingin dihitung: a, b, atau c.")
    formula = input("> ")
    if formula == 'a':
        side_b = int(input("Masukkan panjang sisi b: "))
        side_c = int(input("Masukkan panjang sisi c: "))

        side_a = (side_c**2 - side_b**2)**0.5

        print("Panjang sisi a adalah:")
        print(side_a)

    elif formula == 'b':
        side_a = int(input("Masukkan panjang sisi a: "))
        side_c = int(input("Masukkan panjang sisi c: "))

        side_b = (side_c**2 - side_a**2)**0.5

        print("Panjang sisi b adalah:")
        print(side_b)

    elif formula == 'c':
        side_a = int(input("Masukkan panjang sisi a: "))
        side_b = int(input("Masukkan panjang sisi b: "))

        side_c = (side_a**2 + side_b**2)**0.5

        print("Panjang sisi c adalah:")
        print(side_c)

    else:
        print("Silakan masukkan nama sisi antara a, b, atau c.")