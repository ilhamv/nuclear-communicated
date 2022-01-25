import numpy as np

# Total radioaktivitas dari kecelakaan nuklir Fukushima: 940 PBq (I-131 eq)
# [https://world-nuclear.org/information-library/safety-and-security/safety-of-plants/fukushima-daiichi-accident.aspx]

aktivitas = 940E15 # Bq, atau perluruhan/detik

# Spesifikasi I-131
waktu_paruh         = 8.02*86400              # Hari --> detik
koefisien_peluruhan = np.log(2.0)/waktu_paruh # /detik
massa_molar         = 130.9061246             # g/mol
densitas            = 4.93                    # g/ml

# Jumlah I-131
atom   = aktivitas/koefisien_peluruhan
mol    = atom/6.0221409E23 # Dari angka Avogadro
massa  = mol*massa_molar # g
volume = massa/densitas  # ml

# Sendok makan (15 ml)
sendok_makan = volume/15
print(sendok_makan)