# -*- coding: utf-8 -*-
# Ödev 4: Kural Tabanlı Sınıflandırma ile Müşteri Segmentasyonu
# Dosya beklenen konumda olmalı: customers.csv (aynı klasörde)
# Sadece temel kütüphaneler kullanılmıştır (pandas).

import pandas as pd

# ------------------------------------------------------------------
# Veri setini oku
# ------------------------------------------------------------------
df = pd.read_csv("customers.csv")

# ------------------------------------------------------------------
# Görev 1: customers.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
# ------------------------------------------------------------------

# Soru 1: Genel bilgiler
print("\n=== Görev 1 / Soru 1: Genel Bilgiler ===")
print("Shape:", df.shape)
print("\nDtype'lar:\n", df.dtypes)
print("\nİlk 5 satır:\n", df.head())
print("\nHer sütunun unique sayısı:\n", df.nunique())
print("\nHer sütunun boş değer sayısı:\n", df.isnull().sum())

# Soru 2: Kaç unique PLATFORM vardır? Frekansları nedir?
print("\n=== Görev 1 / Soru 2: Unique PLATFORM ve frekansları ===")
print("Unique PLATFORM sayısı:", df["PLATFORM"].nunique())
print(df["PLATFORM"].value_counts())

# Soru 3: Kaç unique PRICE vardır?
print("\n=== Görev 1 / Soru 3: Unique PRICE sayısı ===")
print("Unique PRICE sayısı:", df["PRICE"].nunique())

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
print("\n=== Görev 1 / Soru 4: PRICE frekansları ===")
print(df["PRICE"].value_counts().sort_index())

# Soru 5: Hangi ülkeden (REGION) kaçar tane satış olmuş?
print("\n=== Görev 1 / Soru 5: REGION frekansları ===")
print(df["REGION"].value_counts())

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış? (PRICE toplamı)
print("\n=== Görev 1 / Soru 6: Ülkelere göre toplam gelir (PRICE toplamı) ===")
print(df.groupby("REGION")["PRICE"].sum())

# Soru 7: PLATFORM türlerine göre satış sayıları nedir?
print("\n=== Görev 1 / Soru 7: PLATFORM'a göre satış sayıları ===")
print(df["PLATFORM"].value_counts())

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
print("\n=== Görev 1 / Soru 8: REGION'a göre PRICE ortalamaları ===")
print(df.groupby("REGION")["PRICE"].mean())

# Soru 9: PLATFORM'lara göre PRICE ortalamaları nedir?
print("\n=== Görev 1 / Soru 9: PLATFORM'a göre PRICE ortalamaları ===")
print(df.groupby("PLATFORM")["PRICE"].mean())

# Soru 10: REGION-PLATFORM kırılımında PRICE ortalamaları nedir?
print("\n=== Görev 1 / Soru 10: REGION-PLATFORM kırılımında PRICE ortalamaları ===")
print(df.groupby(["REGION", "PLATFORM"])["PRICE"].mean())

# ------------------------------------------------------------------
# Görev 2: REGION, PLATFORM, GENDER, AGE kırılımında ortalama kazançlar (PRICE ortalaması) nedir?
# ------------------------------------------------------------------
print("\n=== Görev 2: REGION-PLATFORM-GENDER-AGE kırılımında PRICE ortalaması ===")
grouped = (
    df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"], as_index=False)
      .agg(PRICE=("PRICE", "mean"))
      .sort_values(["REGION","PLATFORM","GENDER","AGE"])
      .reset_index(drop=True)
)
grouped["PRICE"] = grouped["PRICE"].round(2)
print(grouped.head(20))

# ------------------------------------------------------------------
# Görev 3: Çıktıyı PRICE’a göre azalan şekilde sıralayın ve sonuçları agg_df olarak kaydedin.
# ------------------------------------------------------------------
print("\n=== Görev 3: PRICE'a göre azalan sıralı agg_df ===")
agg_df = (
    df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"], as_index=False)
      .agg(PRICE=("PRICE", "mean"))
      .sort_values("PRICE", ascending=False)
      .reset_index(drop=True)
)
agg_df["PRICE"] = agg_df["PRICE"].round(2)
print(agg_df.head(20))

# ------------------------------------------------------------------
# Görev 4: İndekste bulunan isimleri değişken olarak tanımlayın. (reset_index)
# Not: Zaten as_index=False ve reset_index kullandığımız için sütunlar değişken olarak mevcut.
# ------------------------------------------------------------------
print("\n=== Görev 4: reset_index sonrası kontrol (ilk 5 satır) ===")
agg_df = agg_df.reset_index(drop=True)
print(agg_df.head())

# ------------------------------------------------------------------
# Görev 5: AGE değişkenini kategorik hale getirin ve agg_df'e ekleyin.
# Kategoriler: 0_18, 19_23, 24_30, 31_40, 41_70
# ------------------------------------------------------------------
print("\n=== Görev 5: AGE'i kategorik hale getir (AGE_CAT) ===")
bins = [0, 18, 23, 30, 40, 70]
labels = ["0_18", "19_23", "24_30", "31_40", "41_70"]
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=bins, labels=labels, right=True, include_lowest=True)
print(agg_df[["REGION","PLATFORM","GENDER","AGE","AGE_CAT","PRICE"]].head(15))

# ------------------------------------------------------------------
# Görev 6: Yeni seviye tabanlı müşteri grupları oluşturun (customer_profile).
# Biçim: REGION_PLATFORM_GENDER_AGE_CAT (büyük harf).
# ------------------------------------------------------------------
print("\n=== Görev 6: customer_profile oluştur ve profile göre PRICE ortalaması ===")
agg_df["customer_profile"] = (
    agg_df["REGION"].str.upper() + "_" +
    agg_df["PLATFORM"].str.upper() + "_" +
    agg_df["GENDER"].str.upper() + "_" +
    agg_df["AGE_CAT"].astype(str)
)

agg_df_final = (
    agg_df.groupby("customer_profile", as_index=False)
          .agg(PRICE=("PRICE", "mean"))
          .sort_values("PRICE", ascending=False)
          .reset_index(drop=True)
)
agg_df_final["PRICE"] = agg_df_final["PRICE"].round(2)
print(agg_df_final.head(20))

# ------------------------------------------------------------------
# Görev 7: Yeni müşterileri PRICE’a göre 4 segmente ayırın.
# Segment adları: A (en yüksek) > B > C > D (en düşük)
# ------------------------------------------------------------------
print("\n=== Görev 7: 4 segmente ayır (A en yüksek) ve özet tablo ===")
agg_df_final["SEGMENT"] = pd.qcut(agg_df_final["PRICE"], 4, labels=["D", "C", "B", "A"])

segment_summary = (
    agg_df_final.groupby("SEGMENT")
                .agg(PRICE_MEAN=("PRICE", "mean"),
                     PRICE_MAX=("PRICE", "max"),
                     PRICE_MIN=("PRICE", "min"),
                     PRICE_SUM=("PRICE", "sum"),
                     N=("PRICE", "count"))
                .sort_index()  # D, C, B, A
)
print(segment_summary)

# ------------------------------------------------------------------
# Görev 8: Yeni gelen müşterileri sınıflandırıp beklenen geliri tahmin edin.
# Örn-1: 33 yaşında ANDROID kullanan bir Türk kadını -> TUR_ANDROID_FEMALE_31_40
# Örn-2: 35 yaşında IOS kullanan bir Fransız kadını -> FRA_IOS_FEMALE_31_40
# ------------------------------------------------------------------
print("\n=== Görev 8: Yeni müşteri örnekleri için tahmin ===")

def age_to_bucket(age: int) -> str:
    if age <= 18:
        return "0_18"
    elif age <= 23:
        return "19_23"
    elif age <= 30:
        return "24_30"
    elif age <= 40:
        return "31_40"
    else:
        return "41_70"

def predict_price(region: str, platform: str, gender: str, age: int):
    profile = f"{region}_{platform}_{gender}_{age_to_bucket(age)}".upper()
    row = agg_df_final.loc[agg_df_final["customer_profile"] == profile]
    if row.empty:
        return profile, None, None
    price = float(row["PRICE"].iloc[0])
    seg = row["SEGMENT"].iloc[0]
    return profile, price, seg

examples = [
    ("TUR", "ANDROID", "FEMALE", 33),
    ("FRA", "IOS", "FEMALE", 35),
]

for ex in examples:
    prof, price, seg = predict_price(*ex)
    print(f"Profil: {prof:30s} | Beklenen PRICE: {price} | Segment: {seg}")
