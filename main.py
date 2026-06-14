import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *


def new_file():
	title = askstring("Name", "Name project:")
	if not title:
		title = "My_project"
	temp = open("temp.prog", "w")
	temp.write("from tkinter import *\napp = Tk()\napp.title(\"{}\")\n".format(title))
	open("name.prog", "w").write(title)


def save_file():
	name = open("name.prog", "r")
	save = asksaveasfilename(title="Save file", defaultextension=".py", initialfile=name.read() + ".py")
	temp = open("temp.prog", "r")
	program = temp.read()
	with open(save, "w") as file:
         file.write(program + "app.mainloop()\n")


def run_file():
	file = askopenfile(title="Open file")
	os.system("start {}" .format(file.name))


def white_theme():
	app.configure(bg="white")
	module_tkinter.configure(bg="white", fg="black")
	create_button.configure(bg="white", fg="black", activebackground="white", activeforeground="black")
	create_text.configure(bg="white", fg="black", activebackground="white", activeforeground="black")
	create_input.configure(bg="white", fg="black", activebackground="white", activeforeground="black")
	create_image.configure(bg="white", fg="black", activebackground="white", activeforeground="black")
	open("theme.prog", "w").write("white")


def black_theme():
	app.configure(bg="black")
	module_tkinter.configure(bg="black", fg="white")
	create_button.configure(bg="purple", fg="white", activebackground="black", activeforeground="white")
	create_text.configure(bg="purple", fg="white", activebackground="black", activeforeground="white")
	create_input.configure(bg="purple", fg="white", activebackground="black", activeforeground="white")
	create_image.configure(bg="purple", fg="white", activebackground="black", activeforeground="white")
	open("theme.prog", "w").write("black")


def button():
	create = Toplevel()
	create.title("Create button")
	create.resizable(0, 0)
	#create.iconbitmap("icon.ico")
	Label(create, text="text:").grid(column=0, row=0)
	text = Entry(create)
	text.grid(column=1, row=0)
	Label(create, text="x:").grid(column=0, row=1)
	x = Entry(create)
	x.grid(column=1, row=1)
	Label(create, text="y:").grid(column=0, row=2)
	y = Entry(create)
	y.grid(column=1, row=2)
	def edit(color):
		choise_color.configure(text=color)
		color = color.lower()
		file = open("color.prog", "w")
		file.write(color)
	choise_color = Menubutton(create, text="Color")
	color_menu = Menu(choise_color, tearoff=0)
	edit("White")
	color_menu.add_command(label="White", command=lambda: edit("White"))
	color_menu.add_command(label="Blue", command=lambda: edit("Blue"))
	color_menu.add_command(label="Green", command=lambda: edit("Green"))
	color_menu.add_command(label="Red", command=lambda: edit("Red"))
	color_menu.add_command(label="Purple", command=lambda: edit("Purple"))
	color_menu.add_command(label="Pink", command=lambda: edit("Pink"))
	color_menu.add_command(label="Yellow", command=lambda: edit("Yellow"))
	choise_color.config(menu=color_menu)
	choise_color.grid(column=0, row=3)
	def func():
		list_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		x_number = list(x.get())
		for a in x_number:
			for b in list_number:
				if a == b:
					break
			else:
				showerror("Error!", "Bad x coordinate!")
				x.delete(0, END)
				x.insert(0, "1")
				break
		y_number = list(y.get())
		for a in y_number:
			for b in list_number:
				if a == b:
					break
			else:
				showerror("Error!", "Bad y coordinate!")
				y.delete(0, END)
				y.insert(0, "1")
				break
		if x.get() == "":
			x.insert(0, "1")
		if y.get() == "":
			y.insert(0, "1")
		color = open("color.prog", "r")
		color = color.read()
		file = open("temp.prog", "a")
		file.write(f"Button(app, text=\"{text.get()}\", bg=\"{color}\", command=lambda: print(\"button pressed\")).place(x={x.get()}, y={y.get()})\n")
		create.withdraw()
		os.remove("color.prog")
	Button(create, text="Continue", command=func).grid(column=0, row=4)


def text():
	create = Toplevel()
	create.title("Create text")
	create.resizable(0, 0)
	#create.iconbitmap("icon.ico")
	Label(create, text="text:").grid(column=0, row=0)
	text = Entry(create)
	text.grid(column=1, row=0)
	Label(create, text="x:").grid(column=0, row=1)
	x = Entry(create)
	x.grid(column=1, row=1)
	Label(create, text="y:").grid(column=0, row=2)
	y = Entry(create)
	y.grid(column=1, row=2)
	def func():
		list_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		x_number = list(x.get())
		for a in x_number:
			for b in list_number:
				if a == b:
					break
			else:
				showerror("Error!", "Bad x coordinate!")
				x.delete(0, END)
				x.insert(0, "1")
				break
		y_number = list(y.get())
		for a in y_number:
			for b in list_number:
				if a == b:
					break
			else:
				showerror("Error!", "Bad y coordinate!")
				y.delete(0, END)
				y.insert(0, "1")
				break
		if x.get() == "":
			x.insert(0, "1")
		if y.get() == "":
			y.insert(0, "1")
		file = open("temp.prog", "a")
		file.write(f"Label(app, text=\"{text.get()}\").place(x={x.get()}, y={y.get()})\n")
		create.withdraw()
	Button(create, text="Continue", command=func).grid(column=0, row=3)


def input():
	create = Toplevel()
	create.title("Create input")
	create.resizable(0, 0)
	#create.iconbitmap("icon.ico")
	Label(create, text="x:").grid(column=0, row=0)
	x = Entry(create)
	x.grid(column=1, row=0)
	Label(create, text="y:").grid(column=0, row=1)
	y = Entry(create)
	y.grid(column=1, row=1)
	def edit(color):
		choise_color.configure(text=color)
		color = color.lower()
		file = open("color.prog", "w")
		file.write(color)
	choise_color = Menubutton(create, text="Color")
	color_menu = Menu(choise_color, tearoff=0)
	edit("White")
	color_menu.add_command(label="White", command=lambda: edit("White"))
	color_menu.add_command(label="Blue", command=lambda: edit("Blue"))
	color_menu.add_command(label="Green", command=lambda: edit("Green"))
	color_menu.add_command(label="Red", command=lambda: edit("Red"))
	color_menu.add_command(label="Purple", command=lambda: edit("Purple"))
	color_menu.add_command(label="Pink", command=lambda: edit("Pink"))
	color_menu.add_command(label="Yellow", command=lambda: edit("Yellow"))
	choise_color.config(menu=color_menu)
	choise_color.grid(column=0, row=2)
	def func():
		list_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		x_number = list(x.get())
		for a in x_number:
			for b in list_number:
				if a == b:
					break
			else:
				showerror("Error!", "Bad x coordinate!")
				x.delete(0, END)
				x.insert(0, "1")
				break
		y_number = list(y.get())
		for a in y_number:
			for b in list_number:
				if a == b:
					break
			else:
				showerror("Error!", "Bad y coordinate!")
				y.delete(0, END)
				y.insert(0, "1")
				break
		if x.get() == "":
			x.insert(0, "1")
		if y.get() == "":
			y.insert(0, "1")
		color = open("color.prog", "r")
		color = color.read()
		file = open("temp.prog", "a")
		file.write(f"Text(app, bg=\"{color}\").place(x={x.get()}, y={y.get()})\n")
		create.withdraw()
		os.remove("color.prog")
	Button(create, text="Continue", command=func).grid(column=0, row=3)


def image():
	create = Toplevel()
	create.title("Create image")
	create.resizable(0, 0)
	# create.iconbitmap("icon.ico")
	file = askopenfile(title="Open file", initialdir="image", defaultextension="png")
	filename = file.name
	Label(create, text="x:").grid(column=0, row=0)
	x = Entry(create)
	x.grid(column=1, row=0)
	Label(create, text="y:").grid(column=0, row=1)
	y = Entry(create)
	y.grid(column=1, row=1)
	def func():
		list_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		x_number = list(x.get())
		for a in x_number:
			for b in list_number:
				if a == b:
					break
			else:
				showerror("Error!", "Bad x coordinate!")
				x.delete(0, END)
				x.insert(0, "1")
				break
		y_number = list(y.get())
		for a in y_number:
			for b in list_number:
				if a == b:
					break
			else:
				showerror("Error!", "Bad y coordinate!")
				y.delete(0, END)
				y.insert(0, "1")
				break
		if x.get() == "":
			x.insert(0, "1")
		if y.get() == "":
			y.insert(0, "1")
		file = open("temp.prog", "a")
		file.write(f"canvas = Canvas(app, width=500, height=500)\ncanvas.place(x={x.get()}, y={y.get()})\nimage = PhotoImage(file=\"{filename}\")\ncanvas.create_image(0, 0, anchor=NW, image=image)\n")
		create.withdraw()
	Button(create, text="Continue", command=func).grid(column=0, row=2)


app = Tk()
if not os.path.exists("temp.prog"):
	new_file()
else:
	question = askyesno("Question!", "Create new file")
	if question:
		new_file()
app.title("Create My Project")
app.geometry("850x900")
# app.iconbitmap("icon.ico")
menu = Menu()
file_menu = Menu()
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Run", command=run_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=app.quit)
menu.add_cascade(label="File", menu=file_menu)
settings_menu = Menu()
settings_theme = Menu()
settings_theme.add_command(label="White", command=white_theme)
settings_theme.add_command(label="Black", command=black_theme)
settings_menu.add_cascade(label="Theme", menu=settings_theme)
menu.add_cascade(label="Settings", menu=settings_menu)
app.config(menu=menu)
module_tkinter = Label(app, text="tkinter", font=("Varanda", 10))
module_tkinter.grid(column=0,  row=0)
create_button = Button(app, text="Create button", command=button)
create_button.grid(column=0, row=1)
create_text = Button(app, text="Create text", command=text)
create_text.grid(column=1, row=1)
create_input = Button(app, text="Create input", command=input)
create_input.grid(column=2, row=1)
create_image = Button(app, text="Create image", command=image)
create_image.grid(column=3, row=1)
if not os.path.exists("theme.prog"):
	file = open("theme.prog", "w")
	file.write("white")
file = open("theme.prog", "r")
file = file.read()
if file == "white":
	white_theme()
elif file == "black":
	black_theme()
else:
	showerror("Error", "bad theme\"{}\"!" .format(file))
	open("theme.prog", "w").write("white")
	white_theme()
app.mainloop()
