import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import pandas_datareader.data as web
import datetime

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2015,1,1)
end = datetime.datetime(2018,2,8)

stock="AAPL"
stock1="IBM"
df= web.DataReader(stock, "yahoo", start, end)
df1=web.DataReader(stock1, "yahoo", start, end)
app = dash.Dash()


app.layout = html.Div(children=[
    
    html.H1(children="Hello Dash"),

    
    html.Div(children="""
    Dash: A web application framework for Python
    """),

    dcc.Graph(
        id="examplr-graph",
        figure={
            "data": [
                 {"x":df.index, "y":df.Close, "type":"line", "name":stock},
                 {"x":df1.index, "y":df1.Close, "type":"line", "name":stock1}
            ],
            "layout": {
                "title": "stock"
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
