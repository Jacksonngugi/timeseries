import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from calendar import month_name
import numpy as np

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],index_col='date')

# Clean data
df = df.sort_values(by=['value'],ascending=True)

df = df.iloc[:-(round((2.5/100)*(len(df))))]

df = df.sort_values(by=['date'])


def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots()
    x = df.index
    y = df['value']

    ax.plot(x,y,'r')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    months = month_name[1:]
    df_bar['months'] = pd.Categorical(df_bar.index.strftime('%B'), categories=months, ordered=True)
    dfp = pd.pivot_table(data=df, index=df.index.year, columns='months', aggfunc = np.mean)
    dfp.columns = dfp.columns.get_level_values(1)

    # Draw bar plot
    fig,ax=plt.subplots()
    dfp.plot(kind='bar', figsize=(8, 4), ylabel='Average Page Views', xlabel='Years',ax=ax)
    ax.legend(bbox_to_anchor=(0,1), loc='upper left',title='Months',ncol=1)
    plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)
    df_box.sort_values(by='month')


    # Draw box plots (using Seaborn)
    fig,ax=plt.subplots(1,2,figsize=(12,4))
    ax[0].set_title('Year-wise Boxplot(Trend)')
    ax[0].set_xlabel('Pageviews')
    ax[0].set_ylabel('Year')
    ax[1].set_title('Month-wise BoxPlot(Trend)')
    ax[1].set_xlabel('Pageviews')
    ax[1].set_ylabel('Month')
    sns.boxplot(ax=ax[0],data=df_box,x=df_box['year'],y=df_box['value'])
    sns.boxplot(ax=ax[1],data=df_box,x=df_box['month'],y=df_box['value'])
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
