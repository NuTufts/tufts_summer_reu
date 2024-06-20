import os,sys
import ROOT as rt
import numpy as np


# first I need to make some data to histogram

# I will define 3 random normal distributions
# I generated the following code from Claude.ai using the following prompt:
# -------------------------------------------------------------------------
"""
Please provide me example code to draw random values from a normal distribution using numpy. 
I want to define 3 different means and variances to define the distributions. 
I then want to draw 100 examples each. 
I want the 3 means to be within an interval of [0,1]. 
The variances can be draw from an interval of [0,3].
"""
# -------------------------------------------------------------------------
# post output edits
"""
* Replaced 3 with a variable, Ndists, to set number of distributions.
"""
Ndists = 3


#Set random seed for reproducibility
np.random.seed(42)

# Define the number of samples for each distribution
n_samples = 1000

# Generate 3 random means within the interval [0, 1]
means = np.random.uniform(0.2, 0.8, Ndists)

# Generate 3 random variances within the interval [0, 3]
variances = np.random.uniform(np.power(0.05,2), np.power(0.2,2), Ndists)

# Draw samples from the three normal distributions
samples = [np.random.normal(loc=mean, scale=np.sqrt(var), size=n_samples) 
           for mean, var in zip(means, variances)]

# I create a temporary (rewritable) output rootfile to save the histograms
temp = rt.TFile("temp.root","recreate")

# dict keep our histograms. else they will go out of scope in the loop below.
hist_d = {}

# we define 3 histograms for each
for idist,sample in enumerate(samples):
    print("filling dist[",idist,"]: nsamples=",sample.shape[0])
    print("  mean: ",means[idist])
    print("  variance: ",variances[idist])
    print("  sigma: ",np.sqrt(variances[idist]))
    #print(sample)
    hist_d[idist] = rt.TH1F("h%d"%(idist),"distribution %d;"%(idist),20,0,1.0)

    # fill the histogram
    for i in range(n_samples):
        hist_d[idist].Fill( sample[i] )

    print("  Intregral=",hist_d[idist].Integral())

# now make a stacked histogram
# think of it as a container
hs = rt.THStack("hstack","Stack of histograms")
colors = [rt.kRed, rt.kBlue, rt.kMagenta, rt.kCyan, rt.kOrange] # see https://root.cern.ch/doc/master/classTAttFill.html for more about colors
imaxhist = 0
maxvalue = 0.0
for k,hist in hist_d.items():
    #hist.SetFillColor( colors[k%5] )
    if hist.GetMaximum()>maxvalue:
        maxvalue = hist.GetMaximum()
        imaxhist = k
    hist.SetLineColor( colors[k%5]+2 )
    hist.SetLineWidth(2)
    hist.SetFillStyle( 3003 + k%3 ) # see https://root.cern.ch/doc/master/classTAttFill.html for more about fill styles
    hist.SetFillColor( colors[k%5] )
    hs.Add(hist)

# create a canvas to draw to
c1 = rt.TCanvas("c1", "Stacked Histograms", 1600, 600)
c1.Divide(2)

# first panel
c1.cd(1)
hs.Draw()

# second panel
c1.cd(2)
hist_d[imaxhist].Draw("hist")
for k,hist in hist_d.items():
    hist.Draw("histsame")


# update the canvas: this tells ROOT to draw the latest content assigned to the canvas
# what gets assigned? whatever called draw aftrer the canvas was 'activated' upon creation.
c1.Update()

#print("stacked integral: ",hs.Integral())

# pause the program by having it wait for user input before closing up
print("[ENTER] to exit")
input()

print("Writing to temp file")
# write stuff to file
for k,hist in hist_d.items():
    hist.Write()

# we can also write the stacked histogram and even the canvas
hs.Write()
c1.Write()

temp.Close()

print("done")
    


