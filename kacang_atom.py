import numpy as np

# Kacang atom (standar diameter: 10-18 mm)
# [https://text-id.123dok.com/document/zk87p34z-kestabilan-kualitas-kacang-atom-di-pt-garudafood-putra-putri-jaya-divisi-coated-peanuts-pati-unika-repository.html]
kacang = {}
kacang['diameter'] = 1.4 # cm
kacang['radius']   = kacang['diameter']/2
kacang['volume']   = 4.0/3.0 * np.pi*kacang['radius']**3

# Kandungan energi (rata-rata energi/fisi: 200 MeV)
# [https://www.nuclear-power.com/nuclear-power/fission/energy-release-from-fission/]
N_avogadro = 6.0221409E23
uranium = {}
uranium['g/cc']       = 19.1
uranium['g/mol']      = 238.02891
uranium['kWh/fisi']   = 200.0*4.45049e-20
uranium['atom/cc']    = uranium['g/cc']/uranium['g/mol']*N_avogadro
uranium['kWh/cc']     = uranium['kWh/fisi']*uranium['atom/cc']
uranium['kWh/kacang'] = uranium['kWh/cc']*kacang['volume']

# Konsumsi energi per kapita per tahun @ 2019, kWh
# [https://ourworldindata.org/grapher/per-capita-energy-use]
energi = {}
energi['US']        = 79897.151
energi['Indonesia'] = 9146.767
energi['Dunia']     = 21027.415

# Ekspektasi usia @ 2019 [https://ourworldindata.org/life-expectancy]
usia = {}
usia['US']        = 78.9
usia['Indonesia'] = 71.1
usia['Dunia']     = 72.6

for s in ['US', 'Indonesia', 'Dunia']:
    print("Kacang atom uranium untuk gaya hidup %s:"%s, 
          usia['%s'%s]*energi['%s'%s]/uranium['kWh/kacang'])
    
# Performa reaktor modern komersial saat ini (sekelas APR1400)
# [https://aris.iaea.org/PDF/APR1400_2020May.pdf]
# [https://www.urenco.com/swu-calculator]
# BB: bahan bakar
# DU: Depleted uranium
lwr = {}
lwr['uranium/BB']     = 8.025 # dari proses pengayaan
lwr['DU/uranium']     = 1.0 - 1.0/lwr['uranium/BB']
lwr['MWd/kg-BB']      = 46.5 # burnup
lwr['MWd/kg-uranium'] = lwr['MWd/kg-BB']/lwr['uranium/BB']
lwr['kWh/cc-uranium'] = lwr['MWd/kg-uranium']*24.0*uranium['g/cc']
lwr['efisiensi']      = lwr['kWh/cc-uranium']/uranium['kWh/cc']
tak_terbakar          = 1.0-lwr['efisiensi']-lwr['DU/uranium']
lwr['BB/limbah']      = tak_terbakar/(1.0-lwr['DU/uranium'])

print("\nEfisiensi LWR komersial: %s %%"%(lwr['efisiensi']*100.0))
print("  ditinggalkan di bangunan pengayaan: %s %%"%(lwr['DU/uranium']*100.0))
print("  tak terbakar dalam reaktor: %s %%"%(tak_terbakar*100.0))
print("Bahan bakar di dalam 'limbah': %s %%"%(lwr['BB/limbah']*100.0))

print("\nDengan LWR,")
for s in ['US', 'Indonesia', 'Dunia']:
    print("Kacang atom uranium untuk gaya hidup %s:"%s, 
          usia['%s'%s]*energi['%s'%s]/uranium['kWh/kacang']/lwr['efisiensi'])

# Rerata kandungan energi batubara Indonesia
# [https://www.bappenas.go.id/files/5415/0898/5954/Laporan_Akhir_Kajian_DMO_Batubara_Final.pdf]
# [https://world-nuclear.org/information-library/facts-and-figures/heat-values-of-various-fuels.aspx]
coal = {}
#coal['kcal/kg'] = (28.48*4600 + 67.22*5600 + 7.57*6600 + 1.78*7600)/100.0
coal['kcal/kg'] = (28.48*10 + 67.22*18 + 7.57*18 + 1.78*25)/100.0*239.006
coal['kWh/ton']  = coal['kcal/kg']*0.00116222*1000.0
kebutuhan_coal  = usia['Indonesia']*energi['Indonesia']/coal['kWh/ton']

print('\nBatubara untuk gaya hidup Indonesia {} ton'.format(kebutuhan_coal))
print('  atau %.2f truk tambang penuh'%(kebutuhan_coal/30))