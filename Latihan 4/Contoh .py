class Pekerja:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur


class Perusahaan:
    def __init__(self, nama, pekerja):
        self.nama = nama
        self.pekerja = pekerja

    def daftar_pekerja1(self):
        for pekerja in self.pekerja:
            print("Gooole", pekerja.nama, pekerja.umur)

    def daftar_pekerja2(self):
        for pekerja in self.pekerja:
            print("Microcof", pekerja.nama, pekerja.umur)



pekerja1 = Pekerja("Purwoto", 22)
pekerja2 = Pekerja("Budi", 30)
perusahaan1 = Perusahaan("ABC", [pekerja1])
perusahaan2 = Perusahaan("Nabati", [pekerja2])
perusahaan1.daftar_pekerja1()
perusahaan2.daftar_pekerja2()
