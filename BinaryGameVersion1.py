#Importing all the libraries used
import pygame,sys
import random as r
import time

#Initializing fonts and music
pygame.font.init()
pygame.init()
pygame.mixer.init()

#Window width and height
WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

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

Milliseconds=60
score=0
Time=120
# Initializing fonts the parameters are (Type,size)
Binary_font = pygame.font.SysFont('arial',45)

Game_BG = pygame.image.load("binary.jpg")

Game_BG = pygame.transform.scale(Game_BG,(WIDTH,HEIGHT))
Box_y=1040
class Binary_boxes:
    
    def __init__(self,a,b,c,d,e,f,g,h):
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
        self.binaryToDecimal(int(self.Binary_digit))
        
        self.selectBox = 0
        self.text = ''
        self.font = pygame.font.Font(None,45)
        self.button=True
        self.G=True
    def binaryToDecimal(self,binary):
     
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        print(decimal)   
        self.decimal = decimal

    def create(self,event,G):
        global Box_y,G_1,G_2,G_3,G_4,G_5,G_6,G_7,G_8
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

        print(self.Box_y)
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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.wav'))
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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.wav'))
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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.wav'))
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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.wav'))
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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.wav'))

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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.wav'))

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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.wav'))

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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.wav'))
# Driver code
NameBox = pygame.Rect(50,70,250,50)
textBox = pygame.Rect(225,150,250,50)
selectBox = 0
text = ''
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
    pygame.display.update()



def main():
    # Globalising time and second to change according to game
    global G_1,G_2,G_3,G_4,G_5,G_6,G_7,G_8,Box_y,score
    clock=pygame.time.Clock()
    # first = Binary_boxes(1,0,0,0,0,0,1,1)
    # second = Binary_boxes(0,0,0,0,0,0,1,1)
    otherevent=None
    first = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    second = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    Third = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    Fourth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    Fifth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    sixth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    seventh = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    eighth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
    interval= Time
    inter_range=5
    while True:
        # slowing down the game according to fps
        clock.tick(FPS)

        # for event allows to quit game whenever needed
        for event in pygame.event.get():
            otherevent =  event
            if event.type == pygame.QUIT:
                # ends the window
                pygame.quit() 
        if first.G:
            first = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            first.G=False
            interval=Time
            interval-=inter_range
            
        if second.G and Time==interval:
            second = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            second.G=False
            interval=Time
            interval-=inter_range

        elif Third.G and Time==interval:
            Third = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            Third.G=False
            interval=Time
            interval-=inter_range

        elif Fourth.G and Time==interval:
            Fourth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            Fourth.G=False
            interval=Time
            interval-=inter_range

        elif Fifth.G and Time==interval:
            Fifth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            Fifth.G=False
            interval=Time
            interval-=inter_range

        elif sixth.G and Time==interval:
            sixth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            sixth.G=False
            interval=Time
            interval-=inter_range

        elif seventh.G and Time==interval:
            seventh = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            seventh.G=False
            interval=Time
            interval-=inter_range

        elif eighth.G and Time==interval:
            eighth = Binary_boxes(0,0,0,0,r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            eighth.G=False
            interval=Time
            interval-=inter_range

        elif Time==interval:
            pygame.quit()

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

main()