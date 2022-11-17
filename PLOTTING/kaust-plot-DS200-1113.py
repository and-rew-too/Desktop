import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.patches as mpatches

#link https://pythoninoffice.com/how-to-make-waterfall-chart-in-python-matplotlib/
df = pd.DataFrame({'category':['Generated Power','Heat Damage','Edge defects','Rs contact','Rs Busbar','Cell Efficiency'],
                   'num':[23.47,-0.42,-0.39,-2.24,-0.14,-8]})


def waterfall(connect, x, y):
    # calculate running totals
    df['tot'] = df[y].cumsum()
    df['tot1']=df['tot'].shift(1).fillna(0)

    # lower and upper points for the bar charts
    lower = df[['tot','tot1']].min(axis=1)
    upper = df[['tot','tot1']].max(axis=1)

    # mid-point for label position #mid = (lower + upper)/2
    mid = upper + upper/100
    # positive number shows green, negative number shows red
    df.loc[df[y] >= 0, 'color'] = 'bisque'
    df.loc[df[y] < 0, 'color'] = 'maroon'
    # calculate connection points
    #connect= df['tot1'].repeat(3).shift(-1)
    #connect[1::3] = np.nan

    fig,ax = plt.subplots()
    # plot first bar with colors
    bars = ax.bar(x=df[x],height=upper, color =df['color'])
    # plot second bar - invisible
    plt.bar(x=df[x], height=lower,color='white')

    ax.set_ylim(15, 26)
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.2))
    ax1 = ax.twinx()
    ax1.set_ylim(15, 26)
    ax1.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax1.yaxis.set_minor_locator(plt.MultipleLocator(0.2))
    ax.set_ylabel("Power and Energy Losses mW/cm2")


    rect=mpatches.Rectangle((0.5,16),3,9,
                            fill=False,
                            color="purple",
                           linewidth=2)
                           #facecolor="red")
    plt.gca().add_patch(rect)

    upperL = upper[:-1]
    # plot bar labels
    for i, v in enumerate(upperL):
        plt.text(i-.25, mid[i], f"{df[y][i]:,.2f}")

waterfall(df,'category','num')


plt.show()
