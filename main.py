from tkinter import* #import tkinter module

host_path='C:\Windows\System32\drivers\etc\hosts'
ip_address='127.0.0.1'

def block():
	website_list=enter_Website.get(1.0,END)
	Website=list(website_list.split(','))
	with open(host_path,'r+')as host_file:
	 file_content=host_file.read()
	 for web in Website:
	  if web in file_content:
	   display=Label(Window,text='Already Blocked',font='arial')
	   display.place(x=200,y=200)
	  
	  else:
	   host_file.write(ip_address+''+web)
	   Label(Window,text='Blocked',font='arial').place(x=200,y=200)

def unblock():
	website_list=enter_Website.get(1.0,END)
	Website=list(website_list.split(','))
	temp_f=''
	with open(host_path,'r+')as host_file:
	 file_content=host_file.read()
	 for web in Website:
	  if web in file_content:
	   Label(Window,text=web+'Unblocked\n',font='arial').place(x=350,y=200)
	   with open(host_path,'r+')as website_un:
	    for line in website_un:
	     print('Line1:-'+line)
	     if web in line:
	       temp_un=ip_address+''+web
	       line=line.replace(temp_un,'')
	     print('line2:-'+line)
	     temp_f=temp_f+line
	   
	   with open(host_path,'w')as new_file:
	    new_file.write(temp_f)
	    print(temp_f)
	  else:   	   
	    display=Label(Window,text='Already UnBlocked',font='arial')
	    display.place(x=350,y=200)
	   

def close():
	root.destroy()

root=Tk() #predefined class

root.title("My Website")
root.geometry('650x450')
root.maxsize(650,450)
root.minsize(650,450)
Label(root,text="WEBSITE BLOCKER",font="arial 12 bold",fg="red").pack()

Label(root,text="Developed By@Pritimayee:2022",font="arial 10 bold",fg="black").pack(side=BOTTOM)

Label(root,text="Enter Website URL",font="arial 8 bold",fg="red").place(x=5,y=60)
enter_Website=Text(root,height=3,width=50)
enter_Website.place(x=160,y=60)

b1=Button(root,text="Block",font="arial 12 bold",bg="red",fg="white",command=block)
b1.place(x=200,y=150)
b2=Button(root,text="UnBlock",font="arial 12 bold",bg="green",fg="white",command=unblock)
b2.place(x=350,y=150)
b3=Button(root,text="Exit",font="arial 12 bold",bg="blue",fg="white",command=close)
b3.place(x=500,y=150)

root.mainloop()