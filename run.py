import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly as ply
import base64
import dash_table
from sklearn.externals import joblib

#table content declaration





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div([

    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content')

])

df = pd.read_csv('insurance_75000.csv',encoding='latin1')
app.config.suppress_callback_exceptions = True
x=df[["VehicleReg","CustomerName","Package","AddonDate","Make","Model","CC","GearType","Gender","Address","VehicleType","VehicleWidth","VehicleHeight","FuelType","BrakeOperation","AvgFuelConsumption","StatusText","Speed","Odo","AssembledDate","Place"]]
y=df["Premium"]
from sklearn.preprocessing import LabelEncoder
le_VehicleType=LabelEncoder()
le_Address=LabelEncoder()
le_Gender=LabelEncoder()
le_GearType=LabelEncoder()
le_Make=LabelEncoder()
le_AddonDate=LabelEncoder()
le_Package=LabelEncoder()
le_CustomerName=LabelEncoder()
le_VehicleReg=LabelEncoder()


le_FuelType=LabelEncoder()
le_BrakeOperation=LabelEncoder()
le_StatusText=LabelEncoder()
le_AssembledDate=LabelEncoder()
le_Place=LabelEncoder()

x['BrakeOperation_n']=le_BrakeOperation.fit_transform(x['BrakeOperation'])
x['FuelType_n']=le_FuelType.fit_transform(x['FuelType'])
x['VehicleType_n']=le_VehicleType.fit_transform(x['VehicleType'])
x['Address_n']=le_Address.fit_transform(x['Address'])
x['Gender_n']=le_Gender.fit_transform(x['Gender'])
x['GearType_n']=le_GearType.fit_transform(x['GearType'])
x['Make_n']=le_Make.fit_transform(x['Make'])
x['AddonDate_n']=le_AddonDate.fit_transform(x['AddonDate'])
x['Package_n']=le_Package.fit_transform(x['Package'])
x['CustomerName_n']=le_CustomerName.fit_transform(x['CustomerName'])
x['VehicleReg_n']=le_VehicleReg.fit_transform(x['VehicleReg'])


x['StatusText_n']=le_StatusText.fit_transform(x['StatusText'])
x['AssembledDate_n']=le_AssembledDate.fit_transform(x['AssembledDate'])
x['Place_n']=le_Place.fit_transform(x['Place'])

index_page = html.Div(style={'backgroundImage': 'url(https://www.carconfident.ca/wp-content/uploads/2019/05/01585ca88d26024.jpg)','backgroundRepeat': 'no-repeat', 'backgroundPosition': 'center', 'backgroundSize': 'cover', 'position': 'fixed', 'height' : "100%", 'width':"100%"},children=[
 
         html.Br(),
         html.Br(),
  html.H2(className='what-is', children="Predicition of Vehicle Insurance Premium",style={ 'color':'black','text-align': 'center', 'fontSize': 35, 'font-family': 'Courgette'}),
  html.H4(className='what-is', children="Data Science",style={ 'color':'black','text-align': 'center', 'fontSize': 25, 'font-family': 'Courgette'}),  
        html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Mountains+of+Christmas&display=swap" ,rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet"),
         html.Link(href="https://fontawesome.com/icons"),
        html.Br(),
        
        
        html.H2(className='what-is', children="Overview of Dash Framework For building Dashboards",style={ 'color':'black','text-align': 'center', 'fontSize': 20, 'font-family': 'Courgette'}),
        
      
html.Div(style={'color':'red','text-align': 'center'},
   className='row',
   children=[
      html.Div(className='two columns', style={'color':'red', 'marginLeft': 195}),
      dcc.Link('Click here for Vehicle Insurance Premium Dashboard visualizations! ', href='/car', style={'color':'red','text-align': 'center', 'justify-content': 'center'})
   ]
),
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
     
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
         html.Br(),
        
      
     
        
        html.H2(className='what-is', children="Narmin | Arisha | Ramsha | 8/1/2019",style={ 'color':'black','text-align': 'center', 'fontSize': 20, 'font-family': 'Courgette'}),
            

])

@app.callback(dash.dependencies.Output('page-content', 'children'),

              [dash.dependencies.Input('url', 'pathname')])

def display_page(pathname):
      if pathname == '/car':
        return car_layout

      else:

        return index_page




d_speed = df['Speed'].unique()
d_odo = df['Odo'].unique()
d_brakeoperation = x['BrakeOperation_n'].unique()
d_addon = x['AddonDate_n'].unique()
d_customername = x['CustomerName_n'].unique()
d_vehiclereg = x['VehicleReg_n'].unique()
d_statustext = x['StatusText_n'].unique()
d_assembleddate = x['AssembledDate_n'].unique()
d_place = x['Place_n'].unique()

colors = {
    'background': '#111111',
    'text':'#FFFFFF',

    }

all_options = {

    'Dimensions': ['Place','AssembledDate','AddonDate','VehicleReg','CustomerName','Package','Make','GearType','Gender','Address','VehicleType','FuelType','BrakeOperation','StatusText'],

    'Measures': ['Model','CC','VehicleWidth','VehicleHeight','AvgFuelConsumption','Speed','Odo'],

    'All': ['Model','CC','VehicleWidth','VehicleHeight','AvgFuelConsumption','Speed','Odo','Place','AssembbledDate','AddonDate','VehicleReg','CustomerName','Package','Make','GearType','Gender','Address','VehicleType','FuelType','BrakeOperation','StatusText']

}








insurance_data = {

    'VehicleReg': {'x': df['VehicleReg'], 'y': df['Premium']},

    'CustomerName': {'x': df['CustomerName'], 'y': df['Premium']},

    'Package':  {'x': df['Package'], 'y': df['Premium']},

    'AddonDate': {'x': df['AddonDate'], 'y': df['Premium']},

    'Make':  {'x': df['Make'], 'y': df['Premium']},

    'Model':  {'x': df['Model'], 'y': df['Premium']},

    'CC':  {'x': df['CC'], 'y': df['Premium']},

    'GearType': {'x': df['GearType'], 'y': df['Premium']},

    'Gender':  {'x': df['Gender'], 'y': df['Premium']},

    'Address':  {'x': df['Address'], 'y': df['Premium']},

    'VehicleType':  {'x': df['VehicleType'], 'y': df['Premium']},

    'VehicleWidth':  {'x': df['VehicleWidth'], 'y': df['Premium']},

    'VehicleHeight':  {'x': df['VehicleHeight'], 'y': df['Premium']},

    'FuelType':  {'x': df['FuelType'], 'y': df['Premium']},

    'BrakeOperation':  {'x': df['BrakeOperation'], 'y': df['Premium']},

    'AvgFuelConsumption':  {'x': df['AvgFuelConsumption'], 'y': df['Premium']},

    'StatusText':  {'x': df['StatusText'], 'y': df['Premium']},

    'Speed':  {'x': df['Speed'], 'y': df['Premium']},

    'Odo':  {'x': df['Odo'], 'y': df['Premium']},

    'AssembledDate':  {'x': df['AssembledDate'], 'y': df['Premium']},

    'Place':  {'x': df['Place'], 'y': df['Premium']}

}


app.config.suppress_callback_exceptions = True

graph_layout = html.Div([
    html.H1(children='Graphical Reresenatiom Of Models With Numeric & Non-Numeric Attributes',style={ 'color':'black','text-align': 'center', 'fontSize': 30, 'font-family': 'EB Garamond'},
           ),


           html.Div(
                [
                    html.P(children='Select Category',
                           style={
                              'text-align': 'center',
                    #          'fontSize':21,
                              'color': 'black',
                    #          'font-family': 'Josefin Sans',}),
                    }),
                    dcc.RadioItems(
                            id = 'Category',
                            options=[{'label': k, 'value': k} for k in all_options.keys()],
                            value='Measures',
                            style={'color':'black','text-align': 'center','font-family': 'Josefin Sans','fontSize': 15},
                            labelStyle={'display': 'inline-block'}
                    ),
                ],

            ),

     html.Br(),



            html.Div(
                [
                   html.P(children='Select Features',
                          style={
                              'text-align': 'center',
                              'fontSize': 21,
                              'color': 'black',
                    #          'font-family': 'Josefin Sans'}),
                    }),
             dcc.Checklist(
                    id='Features',



                    values=['Package'],


                     labelStyle={'display': 'inline-block'},
                     style={
                         'color': 'black',
                         'text-align': 'center',
                       'font-family': 'Josefin Sans',
                         'fontSize': 15

                     }


                    ),
                ],

            ),

   html.Br(),
   html.Br(),


    html.Div([

        html.Div([

            dcc.Graph(

                id='example-graph'

            )], className= 'six columns'

            ),


        html.Div([

            dcc.Graph(

                id='example-graph-2'

            )], className= 'six columns'

            )

    ], className="row"),




    html.Div(id='page-1-content'),

], className='ten columns offset-by-one')


@app.callback(

    dash.dependencies.Output('Features', 'options'),

    [dash.dependencies.Input('Category', 'value')])

def set_cities_options(selected_category):

    return [{'label': i, 'value': i} for i in all_options[selected_category]]



@app.callback(

    dash.dependencies.Output('example-graph', 'figure'),

    [dash.dependencies.Input('Features', 'values')])

def update_image_src(selector):

    data = []

    print (selector)

    for Feature in selector:

        data.append({'x': insurance_data[Feature]['x'], 'y': insurance_data[Feature]['y'],

                    'type': 'bar','name': Feature})

    figure = {

        'data': data,

        'layout': {

            'title': 'Box Graph Represenation of Selected Category & Feature',

            'xaxis' : dict(

                title='x Axis',

                titlefont=dict(

                family='Courier New, monospace',

                size=20,

                color='#7f7f7f',



            )),

            'yaxis' : dict(

                title='y Axis',

                titlefont=dict(

                family='Helvetica, monospace',

                size=20,

                color='#7f7f7f'

            ))

        }

    }

    return figure




@app.callback(

    dash.dependencies.Output('example-graph-2', 'figure'),

    [dash.dependencies.Input('Features', 'values')])

def update_image_src(selector):

    data = []

    for city in selector:

        data.append({'x': insurance_data[city]['x'], 'y': insurance_data[city]['y'],

                    'type': 'line', 'name': city})

    figure = {

        'data': data,

        'layout': {

            'title': 'Line Graph Represenation of Selected Category & Feature',

            'xaxis' : dict(

                title='x Axis',

                titlefont=dict(

                family='Courier New, monospace',

                size=20,

                color='#7f7f7f'

            )),

            'yaxis' : dict(

                title='y Axis',

                titlefont=dict(

                family='Helvetica, monospace',

                size=20,

                color='#7f7f7f'

            ))

        }

    }

    return figure

model_layout = html.Div(children=[
    html.H2(className='what-is', children="Decision Tree Results",style={ 'color':'black','text-align': 'center', 'fontSize': 35, 'font-family': 'EB Garamond'}),
   
  html.A(style={'text-align': 'center','color':'red'},children="Need to download the encoded Guide list  click here!",
             download="abc.csv",
             href="",
            target="_blank"
),
    
  
        html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Mountains+of+Christmas&display=swap" ,rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet"),
    
      
    html.Div(children=[
    html.Div([

         html.Div(
            [
                html.Label('Enter Model '),
                dcc.Dropdown(
                        id = 'CC1',
                        options=[{'label': k, 'value': k} for k in  [2016,2017,2018,2013,2015]],
                        value='2016',

                ),
            ],
            className='four columns',
            style={'margin-top': '10'}
        ),
             html.Div(
                [
                    html.Label('Enter CC '),
                    dcc.Dropdown(
                            id = 'CC2',
                            options=[{'label': k, 'value': k} for k in  [1300,1800]],
                            value='1300',

                    ),
                ],
                className='four columns',
                style={'margin-top': '10'}
            ),
             html.Div(
                [
                    html.Label('Enter Vehicle Width '),
                    dcc.Dropdown(
                            id = 'CC3',
                            options=[{'label': k, 'value': k} for k in  [5,0]],
                            value='5',

                    ),
                ],
                className='four columns',
                style={'margin-top': '10'}
            ),
             ], className="row"
    ),
    ## 2nd row
        html.Div([

             html.Div(
                [
                    html.Label('Enter Vehicle Height '),
                    dcc.Dropdown(
                            id = 'CC4',
                            options=[{'label': k, 'value': k} for k in  [3,0]],
                            value='3',

                    ),
                ],
                className='four columns',
                style={'margin-top': '20'}
            ),
                 html.Div(
                    [
                        html.Label('Enter Average Fuel Consumption '),
                        dcc.Dropdown(
                                id = 'CC5',
                                options=[{'label': k, 'value': k} for k in  [11,8]],
                                value='11',

                        ),
                    ],
                    className='four columns',
                    style={'margin-top': '20'}
                ),
                 html.Div(
                    [
                        html.Label('Enter Fuel Type '),
                        dcc.Dropdown(
                                id = 'CC6',
                                options=[{'label': k, 'value': k} for k in  [1,0]],
                                value='1',

                        ),
                    ],
                    className='four columns',
                    style={'margin-top': '20'}
                ),
                 ], className="row"
        ),
#3rd

    html.Div([

         html.Div(
            [
                html.Label('Enter Vehicle Type'),
                dcc.Dropdown(
                        id = 'CC7',
                        options=[{'label': k, 'value': k} for k in  [1,0]],
                        value='1',

                ),
            ],
            className='four columns',
            style={'margin-top': '20'}
        ),
             html.Div(
                [
                    html.Label('Enter Address '),
                    dcc.Dropdown(
                            id = 'CC8',
                            options=[{'label': k, 'value': k} for k in  [1,0]],
                            value='1',

                    ),
                ],
                className='four columns',
                style={'margin-top': '20'}
            ),
             html.Div(
                [
                    html.Label('Enter Gender: '),
                    dcc.Dropdown(
                            id = 'CC9',
                            options=[{'label': k, 'value': k} for k in  [1,0]],
                            value='1',

                    ),
                ],
                className='four columns',
                style={'margin-top': '20'}
            ),
             ], className="row"
    ),
    #4th
        html.Div([

             html.Div(
                [
                    html.Label('Enter Gear Type '),
                    dcc.Dropdown(
                            id = 'CC11',
                            options=[{'label': k, 'value': k} for k in  [1,0]],
                            value='1',

                    ),
                ],
                className='four columns',
                style={'margin-top': '20'}
            ),
                 html.Div(
                    [
                        html.Label('Enter Make'),
                        dcc.Dropdown(
                                id = 'CC12',
                                options=[{'label': k, 'value': k} for k in  [1,0]],
                                value='1',

                        ),
                    ],
                    className='four columns',
                    style={'margin-top': '20'}
                ),
                 html.Div(
                    [
                        html.Label('Enter Package'),
                        dcc.Dropdown(
                                id = 'CC13',
                                options=[{'label': k, 'value': k} for k in  [1,0]],
                                value='1',

                        ),
                    ],
                    className='four columns',
                    style={'margin-top': '20'}
                ),
                 ], className="row"
        ),
     #5th
             html.Div([

                  html.Div(
                     [
                         html.Label('Enter Speed '),
                         dcc.Dropdown(
                                 id = 'CC14',
                                 options=[{'label': k, 'value': k} for k in  d_speed],
                                 value='27',

                         ),
                     ],
                     className='four columns',
                     style={'margin-top': '20'}
                 ),
                      html.Div(
                         [
                             html.Label('Enter Odo '),
                             dcc.Dropdown(
                                     id = 'CC15',
                                     options=[{'label': k, 'value': k} for k in  d_odo],
                                     value='57',

                             ),
                         ],
                         className='four columns',
                         style={'margin-top': '20'}
                     ),
                      html.Div(
                         [
                             html.Label('Enter Add-on-Date '),
                             dcc.Dropdown(
                                     id = 'CC16',
                                     options=[{'label': k, 'value': k} for k in  d_addon],
                                     value='18:27.1',

                             ),
                         ],
                         className='four columns',
                         style={'margin-top': '20'}
                     ),
                      ], className="row"
             ),
#6th
     html.Div([

          html.Div(
             [
                 html.Label('Enter Customer Name '),
                 dcc.Dropdown(
                         id = 'CC17',
                         options=[{'label': k, 'value': k} for k in  d_customername],
                         value='33',

                 ),
             ],
             className='four columns',
             style={'margin-top': '20'}
         ),
              html.Div(
                 [
                     html.Label('Enter Vehicle Registration Number '),
                     dcc.Dropdown(
                             id = 'CC18',
                             options=[{'label': k, 'value': k} for k in  d_vehiclereg],
                             value='33',

                     ),
                 ],
                 className='four columns',
                 style={'margin-top': '20'}
             ),
              html.Div(
                 [
                     html.Label('Enter Status Text '),
                     dcc.Dropdown(
                             id = 'CC19',
                             options=[{'label': k, 'value': k} for k in  d_statustext],
                             value='0',

                     ),
                 ],
                 className='four columns',
                 style={'margin-top': '20'}
             ),
              ], className="row"
     ),


#7th

     html.Div([

          html.Div(
             [
                 html.Label('Enter Assembled Date'),
                 dcc.Dropdown(
                         id = 'CC22',
                         options=[{'label': k, 'value': k} for k in  d_assembleddate],
                         value='2219',

                 ),
             ],
             className='four columns',
             style={'margin-top': '20'}
         ),
              html.Div(
                 [
                     html.Label('Enter Encoded Place: '),
                     dcc.Dropdown(
                             id = 'CC23',
                             options=[{'label': k, 'value': k} for k in  d_place],
                             value='13716',
                           
                     ),
                 ],
                 className='four columns',
                 style={'margin-top': '20'}
             ),
              html.Div(
                 [
                     html.Label('Enter Brake-Operation '),

                     dcc.Dropdown(
                             id = 'CC24',
                             options=[{'label': k, 'value': k} for k in  d_brakeoperation],
                             value='0',
                             

                     ),
                 ],
                 className='four columns',
                 style={'margin-top': '20'}
             ),
              ], className="row"
     ),



        html.Div(id='result')

    ], style={'textAlign': 'center'}),


])


@app.callback(
    Output(component_id='result', component_property='children'),
    [Input(component_id='CC1', component_property='value'),
    Input(component_id='CC2', component_property='value'),
    Input(component_id='CC3', component_property='value'),
    Input(component_id='CC4', component_property='value'),
    Input(component_id='CC5', component_property='value'),
    Input(component_id='CC6', component_property='value'),
    Input(component_id='CC7', component_property='value'),
    Input(component_id='CC8', component_property='value'),
    Input(component_id='CC9', component_property='value'),
    Input(component_id='CC11', component_property='value'),
    Input(component_id='CC12', component_property='value'),
    Input(component_id='CC13', component_property='value'),
    Input(component_id='CC14', component_property='value'),
    Input(component_id='CC15', component_property='value'),
    Input(component_id='CC16', component_property='value'),
    Input(component_id='CC17', component_property='value'),
    Input(component_id='CC18', component_property='value'),
    Input(component_id='CC19', component_property='value'),
    Input(component_id='CC22', component_property='value'),
    Input(component_id='CC23', component_property='value'),
    Input(component_id='CC24', component_property='value'),
    ])

def update_years_of_experience_input(CC1,CC2,CC3,CC4,CC5,CC6,CC7,CC8,CC9,CC11,CC12,CC13,CC14,CC15,CC16,CC17,CC18,CC19,CC22,CC23,CC24):
    xnew1 = [[CC1,CC2,CC3,CC4,CC5,CC6,CC7,CC8,CC9,CC11,CC12,CC13,CC14,CC15,CC16,CC17,CC18,CC19,CC22,CC23,CC24]]
    if xnew1 is not None and xnew1 is not '':
        try:
            salary = model.predict(xnew1)[0]

            return "suggested premium is {}".format(salary)
        except ValueError:
            return ''
#app main layout
car_layout = html.Div(children=[
        # header

        html.Div([
             html.Div(
                html.Img(src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAABECAYAAAA1DeP1AAAACXBIWXMAAAsSAAALEgHS3X78AAAFcklEQVR42uWcT2hcRRzHv6leFCUL3lR4C5WiYJd36EVI2sWLEARzUCKe9uBBvHQLHqwIBi/xuCLUHLa4ClYQITl5LKtGUBCywaqkbDGtQvwH2SY1scTuz8vvwY9xfjvzdqfZ9/YNPJjM++28mc+bP7/5zrxMERFyEkoA5jm+CqAXMvOpnICIAbQBTPPfNwFUAXSKBmILQGSkXQFwsmggtEJOhXrAsZyMD31L2p2QD8gLiA8safcAaBatawBAXcwaXwN4g+MXAbxcJBBmqImW8gXPIoUEkcB4D8ADAK4BeGzSx4jEl2ixP9FgB6sFYBbALQDHAXQnvUWU2XmaVvyIGMCXAB4ctmUcy1EXmDbSnhSDZAfAaQC7omVEkwjicSW9IuIdAGcEjJ/SwMgLiFtK+l/G3x2u/BUA96WCQUR5udbp/6FPRAsW2xIRfc82+0QUufLPEwgQ0QwR1bliLQGkqcDoCBiVSQJhXospYGitZyJAgIhqHjBaLhihClPlt7NIRGWlMHUiarNNyWITc4HbbGu73xGVbigwrnIeLaMsEsYPZllCv5EkzBs2HeP+lgEjtuTRMvLYstgsi/uvWu73jOdctti0Q4H4W8ucr3NkD+eFzbeKTTLAVZT7OyKPpmLztrDpKjblEH7E/Za0p0T8OeV3z4j4CcXmaaFRuoLmVp8W8YcUm0dDgPjXIaG976E6bSryXIPj1wH8ZrFZ9njOqohvKOVfC9E1zvEAZIausPlGaZLJKB8R0Z6l2UtHKGKnaoevJUtZmkr+ctC+Ju4fJrNIqNVnBcBL/NY2AXxq0QjmuAtsA3gCwFsWhWkBwCkAr/DvD9j2esr9jxqAlQG/K/G1dbdd7JiIdi0tw3f+L6d1kUe97mbmMRHd5MpsK5WpOZqxCaPEv1lk3yVzIMrCGWqIuVvC2PeAsT7ART4goh+NMaCRJRAldlw0h8lnJVgTg2V3AIxBvsbYQVxUCvhaymVx7IDRU55TDwEihB9xXEl/VsR7LLJuCMFkxiKqzALYswixPQA/K8/5Lsym4ug068qb+nDIZbE2yEZEdNt4xnrWBst1h8NkXq0UMPYNGJcGrFAzMX1WuHAVo5UMC6N0lL7EOAWTTMEYt3qElNrjARF9zl2jbdE9xg5iXkxvPQZgg9H1GHBdMMzwYlZAaKJJ1QC1N8LaA0Q0qzznRlZAXFIKuJzCYfKBUfdQqcYKQpPI2o5p0QeG6Sf0U0zRRw4iUgr4q8eqdEeZCbSutMBiSmYdqgX2AomI/uSpLqmEtq64McLaYy4v06fP8tt3IeYSeDLvR/hU1BeGufYoZ1WY8YVxkitQ9XCY5E6V7Ep3DN0jPmoQMU9h8wOcqraoRElZcSaho4g35k5VJGx+t9j8EQpEiSWvHl8NhxucVMLc+zTDpvHWb1tsLju2Don9FNe2wFwIEA1Lxh879iXNAq56FNAWDj3ykP7ItmIzE0KhOmvRa17wOL/0sIifUmxOOHbE5JGgTzx2qlqW+78AWAuhUJFyJEf6CLaw4vAu+wb1tsVmyeGl2hymJW4ZO4r3OnTX6CqViBy7yBcGqFSHir7Q5Ep0ByhMkRB4juzASfJgWdF/lMo0+Q10Q/v5Wbi0uX/VoRzVJg3GoJutFDA+4m24NkOsThKItDAGCTO5B2HCsJ1JuKCA+CxPIHx2umoA3uVTMK9bPh+6qvzuTK6+/AigSGvCzMqkdQ0fGG8aMLqTNli6YKxYBNaZPE6fw56hkh+WjfQtVVbCKIfJYgBfhfiwLAthlPMRHePDskM+GynPRxYChITRB3CvSD8LYLFIIBJdwpbP80UDsaukP1I0EGuw/3eP5aKBSGaQDQbSA/AOgPN5AvEfhe++jTQt3lAAAAAASUVORK5CYII=',height="75%")
                ,style={"float":"left","height":"75%"}),


            html.Span("Predicition Of Vehicle Insurance Premium", style={'font-family': 'Cookie','fontSize': 30},className='app-title'),

            html.Div(
                html.Img(src='https://www.moneymagpie.com/wp-content/uploads/2015/06/MoneyMagpie_Car-Insurance-Protect.jpg',height="100%")
                ,style={"float":"right","height":"100%"})
            ],
            className="row header"
            ),
          # tabs
          html.Div([

            dcc.Tabs(
                id="tabs", value='about_layout',
                style={"height":"22",'font-family': 'Marck Script','fontSize': 18},
                children=[
                    dcc.Tab(label="About", value="about_layout", ),
                    dcc.Tab(label="Model", value="model_layout",),
                    dcc.Tab(label="Graph", value="graph_layout",),
                    dcc.Tab(label="Table", value="table_layout",),
                ]),
       html.Br(),
      html.Br(),
             html.Div(id='tabs-content')


            ],
            className="row tabs_div"
            ),



        # Tab content
        html.Div(id="tab_content", className="row", style={"margin": "2% 3%"}),

        html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Mountains+of+Christmas&display=swap" ,rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet")
    ],
    className="row",





)

@app.callback(dash.dependencies.Output('tabs-content', 'children'),
              [dash.dependencies.Input('tabs', 'value')])
def render_content(tab):
    if tab == 'about_layout':
        return  html.Div(className='control-tab',children=[

              html.H2(className='what-is', children="About Our Project",style={ 'color':'black','text-align': 'center', 'fontSize': 35, 'font-family': 'EB Garamond'}),

                        html.P('The project Predication of vehicle insurance premium is a research project designed for predicting the premium based on driver behavior.The goal of this project is to see how well various statistical methods perform in predicting of insurance premium based on the characteristics of the insured customer’s vehicles.Prediction of Vehicle Insurance Premium will help the insurance issuers to calculate the accurate insurance and also enable the owner of the vehicle to calculate the insurance of their own vehicle by themselves for this particular dataset available from “TPL Trakker LTD” company. A number of factors will determine premium calculation rates, among them a drivers, age, Vehicle registration number ,Vehicle Model number ,Type of vehicle ,Crashes and injuries ,Claim history, Occupation, Driver behavior, Add on Date, Make, Model, Gear Type, Gender, Brake Operation, Vehicle width, Vehicle height, Average Fuel Consumption respectively.However, this contest focused on the relationship between customer’s behavior and vehicle characteristics well as other characteristics associated with the insurance premium policies.',style={ 'color': 'black','fontSize': 15,'font-family': 'Philosopher'}),

                       html.P('This application has a Dashboard named “DASHBOARD” which is built by using the Python Command which is a graphical user interface and enable us to see the result in more precisely and visualized form. DASHBOARD itself is a proper platform that help to integrate the backhand for the user graphical representation. It contains “.py” extension of files that enable us to understand all the successful result and plotly graphs for better understanding of the project. It all the files contain all interfaced controls and designed parts and enable to integrate the backhand codes with these controls and frontend styling ',style={ 'color': 'black','fontSize': 15,'font-family': 'Philosopher'}),

                       html.P('While After running the application (DASHBOARD) the UX will appear on the screen having dashboard view with the Heading name PREDICTION OF VEHICLE INSURANCE PREMIUM moreover we have graph summary view, data summary view, visualizations view of models with their confusion matrix On the other hand the backend working is carried out through different algorithms that are random forest and logistic regressions svm, knn, decision tree through which working on the whole data is being carried on.',style={ 'color': 'black','fontSize': 15,'font-family': 'Philosopher'}),

                        html.P('Decision Tree is used first finding the importance of variables and Confusion matrix is being obtained. Furthermore it also defines accuracy and in our case it is ’93.86%’ with its graphical representation and confusion matrix calculation respectively.',style={'color':'black','fontSize': 15,'font-family': 'Philosopher'}),
                   html.Div(style={ 'color':'black','fontSize': 10 ,'font-family': 'Philosopher'},children=[
                            'Reference: ',
                            html.A('PlotlyDash',
                                   href='https://plot.ly/dash/)',style={ 'color':'black','fontSize': 10, 'font-family': 'Philosopher'})
                        ]),
                        html.Div(style={ 'color':'black','fontSize': 10 ,'font-family': 'Philosopher'},children=[
                            'For a look into Predicition of Vehicle Insurance Premium Files Details,visit the '
                            'original repository ',
                            html.A('here', href='https://github.com/Narmeen-Shahid/Deploying-Plotly-Dash-To-Heroku',style={ 'color':'black','fontSize': 10 ,'font-family': 'Philosopher'}),
                            '.'
                        ]),
                     

        ],style={'marginBottom': 20, 'marginTop': 25})


    elif tab == 'table_layout':
        return html.Div([

            html.H2(className='what-is', children="Customer & Vehicle DataSet Records",style={ 'color':'black','text-align': 'center', 'fontSize': 30, 'font-family': 'EB Garamond'}),


             html.A(style={ 'text-align': 'center','color':'red'},children="Need to download the data then click here!",


             download="insurance_75000.csv",
             href="",
            target="_blank"

             ),


             dash_table.DataTable(
             data=df.to_dict('records'),
             columns=[{'id': i, 'id': i} for i in df.columns],


            style_header={'backgroundColor': '#E8E4E7',
             'color': 'black'},
            style_cell={
           
            'color': 'black'
    },
),




]),

    elif tab == 'graph_layout':
       return graph_layout

    elif tab == 'model_layout':
          return model_layout



if __name__ == '__main__':
    model = joblib.load("Trees_model.pkl")
    app.run_server(debug=True)
