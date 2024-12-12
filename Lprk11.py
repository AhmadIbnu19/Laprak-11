# dp 
class DataNilai:
    def __init__(self):
        self._nilai = 0

    def get_nilai(self):
        return self._nilai

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self._nilai = nilai
            print(f"Nilai berhasil dibuat menjadi: {self._nilai}")
        else:
            print("Nilai harus antara 0 dan 100.")
    def set_nilai2(self, nilai):
        if 0 <= nilai <= 100:
            self._nilai = nilai
            print(f"Nilai berhasil diubah menjadi: {self._nilai}")
        else:
            print("Nilai harus antara 0 dan 100.")

def main():
    data_nilai = DataNilai()
    print("\nMenu:")
    print("1. Membuat Nilai")
    print("2. Tampilkan Nilai")
    print("3. Ubah Nilai")
    print("4. Keluar")

    while True:
        try:
            pilihan = int(input("Pilih menu (1/2/3/4): "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            try:
                nilai = int(input('Masukkan nilai untuk membuatnya (0-100): '))
                data_nilai.set_nilai(nilai)
            except ValueError:
                print("Masukkan angka yang valid!")
        elif pilihan == 2:
            print(f"Nilai saat ini: {data_nilai.get_nilai()}")
        elif pilihan == 3:
            try:
                nilai_baru = int(input("Masukkan nilai baru (0-100): "))
                data_nilai.set_nilai2(nilai_baru)
            except ValueError:
                print("Masukkan angka yang valid!")
        elif pilihan == 4:
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

main()
