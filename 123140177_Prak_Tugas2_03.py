import random
# Kelas Father
class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.alleles = self.get_alleles(blood_type)

    # Fungsi untuk mengubah golongan darah menjadi alel
    @staticmethod
    def get_alleles(blood_type):
        if blood_type == "A":
            return ["A", "O"]  
        elif blood_type == "B":
            return ["B", "O"]  
        elif blood_type == "AB":
            return ["A", "B"]  
        elif blood_type == "O":
            return ["O", "O"] 
        else:
            raise ValueError("Golongan darah tidak valid")

# Kelas Mother
class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.alleles = self.get_alleles(blood_type)

    # Fungsi untuk mengubah golongan darah menjadi alel
    @staticmethod
    def get_alleles(blood_type):
        if blood_type == "A":
            return ["A", "O"] 
        elif blood_type == "B":
            return ["B", "O"] 
        elif blood_type == "AB":
            return ["A", "B"] 
        elif blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid")

# Kelas Child
class Child:
    def __init__(self, father, mother):

        # Memilih satu alel secara acak dari ayah dan ibu
        self.father_allele = random.choice(father.alleles)
        self.mother_allele = random.choice(mother.alleles)
        self.blood_type = self.determine_blood_type()

    # Fungsi untuk menentukan golongan darah anak
    def determine_blood_type(self):


        # Gabungkan alel dari ayah dan ibu
        alleles = sorted([self.father_allele, self.mother_allele])
        if alleles == ["A", "A"] or alleles == ["A", "O"]:
            return "A"
        elif alleles == ["B", "B"] or alleles == ["B", "O"]:
            return "B"
        elif alleles == ["A", "B"]:
            return "AB"
        elif alleles == ["O", "O"]:
            return "O"
        else:
            raise ValueError("Kombinasi alel tidak valid")

    def __str__(self):
        return f"Golongan darah anak: {self.blood_type} (Alel: {self.father_allele}{self.mother_allele})"

def main():
    print("Pewarisan Golongan Darah Anak")
   
#golongan darah ayah dan ibu
    father_blood = input("Masukkan golongan darah ayah (A/B/AB/O): ").upper()
    mother_blood = input("Masukkan golongan darah ibu (A/B/AB/O): ").upper()

# Membuat objek Father dan Mother
    father = Father(father_blood)
    mother = Mother(mother_blood)
 # Membuat objek Child
    child = Child(father, mother)

    print(child)


if __name__ == "__main__":
    main()