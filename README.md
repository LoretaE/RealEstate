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


****Modelio kūrimas:****

Pritaikyta keletą skirtingų regresijos modelių: tiesinė regresija, miškų atsitiktinumas, 
ir palyginti jų rezultatai.
Atliktas kryžminis patikrinimas, kad įvertinti modelių efektyvumą.

![paveikslas](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/2993c30e-d8fc-4034-90e1-43b361d3f731)

Gautos RMSE (Root Mean Squared Error) reikšmės rodo tiesinės regresijos ir atsitiktinių miško modelių veikimą pagal bandymo duomenis. Mažesnės RMSE vertės paprastai rodo geresnį našumą, nes jos rodo mažesnes numatytų ir faktinių verčių paklaidas.

    Tiesinė regresija RMSE: 199237.06
    Atsitiktinis miškas RMSE: 174504.11

Šios vertės rodo, kad Random Forest modelis veikia geriau nei tiesinės regresijos modelis, numatant būsto kainas pagal nurodytas savybes. Atsitiktinio miško modelio RMSE yra mažesnis, o tai rodo, kad jis vidutiniškai pateikia tikslesnes prognozes, palyginti su tiesinės regresijos modeliu.

****Modelio mokymas ir vertinimas:****

Modeliai mokyti naudojant mokymo duomenų rinkinį.
Įvertintas modelio tikslumas naudojant testavimo duomenų rinkinį.
![image-1](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/c6d0f65f-9e4c-4350-9717-62fbe4bfc3bc)
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/78b08792-23a2-49c3-8612-b039f9445e80)

****Prognozių generavimas ir pateikimas:****

Naudojant geriausiai atlikusį modelį, prognozuotos namų kainos.
Rezultatus pateikti grafiškai ir raštu.

    
**Technologijos:**
    pandas, numpy, scikit-learn, matplotlib


