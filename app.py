# Web Application using Dash

import dash
from dash import dcc,html
from dash.dependencies import Input, Output, State

import logging

logging.basicConfig(filename='./Logs/logfile.txt',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

import numpy as np
import pandas as pd
import pickle

app = dash.Dash(__name__)

# load saved model
with open('./Models/xgbmodel.pkl' , 'rb') as f:
    xgb_model = pickle.load(f)

app.layout = html.Div([
        html.H1(children = 'Credit Card Default Prediction -  Utkarsh Gaikwad',
                style = {'textAlign':'center'}),

        html.Br(),
        html.Br(),

        dcc.Link(
            children='GitHub Repository for this project',
            refresh=True,
            href='https://github.com/utkarshg1/Credit-Card-Default-Prediction-Utkarsh'),

        html.Br(),
        html.Br(),

        html.Label('Limit Balance : '),
        dcc.Input(
            id = 'LIMIT_BAL',
            placeholder='LIMIT_BAL',
            value='',
            type = 'number'
        ),
        
        html.Br(),
        html.Br(),

        html.Label('Sex : '),
        dcc.Dropdown(
            id='SEX',
            options=[
                {'label':'Male','value':'1'},
                {'label':'Female','value':'2'}
            ]
        ),

        html.Br(),
        html.Br(),

        html.Label('Education : '),
        dcc.Dropdown(
            id = 'EDUCATION',
            options=[
                {'label':'1) Graduate School','value':'1'},
                {'label':'2) University','value':'2'},
                {'label':'3) High School','value':'3'},
                {'label':'4) Others','value':'4'},
                {'label':'5) Unknown 1','value':'5'},
                {'label':'6) Unknown 2','value':'6'}
            ]
        ),

        html.Br(),
        html.Br(),

        html.Label('Marrtial Status : '),
        dcc.Dropdown(
            id = 'MARRIAGE',
            options=[
                {'label':'Married','value':'1'},
                {'label':'Single','value':'2'},
                {'label':'Others','value':'3'}
            ]
        ),

        html.Br(),
        html.Br(),

        html.Label('Age : '),
        dcc.Input(
            id = 'AGE',
            placeholder='AGE',
            value='',
            type = 'number'
        ),

        html.Br(),
        html.Br(),
        
        html.Label('PAY_0 : '),
        dcc.Slider(
            id = 'PAY_0',
            min = -2,
            max = 8,
            step = 1,
            value = -1
        ),
        
        html.Label('PAY_2 : '),
        dcc.Slider(
            id = 'PAY_2',
            min = -2,
            max = 8,
            step = 1,
            value = -1
        ),

        html.Label('PAY_3 : '),
        dcc.Slider(
            id = 'PAY_3',
            min = -2,
            max = 8,
            step = 1,
            value = -1
        ),

        html.Label('PAY_4 : '),
        dcc.Slider(
            id = 'PAY_4',
            min = -2,
            max = 8,
            step = 1,
            value = -1
        ),

        html.Label('PAY_5 : '),
        dcc.Slider(
            id = 'PAY_5',
            min = -2,
            max = 8,
            step = 1,
            value = -1
        ),

        html.Label('PAY_6 : '),
        dcc.Slider(
            id = 'PAY_6',
            min = -2,
            max = 8,
            step = 1,
            value = -1
        ),

        html.Br(),
        html.Br(),

        html.Label('BILL_AMT1 : '),
        dcc.Input(
            id = 'BILL_AMT1',
            placeholder='BILL_AMT1',
            value='',
            type = 'number'            
        ),

        
        html.Br(),
        html.Br(),

        html.Label('BILL_AMT2 : '),
        dcc.Input(
            id = 'BILL_AMT2',
            placeholder='BILL_AMT2',
            value='',
            type = 'number'            
        ),

        
        html.Br(),
        html.Br(),

        html.Label('BILL_AMT3 : '),
        dcc.Input(
            id = 'BILL_AMT3',
            placeholder='BILL_AMT3',
            value='',
            type = 'number'            
        ),
                
        html.Br(),
        html.Br(),

        html.Label('BILL_AMT4 : '),
        dcc.Input(
            id = 'BILL_AMT4',
            placeholder='BILL_AMT4',
            value='',
            type = 'number'            
        ),

        
        html.Br(),
        html.Br(),

        html.Label('BILL_AMT5 : '),
        dcc.Input(
            id = 'BILL_AMT5',
            placeholder='BILL_AMT5',
            value='',
            type = 'number'            
        ),

        
        html.Br(),
        html.Br(),

        html.Label('BILL_AMT6 : '),
        dcc.Input(
            id = 'BILL_AMT6',
            placeholder='BILL_AMT6',
            value='',
            type = 'number'            
        ),

        html.Br(),
        html.Br(),

        html.Label('PAY_AMT1 : '),
        dcc.Input(
            id = 'PAY_AMT1',
            placeholder='PAY_AMT1',
            value='',
            type = 'number'
        ),

        html.Br(),
        html.Br(),

        html.Label('PAY_AMT2 : '),
        dcc.Input(
            id = 'PAY_AMT2',
            placeholder='PAY_AMT2',
            value='',
            type = 'number'
        ),

        html.Br(),
        html.Br(),

        html.Label('PAY_AMT3 : '),
        dcc.Input(
            id = 'PAY_AMT3',
            placeholder='PAY_AMT3',
            value='',
            type = 'number'
        ),

        html.Br(),
        html.Br(),

        html.Label('PAY_AMT4 : '),
        dcc.Input(
            id = 'PAY_AMT4',
            placeholder='PAY_AMT4',
            value='',
            type = 'number'
        ),

        html.Br(),
        html.Br(),

        html.Label('PAY_AMT5 : '),
        dcc.Input(
            id = 'PAY_AMT5',
            placeholder='PAY_AMT5',
            value='',
            type = 'number'
        ),

        html.Br(),
        html.Br(),

        html.Label('PAY_AMT6 : '),
        dcc.Input(
            id = 'PAY_AMT6',
            placeholder='PAY_AMT6',
            value='',
            type = 'number'
        ),

        html.Br(),
        html.Br(),

        html.Button(children='Predict',id='Button',n_clicks=0),

        html.Div(
            html.H2(id='prediction',children='Output')
        )
])

@app.callback(
    Output(component_id='prediction', component_property='children'),
    [Input(component_id='Button',component_property='n_clicks')],
    [State(component_id='LIMIT_BAL',component_property='value'),
     State(component_id='SEX',component_property='value'),
     State(component_id='EDUCATION',component_property='value'),
     State(component_id='MARRIAGE',component_property='value'),
     State(component_id='AGE',component_property='value'),
     State(component_id='PAY_0',component_property='value'),
     State(component_id='PAY_2',component_property='value'),
     State(component_id='PAY_3',component_property='value'),
     State(component_id='PAY_4',component_property='value'),
     State(component_id='PAY_5',component_property='value'),
     State(component_id='PAY_6',component_property='value'),
     State(component_id='BILL_AMT1',component_property='value'),
     State(component_id='BILL_AMT2',component_property='value'),
     State(component_id='BILL_AMT3',component_property='value'),
     State(component_id='BILL_AMT4',component_property='value'),
     State(component_id='BILL_AMT5',component_property='value'),
     State(component_id='BILL_AMT6',component_property='value'),
     State(component_id='PAY_AMT1',component_property='value'),
     State(component_id='PAY_AMT2',component_property='value'),
     State(component_id='PAY_AMT3',component_property='value'),
     State(component_id='PAY_AMT4',component_property='value'),
     State(component_id='PAY_AMT5',component_property='value'),
     State(component_id='PAY_AMT6',component_property='value')],
     prevent_initial_call=True
)

def prediction(n,lbal,sex,edu,mar,age,p0,p2,p3,p4,p5,p6,b1,b2,b3,b4,b5,b6,pa1,pa2,pa3,pa4,pa5,pa6):
    print('Number of Clicks : ',n)
    logging.debug('Click Number : {}'.format(n))
    li= [lbal,sex,edu,mar,age,p0,p2,p3,p4,p5,p6,b1,b2,b3,b4,b5,b6,pa1,pa2,pa3,pa4,pa5,pa6]
    col = ['LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4',
            'PAY_5','PAY_6','BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5',
            'BILL_AMT6','PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6']
    df = pd.DataFrame(li).T
    df.columns = col
    print(df)
    
    col1= ['LIMIT_BAL', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4',
            'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3',
            'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
            'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
            'SEX_1', 'SEX_2', 'EDUCATION_0', 'EDUCATION_1', 'EDUCATION_2',
            'EDUCATION_3', 'EDUCATION_4', 'EDUCATION_5', 'EDUCATION_6',
            'MARRIAGE_0', 'MARRIAGE_1', 'MARRIAGE_2', 'MARRIAGE_3']
    
    df2 = pd.DataFrame(np.zeros(len(col1))).T
    df2.columns = col1

    df2['LIMIT_BAL']=lbal
    df2['AGE']=age
    df2['PAY_0']=p0
    df2['PAY_2']=p2
    df2['PAY_3']=p3
    df2['PAY_4']=p4
    df2['PAY_5']=p5
    df2['PAY_6']=p6
    df2['BILL_AMT1']=b1
    df2['BILL_AMT2']=b2
    df2['BILL_AMT3']=b3
    df2['BILL_AMT4']=b4
    df2['BILL_AMT5']=b5
    df2['BILL_AMT6']=b6
    df2['PAY_AMT1']=pa1
    df2['PAY_AMT2']=pa2
    df2['PAY_AMT3']=pa3
    df2['PAY_AMT4']=pa4
    df2['PAY_AMT5']=pa5
    df2['PAY_AMT6']=pa6   
     
    if sex=='1':
        df2['SEX_1']=1
    else:
        df2['SEX_2']=1

    if mar=='1':
        df2['MARRIAGE_1']=1
    elif mar=='2':
        df2['MARRIAGE_2']=1
    else:
        df2['MARRIAGE_3']=1
    
    if edu=='1':
        df2['EDUCATION_1']=1
    elif edu=='2':
        df2['EDUCATION_2']=1
    elif edu=='3':
        df2['EDUCATION_3']=1
    elif edu=='4':
        df2['EDUCATION_4']=1
    elif edu=='5':
        df2['EDUCATION_5']=1
    else :
        df2['EDUCATION_6']=1

    print('\nProcessed DataFrame is below \n',df2)
    
    logging.info('dataframe initial - \n{}'.format(df.to_string()))
    logging.info('dataframe processed -\n{}'.format(df2.to_string()))

    op = xgb_model.predict(df2)
    print(op[0])
    if op[0]==1:
        s = "Will Default : Yes"
    else:
        s = "Will Default : No"
    
    print(s)

    logging.info('{}'.format(s))
    logging.info('Server Ran Successfully')

    return "{}".format(s)

if __name__=='__main__':
    app.run_server(debug=True)
    