import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# data = pd.read_csv("Glu_Unacc_16s.csv")
# sample_list = ['Glu_D0', 'Glu_70 RPM_D2', 'Glu_70 RPM_D5', 'Glu_70 RPM_D9','Glu_400 RPM_D2','Glu_400 RPM_D5', 'Glu_400 RPM_D9']
# data = data.drop(columns = ['int.slv.Species','int.slv.cnf','int.slv.lws.txn','int.slv.lws.lvl'])
data = pd.read_csv("master.table.clean_rel.csv")
data_2 = pd.read_csv("master.table.clean_abs.csv")

#organize sample list key
key = pd.read_csv("metadata-filtered.csv")
key = key.iloc[3:]
key = key.iloc[:-1]

#MFW samples
# sample_list = ["S90","S77","S81","S93","S86","S78","S79"]
#GH1 samples
#S91 is end of acclimation, matches == day 0
sample_list = ["S85","S82","S92","S80","S83"]




threshold=.01
df = pd.DataFrame()


for i in sample_list:
    newcol = str(i)+" MC?"
    df['Genus']=data.groupby(['int.slv.Genus'], as_index=False)[i].sum()['int.slv.Genus']
    df[i] = data.groupby(['int.slv.Genus'], as_index=False)[i].sum()[i] 
    df[newcol]=(df[i]/df[i]).where(df[i]>threshold,0)
sample_list_ = [name + " MC?" for name in sample_list]
print(sample_list_)
df["Any_Meet_Criteria?"] = (df[sample_list_[0]]-df[sample_list_[0]]+1).where((df[sample_list_[0]]==1)|(df[sample_list_[1]]==1)|(df[sample_list_[2]]==1)|\
                                              (df[sample_list_[3]]==1)|(df[sample_list_[4]]==1)|(df[sample_list_[4]]==1)|(df[sample_list_[4]]==1)|\
                                               (df[sample_list_[4]]==1))
# df.to_csv("check_16s.csv")
df=df[df["Any_Meet_Criteria?"]==1]
# All samples
sample_list.insert(0,"Genus")
df = df[sample_list]
#Organize to each experiment
#Glucose, acclimated

df.to_csv("MFW_Acc_Filtered_16s.csv")


#Plotting
#GH1
plt.rcParams["figure.figsize"] = (18,7)
index_ = df["Genus"]
df.index = index_
df = df.drop(columns="Genus")
dft = df.transpose()
print(dft)
dft = dft[dft.columns].apply(pd.to_numeric)
dft["Other"] = 1- dft[list(dft.columns)].sum(axis=1)
#change below code if unclutured or unassigned is included
dft["Other/Uncultured/Unassigned"] = dft["Other"]
dft = dft.drop(columns = ['Other'])
dft["Check"] = dft[list(dft.columns)].sum(axis=1)
print(dft)
#(0.37 W/m³)","Day 5 (67.92 W/m³)"
dft["Sample"] = ["Day 0","Day 2","Day 2","Day 5","Day 5"]
y1, y2 = dft[dft.columns[1]], dft[dft.columns[2]]

plt.rcParams["font.family"]= "Times New Roman"
plt.rcParams["font.size"] = 8

dft = dft.drop(columns="Check")
event_colours = plt.cm.rainbow(np.linspace(0,1,num=3))
event_colours_2 = plt.cm.rainbow(np.linspace(0,0.8,num=9))
# event_colours[-3]=event_colours[-2]
event_colours[-1]=event_colours_2[-1]
event_colours[-3]=event_colours_2[-8]
ax = dft.plot(x='Sample',kind='bar',stacked=True,rot=0,color=event_colours)
sec = ax.secondary_xaxis(location=0)
sec.set_xticks([1,2,3,4],labels=['\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³'])
sec.tick_params('x',length=0,width=0)
sec2 = ax.secondary_xaxis(location=0)
sec2.set_xticks([-0.5,0.5,2.5,6.5])
sec2.tick_params('x',length=40,width=0.75)


for c in ax.containers:
    labels=[round(v.get_height(),2) if v.get_height() >0.11 else '' for v in c]
    ax.bar_label(c,labels=labels, label_type='center')
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
plt.subplots_adjust(right=0.6)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.22)
plt.ylabel("Relative Abundance")
plt.xlabel("")


plt.savefig('16s_Glucose_Acc.png',dpi=1200)
plt.show()
# #H1
# plt.rcParams["figure.figsize"] = (18,7)
# index_ = df["Genus"]
# df.index = index_
# df = df.drop(columns="Genus")
# dft = df.transpose()
# dft = dft[dft.columns].apply(pd.to_numeric)
# dft["Other"] = 1- dft[list(dft.columns)].sum(axis=1)
# #change below code if unclutured or unassigned is included
# dft["Other/Uncultured/Unassigned"] = dft["Other"]+dft["Unassigned"]+dft["uncultured"]
# dft = dft.drop(columns = ['Other'])
# dft = dft.drop(columns = ['Unassigned'])
# dft = dft.drop(columns = ['uncultured'])
# dft["Check"] = dft[list(dft.columns)].sum(axis=1)
# #(0.37 W/m³)","Day 5 (67.92 W/m³)"
# dft["Sample"] = ["Day 0","Day 2","Day 2","Day 4","Day 4","Day 8","Day 8"]
# y1, y2,y3, y4,y5, y6,y7, y8,y9, y10 = dft[dft.columns[1]], dft[dft.columns[2]],dft[dft.columns[3]], dft[dft.columns[4]],dft[dft.columns[5]], dft[dft.columns[6]],\
# dft[dft.columns[7]], dft[dft.columns[8]],dft[dft.columns[9]], dft[dft.columns[10]]

# plt.rcParams["font.family"]= "Times New Roman"
# plt.rcParams["font.size"] = 8

# dft = dft.drop(columns="Check")
# ax = dft.plot(x='Sample',kind='bar',stacked=True,rot=0)
# sec = ax.secondary_xaxis(location=0)
# sec.set_xticks([1,2,3,4,5,6],labels=['\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³'],rotation=0)
# sec.tick_params('x',length=0,width=0)
# sec2 = ax.secondary_xaxis(location=0)
# sec2.set_xticks([-0.5,0.5,2.5,4.5])
# sec2.tick_params('x',length=40,width=0.75)


# for c in ax.containers:
#     labels=[round(v.get_height(),2) if v.get_height() >0.09 else '' for v in c]
#     ax.bar_label(c,labels=labels, label_type='center')
# handles, labels = plt.gca().get_legend_handles_labels()
# plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
# plt.subplots_adjust(right=0.6)
# plt.xticks(rotation=45)
# plt.subplots_adjust(bottom=0.22)
# plt.ylabel("Relative Abundance")
# plt.xlabel("")
# plt.savefig('16s_MFW_acc.png',dpi=1200)

plt.show()
