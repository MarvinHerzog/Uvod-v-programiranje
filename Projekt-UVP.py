from tkinter import *
import time
from random import *
from ast import literal_eval



class Kac():
    def __init__(self, master):


        self.size = 2
        self.dim = 200*self.size
        self.kon = 10*self.size
        self.state = 3
        self.speed = 100
        self.speeddef = self.speed
        self.counter = 0
        self.currentstate = 3
        self.score = IntVar(value = 0)
        self.rekord = IntVar(value = 0)
        y1 = StringVar()

        

        self.canv = Canvas(master, width = self.dim, height = self.dim, bg='grey')
        self.canv.grid(row=1, column=0, rowspan=20)




        root.bind('<Up>', self.up)
        root.bind('<Left>', self.left)
        root.bind('<Right>', self.right)
        root.bind('<Down>', self.down)

        
        lab4 = Label(root, text = 'Hitrost kače:')
        lab4.grid(row=1,column=2)
        zrt = Button(master, text="0.5x", command = self.hitro)
        zrt.grid(row=2,column=2)
        zrt = Button(master, text="2x", command = self.pocasno)
        zrt.grid(row=3,column=2)

        
        
        pod = Button(master, text="Podaljšaj", command = self.podaljsaj)
        pod.grid(row=2,column=1)
        korak = Button(master, text="Korak", command = self.spremenkaco)
        korak.grid(row=3,column=1)
        
        tre = Button(master, text="Od znova", command = self.nova)
        tre.grid(row=4,column=1)
        play = Button(master, text="Začni/pauza", command = self.pomoz)
        play.grid(row=5,column=1)


        lab1 = Label(root, textvariable = self.score)
        lab1.grid(row=6,column=1)
        lab2 = Label(root, text = 'Trenutni rekord:')
        lab2.grid(row=7,column=1)
        lab3 = Label(root, textvariable = self.rekord)
        lab3.grid(row=8,column=1)

        odp = Button(master, text="Odpri", command = self.odpri) 
        odp.grid(row=9,column=1)
        shr = Button(master, text="Shrani", command = self.shrani)
        shr.grid(row=10,column=1)
        
        
        
        for i in range(0,int(self.dim//10)*self.size):
            self.canv.create_line(i*self.kon,000,i*self.kon,self.dim,)
            self.canv.create_line(0,i*self.kon,self.dim,i*self.kon)



        self.snake = [(0,((self.dim/self.kon)//2)*self.kon),(self.kon,((self.dim/self.kon)//2)*self.kon),(2*self.kon,((self.dim/self.kon)//2)*self.kon)]
##        self.snake = [(self.dim//2+2*self.kon,self.dim//2),(self.dim//2+1*self.kon,self.dim//2),(self.dim//2,self.dim//2)]
        self.list = []
        #self.canv.create_rectangle(0,0,0+self.kon,0+self.kon, fill='red')
        self.narkaco()
        self.randnjam()
        

    def narkaco(self):     #začetna kača
        for j in self.snake:
            
            a = self.canv.create_rectangle(j[0],j[1],j[0]+self.kon,j[1]+self.kon, fill= '#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
            self.list.append(a)

    def hitro(self):
        self.speed = int(self.speed*2)
        print(self.speed)

    def pocasno(self):
        self.speed = int(self.speed*0.5)
        print(self.speed)

    def spremenkaco(self):  #korak po korak
        self.currentstate = self.state
        if self.state == 2:
            a = self.canv.create_rectangle(self.snake[-1][0]-self.kon,self.snake[-1][1],self.snake[-1][0],self.snake[-1][1]+self.kon,fill= '#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
            self.snake.append((self.snake[-1][0]-self.kon,self.snake[-1][1]))
            self.snake.pop(0)
            self.list.append(a)
            self.canv.delete(self.list[0])
            self.list.pop(0)
            
        if self.state == 1:
            a = self.canv.create_rectangle(self.snake[-1][0],self.snake[-1][1]-self.kon,self.snake[-1][0]+self.kon,self.snake[-1][1],fill= '#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
            self.snake.append((self.snake[-1][0],self.snake[-1][1]-self.kon))
            self.snake.pop(0)
            self.list.append(a)
            self.canv.delete(self.list[0])
            self.list.pop(0) 

        if self.state == 3:
            a = self.canv.create_rectangle(self.snake[-1][0]+self.kon,self.snake[-1][1],self.snake[-1][0]+2*self.kon,self.snake[-1][1]+self.kon,fill= '#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
            self.snake.append((self.snake[-1][0]+self.kon,self.snake[-1][1]))
            self.snake.pop(0)
            self.list.append(a)
            self.canv.delete(self.list[0])
            self.list.pop(0)

        if self.state == 4:
            a = self.canv.create_rectangle(self.snake[-1][0],self.snake[-1][1]+self.kon,self.snake[-1][0]+self.kon,self.snake[-1][1]+2*self.kon,fill= '#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
            self.snake.append((self.snake[-1][0],self.snake[-1][1]+self.kon))
            self.snake.pop(0)
            self.list.append(a)
            self.canv.delete(self.list[0])
            self.list.pop(0) 
        print(self.snake)



    def up(self,event):
        if self.currentstate != 4:
            self.state = 1

    def left(self,event):
        if self.currentstate != 3:
            self.state = 2

    def right(self,event):
        if self.currentstate != 2:
            self.state = 3

    def down(self,event):
        if self.currentstate != 1:
            self.state = 4


    def pomoz(self):
        if self.counter == 0:
            self.counter = 1                                 #counter -> pavza ali ne
        else:
            self.counter = 0
        self.playing()

    def playing(self):                  #glavna zanka igre
        if self.counter == 1:


            for i in range(len(self.snake)-1):
                if self.snake[i] == self.snake[-1]:
                    self.counter = 0
                    print('Zguba')
            if self.snake[-1][0] < 0 or self.snake[-1][0] >= self.dim:                                               #pogoji za izgubljeno igro
                print('Nimaš pojma')
                self.counter = 0
            if self.snake[-1][1] < 0 or self.snake[-1][1] >= self.dim:
                print('Raje odnehaj')
                self.counter = 0

            if self.snake[-1] == self.njam:
                self.score.set(self.score.get()+1)
                if self.score.get() > self.rekord.get():
                    self.rekord.set(self.score.get())
                self.canv.delete(self.njamlik)
                self.podaljsaj()
                self.randnjam()
                
                    
            self.currentstate = self.state
            
            if self.state == 2:
                a = self.canv.create_rectangle(self.snake[-1][0]-self.kon,self.snake[-1][1],self.snake[-1][0],self.snake[-1][1]+self.kon,fill= '#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
                self.snake.append((self.snake[-1][0]-self.kon,self.snake[-1][1]))
                self.snake.pop(0)
                self.list.append(a)
                self.canv.delete(self.list[0])
                self.list.pop(0)
                
            if self.state == 1:
                a = self.canv.create_rectangle(self.snake[-1][0],self.snake[-1][1]-self.kon,self.snake[-1][0]+self.kon,self.snake[-1][1],fill='#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
                self.snake.append((self.snake[-1][0],self.snake[-1][1]-self.kon))
                self.snake.pop(0)
                self.list.append(a)
                self.canv.delete(self.list[0])
                self.list.pop(0) 

            if self.state == 3:
                a = self.canv.create_rectangle(self.snake[-1][0]+self.kon,self.snake[-1][1],self.snake[-1][0]+2*self.kon,self.snake[-1][1]+self.kon,fill='#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
                self.snake.append((self.snake[-1][0]+self.kon,self.snake[-1][1]))
                self.snake.pop(0)
                self.list.append(a)
                self.canv.delete(self.list[0])
                self.list.pop(0)

            if self.state == 4:
                a = self.canv.create_rectangle(self.snake[-1][0],self.snake[-1][1]+self.kon,self.snake[-1][0]+self.kon,self.snake[-1][1]+2*self.kon,fill='#%02x%02x%02x' % (randint(0,10), randint(160,240), randint(0,10)))
                self.snake.append((self.snake[-1][0],self.snake[-1][1]+self.kon))
                self.snake.pop(0)
                self.list.append(a)
                self.canv.delete(self.list[0])
                self.list.pop(0) 
            root.after(self.speed,self.playing)
        elif self.counter == 0:
            pass



    def randnjam(self):
##        for i in range(0,int(self.dim//10)*self.size):
##            print(i)
##            for j in range(0,int(self.dim//10)*self.size):
##                print(i,j)
        while True:
            self.njam = (randint(0,self.dim//(self.kon)-1)*self.kon,randint(0,self.dim//(self.kon)-1)*self.kon)
            if self.njam not in self.snake:
               self.njamlik = self.canv.create_rectangle(self.njam[0],self.njam[1],self.njam[0]+self.kon,self.njam[1]+self.kon,fill='red')
               break






        
        
    def podaljsaj(self):
        self.snake.insert(0,self.snake[0])
        self.list.insert(0,'mark')

    def nova(self):
        self.counter = 0
        self.state = 3
        self.currentstate = 3
        self.canv.delete(self.njamlik)
        self.speed = self.speeddef
        for i in self.list:
            try:
                self.canv.delete(i)
            except:
                pass
        self.snake = [(0,((self.dim/self.kon)//2)*self.kon),(self.kon,((self.dim/self.kon)//2)*self.kon),(2*self.kon,((self.dim/self.kon)//2)*self.kon)]
        self.list = []
        self.narkaco()
        self.randnjam()
        self.score.set(0)


    def shrani(self):
        self.counter = 0
        ime = filedialog.asksaveasfilename()
        if ime == "":  
            return

        with open(ime, "wt", encoding="utf8") as f:
            f.write(str(self.snake)+',,'+str(self.njam)+',,'+str(self.rekord.get())+',,'+str(self.state)+',,'+str(self.dim)+',,'+str(self.size)+',,'+str(self.score.get()))
        
        
    def odpri(self):
        self.counter = 0
        ime = filedialog.askopenfilename()
        if ime == "":  # Pritisnili smo Cancel
            return

        self.canv.delete(self.njamlik)
        for i in self.list:
            try:
                self.canv.delete(i)
            except:
                pass
        self.list = []
        self.score.set(0)

        
        with open(ime, encoding="utf8") as f:
            for i in f:
                by=i.split(',,')
                self.snake = literal_eval(by[0])
                self.njam = literal_eval(by[1])
                self.state = int(by[3])
                self.rekord.set(int(by[2]))
                if self.dim//self.size != int(by[4])//int(by[5]):
                    print('Napačna dimenzija! Ob zagonu nastavi dimenzijo na '+ str(int(by[4])//int(by[5])))
                self.size = int(by[5])
                self.score.set(int(by[6]))
                self.narkaco()
                self.njamlik = self.canv.create_rectangle(self.njam[0],self.njam[1],self.njam[0]+self.kon,self.njam[1]+self.kon,fill='red')
                    


root = Tk()
app = Kac(root)
root.mainloop
