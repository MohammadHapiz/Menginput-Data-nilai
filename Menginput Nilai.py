print("*"*100)
print("--input Data Nilai--")
Nis = input("Nis : ")
Nama = input("Nama : ")
jk = input("jk :")
Rombel = input("Rombel : ")
Rayon = input("Rayon : ")
Bindo = int(input("B.Indonesia : "))

mtk = int(input("Matematika : "))
bing = int(input("B.inggris : "))
print("*"*100)
print("----Laporan Hasil UAS----")
print("----Smk Wikrama Bogor----")
print("Nis:" , Nis)
print("Nama:", Nama)
print("jk:", jk)
print("Rombel:",Rombel)
print("Rayon: ",Rayon)
print("B.indonesia:",Bindo )
print("Matematika:",mtk)
print("B.inggris:", bing)
Rata2 = (Bindo+mtk+bing/3)
if Rata2 >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")





