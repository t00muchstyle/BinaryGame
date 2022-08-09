#Importing all the libraries used
import pygame,sys
import random as r
import time
import sqlite3 as sq
from menu import use_username,level_button




# Checking which level should be played
level = level_button
level2 = 0 
level3 = 0
level4 = 0

if level == 1:
    level2 = 0 
    level3 = 0
    level4 = 0

elif level == 2:
    level2 = 1

elif level == 3:
    level2 = 1
    level3 = 1

elif level == 4:
    level2 = 1
    level3 = 1
    level4 = 1

# Connecting database
db = sq.connect("Studentdatabase.db")

# fetc = """SELECT * FROM
#             Uhighscore
#             """
# data = db.execute(fetc)
# for row in data:
#     print(row)


#Initializing fonts and music
pygame.font.init()
pygame.init()
pygame.mixer.init()

#Window width and height
WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT),9,-50)

# setting caption of the window 
pygame.display.set_caption("Binary game")
# Setting the speed of the game by fps(FRAMES PER SECOND)
FPS = 60
G_1=False
G_2=False
G_3=False
G_4=False
G_5=False
G_6=False
G_7=False
G_8=False

# Millisecond to be converted into seconds
Milliseconds=60
score=0
Time=120
list_scores=[]
fetc = """SELECT * FROM
    HIGHSCORE
    """
data = db.execute(fetc)
for row in data:
    list_scores.append(str(row[0]))
    list_scores.append(''.join(row[1]))
# Initializing fonts the parameters are (Type,size)
Binary_font = pygame.font.SysFont('arial',45)

Game_BG = pygame.image.load("assets/Binary.jpg")

Game_BG = pygame.transform.scale(Game_BG,(WIDTH,HEIGHT))
Box_y=1040
class Binary_boxes:
    # Takes 8 variables all of which can be binary or hexa decimal
    def __init__(self,a,b,c,d,e,f,g,h):
        # globalising Box allows to have some space in between the boxes of numbers
        global Box_y
        Box_y -= 60
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.B_box = pygame.Rect(1000,0,30,30)
        self.Box_y = Box_y
        self.animate_box=0
        self.Binary_digit = str(self.a)+str(self.b)+str(self.c)+str(self.d)+str(self.e)+str(self.f)+str(self.g)+str(self.h)
        if level<=4:
            self.binaryToDecimal(int(self.Binary_digit))
        elif level==5:
            self.HextoDec(str(self.Binary_digit))
        self.selectBox = 0
        self.text = ''
        self.font = pygame.font.Font(None,45)
        self.button=True
        self.G=True

    # Called when level 5
    def HextoDec (self,string):
        ret = 0
        for i,d in enumerate(string) : 
            hex = "0123456789ABCDEF"
            value= hex.index(d) # 0 to 15
            
            power = (len(string) -(i+1)) #power of 16
            ret += (value*16**power)
        self.decimal = ret

    # Called when level less than 5
    def binaryToDecimal(self,binary):
     
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1  
        self.decimal = decimal

    # Function to display boxes
    def create(self,event,G):
        global Box_y,G_1,G_2,G_3,G_4,G_5,G_6,G_7,G_8
        # Checking which key pressed
        key=pygame.key.get_pressed()
        x,y = pygame.mouse.get_pos()
        self.NameBox = pygame.Rect(500,self.Box_y,90,50)
        
        if self.NameBox.collidepoint(x,y):
            if event.type== pygame.KEYUP:
                self.button=True
            elif key[pygame.K_1] and self.button:
                self.text=self.text+'1'
                self.button=False
            elif key[pygame.K_2] and self.button:
                self.text=self.text+'2'
                self.button=False
            elif key[pygame.K_3] and self.button:
                self.text=self.text+'3'
                self.button=False
            elif key[pygame.K_4] and self.button:
                self.text=self.text+'4'
                self.button=False
            elif key[pygame.K_5] and self.button:
                self.text=self.text+'5'
                self.button=False
            elif key[pygame.K_6] and self.button:
                self.text=self.text+'6'
                self.button=False
            elif key[pygame.K_7] and self.button:
                self.text=self.text+'7'
                self.button=False
            elif key[pygame.K_8] and self.button:
                self.text=self.text+'8'
                self.button=False
            elif key[pygame.K_9] and self.button:
                self.text=self.text+'9'
                self.button=False
            elif key[pygame.K_0] and self.button:
                self.text=self.text+'0'
                self.button=False
            elif key[pygame.K_BACKSPACE] and self.button:
                self.text=self.text[:-1]
                self.button=False

        
        if self.Box_y==500:
            textSurf = self.font.render(self.text,True,'orange')
            WIN.blit(textSurf,(500,self.Box_y+10))
            pygame.draw.rect(WIN,'orange',self.NameBox,2)

        pygame.draw.rect(WIN,'orange',(8,self.animate_box+5,45,45))
        Binary_num1 = Binary_font.render(str(self.a),1,"White")
        WIN.blit(Binary_num1,(20,self.animate_box))

        pygame.draw.rect(WIN,'orange',(68,self.animate_box+5,45,45))
        Binary_num2 = Binary_font.render(str(self.b),1,"White")
        WIN.blit(Binary_num2,(80,self.animate_box))

        pygame.draw.rect(WIN,'orange',(128,self.animate_box+5,45,45))
        Binary_num3 = Binary_font.render(str(self.c),1,"White")
        WIN.blit(Binary_num3,(140,self.animate_box))

        pygame.draw.rect(WIN,'orange',(188,self.animate_box+5,45,45))
        Binary_num4 = Binary_font.render(str(self.d),1,"White")
        WIN.blit(Binary_num4,(200,self.animate_box))

        pygame.draw.rect(WIN,'orange',(248,self.animate_box+5,45,45))
        Binary_num5 = Binary_font.render(str(self.e),1,"White")
        WIN.blit(Binary_num5,(260,self.animate_box))

        pygame.draw.rect(WIN,'orange',(308,self.animate_box+5,45,45))
        Binary_num6 = Binary_font.render(str(self.f),1,"White")
        WIN.blit(Binary_num6,(320,self.animate_box))

        pygame.draw.rect(WIN,'orange',(368,self.animate_box+5,45,45))
        Binary_num7 = Binary_font.render(str(self.g),1,"White")
        WIN.blit(Binary_num7,(380,self.animate_box))

        pygame.draw.rect(WIN,'orange',(428,self.animate_box+5,45,45))
        Binary_num8 = Binary_font.render(str(self.h),1,"White")
        WIN.blit(Binary_num8,(440,self.animate_box))
        
        if self.Box_y>self.animate_box:
            self.animate_box+=10

        # Moving boxes down if one is solved
        if self.text == str(self.decimal) and G==1:
            
            self.text=''
            self.G=True
            G_2=True
            G_3=True
            G_4=True
            G_5=True
            G_6=True
            G_7=True
            G_8=True
            Box_y+=60

            # Playing sound
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))
        if self.text == str(self.decimal) and G==2:
            G_1=True
            G_3=True
            G_4=True
            G_5=True
            G_6=True
            G_7=True
            G_8=True
            self.text=''
            
            self.G=True
            Box_y+=60
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))
        if self.text == str(self.decimal) and G==3:
            G_2=True
            G_4=True
            G_5=True
            G_1=True
            G_6=True
            G_7=True
            G_8=True
            self.text=''
            self.G=True
            Box_y+=60
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))
        if self.text == str(self.decimal) and G==4:
            G_2=True
            G_1=True
            G_5=True
            G_3=True
            G_6=True
            G_7=True
            G_8=True
            self.text=''
            self.G=True
            Box_y+=60
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))
        if self.text == str(self.decimal) and G==5:
            G_2=True
            G_4=True
            G_3=True
            G_1=True
            G_6=True
            G_7=True
            G_8=True
            self.text=''
            self.G=True
            Box_y+=60
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))

        if self.text == str(self.decimal) and G==6:
            G_2=True
            G_4=True
            G_5=True
            G_3=True
            G_7=True
            G_8=True
            G_1=True
            self.text=''
            self.G=True
            Box_y+=60
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))

        if self.text == str(self.decimal) and G==7:
            G_2=True
            G_4=True
            G_6=True
            G_8=True
            G_5=True
            G_3=True
            G_1=True
            self.text=''
            self.G=True
            Box_y+=60
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))

        if self.text == str(self.decimal) and G==8:
            G_2=True
            G_4=True
            G_6=True
            G_7=True
            G_5=True
            G_3=True
            G_1=True
            self.text=''
            self.G=True
            Box_y+=60
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))
# # Driver code
# NameBox = pygame.Rect(50,70,250,50)
# textBox = pygame.Rect(225,150,250,50)
# selectBox = 0
# text = ''

# Window function displays everything
def window(event,first,second,Third,fourth,fifth,sixth,seventh,eighth):
    global text,selectBox,Milliseconds,Time,score
    # WIN.fill('orange')
    WIN.blit(Game_BG,(0,0))
    if first.G==False:
        first.create(event,1)
    if second.G==False:
        second.create(event,2)
    if Third.G==False:
        Third.create(event,3)
    if fourth.G==False:
        fourth.create(event,4)
    if fifth.G==False:
        fifth.create(event,5)
    if sixth.G==False:
        sixth.create(event,6)
    if seventh.G==False:
        seventh.create(event,7)
    if eighth.G==False:
        eighth.create(event,8)

    if Milliseconds==0:
        Time-=1
        Milliseconds=50
    Milliseconds-=1
    Time_text = Binary_font.render(str(Time),1,"RED")
    WIN.blit(Time_text,(500,0))

    score_text = Binary_font.render(str(score),1,"Green")
    WIN.blit(score_text,(520,550))

    # Allows to update screen everysecond
    pygame.display.update()

# Function which saves data at the end and the gameover screen
def gameover(No_times,realtime):
    No_times+=1
    clock=pygame.time.Clock()
    clock.tick(8)
    Over_text = Binary_font.render("Game Over!",1,"WHITE")
    WIN.blit(Over_text,(150,280))
    pygame.display.update()
    clock.tick(8)
    Over_text = Binary_font.render("Game Over!",1,"RED")
    WIN.blit(Over_text,(150,280))
   
    pygame.display.update()
    if No_times==10:
        Score_text = Binary_font.render("You score is",1,'RED')
        WIN.blit(Score_text,(150,340))
        pygame.display.update()
        pygame.draw.rect(WIN,"BLACK",(200,400,120,50))
        Score_text = Binary_font.render(str(realtime),1,'RED')
        WIN.blit(Score_text,(250,400))
        pygame.display.update()
        print(list_scores)
        try:
            insert = "INSERT INTO Uhighscore(username,highscore,Time,LEVEL) VALUES ('{}','{}','{}','{}')".format(use_username,str(realtime),str(Time),str(level))
            db.execute(insert)
            db.commit()

        except:
            fetc = """SELECT * FROM
                Uhighscore
                """
            data = db.execute(fetc)
            for row in data:
                if int(row[1])<realtime:
                    insert = "UPDATE Uhighscore SET highscore = "+ str(realtime) +" WHERE username =('{}')".format(use_username) 
                    db.execute(insert)
                    db.commit()
        if len(list_scores) <=12:
            insert = "INSERT INTO HIGHSCORE(highscore) VALUES ('{}')".format(str(realtime))
            db.execute(insert)
            db.commit()
        else:
            fetc = """SELECT * FROM
            HIGHSCORE
            """
            data = db.execute(fetc)
            for row in data:
                if realtime>int(row[1]):
                    insert = "UPDATE HIGHSCORE SET highscore = "+ str(realtime) +" WHERE id =({})".format(int(row[0]))
                    db.execute(insert)
                    db.commit()
                    break
        time.sleep(3)
        pygame.quit()
        
    gameover(No_times,realtime)

# Main function which begins everything
def main():
    # Globalising time and second to change according to game
    global G_1,G_2,G_3,G_4,G_5,G_6,G_7,G_8,Box_y,score
    clock=pygame.time.Clock()

    otherevent=None

    # Calling every box class
    first = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    second = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    Third = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    Fourth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    Fifth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    sixth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    seventh = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    eighth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    interval= Time

    # inter_range determines how long it will take for next box to fall
    inter_range=6
    list_of_hex =[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    while True:
        # slowing down the game according to fps
        clock.tick(FPS)

        # for event allows to quit game whenever needed
        for event in pygame.event.get():
            otherevent =  event
            if event.type == pygame.QUIT:
                # ends the window
                pygame.quit()

        # Using random binary or hex numbers 
        if first.G:
            if level<=4:
                first = Binary_boxes(0,r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                first = Binary_boxes(0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            first.G=False
            interval=Time
            interval-=inter_range
            
        if second.G and Time==interval:
            if level <= 4:
                second = Binary_boxes(0,r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                second = Binary_boxes(0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            second.G=False
            interval=Time
            interval-=inter_range

        elif Third.G and Time==interval:
            if level <= 4:
                Third = Binary_boxes(0,r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                Third = Binary_boxes(0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            Third.G=False
            interval=Time
            interval-=inter_range

        elif Fourth.G and Time==interval:
            if level <= 4:
                Fourth = Binary_boxes(0,r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                Fourth = Binary_boxes(0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            Fourth.G=False
            interval=Time
            interval-=inter_range

        elif Fifth.G and Time==interval:
            if level <= 4:
                Fifth = Binary_boxes(0,r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                Fifth = Binary_boxes(0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            Fifth.G=False
            interval=Time
            interval-=inter_range

        elif sixth.G and Time==interval:
            if level <= 4:
                sixth = Binary_boxes(0,r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                sixth = Binary_boxes(0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            sixth.G=False
            interval=Time
            interval-=inter_range

        elif seventh.G and Time==interval:
            if level <= 4:
                seventh = Binary_boxes(0,r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                seventh = Binary_boxes(0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            seventh.G=False
            interval=Time
            interval-=inter_range

        elif eighth.G and Time==interval:
            if level <= 4:
                eighth = Binary_boxes(0,r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                eighth = Binary_boxes(0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            eighth.G=False
            interval=Time
            interval-=inter_range

        elif Time==interval:
            gameover(0,score)

        elif Time==0:
            gameover(0,score)

        # increasing score and recalling when one problem is solved
        if G_1:
            first.Box_y+=60  
            G_1=False
            score+=1
            
        if G_2:
            second.Box_y+=60   
            
            G_2=False 
            score+=1 
        if G_3:
            Third.Box_y+=60   
            G_3=False
            score+=1  
        if G_4:
            Fourth.Box_y+=60   
            G_4=False  
            score+=1
        if G_5:
            Fifth.Box_y+=60   
            G_5=False  
            score+=1
        if G_6:
            sixth.Box_y+=60   
            G_6=False
            score+=1  
        if G_7:
            seventh.Box_y+=60   
            G_7=False  
            score+=1
        if G_8:
            eighth.Box_y+=60   
            G_8=False  
            score+=1
       
        window(otherevent,first,second,Third,Fourth,Fifth,sixth,seventh,eighth)

# Main function is called
main()