import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#THIS IS MOST IMPORTANT VARIABLE, CHANGES THE WAFER BEING LOOKED AT
start = 28 #14,21,28,35

sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=296250147"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)

x = df.iloc[:,11]
y = df.iloc[:,2]


#https://stackoverflow.com/questions/27164114/show-confidence-limits-and-prediction-limits-in-scatter-plot
slope, intercept = np.polyfit(x, y, 1)  # linear model adjustment
y_model = np.polyval([slope, intercept], x)   # modeling...
x_mean = np.mean(x)
y_mean = np.mean(y)
n = x.size                        # number of samples
m = 2                             # number of parameters
dof = n - m                       # degrees of freedom
t = stats.t.ppf(0.975, dof)       # Students statistic of interval confidence

residual = y - y_model

std_error = (np.sum(residual**2) / dof)**.5   # Standard deviation of the error

# calculating the r2
# https://www.statisticshowto.com/probability-and-statistics/coefficient-of-determination-r-squared/
# Pearson's correlation coefficient
numerator = np.sum((x - x_mean)*(y - y_mean))
denominator = ( np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2) )**.5
correlation_coef = numerator / denominator
r2 = correlation_coef**2

# mean squared error
MSE = 1/n * np.sum( (y - y_model)**2 )

# to plot the adjusted model
x_line = np.linspace(np.min(x), np.max(x), 100)
y_line = np.polyval([slope, intercept], x_line)
# predicting interval
pi = t * std_error * (1 + 1/n + (x_line - x_mean)**2 / np.sum((x - x_mean)**2))**.5





############### Ploting
plt.rcParams.update({'font.size': 12})
fig = plt.figure()
ax = fig.add_axes([.15, .12, .75, .75])

ax.plot(x, y, "o", color="#b9cfe7", markersize=3,
    markeredgewidth=1, markeredgecolor="b", markerfacecolor="None", label = 'experimental')
ax.plot(x_line, y_line, color = 'royalblue', label = 'fit')
ax.fill_between(x_line, y_line + pi, y_line - pi, color = 'lightcyan', label = '95% prediction interval')

# rounding changed for each case and preference
a = str(np.round(intercept))
b = str(np.round(slope,2))
r2s = str(np.round(r2,2))
MSEs = str(np.round(MSE))
plt.legend(loc="lower right")
ax.set_xlabel('pFF[%]')

#Rsh[Ohm-cm2]
#Eff[%]
#Pmp[W]
#Voc[V]
#
ax.set_ylabel('Isc[A]')
plt.title('Fit Plot for SAS G1ups  $r^2$ =' + r2s)
plt.savefig("22-0181-G_Isc.png")
#plt.legend(bbox_to_anchor=(1, .25), fontsize=12)
plt.show()
