import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_absolute_error, explained_variance_score
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
from dash import Dash, html, dcc
import plotly.express as px


pd.options.display.max_columns = None
pd.options.display.max_rows = None


def duomenu_parengimas_modeliui(failas):
    df = pd.read_csv(failas)
    df = df[['Title_', 'City_district', 'Price', 'House area', 'Rooms No.',
             'Floors', 'Year of construction', 'Land area (a)']]

    # NT objekto tipo ir vietos perkodavimas
    label_encoder = LabelEncoder()
    df['Object type'] = label_encoder.fit_transform(df['Title_'])
    np.array(to_categorical(df['Object type']))
    df['Municipality'] = label_encoder.fit_transform(df['City_district'])
    np.array(to_categorical(df['Municipality']))
    df = df.drop(['Title_', 'City_district'], axis=1)

    # Siekiant eliminuoti kainų ektremumus (nepakankamą kiekį duomenų modelio apmokymui), nubraižoma namų kainos histograma
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Price'])
    plt.title('Namų kainos histograma')
    plt.xlabel('Namo kaina, mln. eurų')
    plt.ylabel('Namų skaičius')
    plt.show()

    # Pagal kainų histogramą modeliui bus imami duomenys su kaina iki 0,5 mln.(nuo 178 indekso, atmetant 5% duomenų)
    df.sort_values('Price', ascending=False, ignore_index=True, inplace=True)
    df = df.iloc[178:]
    print(df.describe().transpose())

    # Modeliui išskiriame X - namų savybes ir y - namų kaina
    X = df.drop('Price', axis=1).values
    y = df['Price'].values

    # Išskiriami duomenys modelio mokymui ir testavimui
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standartizuojami savybių skaitiniai duomenys
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    plt.figure(figsize=(10, 6))
    sns.histplot(df['Price'])
    plt.title('Namų kainos histograma. Duomenys modelio apmokymui.')
    plt.xlabel('Namo kaina, eurais')
    plt.ylabel('Namų skaičius')
    plt.show()

    # Koreliacijos matrica - heatmap
    plt.figure(figsize=(12, 14))
    sns.heatmap(df.corr(), annot=True)
    plt.title('Koreliacijos matrica')
    plt.show()

    return X_train, X_test, y_train, y_test



def neural_model(X_train, X_test, y_train, y_test):
    # Neuroninių tinklų modelio kūrimas
    model = Sequential()
    model.add(Dense(7, activation='relu'))
    model.add(Dense(49, activation='relu'))
    model.add(Dense(98, activation='relu'))
    model.add(Dense(196, activation='relu'))
    model.add(Dense(392, activation='relu'))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mae')
    early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=3)
    model.fit(x=X_train, y=y_train, validation_data=(X_test, y_test), batch_size=32, epochs=400, callbacks=[early_stop])

    # Modelio vertinimas
    loss_df = pd.DataFrame(model.history.history)
    plt.figure(figsize=(10, 6))
    loss_df.plot()
    plt.title('Neuroniniai tinklai. Nuostolių kaita.')
    plt.xlabel('Ciklai (epochs)')
    plt.ylabel('Nuostoliai (loss)')
    plt.tight_layout()
    plt.show()

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    evc = explained_variance_score(y_test, predictions)
    print(f'MAE paklaida: {mae:.2f}')
    print(f'Explained variance score: {evc: .2f}')

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions)
    plt.plot(y_test, y_test, 'r')
    plt.title('Neuroniniai tinklai. Mokymo duomenys ir prognozė')
    plt.xlabel('Mokymo duomenys')
    plt.ylabel('Prognozė')
    plt.show()
    return y_test, predictions, loss_df


def nt_plotly(y_test, predictions, loss_df):
    # Duomenų parengimas vizualizacijai
    loss_df['loss_type'] = 'loss type'
    loss_df1 = loss_df[['loss', 'loss_type']]
    loss_df1['loss_type'] = 'loss'
    loss_df2 = loss_df[['val_loss', 'loss_type']]
    loss_df2.rename(columns={'val_loss': 'loss'}, inplace=True)
    loss_df2['loss_type'] = 'val_loss'
    model_df = pd.concat([loss_df1, loss_df2], axis=0)
    model_df.index.names = ['Epochs']

    dataset = pd.DataFrame({'Test Price': y_test, 'Predicted Price': predictions[:, 0]})

    # Vizualizacija naudojant Plotly
    app = Dash(__name__)

    app.layout = html.Div([
        html.H2('Neural Networks Visualization \n'),
        dcc.Graph(figure=px.line(
                      model_df.query("loss_type in ['loss', 'val_loss']"),
                      x=model_df.index,
                      y='loss',
                      color='loss_type',
                      title=f'Neural Networks. Loss Trend.'
                  )),
        dcc.Graph(figure=px.scatter(
                      dataset,
                      x='Test Price',
                      y='Predicted Price',
                      title=f'Neural Networks. Test vs Predicted Prices.'
                  ))
    ])

    app.run_server(port=8066)


def main():
    X_train, X_test, y_train, y_test = duomenu_parengimas_modeliui('nt_data_fin.csv')
    y_test, predictions, loss_df = neural_model(X_train, X_test, y_train, y_test)
    nt_plotly(y_test, predictions, loss_df)

if __name__ == '__main__':
    main()
