class Mobil:
    def __init__(self, merk, warna, jenis, pemilik):
     self.merk = merk
     self.warna = warna
     self.jenis = jenis
     self.pemilik = pemilik
    
    def info(self):
        print(f"Mobil {self.merk} berwarna {self.merk} jenis {self.jenis} pemilik {self.pemilik}")

mobilA = Mobil("Toyota", "Hitam", "jeep", "purwoto")
mobilA.info() 