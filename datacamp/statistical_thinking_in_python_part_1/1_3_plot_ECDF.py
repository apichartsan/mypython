import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
#import ROOT
from ROOT import *
import array as arr

# Create bee swarm plot with Seaborn's default settings
sns.set()

def ecdf(data):
	"""Compute ECDF for a one-dimensional array of measurements."""
	# Number of data points: n
	n = len(data)

	# x-data for the ECDF: x
	x = np.sort(data)
		
	# y-data for the ECDF: y
	y = np.arange(1, n+1) / float(n)
	# The y data of the ECDF go from 1/n to 1 in equally spaced increments. You can construct this using np.arange(). Remember, however, that the end value in np.arange() is not inclusive. Therefore, np.arange() will need to go from 1 to n+1. Be sure to divide this by n
	return x, y


#versicolor_petal_length = np.array([4.7, 4.5, 4.9, 4. , 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4. ,
#									4.7, 3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4. , 4.9, 4.7, 4.3, 4.4,
#									4.8, 5. , 4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1,
#									4. , 4.4, 4.6, 4. , 3.3, 4.2, 4.2, 4.2, 4.3, 3. , 4.1])

df = pd.read_csv('iris.csv')
df['species'].value_counts()
set  = df['species'] == 'setosa'
vers = df['species'] == 'versicolor'
virg = df['species'] == 'virginica'

setosa_petal_length = df[set]['petal_length']
versicolor_petal_length = df[vers]['petal_length']
virginica_petal_length = df[virg]['petal_length']

# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker='.', linestyle='none')
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
_ = plt.plot(x_virg, y_virg, marker='.', linestyle='none')

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()


## plot by using ROOT
#xErr,yErr = [],[]
#nBins = len(x_set)
#for i in range(nBins):
#	xErr  += [0.0]
#	yErr  += [0.0]
#
#gr = TGraphAsymmErrors(nBins, x_set, y_set, arr.array('d',xErr), arr.array('d',xErr), arr.array('d',yErr), arr.array('d',yErr))
#gr.GetYaxis().SetTitle("ECDF")
#gr.GetXaxis().SetTitle("petal length (cm)")
#gr.SetTitle("ECDF of petal length")
#gr.SetMarkerStyle(7)
##gr.GetYaxis().SetNdivisions(520)
##gr.GetXaxis().SetNdivisions(520)
#
#gr2 = TGraphAsymmErrors(nBins, x_vers, y_vers, arr.array('d',xErr), arr.array('d',xErr), arr.array('d',yErr), arr.array('d',yErr))
#gr2.SetMarkerStyle(7)
#gr2.SetLineColor(kBlue)
#gr2.SetMarkerColor(kBlue)
#
#gr3 = TGraphAsymmErrors(nBins, x_virg, y_virg, arr.array('d',xErr), arr.array('d',xErr), arr.array('d',yErr), arr.array('d',yErr))
#gr3.SetMarkerStyle(7)
#gr3.SetLineColor(kRed)
#gr3.SetMarkerColor(kRed)
#
#can1 = TCanvas("can1", "can1", 800, 550)
#can1.cd()
#can1.SetTicks()
#can1.SetGrid()
##//--- TLegend ---
#legend = TLegend(0.7, 0.12, 0.85, 0.3)
##legend.SetX1(0.12)
##legend.SetY1(0.15)
##legend.SetX2(0.3)
##legend.SetY2(0.6)
#legend.SetTextSize(.034)
#legend.SetFillColor(0)
#legend.SetFillStyle(1001)
#legend.SetBorderSize(0)
#legend.AddEntry(gr, "setosa", "pl")
#legend.AddEntry(gr2, "versicolor", "pl")
#legend.AddEntry(gr3, "virginica", "pl")
#
#gr.Draw("ap")
#gr.GetXaxis().SetLimits(0.0,9)
#gr.Draw("ap")
#can1.Update()
#
#gr2.Draw("same p")
#gr3.Draw("same p")
#legend.Draw()
#can1.Print("ECDF.pdf")



