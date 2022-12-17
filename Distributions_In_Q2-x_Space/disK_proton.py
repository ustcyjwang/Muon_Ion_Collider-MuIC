import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mtl
data_proton = np.genfromtxt('protonKppp.csv', delimiter='\t')
length_proton = int(len(data_proton)/4.0)
print("*****Load proton Successfully!*****")
print("size:", length_proton, "* 4 (eta, pt, Q^2, x)")

proton_theta = data_proton[0: length_proton-1]
proton_pt = data_proton[length_proton: 2*length_proton-1]
proton_Q2 = data_proton[2*length_proton: 3*length_proton-1]
proton_x = data_proton[3*length_proton: 4*length_proton-1]
print("szie of theta:", len(proton_theta), data_proton[2])
print("szie of pt:", len(proton_theta), proton_pt.max())
print("szie of Q^2:", len(proton_theta))
print("szie of x:", len(proton_theta))
df = pd.DataFrame()

proton_theta_rescale = np.pi/2.0 + (np.pi/8.0)*(np.log(np.tan(proton_theta/2.0)))

proton_eta_015w = []
proton_eta_0154 = []
proton_eta_0143 = []
proton_eta_01w3 = []
proton_eta_124w = []
proton_eta_1243 = []
proton_eta_1232 = []
proton_eta_12w2 = []
proton_eta_233w = []
proton_eta_2332 = []
proton_eta_2321 = []
proton_eta_23w1 = []
proton_eta_342w = []
proton_eta_3421 = []
proton_eta_3410 = []
proton_eta_451w = []
proton_eta_4510 = []
proton_eta_w5w1 = []
proton_pt_015w = []
proton_pt_0154 = []
proton_pt_0143 = []
proton_pt_01w3 = []
proton_pt_124w = []
proton_pt_1243 = []
proton_pt_1232 = []
proton_pt_12w2 = []
proton_pt_233w = []
proton_pt_2332 = []
proton_pt_2321 = []
proton_pt_23w1 = []
proton_pt_342w = []
proton_pt_3421 = []
proton_pt_3410 = []
proton_pt_451w = []
proton_pt_4510 = []
proton_pt_w5w1 = []

pt_max = 20

for j in range(length_proton-1):
    if proton_Q2[j]>1 and proton_Q2[j]<10:
        if proton_x[j]<0.00001:
            proton_eta_015w.append(proton_theta_rescale[j])
            proton_pt_015w.append(proton_pt[j])
        elif proton_x[j]<0.0001 and proton_x[j]>0.00001:
            proton_eta_0154.append(proton_theta_rescale[j])
            proton_pt_0154.append(proton_pt[j])
        elif proton_x[j]<0.001 and proton_x[j]>0.0001:
            proton_eta_0143.append(proton_theta_rescale[j])
            proton_pt_0143.append(proton_pt[j])
        else:
            proton_eta_01w3.append(proton_theta_rescale[j])
            proton_pt_01w3.append(proton_pt[j])

    elif proton_Q2[j]>10 and proton_Q2[j]<100:
        if proton_x[j] < 0.0001:
            proton_eta_124w.append(proton_theta_rescale[j])
            proton_pt_124w.append(proton_pt[j])
        elif proton_x[j] < 0.001 and proton_x[j] > 0.0001:
            proton_eta_1243.append(proton_theta_rescale[j])
            proton_pt_1243.append(proton_pt[j])
        elif proton_x[j] < 0.01 and proton_x[j] > 0.001:
            proton_eta_1232.append(proton_theta_rescale[j])
            proton_pt_1232.append(proton_pt[j])
        else:
            proton_eta_12w2.append(proton_theta_rescale[j])
            proton_pt_12w2.append(proton_pt[j])

    elif proton_Q2[j]>100 and proton_Q2[j]<1000:
        if proton_x[j] < 0.001:
            proton_eta_233w.append(proton_theta_rescale[j])
            proton_pt_233w.append(proton_pt[j])
        elif proton_x[j] < 0.01 and proton_x[j] > 0.001:
            proton_eta_2332.append(proton_theta_rescale[j])
            proton_pt_2332.append(proton_pt[j])
        elif proton_x[j] < 0.1 and proton_x[j] > 0.01:
            proton_eta_2321.append(proton_theta_rescale[j])
            proton_pt_2321.append(proton_pt[j])
        else:
            proton_eta_23w1.append(proton_theta_rescale[j])
            proton_pt_23w1.append(proton_pt[j])

    elif proton_Q2[j]>1000 and proton_Q2[j]<10000:
        if proton_x[j] < 0.01:
            proton_eta_342w.append(proton_theta_rescale[j])
            proton_pt_342w.append(proton_pt[j])
        elif proton_x[j] < 0.1 and proton_x[j] > 0.01:
            proton_eta_3421.append(proton_theta_rescale[j])
            proton_pt_3421.append(proton_pt[j])
        else:
            proton_eta_3410.append(proton_theta_rescale[j])
            proton_pt_3410.append(proton_pt[j])

    elif proton_Q2[j]>10000 and proton_Q2[j]<100000:
        if proton_x[j] < 0.1:
            proton_eta_451w.append(proton_theta_rescale[j])
            proton_pt_451w.append(proton_pt[j])
        else:
            proton_eta_4510.append(proton_theta_rescale[j])
            proton_pt_4510.append(proton_pt[j])
    elif proton_Q2[j]>100000:
        proton_eta_w5w1.append(proton_theta_rescale[j])
        proton_pt_w5w1.append(proton_pt[j])

proton_theta_select = []
proton_pt_select = []

rbins = np.linspace(0, np.log10(pt_max), 120)
abins = np.linspace(0, 2*np.pi, 120)

h2d015w, _, _ = np.histogram2d(proton_eta_015w, proton_pt_015w, bins=(abins, np.power(10, rbins)))
h2d0154, _, _ = np.histogram2d(proton_eta_0154, proton_pt_0154, bins=(abins, np.power(10, rbins)))
h2d0143, _, _ = np.histogram2d(proton_eta_0143, proton_pt_0143, bins=(abins, np.power(10, rbins)))
h2d01w3, _, _ = np.histogram2d(proton_eta_01w3, proton_pt_01w3, bins=(abins, np.power(10, rbins)))
h2d124w, _, _ = np.histogram2d(proton_eta_124w, proton_pt_124w, bins=(abins, np.power(10, rbins)))
h2d1243, _, _ = np.histogram2d(proton_eta_1243, proton_pt_1243, bins=(abins, np.power(10, rbins)))
h2d1232, _, _ = np.histogram2d(proton_eta_1232, proton_pt_1232, bins=(abins, np.power(10, rbins)))
h2d12w2, _, _ = np.histogram2d(proton_eta_12w2, proton_pt_12w2, bins=(abins, np.power(10, rbins)))
h2d233w, _, _ = np.histogram2d(proton_eta_233w, proton_pt_233w, bins=(abins, np.power(10, rbins)))
h2d2332, _, _ = np.histogram2d(proton_eta_2332, proton_pt_2332, bins=(abins, np.power(10, rbins)))
h2d2321, _, _ = np.histogram2d(proton_eta_2321, proton_pt_2321, bins=(abins, np.power(10, rbins)))
h2d23w1, _, _ = np.histogram2d(proton_eta_23w1, proton_pt_23w1, bins=(abins, np.power(10, rbins)))
h2d342w, _, _ = np.histogram2d(proton_eta_342w, proton_pt_342w, bins=(abins, np.power(10, rbins)))
h2d3421, _, _ = np.histogram2d(proton_eta_3421, proton_pt_3421, bins=(abins, np.power(10, rbins)))
h2d3410, _, _ = np.histogram2d(proton_eta_3410, proton_pt_3410, bins=(abins, np.power(10, rbins)))
h2d451w, _, _ = np.histogram2d(proton_eta_451w, proton_pt_451w, bins=(abins, np.power(10, rbins)))
h2d4510, _, _ = np.histogram2d(proton_eta_4510, proton_pt_4510, bins=(abins, np.power(10, rbins)))
h2dw5w1, _, _ = np.histogram2d(proton_eta_w5w1, proton_pt_w5w1, bins=(abins, np.power(10, rbins)))

rtick = [0, 1, 2]
rname = [1, 10, 100]
etaname = [4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, 7, 6, 5]
etatick = [0, np.pi/8, 2*np.pi/8, 3*np.pi/8, 4*np.pi/8, 5*np.pi/8, 6*np.pi/8, 7*np.pi/8, 8*np.pi/8, 9*np.pi/8, 10*np.pi/8, 11*np.pi/8, 12*np.pi/8, 13*np.pi/8, 14*np.pi/8, 15*np.pi/8]
nonename = []
A, R = np.meshgrid(abins, rbins)
fig, ax = plt.subplots(6, 6, subplot_kw=dict(polar=True))
plt.subplots_adjust(wspace=0, hspace=0.1)
maxcolor = 100
alphapara = 0.2

ax[5, 0].pcolor(A, R, h2d015w.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[5, 0])
ax[5, 0].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[5, 1].pcolor(A, R, h2d0154.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[5, 1])
ax[5, 1].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[5, 2].pcolor(A, R, h2d0143.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[5, 2])
ax[5, 2].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[5, 3].pcolor(A, R, h2d01w3.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[5, 3])
ax[5, 3].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[4, 1].pcolor(A, R, h2d124w.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[4, 1])
ax[4, 1].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[4, 2].pcolor(A, R, h2d1243.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[4, 2])
ax[4, 2].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[4, 3].pcolor(A, R, h2d1232.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[4, 3])
ax[4, 3].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[4, 4].pcolor(A, R, h2d12w2.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[4, 4])
ax[4, 4].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)

ax[3, 2].pcolor(A, R, h2d233w.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[3, 2])
ax[3, 2].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[3, 3].pcolor(A, R, h2d2332.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[3, 3])
ax[3, 3].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[3, 4].pcolor(A, R, h2d2321.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[3, 4])
ax[3, 4].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[3, 5].pcolor(A, R, h2d23w1.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[3, 5])
ax[3, 5].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)

ax[2, 3].pcolor(A, R, h2d342w.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[2, 3])
ax[2, 3].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[2, 4].pcolor(A, R, h2d3421.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[2, 4])
ax[2, 4].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[2, 5].pcolor(A, R, h2d3410.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[2, 5])
ax[2, 5].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)

ax[1, 4].pcolor(A, R, h2d451w.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[1, 4])
ax[1, 4].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)
ax[1, 5].pcolor(A, R, h2d4510.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[1, 5])
ax[1, 5].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)

ax[0, 5].pcolor(A, R, h2dw5w1.T, norm=mtl.colors.LogNorm(vmin=1, vmax=maxcolor))
plt.sca(ax[0, 5])
ax[0, 5].grid(True, alpha=alphapara)
plt.yticks(rtick, nonename)
plt.xticks(etatick, nonename)

plt.sca(ax[0, 0])
plt.axis('off')
plt.sca(ax[0, 1])
plt.axis('off')
plt.sca(ax[0, 2])
plt.axis('off')
plt.sca(ax[0, 3])
plt.axis('off')
plt.sca(ax[0, 4])
plt.axis('off')
plt.sca(ax[1, 0])
plt.axis('off')
plt.sca(ax[1, 1])
plt.axis('off')
plt.sca(ax[1, 2])
plt.axis('off')
plt.sca(ax[1, 3])
plt.axis('off')
plt.sca(ax[2, 0])
plt.axis('off')
plt.sca(ax[2, 1])
plt.axis('off')
plt.sca(ax[2, 2])
plt.axis('off')
plt.sca(ax[3, 0])
plt.axis('off')
plt.sca(ax[3, 1])
plt.axis('off')
plt.sca(ax[4, 0])
plt.axis('off')
plt.sca(ax[5, 4])
plt.axis('off')
plt.sca(ax[5, 5])
plt.axis('off')
plt.sca(ax[4, 5])
plt.axis('off')

plt.show()