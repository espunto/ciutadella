from tkinter import *
from tkinter import messagebox

def check():
    answers = ["gargallo","книгa","журaвль","historiador","hulla","aquarium","пaмятник","сaпог","три"]
    words = [[grid[0][2].get(),grid[5][2].get(),grid[6][2].get(),grid[7][2].get(),grid[11][2].get(),
    grid[15][2].get(),grid[16][2].get(),grid[26][2].get()],[grid[1][2].get(),grid[2][2].get(),grid[3][2].get(),grid[4][2].get(),grid[5][2].get()],
    [grid[8][2].get(),grid[9][2].get(),grid[10][2].get(),grid[11][2].get(),grid[12][2].get(),grid[13][2].get(),
    grid[14][2].get()],[grid[17][2].get(),grid[18][2].get(),grid[19][2].get(),grid[20][2].get(),
    grid[21][2].get(),grid[22][2].get(),grid[23][2].get(),grid[24][2].get(),grid[25][2].get(),
    grid[26][2].get(),grid[27][2].get()],[grid[17][2].get(),grid[28][2].get(),grid[30][2].get(),grid[32][2].get(),
    grid[42][2].get()],[grid[24][2].get(),grid[29][2].get(),grid[31][2].get(),grid[34][2].get(),grid[46][2].get(),
    grid[48][2].get(),grid[50][2].get(),grid[51][2].get()],[grid[33][2].get(),grid[34][2].get(),
    grid[35][2].get(),grid[36][2].get(),grid[37][2].get(),grid[38][2].get(),grid[39][2].get(),grid[40][2].get()],
    [grid[41][2].get(),grid[42][2].get(),grid[43][2].get(),grid[44][2].get(),grid[45][2].get()],[grid[37][2].get(),
    grid[47][2].get(),grid[49][2].get()]]
    false = 0
    for i in range(0,len(answers)):
        b = "".join(words[i])
        b.replace("а","a")
        names[i][3].config(bg="green")
        if b != answers[i]:
            names[i][3].config(bg="red")
            false = 1
    if false == 0:
        messagebox.showinfo(message="Вы победили!")
def time():
    global min
    timeLabel.config(text=str(min))
    min += 1
    root.after(1000,time)

root = Tk()
root.geometry("300x500")
root.title('Квест "Цитадель"')
root.resizable(width=False, height=False)
    
names = [["Ф",0,11],["1",2,6],["2",5,7],["3",8,1],["4",7,2],["5",7,9],
         ["6",11,7],["7",12,0],["8",10,12]]
for i in range(0,len(names)):
    a = Label(root,text=names[i][0])
    a.grid(row=names[i][1],column=names[i][2])
    names[i].append(a)
button = Button(root,text="Проверить",bg="red",command=check)
button.grid(column=5,row=16,columnspan=10,pady=10)

grid = [[1,11],[2,7],[2,8],[2,9],[2,10],[2,11],[3,11],[4,11],[5,8],[5,9],[5,10],
        [5,11],[5,12],[5,13],[5,14],[6,11],[7,11],[8,2],[8,3],[8,4],[8,5],[8,6],
        [8,7],[8,8],[8,9],[8,10],[8,11],[8,12],[9,2],[9,9],[10,2],[10,9],[11,2],
        [11,8],[11,9],[11,10],[11,11],[11,12],[11,13],[11,14],[11,15],[12,1],
        [12,2],[12,3],[12,4],[12,5],[12,9],[12,12],[13,9],[13,12],[14,9],[15,9]]
for i in range(0,len(grid)):
    a = Entry(root,width=2)
    a.grid(column=grid[i][1],row=grid[i][0])
    grid[i].append(a)
min = 0
timeLabel = Label(text=min)
timeLabel.grid(row=0,column=0)
time()
root.mainloop()