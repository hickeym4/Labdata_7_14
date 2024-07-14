import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

MFW_MI_Acc = pd.read_csv("HSMFW_MI_Acclimated_NewHeaders.csv")
MFW_MI_Acc = MFW_MI_Acc.fillna(0)
MFW_MI_Acc["Day"] = round(MFW_MI_Acc["Day"],1)
MFW_MI_Unacc = pd.read_csv("HSMFW_MI_Unacclimated_NewHeaders.csv")
MFW_MI_Unacc = MFW_MI_Unacc.fillna(0)
MFW_MI_Unacc["Day"] = round(MFW_MI_Unacc["Day"],1)
plt.rcParams["font.family"]= "Times New Roman"

def Insert_row_(row_number, df, row_value):
    df1 = df[0:row_number]
    df2 = df[row_number:]
    df1.loc[row_number]=row_value
    df_result = pd.concat([df1, df2])
    df_result.index = [*range(df_result.shape[0])]
    return df_result

# #Acclimated run
# #Rearrange dataframe for bar charts
# MFW_MI_Acc_1 = MFW_MI_Acc[MFW_MI_Acc.columns[1:9]]
# MFW_MI_Acc_1 = MFW_MI_Acc_1.rename(columns={'Glucose (0.364 W/m³)': 'Glucose', 'Acetic (0.364 W/m³)': 'Acetic','Butyric (0.364 W/m³)': 'Butyric', 'Caproic (0.364 W/m³)': 'Caproic','Ethanol (0.364 W/m³)': 'Ethanol','Lactic (0.364 W/m³)': 'Lactic'})
# MFW_MI_Acc_2 = MFW_MI_Acc[MFW_MI_Acc.columns[9:14]]
# MFW_MI_Acc_2 = MFW_MI_Acc_2.rename(columns={'Glucose (67.9138 W/m³)': 'Glucose', 'Acetic (67.9138 W/m³)': 'Acetic','Butyric (67.9138 W/m³)': 'Butyric', 'Caproic (67.9138 W/m³)': 'Caproic','Ethanol (67.9138 W/m³)': 'Ethanol'})
# MFW_MI_Acc_2["Hour"] = MFW_MI_Acc_1["Hour"]
# MFW_MI_Acc_2["Day"] = MFW_MI_Acc_1["Day"]
# MFW_MI_Acc_2["Lactic"]=0
# MFW_MI_Acc_2 = MFW_MI_Acc_2[["Hour","Day","Glucose","Acetic","Butyric","Caproic","Lactic","Ethanol"]]
# MFW_MI_Acc_1 = MFW_MI_Acc_1[["Hour","Day","Glucose","Acetic","Butyric","Caproic","Lactic","Ethanol"]]
# #Day 1.6 is right after glucose depletion
# #Day 5 is when caproate starts at low RPM
# #create two possibilities, one with hour as x category and other with day as x category
# #Day
# # index_ = MFW_MI_Acc_1["Day"]
# # MFW_MI_Acc_1.index = index_
# # MFW_MI_Acc_1 = MFW_MI_Acc_1.drop(columns="Day")
# MFW_MI_Acc_1 = MFW_MI_Acc_1.drop(columns="Hour")
# MFW_MI_Acc_2 = MFW_MI_Acc_2.drop(columns="Hour")
# MFW_MI_Acc_1 = MFW_MI_Acc_1.drop(columns="Glucose")
# MFW_MI_Acc_2 = MFW_MI_Acc_2.drop(columns="Glucose")
# # dft_acc_1 = MFW_MI_Acc_1.transpose()
# MFW_MI_Acc= MFW_MI_Acc_1.where((MFW_MI_Acc_1["Day"]==1.6)|(MFW_MI_Acc_1["Day"]==4.8)|(MFW_MI_Acc_1["Day"]==8.8))
# MFW_MI_Acc_2= MFW_MI_Acc_2.where((MFW_MI_Acc_2["Day"]==1.6)|(MFW_MI_Acc_2["Day"]==4.8)|(MFW_MI_Acc_2["Day"]==8.8))
# Time_Zero = MFW_MI_Acc_1.where(MFW_MI_Acc_1["Day"]==0)
# MFW_MI_Acc=MFW_MI_Acc.dropna()
# MFW_MI_Acc_2=MFW_MI_Acc_2.dropna()
# # Function to insert row in the dataframe
# #Combine dataframes
# MFW_MI_Acc = Insert_row_(1, MFW_MI_Acc, MFW_MI_Acc_2.iloc[0])
# MFW_MI_Acc = Insert_row_(3, MFW_MI_Acc, MFW_MI_Acc_2.iloc[1])
# MFW_MI_Acc = Insert_row_(5, MFW_MI_Acc, MFW_MI_Acc_2.iloc[2])
# MFW_MI_Acc = Insert_row_(0, MFW_MI_Acc, Time_Zero.iloc[0])
# MFW_MI_Acc=MFW_MI_Acc.fillna(0)
# MFW_MI_Acc["Sample"] = ["Time 0","Day 2","Day 2","Day 5","Day 5","Day 9","Day 9"]
# MFW_MI_Acc=MFW_MI_Acc.drop(columns="Day")
# #Generate plot
# event_colours = plt.cm.rainbow(np.linspace(0,1,num = 6))
# # event_colours[-7] = (1,0.2,0.3,0.6)
# # event_colours[-5] = (0.1,0.1,0.1,0.1)
# # event_colours[-3] = (0.5,0.5,0.8,0.8)
# ax = MFW_MI_Acc.plot(x='Sample',kind='bar',stacked=True,rot=0,figsize=(12,5))
# sec = ax.secondary_xaxis(location=0)
# sec.set_xticks([0,1,2,3,4,5,6],labels=['','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³'])
# sec.tick_params('x',length=0,width=0)
# sec2 = ax.secondary_xaxis(location=0)
# sec2.set_xticks([-0.5,0.5,2.5,4.5,6.5])
# sec2.tick_params('x',length=60,width=0.75)
# for c in ax.containers:
#     labels=[round(v.get_height(),2) if v.get_height() >0.12 else '' for v in c]
#     ax.bar_label(c,labels=labels, label_type='center')
# handles, labels = plt.gca().get_legend_handles_labels()
# plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
# plt.subplots_adjust(right=0.6)
# plt.xticks(rotation=45)
# plt.subplots_adjust(bottom=0.22)
# plt.ylabel("Yield (g/g COD Fed)")
# plt.title("Acclimated Inoculum", loc="left")
# plt.xlabel("")
# plt.savefig('Glucose_Acc_VFA_Bar.png',dpi=1200)
# plt.show()

#Unacclimated run
# Rearrange dataframe for bar charts
MFW_MI_Unacc_1 = MFW_MI_Unacc[MFW_MI_Unacc.columns[1:7]]
# MFW_MI_Unacc_1 = MFW_MI_Unacc_1.rename(columns={'Glucose (0.37 W/m³)': 'Glucose', 'Acetic (0.37 W/m³)': 'Acetic','Butyric (0.37 W/m³)': 'Butyric', 'Caproic (0.37 W/m³)': 'Caproic','Lactic (0.37 W/m³)': 'Lactic'})
MFW_MI_Unacc_2 = MFW_MI_Unacc[MFW_MI_Unacc.columns[7:12]]
# MFW_MI_Unacc_2 = MFW_MI_Unacc_2.rename(columns={'Glucose (67.92 W/m³)': 'Glucose', 'Acetic (67.92 W/m³)': 'Acetic','Butyric (67.92 W/m³)': 'Butyric', 'Caproic (67.92 W/m³)': 'Caproic'})
MFW_MI_Unacc_2["Hour"] = MFW_MI_Unacc_1["Hour"]
MFW_MI_Unacc_2["Day"] = MFW_MI_Unacc_1["Day"]
# MFW_MI_Unacc_2 = MFW_MI_Unacc_2[["Hour","Day","Glucose","Acetic","Butyric","Caproic"]]
# MFW_MI_Unacc_2["Lactic"] = 0
#Day 1.7 is right after glucose depletion
#Day 4.5 is when caproate starts at low RPM
#create two possibilities, one with hour as x category and other with day as x category
#Day
# MFW_MI_Acc_1 = MFW_MI_Acc_1.drop(columns="Day")
MFW_MI_Unacc_1 = MFW_MI_Unacc_1.drop(columns="Hour")
MFW_MI_Unacc_2 = MFW_MI_Unacc_2.drop(columns="Hour")
# MFW_MI_Unacc_1 = MFW_MI_Unacc_1.drop(columns="Glucose")
# MFW_MI_Unacc_2 = MFW_MI_Unacc_2.drop(columns="Glucose")
# # dft_acc_1 = MFW_MI_Acc_1.transpose()
MFW_MI_Unacc= MFW_MI_Unacc_1.where((MFW_MI_Unacc_1["Day"]==0.9)|(MFW_MI_Unacc_1["Day"]==4.8)|(MFW_MI_Unacc_1["Day"]==4.8))
MFW_MI_Unacc_2= MFW_MI_Unacc_2.where((MFW_MI_Unacc_2["Day"]==0.9)|(MFW_MI_Unacc_2["Day"]==4.8)|(MFW_MI_Unacc_2["Day"]==4.8))
MFW_MI_Unacc=MFW_MI_Unacc.astype('float32')
MFW_MI_Unacc_2=MFW_MI_Unacc_2.astype('float32')
Time_Zero = MFW_MI_Unacc_1.where(MFW_MI_Unacc_1["Day"]==0)
MFW_MI_Unacc=MFW_MI_Unacc.dropna()
MFW_MI_Unacc_2=MFW_MI_Unacc_2.dropna()
# # Function to insert row in the dataframe
# #Combine dataframes

MFW_MI_Unacc = Insert_row_(1, MFW_MI_Unacc, MFW_MI_Unacc_2.iloc[0])
print(MFW_MI_Unacc)
MFW_MI_Unacc = Insert_row_(3, MFW_MI_Unacc, MFW_MI_Unacc_2.iloc[1])
MFW_MI_Unacc = Insert_row_(0, MFW_MI_Unacc, Time_Zero.iloc[0])
MFW_MI_Unacc=MFW_MI_Unacc.fillna(0)
MFW_MI_Unacc["Sample"] = ["Day 0","Day 1","Day 1","Day 5","Day 5"]
MFW_MI_Unacc=MFW_MI_Unacc.drop(columns="Day")
# #Generate plot
# event_colours = plt.cm.rainbow(np.linspace(0,1,num = 6))
# # event_colours[-7] = (1,0.2,0.3,0.6)
# # event_colours[-5] = (0.1,0.1,0.1,0.1)
# # event_colours[-3] = (0.5,0.5,0.8,0.8)
ax = MFW_MI_Unacc.plot(x='Sample',kind='bar',stacked=True,rot=0,figsize=(11,5))
sec = ax.secondary_xaxis(location=0)
sec.set_xticks([0,1,2,3,4,5,6],labels=['','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³'])
sec.tick_params('x',length=0,width=0)
sec2 = ax.secondary_xaxis(location=0)
sec2.set_xticks([-0.5,0.5,2.5,4.5,6.5])
sec2.tick_params('x',length=60,width=0.75)
for c in ax.containers:
    labels=[round(v.get_height(),2) if v.get_height() >0.03 else '' for v in c]
    ax.bar_label(c,labels=labels, label_type='center')
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
plt.subplots_adjust(right=0.6)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.22)
plt.ylabel("Yield (g/g COD Fed)")
plt.title("Unacclimated Inoculum", loc="left")
plt.xlabel("")
plt.savefig('HSMFW_MI_Unacc_VFA_Bar.png',dpi=1200)
plt.show()