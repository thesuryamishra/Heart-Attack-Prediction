import pickle
x = pickle.load(open("Log_model.sav", "rb"))
y = pickle.load(open("KNN_model.sav", "rb"))
z = pickle.load(open("Decision_Tree_model.sav", "rb"))

print(x.predict([[3, 150, 0, 2.3]]))
print(y.predict([[3, 150, 0, 2.3]]))
print(z.predict([[3, 150, 0, 2.3]]))

from tkinter import *
root = Tk()
l = Label(root, text = x.predict([[3, 150, 0, 2.3]]))
l.pack()
root.mainloop()
print("End of ram!!!")
print("Hiimaja aa gis bhai")