import csv
import numpy as np

# Rašoma funkcija stulpelio 'Title' padalinimui į 3 stulpelius, pagal požymį ","
def split_title(title):
    parts = title.split(',', 2)
    if len(parts) == 1:
        return parts[0].strip(), '', ''
    elif len(parts) == 2:
        return parts[0].strip(), parts[1].strip(), ''
    else:
        return parts[0].strip(), parts[1].strip(), parts[2].strip()

# Nuskaitomas .csv failas ir 'Title' dalinamas į tris stulpelius
with open('nt_data.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    next(reader)  # praleidžiame "header" eilutę
    rows = []
    land_area_values = []
    rooms_no_values = []
    floors_values = []
    for row in reader:
        row['Title_'], row['City_district'], row['Place_rooms'] = split_title(row['Title'])
        del row['Title'], row['Place']  # ištriname nereikalingus stulpelius

        # Konvertuojame į 'intiger' ar į 'float'
        row['Price'] = int(row['Price'])
        row['House area'] = float(row['House area'])

        # Konvertuojame 'Rooms No.' ir 'Floors' į 'intiger' jei yra reikšmės
        if row['Rooms No.']:
            row['Rooms No.'] = int(float(row['Rooms No.']))
            rooms_no_values.append(row['Rooms No.'])
        if row['Floors']:
            row['Floors'] = int(float(row['Floors']))
            floors_values.append(row['Floors'])

        # Sutvarkomas 'Year of construction' stulpelis
        year_value = row['Year of construction']
        if year_value:
            try:
                row['Year of construction'] = int(float(year_value))
            except ValueError:
                pass

        # Pridedame 'mean' vertes 
        land_area_value = row['Land area (a)']
        if land_area_value:
            land_area_values.append(float(land_area_value))

        rows.append(row)

# Skaičiuojame mean vertes
land_area_mean = np.mean(land_area_values)
rooms_no_mean = int(np.mean(rooms_no_values)) if rooms_no_values else None
floors_mean = int(np.mean(floors_values)) if floors_values else None

# Užpildome trūkstamas vertes su 'mean' vertėmis
for row in rows:
    if not row['Land area (a)']:
        row['Land area (a)'] = "{:.2f}".format(land_area_mean)
    if row['Rooms No.'] == '':
        row['Rooms No.'] = rooms_no_mean
    if row['Floors'] == '':
        row['Floors'] = floors_mean

#  Apdorota informacija irasoma i nauja .csv
with open('nt_data_2.csv', 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['Title_', 'City_district', 'Place_rooms'] + [field for field in reader.fieldnames if field != 'Title']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

