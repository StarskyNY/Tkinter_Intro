from Tkinter import *

window=Tk()


def converter():
	num = e1_input.get()
	kg = int(num) *1000
	grams= int(num) * 2.20462
	ounces = int(num) * 35.274 
	t1.insert(END,kg)
	t2.insert(END,grams)
	t3.insert(END,ounces)

#b1 = Button(window,text="Execute",command=km_to_mi)

Label(window, text="kg").grid(row=0,column=1)
Label(window, text="grams").grid(row=0,column=2)
Label(window, text="pounds").grid(row=0,column=3)
Label(window, text="ounces").grid(row=0,column=4)
#Label(window, text="pounds").grid(column=1)
#Label(window, text="ounces").grid(column=1)

b1= Button(window,text="Convert",command=converter)
b1.grid(row=1,column=0)


t1=Text(window,height=1,width=20)
t1.grid(row=1,column=2)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=3)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=4)

e1_input=StringVar()
e1 = Entry(window,textvariable=e1_input)
e1.grid(row=1,column=1)

#t2=Text(window,height=1,width=20)
#t2.grid(row=0,column=3)



window.mainloop()

#print help(t1.insert)