import pickle
import numpy as np
import pandas as pd

def getPrediction(floor, highestfloor, area, rooms,  document, renovation, subway):
    model = pickle.load(open('model_gbr.pkl', 'rb'))

    subway_dummy = [0 for i in range(22)]

    subway_list = ['Subway_28 May m.', 'Subway_8 Noyabr m.',
       'Subway_Avtovağzal m.', 'Subway_Azadlıq Prospekti m.',
       'Subway_Bakmil m.', 'Subway_Dərnəgül m.',
       'Subway_Elmlər Akademiyası m.', 'Subway_Əhmədli m.',
       'Subway_Gənclik m.', 'Subway_Həzi Aslanov m.',
       'Subway_Xalqlar Dostluğu m.', 'Subway_İçəri Şəhər m.',
       'Subway_İnşaatçılar m.', 'Subway_Koroğlu m.', 'Subway_Qara Qarayev m.',
       'Subway_Memar Əcəmi m.', 'Subway_Neftçilər m.', 'Subway_Nizami m.',
       'Subway_Nəriman Nərimanov m.', 'Subway_Nəsimi m.', 'Subway_Sahil m.',
       'Subway_Şah İsmayıl Xətai m.']

    subway_index = subway_list.index(subway)
    subway_dummy[subway_index]=1
    
    six_predictors = [floor, highestfloor, area, rooms, renovation, document]

    new_data_point = six_predictors+subway_dummy
    new_data_point = np.array(new_data_point).reshape(1,-1)

    prediction = model.predict(new_data_point)
    result = f'The predicted price is  {prediction}'

    return result