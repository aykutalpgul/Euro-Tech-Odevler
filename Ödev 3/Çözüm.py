# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")
print(df.head())

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
print(df["sex"].value_counts())

# Görev 3: Her bir sütuna ait unique değerlerin sayısını bulunuz.
print(df.nunique())

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
print(df["pclass"].nunique())

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
print(df[["pclass", "parch"]].nunique())

# Görev 6: embarked değişkeninin tipini kontrol ediniz.
print(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
print(df["embarked"].dtype)

# Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz.
print(df[df["embarked"] == "C"])

# Görev 8: embarked değeri S olmayanların tüm bilgilerini gösteriniz.
print(df[df["embarked"] != "S"])

# Görev 9: Yaşı 30’dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
print(df[(df["age"] < 30) & (df["sex"] == "female")])

# Görev 10: Fare'i 500’den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.
print(df[(df["fare"] > 500) | (df["age"] > 70)])

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
print(df.isnull().sum())

# Görev 12: who değişkenini dataframe’den çıkarınız.
df = df.drop("who", axis=1)

# Görev 13: deck değişkenindeki boş değerleri en çok tekrar eden değer ile doldurunuz.
df["deck"].fillna(df["deck"].mode()[0], inplace=True)

# Görev 14: age değişkenindeki boş değerleri medyan ile doldurunuz.
df["age"].fillna(df["age"].median(), inplace=True)

# Görev 15: survived değişkeninin pclass ve cinsiyet kırılımında sum, count, mean değerlerini bulunuz.
print(df.groupby(["pclass", "sex"])["survived"].agg(["sum","count","mean"]))

# Görev 16: 30 yaşın altında olanlara 1, diğerlerine 0 verecek age_flag değişkeni oluşturunuz.
df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
tips = sns.load_dataset("tips")
print(tips.head())

# Görev 18: Time değişkeninin kategorilerine göre total_bill değerlerinin toplamı, min, max ve ortalamasını bulunuz.
print(tips.groupby("time")["total_bill"].agg(["sum","min","max","mean"]))

# Görev 19: Günlere ve time’a göre total_bill değerlerinin toplamı, min, max ve ortalamasını bulunuz.
print(tips.groupby(["day","time"])["total_bill"].agg(["sum","min","max","mean"]))

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day’e göre toplamını, min, max ve ortalamasını bulunuz.
print(tips[(tips["time"]=="Lunch") & (tips["sex"]=="Female")]
      .groupby("day")[["total_bill","tip"]].agg(["sum","min","max","mean"]))

# Görev 21: size’i 3’ten küçük, total_bill’i 10’dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
print(tips.loc[(tips["size"]<3) & (tips["total_bill"]>10)].mean(numeric_only=True))

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz (total_bill + tip).
tips["total_bill_tip_sum"] = tips["total_bill"] + tips["tip"]
print(tips.head())

# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız
# ve ilk 30 kişiyi yeni bir dataframe’e atayınız.
new_df = tips.sort_values("total_bill_tip_sum", ascending=False).head(30)
print(new_df)