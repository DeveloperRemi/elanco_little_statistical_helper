from methods import methodsss as mthds
import requests
import json
from tkinter import *

#initialization of output box
master = Tk()
master.title('ELANCO LITTLE STATISTICAL HELPER')
master.geometry("670x750")

#publicly accessible variable
labels = []

#crearing output box method
def clear():
		for label in labels:
			label.destroy()

		del labels[:]

#dropdown RESOURCES list
OPTIONS = mthds.send_request_res()

variable_res = StringVar(master)
variable_res.set('Resources') # default value
w = OptionMenu(master, variable_res, *OPTIONS)
w.pack()
w.place(relx=0.2, rely=0.01, anchor=N)

#dropdown APPLICATIONS list
OPTIONS2 = mthds.send_request_apps()

variable_apps = StringVar(master)
variable_apps.set('Applications') # default value
v = OptionMenu(master, variable_apps, *OPTIONS2)
v.pack()
v.place(relx=0.53, rely=0.01, anchor=N)

#dropdown TOPS list
OPTIONS3 = mthds.top_tens

variable_top_tens = StringVar(master)
variable_top_tens.set('Top tens') # default value
w = OptionMenu(master, variable_top_tens, *OPTIONS3)
w.pack()
w.place(relx=0.83, rely=0.01, anchor=N)




# OK button
# when OK is pressed VAR = pressed/selected value
def ok():
	latest_op_one = variable_res.get()
	latest_op_two = variable_apps.get()
	latest_op_three = variable_top_tens.get()
	
	#Check which of the dropdown lists were selected
	#if RESOURCES list
	if latest_op_one != "Resources":
		var = latest_op_one
		urrl = "https://engineering-task.elancoapps.com/api/resources/" + var
		response_url = requests.get(urrl)
		data = response_url.text
		lst = json.loads(data)

		if  len(labels) == 0:
			my_label = Label(text=var + "\n\nTotal cost: " + str(mthds.total_cost(lst)) + "\nAverage cost: " + str(mthds.average_cost(lst)) + "\nDate frame: " + str(mthds.time_frame(lst)[0]) + " - " + str(mthds.time_frame(lst)[1]) + "\nTop location: " + mthds.location_counter(lst))
			my_label.pack(pady=(100,0), side=TOP, anchor=NW)
		else:
			my_label = Label(text=var + "\n\nTotal cost: " + str(mthds.total_cost(lst)) + "\nAverage cost: " + str(mthds.average_cost(lst)) + "\nDate frame: " + str(mthds.time_frame(lst)[0]) + " - " + str(mthds.time_frame(lst)[1]) + "\nTop location: " + mthds.location_counter(lst))
			my_label.pack(pady=24, side=TOP, anchor=NW)
	
	#if APPLICATIONS list
	elif latest_op_two != "Applications":
		var = latest_op_two
		urrl = "https://engineering-task.elancoapps.com/api/applications/" + var
		response_url = requests.get(urrl)
		data = response_url.text
		lst = json.loads(data)

		if  len(labels) == 0:
			my_label = Label(text=var + "\n\nTotal cost: " + str(mthds.total_cost(lst)) + "\nAverage cost: " + str(mthds.average_cost(lst)) + "\nConsumed quantity: " + str(mthds.consumed_quantity(lst)) + "\nDate frame: " + str(mthds.time_frame(lst)[0]) + " - " + str(mthds.time_frame(lst)[1]) + "\nTop location: " + mthds.location_counter(lst))
			my_label.pack(pady=(100,0), side=TOP, anchor=NW)
		else:
			my_label = Label(text=var + "\n\nTotal cost: " + str(mthds.total_cost(lst)) + "\nAverage cost: " + str(mthds.average_cost(lst)) + "\nConsumed quantity: " + str(mthds.consumed_quantity(lst)) + "\nDate frame: " + str(mthds.time_frame(lst)[0]) + " - " + str(mthds.time_frame(lst)[1]) + "\nTop location: " + mthds.location_counter(lst))
			my_label.pack(pady=24, side=TOP, anchor=NW)
	
	#if TOP TENS list
	else:
		var = latest_op_three
		if  len(labels) == 0:			
			my_label = Label(text=var +"\n\n" + mthds.which_top_selection(var))
			my_label.pack(pady=(100,0), side=TOP, anchor=NW)
		else:
			my_label = Label(text=var +"\n\n" + mthds.which_top_selection(var))
			my_label.pack(pady=24, side=TOP, anchor=NW)
	

	

	#update publicly accesible list 'labels'
	labels.append(my_label)

	#set all dropdown lists to default position
	variable_res.set('Resources')
	variable_apps.set('Applications')
	variable_top_tens.set('Top tens')
	
	
#OK button
OKbutton = Button(master, text="OK", command=ok)
OKbutton.pack(pady=20, padx=20)
OKbutton.config(height=1, width=8)
OKbutton.place(relx=0.42, rely=0.08, anchor=N)

#Clear button
Clearbutton = Button(master, text="CLEAR", command=clear)
Clearbutton.pack(pady=20 ,padx=20)
Clearbutton.config(height=1, width=8)
Clearbutton.place(relx=0.55, rely=0.08, anchor=N)

#start ant loop through the program
mainloop()
