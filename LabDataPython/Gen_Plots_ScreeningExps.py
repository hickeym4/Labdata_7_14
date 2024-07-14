import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HSMFW_Acc_MI = pd.read_csv("HSMFW_MI_Acclimated_NewHeaders.csv")
HSMFW_Acc_MI = HSMFW_Acc_MI.fillna(0)
HSMFW_Unacc_MI = pd.read_csv("HSMFW_MI_Unacclimated_NewHeaders.csv")
HSMFW_Unacc_MI = HSMFW_Unacc_MI.fillna(0)
Glucose_Surfactant = pd.read_csv("Glucose_Surfactant_NewHeaders.csv")
Glucose_Surfactant = Glucose_Surfactant.fillna(0)


plt.rcParams["font.family"]= "Times New Roman"

######################################
#Not converted to per-gram-substrate
######################################

#COD Calib
# x = 2.0281
# b = .0382
# HSMFW_Unacc_Lo_COD_raw = .110
# HSMFW_Unacc_Hi_COD_raw = .112
# Unacc_Dil = 31
# HSMFW_Acc_Lo_COD_raw = .202
# HSMFW_Acc_Hi_COD_raw = .202
# Acc_Dil = 21

# HSMFW_Acc_Lo_COD_raw = (HSMFW_Acc_Lo_COD_raw*x+b)*Acc_Dil
# HSMFW_Acc_Hi_COD_raw = (HSMFW_Acc_Hi_COD_raw*x+b)*Acc_Dil
# HSMFW_Unacc_Lo_COD_raw = (HSMFW_Unacc_Lo_COD_raw*x+b)*Unacc_Dil
# HSMFW_Unacc_Hi_COD_raw = (HSMFW_Unacc_Hi_COD_raw*x+b)*Unacc_Dil




# HSMFW_Unacc.iloc[:, [3,4,5,6,7]] = HSMFW_Unacc.iloc[:, [3,4,5,6,7]]/HSMFW_Unacc_Lo_COD_raw
# HSMFW_Unacc.iloc[:, [8,9,10,11,12]] = HSMFW_Unacc.iloc[:, [8,9,10,11,12]]/HSMFW_Unacc_Hi_COD_raw
# HSMFW_Acc.iloc[:, [3,4,5,6,7]] = HSMFW_Acc.iloc[:, [3,4,5,6,7]]/HSMFW_Acc_Lo_COD_raw
# HSMFW_Acc.iloc[:, [8,9,10,11]] = HSMFW_Acc.iloc[:, [8,9,10,11]]/HSMFW_Acc_Hi_COD_raw


#HSMFW w/ MI only
HSMFW_Acc_MI["Total (7.64 W/m³)"]=HSMFW_Acc_MI["Butyric (7.64 W/m³)"]+HSMFW_Acc_MI["Acetic (7.64 W/m³)"]+HSMFW_Acc_MI["Caproic (7.64 W/m³)"]
HSMFW_Acc_MI["Total (76.49 W/m³)"]=HSMFW_Acc_MI["Butyric (76.49 W/m³)"]+HSMFW_Acc_MI["Acetic (76.49 W/m³)"]+HSMFW_Acc_MI["Caproic (76.49 W/m³)"]
HSMFW_Unacc_MI["Total (7.64 W/m³)"]=HSMFW_Unacc_MI["Butyric (7.64 W/m³)"]+HSMFW_Unacc_MI["Acetic (7.64 W/m³)"]+HSMFW_Unacc_MI["Isobutyric (7.64 W/m³)"]
HSMFW_Unacc_MI["Total (76.49 W/m³)"]=HSMFW_Unacc_MI["Butyric (76.49 W/m³)"]+HSMFW_Unacc_MI["Acetic (76.49 W/m³)"]+HSMFW_Unacc_MI["Isovaleric (76.49 W/m³)"]+HSMFW_Unacc_MI["Isobutyric (76.49 W/m³)"]


#COMPARE Total
#Acclimated
x1 = HSMFW_Acc_MI["Day"]
x2 = HSMFW_Unacc_MI["Day"]
y = HSMFW_Acc_MI.iloc[:,17]
y2 = HSMFW_Acc_MI.iloc[:,18]
label1_list = HSMFW_Acc_MI.columns[17].split(" (")
label1 = "Acclimated ("+label1_list[1]
label2_list = HSMFW_Acc_MI.columns[18].split(" (")
label2 = "Acclimated ("+label2_list[1]
plt.plot(x1,y,marker='o',color="b",label=label1)
plt.plot(x1,y2,linestyle='--',marker='x',color="b",label=label2)
#Unacclimated
y3 = HSMFW_Unacc_MI.iloc[:,12]
y4 = HSMFW_Unacc_MI.iloc[:,13]
label3_list = HSMFW_Unacc_MI.columns[12].split(" (")
label3 = "Unacclimated ("+label3_list[1]
label4_list = HSMFW_Unacc_MI.columns[13].split(" (")
label4 = "Unacclimated ("+label4_list[1]
plt.plot(x2,y3,marker="o",color='r',label=label3)
plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
#Titles, axis, etc.
# plt.title("Substrate: HSMFW",loc="right")
plt.xlabel("Day")
plt.ylabel("Total VFA's (g/L)")
plt.legend(loc="lower right")
plt.ylim(0,5.5)
plt.xlim(0,6)
# plt.savefig('TotalVFAs_HSMFW_MI_Acc_Unacc.png',dpi=1200)
# plt.show()


#Glucose w/ surfactant
print(Glucose_Surfactant.columns)
# Glucose_Surfactant.iloc[:, [8,9,10,11]] = Glucose_Surfactant.iloc[:, [8,9,10,11]]/Glucose_Surfactant_Init