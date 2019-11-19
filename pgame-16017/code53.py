# Pemrogramana Game Praktikum 5
# Latihan code 5.3 : Dictionary

# Buat variabel dan memberikan nilai elemen
dc = { "Kampus":"UMMU", "Prodi":"Info", "Lokasi":"Ternate",
	"Tahun":2019 }

# print elemen dengan key "Tahun"
print (dc["Tahun"])

# Cara lain untuk print element dengan key "Tahun"
print (dc.get ("Tahun"))

# Mengubah nilai (Value) dari sebuah key "tahun"
dc ["Tahun"] = 2020
dc ["Lokasi"] = "Sasa"

# print dc (dictionary) setelah perubahan
print ("Dictionary :", dc)
