from flask import Flask, render_template, Response
import io
import time
import webbrowser
from threading import Timer
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import datetime
from datetime import date, timedelta

sheet_url = "https://docs.google.com/spreadsheets/d/1s11-AF4lHdxQnXZpyFEb1WsjP1Y2FPt80yLf0sub7ig/edit#gid=240418990"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
# 3 ITEMS THAT NEED TO BE CONSTANT, df.iloc, and df[column] df['Time name']
df = pd.read_csv(url_1,)
for i in range(0, len(df.index)):
    df.iloc[i, 1] = df.iloc[i, 2].find("REFERENCE1")
    df.iloc[i, 1] = int(df.iloc[i, 1])

MindexNames = df[(df.iloc[:, 1] == -1)].index
df.drop(MindexNames, inplace=True)

#these lines below initialize, application, then load in html format
application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index2.html')

#these lines link directly to the matplotlib plot to display in html


@application.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


#these lines later create the matplotlib plot, main code here
def create_figure():
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    df['Measurement_Date-Time'] = pd.to_datetime(
        df['Measurement_Date-Time'], format='%m/%d/%Y')
    pmpmean = df['Isc_(A)'].mean()
    P1 = (df['Isc_(A)'].sub(pmpmean)).pow(2)
    P2 = P1.sum()
    pmpSD = (P2 / len(df.index))**(1/2)
    pmpUCL = pmpmean+pmpSD*3
    pmpLCL = pmpmean-pmpSD*3
    ax.plot(df.iloc[:, 0], df.iloc[:, 5])
    #ax.set_xlim([date.today() - timedelta(days=90),  date.today()])
    ax.axhline(pmpUCL, color='red')
    ax.axhline(pmpLCL, color='red')
    ax.axhline(pmpmean, color='#c2deb6')
    ax.set_title('Reference-1x2 SPC Chart of Isc')
    ax.set(xlabel='Observation', ylabel='Individual Value')
    return fig


@application.route('/plot2.png')
def plot_png2():
    fig = create_figure2()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure2():
    fig = Figure()

    ax = fig.add_subplot(1, 1, 1)
    df['Measurement_Date-Time'] = pd.to_datetime(
        df['Measurement_Date-Time'], format='%m/%d/%Y')
    pmpmean = df['Isc_(A)'].mean()
    P1 = (df['Isc_(A)'].sub(pmpmean)).pow(2)
    P2 = P1.sum()
    pmpSD = (P2 / len(df.index))**(1/2)
    pmpUCL = pmpmean+pmpSD*3
    pmpLCL = pmpmean-pmpSD*3
    # crucial difference is the x-axis bounds, dates change
    ax.plot(df.iloc[:, 0], df.iloc[:, 5])
    ax.set_xlim([date.today() - timedelta(days=5),  date.today()])
    ax.axhline(pmpUCL, color='red')
    ax.axhline(pmpLCL, color='red')
    ax.axhline(pmpmean, color='#c2deb6')
    ax.set_title('Recent Reference-1x2 SPC Chart of Isc')
    ax.set(xlabel='Observation', ylabel='Individual Value')
    return fig


#run the flask website on 3000 port, separate from 5000 port
def open_browser():
    webbrowser.open_new('http://127.0.0.1:3000/')


#run the flask website on 3000 port, separate from 5000 port
if __name__ == '__main__':
    Timer(1, open_browser).start()
    application.run(host='127.0.0.1', port=3000, debug=True)
