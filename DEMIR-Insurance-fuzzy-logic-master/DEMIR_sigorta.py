import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as karar
#doğal dil işleme, zembelek
#sentiment analiz
#tek
giris1 = karar.Antecedent(np.arange(0,101,1),'aracın motor gücü')
giris2 = karar.Antecedent(np.arange(0,101,1),'daha önceki kaza oranı')
giris3 = karar.Antecedent(np.arange(0,101,1),'aldigi_trafik_cezasi')
cikis = karar.Consequent(np.arange(0,101,1),'fiyat')

giris1['cok_düsük_motor'] = fuzzy.trimf(giris1.universe, [0, 0, 50])
giris1['düsük_motor'] = fuzzy.trimf(giris1.universe, [0, 50, 100])
giris1['orta_motor'] = fuzzy.trimf(giris1.universe, [50, 100, 150])
giris1['yüksek_motor'] = fuzzy.trimf(giris1.universe, [100, 150, 200])
giris1['cok_yüksek_motor'] = fuzzy.trimf(giris1.universe, [150, 200, 200])

giris2['cok_az_km'] = fuzzy.trimf(giris2.universe, [0, 0, 50])
giris2['düsük_km'] = fuzzy.trimf(giris2.universe, [0, 50, 100])
giris2['orta_km'] = fuzzy.trimf(giris2.universe, [50, 100, 150])
giris2['yüksek_km'] = fuzzy.trimf(giris2.universe, [100, 150, 200])
giris2['cok_yüksek_km'] = fuzzy.trimf(giris2.universe, [150, 200, 200])

giris3['cok_az_kazali'] = fuzzy.trimf(giris3.universe, [0, 0, 50])
giris3['düsük_kazali'] = fuzzy.trimf(giris3.universe, [0, 50, 100])
giris3['orta_kazali'] = fuzzy.trimf(giris3.universe, [50, 100, 150])
giris3['yüksek_kazali'] = fuzzy.trimf(giris3.universe, [100, 150, 200])
giris3['cok_yüksek_kazali'] = fuzzy.trimf(giris3.universe, [150, 200, 200])

cikis['cok_düsük'] = fuzzy.trimf(cikis.universe, [0, 0, 50])
cikis['düsük'] = fuzzy.trimf(cikis.universe, [0, 50, 100])
cikis['orta'] = fuzzy.trimf(cikis.universe, [50, 100, 150])
cikis['yüksek'] = fuzzy.trimf(cikis.universe, [100, 150, 200])
cikis['cok_yüksek'] = fuzzy.trimf(cikis.universe, [150, 200, 200])

giris1.view()
giris2.view()
giris3.view()
cikis.view()


kural1 = karar.Rule(giris1['cok_düsük_motor'] & giris2['düsük_km'] & giris3['cok_az_kazali'], cikis['cok_düsük'])
kural2 = karar.Rule(giris1['düsük_motor'] & giris2['düsük_km'] & giris3['düsük_kazali'], cikis['düsük'])
kural3 = karar.Rule(giris1['yüksek_motor']& giris2['cok_az_km'] & giris3['cok_yüksek_kazali'] , cikis['cok_yüksek'])
kural4 = karar.Rule(giris1['yüksek_motor']& giris2['cok_az_km'] & giris3['cok_yüksek_kazali'] , cikis['cok_yüksek'])
kural5 = karar.Rule(giris1['cok_yüksek_motor']& giris2['orta_km'] & giris3['yüksek_kazali'] , cikis['orta'])


teklif_karar = karar.ControlSystem([kural1, kural2, kural3, kural4, kural5])
teklif_ = karar.ControlSystemSimulation(teklif_karar)

teklif_.input['aracın motor gücü'] = 10
teklif_.input['daha önceki kaza oranı'] = 10
teklif_.input['aldigi_trafik_cezasi'] = 30

teklif_.compute()

print(teklif_.output['fiyat'])

cikis.view(sim=teklif_)

input("")

#makineler her şeyi yaptığında biz ne yapacağız , aganta yaın evi
# buy.olgy
# veri madenciliği papatya gökhan silahdaroğlu




