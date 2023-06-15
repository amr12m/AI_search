from tkinter import *
from BFS_ALOG import BFS
from DFS_ALGO import dfs
from UCS_ALGO import ucs
from A_star_ALGO import A_star


root =Tk()
root.title("My_Search")

# Define labels
label1 = Label(root, text=" Start point")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = Label(root, text=" End point")
label2.grid(row=0, column=1, padx=10, pady=10)


# Define radio buttons
var = StringVar()
BFS_rb = Radiobutton(root, text="BFS", variable=var, value="BFS")
BFS_rb.grid(row=2, column=0, padx=10, pady=10)

DFS_rb = Radiobutton(root, text="DFS", variable=var, value="DFS")
DFS_rb.grid(row=3, column=0, padx=10, pady=10)

UCS_rb = Radiobutton(root, text="UCS", variable=var, value="UCS")
UCS_rb.grid(row=4, column=0, padx=10, pady=10)

A_STAR_rb = Radiobutton(root, text="A*", variable=var, value="A*")
A_STAR_rb.grid(row=5, column=0, padx=10, pady=10)

# Define option menus
clicked_1 = StringVar()
option_menu1 = OptionMenu(root,clicked_1, 'Giza','Cairo','October','Madinati','Alshuruq','Aleubur','ShubraAlkhayma','Qalyub','Smadun','Balbis','Sadat','SirsAlliyan','Banha','MinyaAlqamh','Zagzig','Alsharqia','Menouf','ShbeenElkoom','AbuKabir','Alshuada','Tala','Mtgmer','Tanta','KafrElzayat','Shabrakhit','Damanhour','Desouq','KafrElsheikh','AlmahallaAlkubra','Mansoura','Sinbillawain','Abushaqq')
option_menu1.grid(row=1, column=0, padx=10, pady=10)
clicked_2 = StringVar()
option_menu2 = OptionMenu(root, clicked_2, 'Giza','Cairo','October','Madinati','Alshuruq','Aleubur','ShubraAlkhayma','Qalyub','Smadun','Balbis','Sadat','SirsAlliyan','Banha','MinyaAlqamh','Zagzig','Alsharqia','Menouf','ShbeenElkoom','AbuKabir','Alshuada','Tala','Mtgmer','Tanta','KafrElzayat','Shabrakhit','Damanhour','Desouq','KafrElsheikh','AlmahallaAlkubra','Mansoura','Sinbillawain','Abushaqq')
option_menu2.grid(row=1, column=1, padx=10, pady=10)




def choose_algo():
    if var.get() == 'BFS':
        tryimg = BFS(clicked_1.get(),clicked_2.get())
        print(tryimg)

    elif var.get() == 'DFS':
        tryimg = dfs(clicked_1.get(), clicked_2.get())

    elif var.get() == 'UCS':
        tryimg = ucs(clicked_1.get(), clicked_2.get())
    elif var.get() == 'A*':
        tryimg = A_star(clicked_1.get(), clicked_2.get())
   
# Define buttons
button1 = Button(root, text="Run",command=choose_algo)
button1.grid(row=6, column=0, padx=10, pady=10)

button2 = Button(root, text='Exit', command=root.quit)
button2.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
