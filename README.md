**Darbo autoriai💻📈:** Loreta Eimontaitė, Valentina Verikė


****Tema:****
 NT kainų prognozavimo sistema

****Aprašymas:****

Šis projektas yra skirtas namų kainų prognozavimui, remiantis įvairiomis jų savybėmis.
Naudojant duomenų rinkinį, kuriame yra namų pardavimo duomenys, projektas apima duomenų analizę, modelio mokymą ir galutinių prognozių generavimą.


Duomenų rinkinys: Duomenų rinkinys apima tokius namų atributus kaip plotas kvadratiniais metrais, kambarių skaičius, pastatymo metus, bei kitus svarbius parametrus.
Taip pat yra pateikiamos realios namų pardavimo kainos.
Darbo etapai:

****Duomenų surinkimas:****

Įkelti duomenis iš failo ar surinkti iš interneto ir  naudojant pandas biblioteką.
Atlikti pirminę duomenų analizę, nustatyti trūkstamus duomenis, pašalinti arba užpildyti juos.

****Duomenų apdorojimas:****

Atliktas duomenų valymas, įskaitant trūkstamų duomenų tvarkymą ir kategorinių 
kintamųjų kodavimą.
Normalizuoti ir standartizuoti numeriniai duomenis.
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/791fe7c0-6841-4598-b042-ffbda61528bc)
![image-1](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/c6d0f65f-9e4c-4350-9717-62fbe4bfc3bc)
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/78b08792-23a2-49c3-8612-b039f9445e80)

****Modelio kūrimas:****

Pritaikyta keletą skirtingų regresijos modelių: tiesinė regresija, miškų atsitiktinumas, 
ir palyginti jų rezultatai.
Atliktas kryžminis patikrinimas, kad įvertinti modelių efektyvumą.

![paveikslas](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/2993c30e-d8fc-4034-90e1-43b361d3f731)

Gautos RMSE (Root Mean Squared Error) reikšmės rodo tiesinės regresijos ir atsitiktinių miško modelių veikimą pagal bandymo duomenis. Mažesnės RMSE vertės paprastai rodo geresnį našumą, nes jos rodo mažesnes numatytų ir faktinių verčių paklaidas.
 Tiesinės regresijos 'Cross-Validated' RMSE: [185379.30777775 164546.19446714 213715.78011496 224008.21167983
 174502.23518214]
 Atsitiktinio miško 'Cross-Validated' RMSE: [192597.37250449 168142.40811973 220196.71099608 173391.91465119
 186158.67033559]
 
 Tiesinė regresija RMSE: 199237.06
 Atsitiktinio miško RMSE: 174504.11
 
Šios vertės rodo, kad Random Forest modelis veikia geriau nei tiesinės regresijos modelis, numatant būsto kainas pagal nurodytas savybes. Atsitiktinio miško modelio RMSE yra mažesnis, o tai rodo, kad jis vidutiniškai pateikia tikslesnes prognozes, palyginti su tiesinės regresijos modeliu.

****Modelio mokymas ir vertinimas:****

Modeliai mokyti naudojant mokymo duomenų rinkinį.
Įvertintas modelio tikslumas naudojant testavimo duomenų rinkinį.
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/c49bf5d7-4273-4211-8c34-6403c0f6ec10)


****Prognozių generavimas ir pateikimas:****
![image-1](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/79de465e-b92e-4957-9495-beb2d42cd192)

Naudojant geriausiai atlikusį modelį, prognozuotos namų kainos.
Rezultatus pateikti grafiškai ir raštu.

    
**Technologijos:**
    pandas, numpy, scikit-learn, matplotlib


