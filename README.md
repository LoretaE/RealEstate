**Darbo autoriai💻📈:** Loreta Eimontaitė, Valentina Verikė


****Tema****
 NT kainų prognozavimo sistema

****Aprašymas****

Šis projektas yra skirtas namų kainų prognozavimui, remiantis įvairiomis jų savybėmis.
Naudojant duomenų rinkinį, kuriame yra namų pardavimo duomenys, projektas apima duomenų analizę, modelio mokymą ir galutinių prognozių generavimą.


Duomenų rinkinys: Duomenų rinkinys apima šias namų savybes: objekto tipas, dislokacijos vieta, namo plotas (kvadratiniais metrais), kambarių skaičius, aukštų skaičius, pastatymo metai ir žemės plotas (arais).
Taip pat yra pateikiamos namų pardavimo kainos.

Darbo etapai:

****Duomenų surinkimas****

Duomenys įkelti iš interneto svetainės www.kampas.lt naudojant "Web scraping".
Atlikta pirminė duomenų analizė, nustatyti, pašalinti ir užpildyti trūkstami duomenys.

****Duomenų apdorojimas****

Atliktas duomenų valymas, įskaitant trūkstamų duomenų tvarkymą ir kategorinių 
kintamųjų kodavimą.
Standartizuoti skaitiniai duomenys.

Siekiant eliminuoti kainų ektremumus (nepakankamą kiekį duomenų modelio apmokymui), analizuotos namų kainos histogramoje. 
Pagal kainų histogramą modeliui bus imami duomenys su kaina iki 0,5 mln.(nuo 178 indekso, atmetant 5% duomenų)

![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/791fe7c0-6841-4598-b042-ffbda61528bc)
![image-1](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/c6d0f65f-9e4c-4350-9717-62fbe4bfc3bc)
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/78b08792-23a2-49c3-8612-b039f9445e80)

****Modelio kūrimas, mokymas ir vertinimas, prognozių generavimas:****

Pritaikyta keletą skirtingų regresijos modelių: tiesinė regresija, miškų atsitiktinumas. Taip pat neuroninių tinklų modelis.

Atliktas kryžminis patikrinimas, kad įvertinti modelių efektyvumą.

![image_720](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/14ff7e87-c2b6-4d91-b822-57c92b912278)


![image_720-1](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/9629d8cb-cf6f-48b5-95ee-33d7bc1a8e9d)


Gautos RMSE (Root Mean Squared Error) reikšmės rodo tiesinės regresijos ir atsitiktinių miško modelių veikimą pagal bandymo duomenis. 
Mažesnės RMSE vertės paprastai rodo geresnį našumą, nes jos rodo mažesnes numatytų ir faktinių verčių paklaidas.

Linear Regression RMSE: 85199.83

Random Forest Test RMSE: 72180.10

Linear Regression r2 Score = 0.44

Random Forest r2 Score = 0.60
 
Šios vertės rodo, kad Random Forest modelis veikia geriau nei tiesinės regresijos modelis, numatant būsto kainas pagal nurodytas savybes. Atsitiktinio miško modelio RMSE yra mažesnis, o tai rodo, kad jis vidutiniškai pateikia tikslesnes prognozes, palyginti su tiesinės regresijos modeliu.


Modeliai mokyti naudojant mokymo duomenų rinkinį.
Įvertintas modelio tikslumas naudojant testavimo duomenų rinkinį.
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/c49bf5d7-4273-4211-8c34-6403c0f6ec10)


![image-1](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/79de465e-b92e-4957-9495-beb2d42cd192)

Naudojant geriausiai atlikusį modelį, prognozuotos namų kainos.
Rezultatus pateikti grafiškai ir raštu.

    
**Technologijos:**
    pandas, numpy, scikit-learn, matplotlib


