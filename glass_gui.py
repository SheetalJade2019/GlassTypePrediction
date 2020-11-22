import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import preprocessing

df = pd.read_csv("E:\ML\AISS\glass_1_0710\glass.csv")
# print()
# print(df.head(1))
# print()
#df.shape

print(df['Type'].unique())
label_encoder = preprocessing.LabelEncoder()
df['Type'] = label_encoder.fit_transform(df['Type'])
print(df['Type'].unique())
#df.info() .. df.describe()
X = df[["RI","Na","Mg","Al","Si","K","Ca","Ba","Fe"]]
y = df['Type']

from sklearn.preprocessing import MinMaxScaler
mmscalar = MinMaxScaler()
df[["RI","Na","Mg","Al","Si","K","Ca","Ba","Fe"]] = mmscalar.fit_transform(df[["RI","Na","Mg","Al","Si","K","Ca","Ba","Fe"]])

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 50)
classifier.fit(X, y)

# ............ pickle .........
import pickle
Model = pickle.dumps(classifier)

# ............. GUI............

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
canvas1 = tk.Canvas(root, width=500, height=650)
canvas1.pack()
#labels and input boxes

label0 = tk.Label(root,text="GLASS TYPE PREDICTION")
canvas1.create_window(220,30,window=label0)
label0.config(font=("Times",25))


label1 = tk.Label(root,text="RI")
canvas1.create_window(50,100,window=label1)
label1.config(font=("Times",18))

entry1 = tk.Entry(root)
canvas1.create_window(200,100,window=entry1)
entry1.config(font=("Times",18))

label2 = tk.Label(root,text="Na")
canvas1.create_window(50,150,window=label2)
label2.config(font=("Times",18))

entry2 = tk.Entry(root)
canvas1.create_window(200,150,window=entry2)
entry2.config(font=("Times",18))

label3 = tk.Label(root,text="Mg")
canvas1.create_window(50,200,window=label3)
label3.config(font=("Times",18))

entry3 = tk.Entry(root)
canvas1.create_window(200,200,window=entry3)
entry3.config(font=("Times",18))

label4 = tk.Label(root,text="Al")
canvas1.create_window(50,250,window=label4)
label4.config(font=("Times",18))

entry4 = tk.Entry(root)
canvas1.create_window(200,250,window=entry4)
entry4.config(font=("Times",18))

label5= tk.Label(root,text="Si")
canvas1.create_window(50,300,window=label5)
label5.config(font=("Times",18))

entry5 = tk.Entry(root)
canvas1.create_window(200,300,window=entry5)
entry5.config(font=("Times",18))

label6 = tk.Label(root,text="K")
canvas1.create_window(50,350,window=label6)
label6.config(font=("Times",18))

entry6 = tk.Entry(root)
canvas1.create_window(200,350,window=entry6)
entry6.config(font=("Times",18))

label7 = tk.Label(root,text="Ca")
canvas1.create_window(50,400,window=label7)
label7.config(font=("Times",18))

entry7 = tk.Entry(root)
canvas1.create_window(200,400,window=entry7)
entry7.config(font=("Times",18))

label8 = tk.Label(root,text="Ba")
canvas1.create_window(50,450,window=label8)
label8.config(font=("Times",18))

entry8 = tk.Entry(root)
canvas1.create_window(200,450,window=entry8)
entry8.config(font=("Times",18))

label9 = tk.Label(root,text="Fe")
canvas1.create_window(50,500,window=label9)
label9.config(font=("Times",18))

entry9 = tk.Entry(root)
canvas1.create_window(200,500,window=entry9)
entry9.config(font=("Times",18))

# get values RI,Na,Mg,Al,Ca from gui
def values():
    global RI
    RI = float(entry1.get())
    global Na
    Na = float(entry2.get())
    global Mg
    Mg = float(entry3.get())
    global Al
    Al = float(entry4.get())
    global Si
    Si  = float(entry5.get())
    global K
    K  = float(entry6.get())
    global Ca
    Ca  = float(entry7.get())
    global Ba
    Ba  = float(entry8.get())
    global Fe
    Fe  = float(entry9.get())
    test_df = df2 = pd.DataFrame([(RI,Na,Mg,Al,Si,K,Ca,Ba,Fe)],
                  columns=('RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe'))

    res = Model.predict(test_df)

    # "'build wind float'" "'vehic wind float'" 'tableware'
    # "'build wind non-float'" 'headlamps' 'containers']
    if res == 0:
        res = "build wind float"
    elif res == 1 :
        res = "build wind non-float"
    elif res == 2 :
        res = "vehic wind float"
    elif res == 3 :
        res = "containers"
    elif res == 4 :
        res = "headlamps"
    elif res == 5 :
        res = "tableware"
    prediction_res = ("Result :", res)
    label_prediction = tk.Label(root, text=prediction_res, bg="green")
    canvas1.create_window(200,600,window=label_prediction)
    label_prediction.config(font=("Times",18))

button1 = tk.Button(root, text="Predict Glass Type", command=values, bg='blue')
canvas1.create_window(200,550,window=button1)
button1.config(font=("Times",18))

root.mainloop()
