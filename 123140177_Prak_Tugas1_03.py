import math

class Calculator:
    def __init__(self, value):
        self.value = value

#penjumlahan
    def __add__(self, other):
        return Calculator(self.value + other.value)

#pengurangan
    def __sub__(self, other):
        return Calculator(self.value - other.value)

#perkalian
    def __mul__(self, other):
        return Calculator(self.value * other.value)

#pembagian
    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("Tidak bisa membagi dengan nol")
        return Calculator(self.value / other.value)

#pangkat
    def __pow__(self, other):
        return Calculator(self.value ** other.value)

#logaritma natural (Log)
    def log(self):
        if self.value <= 0:
            raise ValueError("Logaritma tidak terdefinisi untuk nilai non-positif")
        return math.log(self.value)

#string untuk mencetak nilai
    def __str__(self):
        return f"Hasil: {self.value}"

#Fungsi untuk meminta input
def input_angka(pesan):
    while True:
        try:
            angka = float(input(pesan))
            return angka
        except ValueError:
            print("Masukkan angka yang valid!")
# Fungsi main
def main():
    print("Kalkulator Note 20 Pro")

#input angka pertama
    angka1 = input_angka("Masukkan angka pertama: ")
    a = Calculator(angka1)
#pilihan operasi
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (**)")
    print("6. Logaritma Natural (log)")

#memilih operasi
    pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

    #jika piliha operasi bukan 6 (Log) maka akan memilih angka ke 2
    if pilihan != '6':
        angka2 = input_angka("Masukkan angka kedua: ")
        b = Calculator(angka2)

#Melakukan operasi sesuai pilihan
    if pilihan == '1':
        print(a + b)
    elif pilihan == '2':
        print(a - b)
    elif pilihan == '3':
        print(a * b)
    elif pilihan == '4':
        try:
            print(a / b)
        except ZeroDivisionError as e:
            print(e)
    elif pilihan == '5':
        print(a ** b)
    elif pilihan == '6':
        try:
            print(f"Logaritma natural dari {a.value}: {a.log()}")
        except ValueError as e:
            print(e)
    else:
        print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()