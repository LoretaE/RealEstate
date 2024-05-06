**Darbo autoriai💻📈:** Loreta Eimontaitė, Valentina Verikė


****Tema****
 NT kainų prognozavimo sistema

****Aprašymas****

Šis projektas yra skirtas namų kainų prognozavimui, remiantis įvairiomis jų savybėmis.
Naudojant duomenų rinkinį, kuriame yra namų pardavimo duomenys, projektas apima duomenų analizę, modelio mokymą ir galutinių prognozių generavimą.

**Technologijos**
pandas, numpy, scikit-learn, matplotlib, plotly dash, tensorflow, seaborn, sklearn, BeautifulSoup, requests 

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
Pagal kainų histogramą modeliui imami duomenys, kurių kaina iki 0,5 mln.eurų (atmetant 5% duomenų).

![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/791fe7c0-6841-4598-b042-ffbda61528bc)
![image-1](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/c6d0f65f-9e4c-4350-9717-62fbe4bfc3bc)
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/157985262/78b08792-23a2-49c3-8612-b039f9445e80)

****Modelio kūrimas, mokymas ir vertinimas, prognozių generavimas:****

Pritaikyta keletą skirtingų regresijos modelių: tiesinė regresija, atsitiktinių miškų metodas. Taip pat neuroninių tinklų modelis.

Modeliai mokyti naudojant mokymo duomenų rinkinį. Modelių tikslumas vertintas, naudojant testavimo duomenų rinkinį.
Atliktas kryžminis patikrinimas, kad įvertinti modelių efektyvumą.


![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/163419704/dfbfc903-7e78-4d42-9aad-c971126ec746)
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/163419704/cf95830f-4e5a-476d-940d-08e586405f65)


Gautos RMSE (Root Mean Squared Error) reikšmės rodo tiesinės regresijos ir atsitiktinių miškų modelių veikimo tikslumą, vertintą naudojant testavimo duomenis. Mažesnės RMSE vertės rodo geresnį našumą, nes jos rodo mažesnes numatytų ir faktinių verčių paklaidas. Koeficientas r2 parodo modelio gebėjimą nustatyti tinkamas vertes. Kuo r2 artimesnis 1, tuo modelis tikslesnis.

  - Linear Regression RMSE: 85199.83

  - Random Forest Test RMSE: 72180.10

  - Linear Regression r2 Score = 0.44

  - Random Forest r2 Score = 0.60
 
RMSE paklaidos ir r2 koeficiento vertės rodo, kad atsitiktinių miškų modelis pateikia tikslesnes prognozes numatant būsto kainas pagal nurodytas savybes, nei tiesinės regresijos modelis. 



![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/163419704/39a6d5d0-2568-4b36-a951-b917140b0f16)
![image](https://github.com/ValentinaVerik/NT-kain-prognozavimo-sistema/assets/163419704/a41b9caa-46d5-4076-b4c1-d239c9d2cc3d)


 - MAE paklaida: 55619.26

 - Explained variance score:  0.57

Neuroninių tinklų modelio koeficientas, rodantis modelio tikslumą, yra gana panašus į atsitiktinių miškų modelio koeficientą. 

****Išvados****

1. Prognozuojant namų kainas pagal aukščiau nurodytas savybes, vertėtų naudoti tiksliausią - atsitiktinių miškų (Random Forests) modelį.
2. Atsitiktinių miškų (Random Forests) modelio tikslumas - 60 proc. Tikslumą ribojantys veiksniai: (1) modelio mokymui ir testavimui naudotas duomenų kiekis (3,4 tūkst. parduodamų namų duomenų), (2) kainai taip pat įtaką daro kitos savybės, kurios kuriant ir testuojant modelį nebuvo naudotos (nes tik apie 1/3 namų turėjo informaciją apie kitas savybes).    


    



