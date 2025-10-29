# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz. (type() metodunu kullanınız)

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake", "Age": 27, "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(l))
print(type(d))
print(type(t))
print(type(s))


# Görev 2: Verilen string ifadeyi büyük harfe çeviriniz,
# noktalama işaretlerini boşluk ile değiştiriniz, kelimelere ayırınız.

text = "The goal is to turn data into information, and information into insight."
text = text.upper()
text = text.replace(",", " ").replace(".", " ")
words = text.split()
print(words)


# Görev 3: Verilen listeye işlemleri uygulayınız.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Eleman sayısı
print(len(lst))

# Adım 2: 0. ve 10. indeks
print(lst[0], lst[10])

# Adım 3: ["D","A","T","A"]
print(lst[0:4])

# Adım 4: 8. indeksi sil
lst.pop(8)
print(lst)

# Adım 5: Yeni eleman ekle
lst.append("X")
print(lst)

# Adım 6: 8. indekse "N" ekle
lst.insert(8, "N")
print(lst)


# Görev 4: Sözlük üzerinde işlemler yapınız.

dict_ = {
    'Christian': ["America",18],
    'Daisy':["England",12],
    'Antonio':["Spain",22],
    'Dante':["Italy",25]
}

# Adım 1: Key'ler
print(dict_.keys())

# Adım 2: Value'lar
print(dict_.values())

# Adım 3: Daisy’nin yaşını 13 yap
dict_["Daisy"][1] = 13
print(dict_)

# Adım 4: Ahmet ekle
dict_["Ahmet"] = ["Turkey",24]
print(dict_)

# Adım 5: Antonio’yu sil
dict_.pop("Antonio")
print(dict_)


# Görev 5: Fonksiyon ile tek/çift sayıları ayırınız.

l = [2,13,18,93,22]

def func(lst):
    even_list = []
    odd_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list

even_list, odd_list = func(l)
print("Çiftler:", even_list)
print("Tekler:", odd_list)


# Görev 6: Öğrencileri fakülte sırasına göre yazdırınız.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i, ogr in enumerate(ogrenciler, 1):
    if i <= 3:
        print(f"Mühendislik Fakültesi {i}. öğrenci: {ogr}")
    else:
        print(f"Tıp Fakültesi {i-3}. öğrenci: {ogr}")


# Görev 7: Zip kullanarak ders bilgilerini yazdırınız.

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for kod, kr, kon in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kr} olan {kod} kodlu dersin kontenjanı {kon} kişidir.")


# Görev 8: Set işlemleri yapınız.

kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])

def check_sets(set1, set2):
    if set1.issuperset(set2):
        return set1.intersection(set2)
    else:
        return set2.difference(set1)

print(check_sets(kume1, kume2))
