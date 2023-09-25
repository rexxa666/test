import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import dash_table
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash import html
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64

# Mendapatkan working directory saat ini
current_wd = os.getcwd()
print("Current working directory:", current_wd)

# Mengubah working directory ke direktori yang diinginkan
#new_wd = "C:/Users/Putu Wira/Documents/Jupiter cmd"
new_wd = "D:\CLOUD_BPS_WIRA\Jupiter cmd"
os.chdir(new_wd)
print("New working directory:", os.getcwd())

#import Monitoring_Ninja1

# Memanggil fungsi atau menjalankan kode dari file 'dashboard.py'
#Monitoring_Ninja1.monitoring()

# membaca file csv
df_waktu = pd.read_csv('df_waktu.csv', index_col=0)
df_DSPU_VPAW23 = pd.read_csv('df_DSPU_VPAW23.csv', index_col=0)
df_VPAW23 = pd.read_csv('df_VPAW23.csv', index_col=0)
df_VPDP23 = pd.read_csv('df_VPDP23.csv', index_col=0)
df_STKUG = pd.read_csv('df_STKUG.csv', index_col=0)
df_STKUH = pd.read_csv('df_STKUH.csv', index_col=0)
df_STKUJ = pd.read_csv('df_STKUJ.csv', index_col=0)
df_STKUK = pd.read_csv('df_STKUK.csv', index_col=0)
df_STKUO = pd.read_csv('df_STKUO.csv', index_col=0)
df_TransportasiLaut = pd.read_csv('df_TransportasiLaut.csv', index_col=0)
df_TransportasiUdara = pd.read_csv('df_TransportasiUdara.csv', index_col=0)
df_SAPBTerminal = pd.read_csv('df_SAPBTerminal.csv', index_col=0)
df_SAPBJembatanTimbang = pd.read_csv('df_SAPBJembatanTimbang.csv', index_col=0)
df_SDT = pd.read_csv('df_SDT.csv', index_col=0)
df_VHTS = pd.read_csv('df_VHTS.csv', index_col=0)
df_VHTSnon = pd.read_csv('df_VHTSnon.csv', index_col=0)
df_VHTL = pd.read_csv('df_VHTL.csv', index_col=0)
df_VDTW = pd.read_csv('df_VDTW.csv', index_col=0)
df_VREST = pd.read_csv('df_VREST.csv', index_col=0)

dataSTKU=[[df_STKUG.iloc[9, 3],df_STKUG.iloc[9, 7],df_STKUG.iloc[9, 5]],
        [df_STKUH.iloc[9, 3],df_STKUH.iloc[9, 7],df_STKUH.iloc[9, 5]],
        [df_STKUJ.iloc[9, 3],df_STKUJ.iloc[9, 7],df_STKUJ.iloc[9, 5]],
        [df_STKUK.iloc[9, 3],df_STKUK.iloc[9, 7],df_STKUK.iloc[9, 5]]]
df_dataSTKU=pd.DataFrame(dataSTKU,columns=['Belum','Clean','Error'])


# Buat aplikasi Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Definisikan style untuk tabel
table_style = {
    'font-family': 'Arial, sans-serif',  # Nama font
    'font-size': '14px',  # Ukuran font
    'color': 'black',  # Warna teks
    'border': '1px solid #ddd',  # Border tabel
    'border-collapse': 'collapse',  # Gabungkan border yang sama
    'width': '100%',  # Lebar tabel
    'margin': '10px 0'  # Margin atas dan bawah
}

# Definisikan style untuk header tabel
header_style = {
    'fontFamily': 'Helvetica, Arial, sans-serif',
    'fontSize': '14px',
    'color': 'black',
    'background-color': '#BDB7AB',  # Warna latar belakang header
    'font-weight': 'bold',  # Tebal teks header
    'text-align': 'center',  # Tepi kiri teks header
    'padding': '8px'  # Padding header
}

# Definisikan style untuk baris tabel
row_style = {
    'padding': '8px'  # Padding baris
}

# Definisikan style untuk sel tabel
cell_style = {
    'fontFamily': 'Helvetica, Arial, sans-serif',
    'fontSize': '14px',
    'color': 'black',
    'border': '1px solid #ddd',  # Border sel
    'padding': '8px'  # Padding sel
}


data_table_VHTS=dash_table.DataTable(
    id='table30',
    data=df_VHTS.to_dict('records'),
    columns=[{'name': col, 'id': col} for col in df_VHTS.columns],
    style_table=table_style,
    style_header=header_style,
    style_cell=row_style,
    style_data=cell_style,
    style_data_conditional=[
        # Set style untuk baris dengan nilai 100 pada kolom Number
        {
            'if': {
                'filter_query': '{%.1} = 100',  # Query untuk filter nilai 100
                'column_id': '%.1'  # ID kolom yang ingin di-filter
            },
            'backgroundColor': 'green',  # Warna latar belakang
            'color': 'black'  # Warna teks
        }
    ]
)

data_table_VHTSnon=dash_table.DataTable(
    id='table31',
    data=df_VHTSnon.to_dict('records'),
    columns=[{'name': col, 'id': col} for col in df_VHTSnon.columns],
    style_table=table_style,
    style_header=header_style,
    style_cell=row_style,
    style_data=cell_style,
    style_data_conditional=[
        # Set style untuk baris dengan nilai 100 pada kolom Number
        {
            'if': {
                'filter_query': '{%.1} = 100',  # Query untuk filter nilai 100
                'column_id': '%.1'  # ID kolom yang ingin di-filter
            },
            'backgroundColor': 'green',  # Warna latar belakang
            'color': 'black'  # Warna teks
        }
    ]
)

pie_chart_VHTL = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_VHTL.iloc[9, 1]- df_VHTL.iloc[9, 6],df_VHTL.iloc[9, 4],df_VHTL.iloc[9, 2]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'VHTL',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        },
    }
)

pie_chart_VDTW = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_VDTW.iloc[9, 1]- df_VDTW.iloc[9, 6],df_VDTW.iloc[9, 4],df_VDTW.iloc[9, 2]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'VDTW',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_VREST = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_VREST.iloc[9, 1]- df_VREST.iloc[9, 6],df_VREST.iloc[9, 4],df_VREST.iloc[9, 2]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'VREST',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_DVPAW = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_DSPU_VPAW23.iloc[9, 2],df_DSPU_VPAW23.iloc[9, 4],df_DSPU_VPAW23.iloc[9, 6]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'DVPAW',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_VPAW = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_VPAW23.iloc[9, 2],df_VPAW23.iloc[9, 4],df_VPAW23.iloc[9, 6]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'VPAW',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_VPDP = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_VPDP23.iloc[9, 2],df_VPDP23.iloc[9, 4],df_VPDP23.iloc[9, 6]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'VPDP',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_STKUG = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_STKUG.iloc[9, 3],df_STKUG.iloc[9, 7],df_STKUG.iloc[9, 5]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'STKUG',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_STKUH = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_STKUH.iloc[9, 3],df_STKUH.iloc[9, 7],df_STKUH.iloc[9, 5]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'STKUH',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_STKUJ = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_STKUJ.iloc[9, 3],df_STKUJ.iloc[9, 7],df_STKUJ.iloc[9, 5]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'STKUJ',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_STKUK = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_STKUK.iloc[9, 3],df_STKUK.iloc[9, 7],df_STKUK.iloc[9, 5]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'STKUK',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_STKUO = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_STKUO.iloc[9, 2],df_STKUO.iloc[9, 6],df_STKUO.iloc[9, 4]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'STKUO',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_TLaut = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_TransportasiLaut.iloc[9, 2],df_TransportasiLaut.iloc[9, 4],df_TransportasiLaut.iloc[9, 3]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'Transportasi Laut',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_TUdara = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_TransportasiUdara.iloc[9, 2],df_TransportasiUdara.iloc[9, 4],df_TransportasiUdara.iloc[9, 3]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'Transportasi Udara',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 12,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_SAPBJembatanTimbang = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_SAPBJembatanTimbang.iloc[9, 2],df_SAPBJembatanTimbang.iloc[9, 4],df_SAPBJembatanTimbang.iloc[9, 3]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'SAPBJembatanTimbang',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 14,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_SAPBTerminal = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_SAPBTerminal.iloc[9, 2],df_SAPBTerminal.iloc[9, 4],df_SAPBTerminal.iloc[9, 3]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'SAPBTerminal',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 14,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

pie_chart_SDT = go.Figure(
    data=[
        go.Pie(
            labels=['Belum Entri', 'Clean', 'Error'],
            values=[df_SDT.iloc[9, 2],df_SDT.iloc[9, 4],df_SDT.iloc[9, 3]],
            hole=0.3,
            marker={'colors': ['blue', 'green', 'red']}
        ),
    ],
    layout={
        'title': 'SDT',
        'font': {
            'family': 'Helvetica, Arial, sans-serif',  # Nama font
            'size': 14,  # Ukuran font
            'color': 'black'  # Warna font
        }
    }
)

# Membuat DataFrame contoh
# Read the image file and encode it as base64
with open("ninja.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("ascii")

app.layout = html.Div([
    html.Div([
        html.Br(style={'background-color': 'white'}),
            dbc.Row([
                dbc.Col([
                    html.Img(src="data:image/jpg;base64,{}".format(encoded_image), style={'width': '70%', 'height': '7  0%'}),
                ], className='col-md-2'),
                dbc.Col([
                    html.H1('MONITORING SURVEI STATISTIK DISTRIBUSI DAN PARIWISATA', style={'textAlign': 'center', 'fontSize': 40, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'background-color': 'white', 'color': 'black', 'font-weight': '700'}),
                    html.H1('TAHUN 2023', style={'textAlign': 'center', 'fontSize': 38, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'background-color': 'white', 'color': 'black', 'font-weight': '700'}),
                    html.Br(),
                    html.H1('Kondisi: ('+str(df_waktu.iloc[0, 4])+' '+df_waktu.iloc[0, 0]+' '+str(df_waktu.iloc[0, 5])+' '+df_waktu.iloc[0, 2]+' WITA)', style={'textAlign': 'center', 'fontSize': 20, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),    
                ], className='col-md-10'),
            ]),
    ], style={'background-color': 'white'}),
    html.Br(),
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(
            label='Rekapitulasi Provinsi',
            value='tab-1',
            style={
                'font-size': '16px',
                'font-weight': 'bold',
                'font-family': 'Lato, Arial, sans-serif',
                'color': '#333333',
                'background-color': '#dcdcdc',
                'border': 'none'
                #'padding': '10px',
                #'width': '500px'
            },
            selected_style={
                'font-size': '16px',
                'font-weight': 'bold',
                'font-family': 'Lato, Arial, sans-serif',
                'color': '#333333',
                'background-color': '#CCFFCC',
                'border': 'none'
                #'padding': '10px',
                #'width': '500px'
            },
            children=[
                html.Div([
                    html.Br(),
                    html.Div([
                        html.H1(' ', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.H1('SURVEI PARIWISATA BULANAN (VHTS) (Bulan '+df_waktu.iloc[0, 3]+')', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                        html.H1('Batas akhir : '+ df_waktu.iloc[0, 0], style={'textAlign': 'left', 'fontSize': 20, 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.Div([
                        dbc.Row([
                            dbc.Col(
                                html.H4('Progres', style={'textAlign': 'center', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                className='col-md-1'
                            ),                            
                            dbc.Col([
                                html.H1('VHTS Hotel Bintang', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                data_table_VHTS,
                                html.H1('Berdasarkan hasil pengolahan diperoleh jumlah dokumen VHTS Bintang yang masuk seperti pada tabel.', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                html.H1('VHTS Hotel Non Bintang', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                data_table_VHTSnon,
                                html.H1('Berdasarkan hasil pengolahan diperoleh jumlah dokumen VHTS Non Bintang yang masuk seperti pada tabel.', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),

                            ], className='col-md-9')
                        ])
                    ])
                    ], style={'background-color': 'white'}),
                    html.Br(),
                    html.Div([
                        html.H2(' ', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.H2('    SURVEI PARIWISATA TAHUNAN (VHTL, VDTW, VREST)', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                        html.H2('Batas akhir: September', style={'textAlign': 'left', 'fontSize': 20, 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.Div([
                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_VHTL,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen VHTL yang clean sebanyak '+ str(df_VHTL.iloc[9, 4])+' dari total target '+ str(df_VHTL.iloc[9, 1])+' ('+str(round(df_VHTL.iloc[9, 4]/df_VHTL.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                ),
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_VDTW,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen VDTW yang clean sebanyak '+ str(df_VDTW.iloc[9, 4])+' dari total target '+ str(df_VDTW.iloc[9, 1])+' ('+str(round(df_VDTW.iloc[9, 4]/df_VDTW.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                ),
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_VREST,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen VREST yang clean sebanyak '+ str(df_VREST.iloc[9, 4])+' dari total target '+ str(df_VREST.iloc[9, 1])+' ('+str(round(df_VREST.iloc[9, 4]/df_VREST.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                )
                            ])
                        ]),
                    ], style={'background-color': 'white'}),    
                    html.Br(),
                    html.Div([
                        html.H2(' ', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.H2('    SURVEI PERDAGANGAN DALAM NEGERI (PAW & POLDIS)', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                        html.H2('Batas akhir: April', style={'textAlign': 'left', 'fontSize': 20, 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.Div([
                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_DVPAW,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah DSPU PAW yang clean sebanyak '+ str(df_DSPU_VPAW23.iloc[9, 4])+' dari total target '+ str(df_DSPU_VPAW23.iloc[9, 1])+' ('+str(round(df_DSPU_VPAW23.iloc[9, 4]/df_DSPU_VPAW23.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                ),
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_VPAW,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen PAW yang clean sebanyak '+ str(df_VPAW23.iloc[9, 4])+' dari total target '+ str(df_VPAW23.iloc[9, 1])+' ('+str(round(df_VPAW23.iloc[9, 4]/df_VPAW23.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                ),
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_VPDP,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen POLDIS yang clean sebanyak '+ str(df_VPDP23.iloc[9, 4])+' dari total target '+ str(df_VPDP23.iloc[9, 1])+' ('+str(round(df_VPDP23.iloc[9, 4]/df_VPDP23.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                )
                            ])
                        ]),
                    ], style={'background-color': 'white'}),    
                    html.Div([
                        html.Br(),                        
                        html.H2('SURVEI TRIWULANAN KEGIATAN USAHA (STKU) (Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                        html.H2('Batas akhir : '+ df_waktu.iloc[0, 6], style={'textAlign': 'left', 'fontSize': 20, 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.Div([
                            dbc.Row([
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_STKUG,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen STKU G yang clean sebanyak '+ str(df_STKUG.iloc[9, 7])+' dari total target '+ str(df_STKUG.iloc[9, 2])+' ('+str(round(df_STKUG.iloc[9, 7]/df_STKUG.iloc[9, 2]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                ),
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_STKUH,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen STKU H yang clean sebanyak '+ str(df_STKUH.iloc[9, 7])+' dari total target '+ str(df_STKUH.iloc[9, 2])+' ('+str(round(pd.to_numeric(df_STKUH.iloc[9, 7])/pd.to_numeric(df_STKUH.iloc[9, 2])*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                ),
                                dbc.Col([
                                    dcc.Graph(
                                        figure=pie_chart_STKUJ,
                                        style={'height': '450px', 'width': '450px'}
                                    ),
                                    html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen STKU J yang clean sebanyak '+ str(df_STKUJ.iloc[9, 7])+' dari total target '+ str(df_STKUJ.iloc[9, 2])+' ('+str(round(df_STKUJ.iloc[9, 7]/df_STKUJ.iloc[9, 2]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                                ], className='col-md-4'
                                )
                            ])
                        ]),
                        html.Br(),
                        html.Div([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(
                                    figure=pie_chart_STKUK,
                                    style={'height': '450px', 'width': '450px'}
                                ),
                                html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen STKU K yang clean sebanyak '+ str(df_STKUK.iloc[9, 7])+' dari total target '+ str(df_STKUK.iloc[9, 2])+' ('+str(round(df_STKUK.iloc[9, 7]/df_STKUK.iloc[9, 2]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                            ], className='col-md-4'
                            ),
                            dbc.Col([
                                dcc.Graph(
                                    figure=pie_chart_STKUO,
                                    style={'height': '450px', 'width': '450px'}
                                ),
                                html.H1('Berdasarkan hasil pengolahan diperoleh jumlah Dokumen STKU O yang clean sebanyak '+ str(df_STKUO.iloc[9, 6])+' dari total target '+ str(df_STKUO.iloc[9, 1])+' ('+str(round(pd.to_numeric(df_STKUO.iloc[9, 6])/pd.to_numeric(df_STKUO.iloc[9, 1])*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                            ], className='col-md-4'
                            )
                        ])
                    ]),
                    ], style={'background-color': 'white'}),
                    html.Br(),
                    html.Div([
                        html.H1(' TRANSPORTASI LAUT DAN UDARA (Periode '+ df_waktu.iloc[0, 3]+ ')', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                        html.H1('Batas akhir Periode : 20 '+ df_waktu.iloc[0, 0], style={'textAlign': 'left', 'fontSize': 20, 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.Div([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(
                                    figure=pie_chart_TLaut,
                                    style={'height': '450px', 'width': '450px'}
                                ),
                                html.H1('Berdasarkan hasil simopel diperoleh jumlah Dokumen transportasi laut yang clean sebanyak '+ str(df_TransportasiLaut.iloc[9, 4])+' dari total target '+ str(df_TransportasiLaut.iloc[9, 1])+' ('+str(round(df_TransportasiLaut.iloc[9, 4]/df_TransportasiLaut.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                            ], className='col-md-4'
                            ),
                            dbc.Col([
                                dcc.Graph(
                                    figure=pie_chart_TUdara,
                                    style={'height': '450px', 'width': '450px'}
                                ),
                                html.H1('Berdasarkan hasil simopel diperoleh jumlah Dokumen transportasi udara yang clean sebanyak '+ str(df_TransportasiUdara.iloc[9, 4])+' dari total target '+ str(df_TransportasiUdara.iloc[9, 1])+' ('+str(round(df_TransportasiUdara.iloc[9, 4]/df_TransportasiUdara.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                            ], className='col-md-4'
                            )
                        ])
                    ]),
                    ], style={'background-color': 'white'}),
                    html.Div([
                        html.Br(),
                        html.H1(' SURVEI ANGKUTAN PENUMPANG DAN BARANG (SAPB) DAN SURVEI DWELLING TIME (SDT) (Triwulan '+ str(df_waktu.iloc[0, 1])+ ')', style={'textAlign': 'left', 'fontSize': 28, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                        html.H1('Batas akhir : '+ df_waktu.iloc[0, 6], style={'textAlign': 'left', 'fontSize': 20, 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                        html.Div([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(
                                    figure=pie_chart_SAPBJembatanTimbang,
                                    style={'height': '440px', 'width': '440px'}
                                ),
                                html.H1('Berdasarkan hasil upload dokumen SAPB Jembatan Timbang dari daerah diperoleh jumlah dokumen yang terupload sebanyak '+ str(df_SAPBJembatanTimbang.iloc[9, 4])+' dari total target '+ str(df_SAPBJembatanTimbang.iloc[9, 1])+' ('+str(round(df_SAPBJembatanTimbang.iloc[9, 4]/df_SAPBJembatanTimbang.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                            ], className='col-md-4'
                            ),
                            dbc.Col([
                                dcc.Graph(
                                    figure=pie_chart_SAPBTerminal,
                                    style={'height': '440px', 'width': '440px'}
                                ),
                                html.H1('Berdasarkan hasil upload dokumen SAPB Terminal dari daerah diperoleh jumlah dokumen yang terupload sebanyak '+ str(df_SAPBTerminal.iloc[9, 4])+' dari total target '+ str(df_SAPBTerminal.iloc[9, 1])+' ('+str(round(df_SAPBTerminal.iloc[9, 4]/df_SAPBTerminal.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                            ], className='col-md-4'
                            ),
                            dbc.Col([
                                dcc.Graph(
                                    figure=pie_chart_SDT,
                                    style={'height': '440px', 'width': '440px'}
                                ),
                                html.H1('Berdasarkan hasil upload dokumen SDT dari daerah diperoleh jumlah dokumen yang terupload sebanyak '+ str(df_SDT.iloc[9, 4])+' dari total target '+ str(df_SDT.iloc[9, 1])+' ('+str(round(df_SDT.iloc[9, 4]/df_SDT.iloc[9, 1]*100,2)) +'%)', style={'textAlign': 'left', 'fontSize': 16, 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                            ], className='col-md-4'
                            )
                        ])
                    ]),
                    ], style={'background-color': 'white'}),
                ])
            ]
        ),
        dcc.Tab(
            label='Rekapitulasi Kab/Kota',
            value='tab-2',
            style={
                'font-size': '16px',
                'font-weight': 'bold',
                'font-family': 'Lato, Arial, sans-serif',
                'color': '#333333',
                'background-color': '#dcdcdc',
                'border': 'none'
                #'padding': '10px',
                #'width': '500px'
            },
            selected_style={
                'font-size': '16px',
                'font-weight': 'bold',
                'font-family': 'Lato, Arial, sans-serif',
                'color': '#333333',
                'background-color': '#CCFFCC',
                'border': 'none'
                #'padding': '10px',
                #'width': '500px'
            },
            children=[
                html.Div([
                    html.H2('===========================================================================================================================', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H2('  Rekapitulasi Capaian Pengolahan VHTL Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H3('  *Deadline September 2023', style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_VHTL
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table21',
                                    data=df_VHTL.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_VHTL.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{%.1} = 100',  # Query untuk filter nilai 100
                                                'column_id': '%.1'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan VDTW Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H3('  *Deadline September 2023', style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),

                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_VDTW
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table22',
                                    data=df_VDTW.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_VDTW.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{%.1} = 100',  # Query untuk filter nilai 100
                                                'column_id': '%.1'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan VREST Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H3('  *Deadline September 2023', style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_VREST
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table23',
                                    data=df_VREST.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_VREST.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{%.1} = 100',  # Query untuk filter nilai 100
                                                'column_id': '%.1'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2('===========================================================================================================================', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H2('  Rekapitulasi Capaian Pengolahan DSPU Survei PAW 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H3('  *Deadline April 2023', style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_DVPAW
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table1',
                                    data=df_DSPU_VPAW23.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_DSPU_VPAW23.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{%.1} = 100',  # Query untuk filter nilai 100
                                                'column_id': '%.1'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei PAW 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H3('  *Deadline April 2023', style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_VPAW
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table2',
                                    data=df_VPAW23.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_VPAW23.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{%.1} = 100',  # Query untuk filter nilai 100
                                                'column_id': '%.1'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei POLDIS 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H3('  *Deadline April 2023', style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_VPDP
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table3',
                                    data=df_VPDP23.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_VPDP23.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{%.1} = 100',  # Query untuk filter nilai 100
                                                'column_id': '%.1'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.H2('===========================================================================================================================', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei Triwulanan Kegiatan Usaha (STKU)-G 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline '+df_waktu.iloc[0, 6]+' '+str(df_waktu.iloc[0, 5]), style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_STKUG
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table4',
                                    data=df_STKUG.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_STKUG.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean %} = 100',  # Query untuk filter nilai 100
                                                'column_id': 'Clean %'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei Triwulanan Kegiatan Usaha (STKU)-H 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline '+df_waktu.iloc[0, 6]+' '+str(df_waktu.iloc[0, 5]), style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_STKUH
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table5',
                                    data=df_STKUH.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_STKUH.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean %} = 100',  # Query untuk filter nilai 100
                                                'column_id': 'Clean %'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei Triwulanan Kegiatan Usaha (STKU)-J 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline '+df_waktu.iloc[0, 6]+' '+str(df_waktu.iloc[0, 5]), style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_STKUJ
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table6',
                                    data=df_STKUJ.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_STKUJ.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean %} = 100',  # Query untuk filter nilai 100
                                                'column_id': 'Clean %'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei Triwulanan Kegiatan Usaha (STKU)-K 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline '+df_waktu.iloc[0, 6]+' '+str(df_waktu.iloc[0, 5]), style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_STKUK
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table7',
                                    data=df_STKUK.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_STKUK.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean %} = 100',  # Query untuk filter nilai 100
                                                'column_id': 'Clean %'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei Triwulanan Kegiatan Usaha (STKU)-O 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline '+df_waktu.iloc[0, 6]+' '+str(df_waktu.iloc[0, 5]), style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_STKUO
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table8',
                                    data=df_STKUO.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_STKUO.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean %} = 100',  # Query untuk filter nilai 100
                                                'column_id': 'Clean %'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.H2('===========================================================================================================================', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Transportasi Laut 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Periode: '+str(df_waktu.iloc[0, 3])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline 20 '+str(df_waktu.iloc[0, 0])+' 2023', style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_TLaut
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table9',
                                    data=df_TransportasiLaut.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_TransportasiLaut.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean} = 100.00%',  # Query untuk filter nilai 100
                                                'column_id': 'Clean'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Transportasi Udara 2023 Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Periode: '+str(df_waktu.iloc[0, 3])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline 20 '+str(df_waktu.iloc[0, 0])+' 2023', style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_TUdara
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table10',
                                    data=df_TransportasiUdara.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_TransportasiUdara.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean} = 100.00%',  # Query untuk filter nilai 100
                                                'column_id': 'Clean'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei Angkutan Penumpang dan Barang (SAPB) di Jembatan Timbang Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline '+df_waktu.iloc[0, 6]+' '+str(df_waktu.iloc[0, 5]), style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_SAPBJembatanTimbang
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table11',
                                    data=df_SAPBJembatanTimbang.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_SAPBJembatanTimbang.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean} = 100.00%',  # Query untuk filter nilai 100
                                                'column_id': 'Clean'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei Angkutan Penumpang dan Barang (SAPB) di Terminal Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline '+df_waktu.iloc[0, 6]+' '+str(df_waktu.iloc[0, 5]), style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_SAPBTerminal
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table12',
                                    data=df_SAPBTerminal.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_SAPBTerminal.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean} = 100.00%',  # Query untuk filter nilai 100
                                                'column_id': 'Clean'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ]),
                    html.Br(),
                    html.Br(),
                    html.H2('  Rekapitulasi Capaian Pengolahan Survei Dwelling Time Menurut Kabupaten/Kota', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif', 'font-weight': '700'}),
                    html.H2('(Triwulan '+str(df_waktu.iloc[0, 1])+')', style={'font-size': '28px', 'font-style': 'bold', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.H3('  *Deadline '+df_waktu.iloc[0, 6]+' '+str(df_waktu.iloc[0, 5]), style={'font-size': '24px', 'font-style': 'italic', 'fontFamily': 'Lato, Arial, sans-serif'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dbc.Row([
                            dbc.Col(
                                dcc.Graph(
                                    figure=pie_chart_SDT
                                ),
                                className='col-md-4'
                            ),
                            dbc.Col(
                                dash_table.DataTable(
                                    id='table13',
                                    data=df_SDT.to_dict('records'),
                                    columns=[{'name': col, 'id': col} for col in df_SDT.columns],
                                    style_table=table_style,
                                    style_header=header_style,
                                    style_cell=row_style,
                                    style_data=cell_style,
                                    style_cell_conditional=[
                                        # Set style untuk kolom pertama (kolom value)
                                        {'if': {'column_id': 'Wilayah'},
                                        'textAlign': 'left'},
                                    ],
                                    style_data_conditional=[
                                        # Set style untuk baris dengan nilai 100 pada kolom Number
                                        {
                                            'if': {
                                                'filter_query': '{Clean} = 100.00%',  # Query untuk filter nilai 100
                                                'column_id': 'Clean'  # ID kolom yang ingin di-filter
                                            },
                                            'backgroundColor': 'green',  # Warna latar belakang
                                            'color': 'black'  # Warna teks
                                        }
                                    ]
                                ),
                                className='col-md-8'
                            )
                        ])
                    ])
                ])
            ]
        ),
    ],
    style={
        'font-family': 'Arial',
        'font-size': '16px'
    },
    vertical=False,
    parent_style={
        'border': '1px solid #ccc',
        'border-radius': '5px'
    })
])


if __name__ == '__main__':
    app.run_server(debug=True)
