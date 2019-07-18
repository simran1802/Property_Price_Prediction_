import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.geometry("555x333")
root.title("GUI")

def pred():
    a = int(e1.get())
    b = int(e2.get())
    c = int(e3.get())
    d = int(e4.get())
    predict = int(reg.predict([[a,b,c,d]]))


    print(f"The predicted price is {predict}")
    msg.showinfo("Predicted output!!", f"Prdicted price: {predict}")


lb1 = Label(root,text='Enter square_feet',bg='red')
lb1.pack()
e1 = Entry()
e1.pack()

lb2 = Label(root,text='Enter number of bedrooms')
lb2.pack()
e2 = Entry()
e2.pack()

lb3 = Label(root,text='Enter number of bathrooms')
lb3.pack()
e3 = Entry()
e3.pack()

lb4 = Label(root,text='Enter built year')
lb4.pack()
e4 = Entry()
e4.pack()

btn = Button(text='Predict',command=pred)
btn.pack()

df = pd.read_csv(r'C:\Users\SIMRAN1\Downloads\house-prediction-for-zipcode\80111.csv')
x = df.iloc[:,2:6].values
y = df.iloc[:,1].values

X_train,X_test,Y_train,Y_test = model_selection.train_test_split(x,y,test_size=0.20,random_state=6)
print(len(X_train))
print(len(X_test))
print(len(Y_test))
print(len(Y_train))

reg = LinearRegression()
reg.fit(X_train,Y_train)

Y_predic1 = reg.predict(X_train)
Y_predic2 = reg.predict(X_test)

print(Y_predic1)
print(Y_predic2)

root.mainloop()


