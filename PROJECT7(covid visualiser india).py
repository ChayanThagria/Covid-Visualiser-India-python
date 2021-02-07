import requests
import json
from tkinter import *

root = Tk()
root.title("Covid Visualiser")

l1 = Label(root,text ="Total active cases- ")
l1.grid(row = 0,column = 1)
l2 = Label(root,text ="Total confirmed cases- ")
l2.grid(row = 1,column = 1)
l3 = Label(root,text ="")
l3.grid(row = 3,column = 1)

def click():
    url = r"https://api.covid19india.org/data.json"
    page = requests.get(url)
    data = json.loads(page.text)

    l1.configure(text="Total active cases - " + data["statewise"][0]["active"])
    l2.configure(text="Total confirmed cases - " + data["statewise"][0]["confirmed"])
    l3.configure(text="Data refreshed")

b1= Button(root,text = "refresh",command = click)
b1.grid(row = 0,column = 2)

root.mainloop()