import numpy as np

# Kacang
kacang = {}
kacang['diameter'] = 1.25 # cm
kacang['radius']   = kacang['diameter']/2
kacang['volume']   = 4.0/3.0 * np.pi*kacang['radius']**3

# Kandungan energi
N_avogadro = 6.0221409E23
uranium = {}
uranium['g/cc']     = 19.1
uranium['g/mol']    = 238.02891
uranium['kWh/fisi'] = 200.0*4.45049e-20
uranium['atom/cc']  = uranium['g/cc']/uranium['g/mol']*N_avogadro
uranium['kWh/cc']   = uranium['kWh/fisi']*uranium['atom/cc']
uranium['kWh/kacang']   = uranium['kWh/cc']*kacang['volume']

# Konsumsi energi per kapita per tahun @ 2019, kWh
# [https://ourworldindata.org/grapher/per-capita-energy-use]
energi = {}
energi['US'] = 79897.151
energi['Indonesia'] = 9146.767
energi['Dunia'] = 21027.415

# Ekspektasi usia [https://ourworldindata.org/life-expectancy]
usia = {}
usia['US'] = 78.9
usia['Indonesia'] = 71.1
usia['Dunia'] = 70.8

for s in ['US', 'Indonesia', 'Dunia']:
    print("Kacang atom uranium untuk gaya hidup %s:"%s, 
          usia['%s'%s]*energi['%s'%s]/uranium['kWh/kacang'])