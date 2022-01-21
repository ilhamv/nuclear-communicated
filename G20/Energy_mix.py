import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt

dfE = pd.read_csv('energy-mix-wid.csv')
dfP = pd.read_csv('UNWPP.csv')

# Build energy data (kWh)
entities = ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'Europe', 'India', 'Indonesia', 'Italy', 'Japan', 'Mexico', 'Russia', 'Saudi Arabia', 'South Africa', 'South Korea', 'Turkey', 'United Kingdom', 'United States']
keys = ['Coal', 'Oil', 'Gas', 'Hydro', 'Nuclear', 'Solar', 'Wind', 'Other renewables']
year = 2019
data = {}
for entity in entities:
    idx = np.array(dfE['Year']==year) & np.array(dfE['Entity']==entity)
    dE = dfE[idx]
    
    idx = np.array(dfP['Region, subregion, country or area *']==entity)
    pop = int((dfP[idx][str(year)].values[0]).replace(' ',''))*1000

    data[entity] = {}
    data[entity]['total'] = 0.0
    for key in keys:
        data[entity][key] = dE[key+' per capita (kWh)'].values[0]*pop
        data[entity]['total'] += data[entity][key]

# G20 energy mix
coal = 0.0
oil = 0.0
gas = 0.0
hydro = 0.0
nuclear = 0.0
solar = 0.0
wind = 0.0
otherRE = 0.0

for entity in entities:
    if entity == 'France' or entity == 'Germany' or entity == 'Italy':
        continue
    coal += data[entity]['Coal']
    oil += data[entity]['Oil']
    gas += data[entity]['Gas']
    hydro += data[entity]['Hydro']
    nuclear += data[entity]['Nuclear']
    solar += data[entity]['Solar']
    wind += data[entity]['Wind']
    otherRE += data[entity]['Other renewables']
total = coal + oil + gas + hydro + nuclear + solar + wind + otherRE
fossil = coal + oil + gas

print("Fossil: %.2f %%"%(fossil/total*100))
print("Non-fossil: %.2f %%"%((1.0-fossil/total)*100))
print("  Hydro: %.2f %%"%(hydro/(total-fossil)*100))
print("  Nuclear: %.2f %%"%(nuclear/(total-fossil)*100))
print("  Solar: %.2f %%"%(solar/(total-fossil)*100))
print("  Wind: %.2f %%"%(wind/(total-fossil)*100))
print("  OtherRE: %.2f %%"%(otherRE/(total-fossil)*100))

dat = [coal, oil, gas, total-fossil]
labels = keys[:3]+['Non-fossil']
colors = ['black','dimgray','darkgray','darkgreen']
_,_,txt = plt.pie(dat, labels=labels, colors=colors, autopct="%.1f%%",wedgeprops = {"edgecolor" : "white",
                      'linewidth': 0.5,
                      'antialiased': True})
for t in txt: t.set_color('white')
plt.title('Energy Consumption of G20 Members')
plt.savefig('G20_energy.svg',dpi=1200,bbox_inches='tight')
plt.savefig('G20_energy.png',dpi=1200,bbox_inches='tight')
plt.show()

dat = [hydro, nuclear, solar, wind, otherRE]
labels = keys[3:-1]+['Other RE']
colors = ['paleturquoise','mediumorchid','yellow','azure','yellowgreen']
_,_,txt = plt.pie(dat, labels=labels, colors=colors, autopct="%.1f%%",wedgeprops = {"edgecolor" : "black",
                      'linewidth': 0.5,
                      'antialiased': True})
plt.title('Non-Fossil Energy consumption of G20 members')
plt.savefig('G20_energyNF.svg',dpi=1200,bbox_inches='tight')
plt.savefig('G20_energyNF.png',dpi=1200,bbox_inches='tight')
plt.show()

'''
for entity in entities:
    tot = 0.0
    for key in keys:
        data[entity][key] /= data[entity]['total']

tot = np.ones(len(entities))
for key in keys:
    plt.barh(np.arange(20),tot)
    tot -= np.array([data[e][key] for e in entities])
plt.yticks(np.arange(20),entities)
plt.show()
'''