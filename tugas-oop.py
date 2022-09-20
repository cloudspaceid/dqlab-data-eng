# Definisikan class Karyawan
class Karyawan:
    def ___(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = ___
        self.usia = ___
        self.pendapatan = ___
        self.pendapatan_tambahan = 0
        self.insentif_lembur = ___
    def lembur(self):
        self.pendapatan_tambahan += ___
    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += ___
    def total_pendapatan(self):
        return ___
# Definisikan class Perusahaan
class Perusahaan:
    def ___(self, nama, alamat, nomor_telepon):
        self.nama = ___
        self.alamat = ___
        self.nomor_telepon = ___
        self.list_karyawan = ___
    def aktifkan_karyawan(self, karyawan):
        self.list_karyawan.___(___)
    def nonaktifkan_karyawan(self, nama_karyawan):
        karyawan_nonaktif = None
        for karyawan in ___:
            if karyawan.nama == ___:
                karyawan_nonaktif = ___
                break
        if karyawan_nonaktif is not None:
            self.list_karyawan.___(___)