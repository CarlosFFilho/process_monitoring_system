# IMPORTING LIBRARIES

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np


# IMPORTING FILE FROM PANDAS SEARCH ENGINES

from data import *


# CLASSES

class NewData:

    def __init__(self, trioolein_feed, water_feed, pressure, number_tubes):
        self.trioolein_feed = trioolein_feed
        self.water_feed = water_feed
        self.pressure = pressure
        self.number_tubes = number_tubes
    
    
class TrainPredict(NewData):  

    def Train_Predict_OA(trioolein_feed, water_feed, pressure, number_tubes):
        
        list = [[water_feed, number_tubes, pressure, trioolein_feed]]

        X_test = pd.DataFrame(list)
        
        previsores = X_train.values
        oa_flows_ = oa_flows.values

        scaler1 = StandardScaler()
        previsores1 = scaler1.fit_transform(previsores)
        test1 = scaler1.transform(X_test)

        regressor1 = MLPRegressor(hidden_layer_sizes=(6,), max_iter=100000, activation='relu', random_state=42, solver = 'adam', batch_size = 210, verbose=1)
        regressor1.fit(previsores1, oa_flows_)

        previsao_oa_flow = regressor1.predict(test1)
        
        return previsao_oa_flow


    def Train_Predict_Conversions(trioolein_feed, water_feed, pressure, number_tubes):
        
        list = [[water_feed, number_tubes, pressure, trioolein_feed]]

        X_test = pd.DataFrame(list)
        
        previsores = X_train.values
        conversions_ = conversions.values

        scaler2 = StandardScaler()
        previsores2 = scaler2.fit_transform(previsores)
        test2 = scaler2.transform(X_test)

        regressor2 = MLPRegressor(hidden_layer_sizes=(6,), max_iter=100000, activation='relu', random_state=42, solver = 'adam', batch_size = 210, verbose=1)
        regressor2.fit(previsores2, conversions_)
        
        previsao_conversion = regressor2.predict(test2)
        
        return previsao_conversion


    def Train_Predict_Water(trioolein_feed, water_feed, pressure, number_tubes):
        
        list = [[water_feed, number_tubes, pressure, trioolein_feed]]

        X_test = pd.DataFrame(list)
        
        previsores = X_train.values
        water_consumptios_ = water_consumptios.values

        scaler3 = StandardScaler()
        previsores3 = scaler3.fit_transform(previsores)
        test3 = scaler3.transform(X_test)

        regressor3 = MLPRegressor(hidden_layer_sizes=(6,), max_iter=100000, activation='relu', random_state=42, solver = 'adam', batch_size = 210, verbose=1)
        regressor3.fit(previsores3, water_consumptios_)
        
        previsao_water = regressor3.predict(test3)
        
        return previsao_water


class StatusAndRecommend(TrainPredict):

    def Status_Concept(previsao_oa_flow, trioolein_feed, water_feed, pressure, number_tubes, previsao_conversion, previsao_water):
        
        if previsao_conversion < 99.85:
            
            process_status = "PROPER CONVERSION NOT ACHIEVED!"
            
            trioolein_feed = float(trioolein_feed)
            
            filtro1 = data['conversion'] > 0.9985
            data_resume1 = data[filtro1]
            
            filtro3 = data_resume1['mass_flow_triolein_kgh'] >= trioolein_feed
            filtro2 = data_resume1['mass_flow_triolein_kgh'] < (trioolein_feed + 0.026*trioolein_feed)
            data_resume2 = data_resume1[filtro2 & filtro3]

            filtro4 = data_resume2['number_tubes'] == float(number_tubes)
            data_resume3 = data_resume2[filtro4]
            
            filtro5 = data_resume3['pressure_bar'] == data_resume3['pressure_bar'].min()
            data_resume4 = data_resume3[filtro5]
            
            filtro6 = data_resume4['mass_flow_water_kgh'] == data_resume4['mass_flow_water_kgh'].min()
            data_resume5 = data_resume4[filtro6]
            
            recommended_actions1 = " "
            recommended_actions2 = " "
            recommended_actions3 = " "
            recommended_actions4 = " "
            
            if data_resume5['mass_flow_triolein_kgh'].iloc[0] > float(trioolein_feed):
                recommended_actions1 = "| INCREASE TRIOLEIN FEED"
            
            if data_resume5['mass_flow_triolein_kgh'].iloc[0] < float(trioolein_feed):
                recommended_actions1 = "| REDUCE TRIOLEIN FEED"
            
            if data_resume5['mass_flow_water_kgh'].iloc[0] > float(water_feed):
                recommended_actions2 = " | INCREASE WATER FEED"
            
            if data_resume5['mass_flow_water_kgh'].iloc[0] < float(water_feed): 
                recommended_actions2 = " | REDUCE WATER FEED"
            
            if round(data_resume5['pressure_bar'].iloc[0], 1) < float(pressure):
                recommended_actions3 = " | REDUCE OPERATING PRESSURE"
            
            if round(data_resume5['pressure_bar'].iloc[0], 1) > float(pressure):
                recommended_actions3 = " | INCREASE OPERATING PRESSURE"
            
            if data_resume5['number_tubes'].iloc[0] < float(number_tubes):
                recommended_actions4 = " | REDUCE NUMBER OF REACTOR TUBES"
            
            if data_resume5['number_tubes'].iloc[0] > float(number_tubes):
                recommended_actions4 = " | INCREASE NUMBER OF REACTOR TUBES"
            
            recommended_actions = recommended_actions1 + recommended_actions2 + recommended_actions3 + recommended_actions4
            
            triolein_feed = data_resume5['mass_flow_triolein_kgh'].iloc[0]
            water_feed = data_resume5['mass_flow_water_kgh'].iloc[0]
            pressure = data_resume5['pressure_bar'].iloc[0]
            tubes = data_resume5['number_tubes'].iloc[0]
            

        else:
            process_status = "PROPER CONVERSION ACHIEVED!"
            recommended_actions = " "
            triolein_feed = " "
            water_feed = " "
            pressure = " "
            tubes = " "
        
        
        return process_status, recommended_actions, triolein_feed, water_feed, pressure, tubes


# INITIAL DATA FEED (Will be replaced by the data entered when executing this code)  

trioolein_feed = 4000
water_feed = 2000
pressure = 50
number_tubes = 8