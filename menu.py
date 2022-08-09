# Importing all functions used
import pygame, sys
from button import Button
import time
import sqlite3 as sq

level_button = 1
w,z=-300,0
g=0
use_username=''
db = sq.connect("Studentdatabase.db")

# Tables created
try:
    st = """
        CREATE TABLE Student
        (id INTEGER PRIMARY KEY,username TEXT,password TEXT,INITIAL TEXT,CLASS TEXT,TEACHER TEXT,Loggedin TEXT)
        """
    db.execute(st)
    st = """
        CREATE TABLE HIGHSCORE
        (id INTEGER PRIMARY KEY,highscore TEXT)
        """
    db.execute(st)

    st = """
    CREATE TABLE Uhighscore
    (username TEXT PRIMARY KEY,highscore TEXT,Time TEXT,LEVEL TEXT)
    """
    db.execute(st)

    st = """
        CREATE TABLE Teacher
        (id INTEGER PRIMARY KEY,username TEXT,password TEXT,INITIAL TEXT,CLASS TEXT,TEACHER TEXT)
        """
    db.execute(st)
except:
    pass

#--------UNCOMMENT THE CODE BELLOW TO DELETE ALL DATA----------#

# st = 'DROP TABLE uhighscore'
# db.execute(st)
# st = 'DROP TABLE HIGHSCORE'
# db.execute(st)
# st = 'DROP TABLE Student'
# db.execute(st)
# st = 'DROP TABLE Teacher'
# db.execute(st)

# Initializing everything
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")
BG = pygame.transform.scale(BG,(1280,720))

# INITIALIZING FONTS
Binary_font = pygame.font.SysFont('arial',40)

# Class to show data
class show_data:
    def __init__(self,x,y,st_num,st_name,st_initial,st_class,st_teacher,st_logged):
        global g
        g+=40
        self.x = x
        self.y = y+g
        self.st_num = st_num
        self.st_name = st_name
        self.st_initial = st_initial
        self.st_class = st_class
        self.st_teacher = st_teacher
        self.st_logged = st_logged

        # TAKING SCORE
        self.score=''
        fetc = """SELECT highscore FROM
                Uhighscore WHERE username =""" +"'"+self.st_name+"'"
        data = db.execute(fetc)
        for row in data:
            self.score = ''.join(row)

        # SHOWING DATA
    def update(self):
        MENU_TEXT = get_font(15).render(str(self.st_num), True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(self.x, self.y))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render(str(self.st_name), True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(self.x+100, self.y))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render(str(self.score), True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(self.x+320, self.y))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render(str(self.st_teacher), True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(self.x+520, self.y))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render(str(self.st_initial), True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(self.x+830, self.y))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render(str(self.st_logged)+"  TIMES", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(self.x+1120, self.y))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

# Checking data of which class is needed
def which_class_student(txt):
    objs = list()
    selection=0

    which_student=[]
    fetc = """SELECT * FROM
    Student WHERE CLASS ="""+"'"+txt+"'"
    data = db.execute(fetc)
    
    for row in data:
        
        which_student= which_student+list(row)

 
    for i in range(int(len(which_student)/7)):
        objs.append(show_data(30,100,which_student[selection],which_student[selection+1],which_student[selection+3],which_student[selection+4],which_student[selection+5],which_student[selection+6]))
        selection+=7
    
    # DISPLAYING EVERYTHING
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill('white')
        pygame.draw.rect(SCREEN,'black',(0,50,1300,50))
        MENU_TEXT = get_font(15).render("STUDENT NAME", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(100, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'black',(250,50,20,1300))
        MENU_TEXT = get_font(15).render("HIGH SCORE", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(350, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'black',(450,50,20,1300))
        MENU_TEXT = get_font(15).render("TEACHER", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'black',(700,50,20,1300))
        MENU_TEXT = get_font(15).render("CLASS INITIAL", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(850, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'black',(1000,50,20,1300))
        MENU_TEXT = get_font(15).render("TIMES LOGGED IN", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(1150, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        OPTIONS_BACK = Button(image=None, pos=(40, 40), 
                                text_input="BACK", font=get_font(35), base_color="RED", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for i in range(int(len(which_student)/7)):
            objs[i].update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    teacher()
        pygame.display.update()

# Creating button of different classes
class separate_button:
    
    def __init__(self,x,y,text):
        global w,z
        w+=400
        if w>901:
            w=100
            z+=150
        self.x = x + w
        self.y = y + z
        self.text = text
        
    # Updating  
    def update(self,event):
        # Checks mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        

        BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(self.x, self.y), 
                            text_input=self.text, font=Binary_font, base_color="green", hovering_color="White")
        BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BUTTON.update(SCREEN)

        if event== pygame.MOUSEBUTTONDOWN and BUTTON.checkForInput(OPTIONS_MOUSE_POS):
            
            which_class_student(self.text)

# Button for all data
def all_data():
    set_of_class=set()
    fetc = """SELECT CLASS FROM
    Student
    """
    data = db.execute(fetc)
    
    for row in data:
        set_of_class.update(row)

    objs = list()
    set_of_class= list(set_of_class)
    for i in range(len(set_of_class)):
        objs.append(separate_button(100,150,set_of_class[i]))

    
    while True:
        SCREEN.fill('white')
        pygame.draw.rect(SCREEN,'BLACK',(50,20,1180,60))
        MENU_TEXT = get_font(50).render("SELECT CLASS", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        for i in range(len(set_of_class)):
            objs[i].update('')
       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(set_of_class)):
                    objs[i].update(event.type)
    
        pygame.display.update()

# teacher menu
def teacher():
    # USING MATHS TO CALCULATE AVERAGE USE TIME
    avg_time=0
    minutes=0
    Top_student_score=0
    Top_student_name=''
    Bottom_student_score=1000
    Bottom_student_name=''
    time_list=[]
    fetc = """SELECT Time FROM
    Uhighscore
    """
    data = db.execute(fetc)
    for row in data:
        time_list.append(''.join(row))

    fetc = """SELECT * FROM
    Uhighscore
    """
    data = db.execute(fetc)
    for row in data:
        if Top_student_score<int(row[1]):
            Top_student_name=row[0]
            Top_student_score=int(row[1])
        if Bottom_student_score>int(row[1]):
            Bottom_student_name=row[0]
            Bottom_student_score=int(row[1])
    for i in time_list:
        avg_time=120-int(i)+avg_time
    try:
        avg_time=int(avg_time/len(time_list))
        
    except:
        pass
    min_time="0"+str(minutes)+':'+str(avg_time)
    if avg_time==60:
        avg_time=0
        minutes+=1
    
    while True:
        SCREEN.fill('white')
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        pygame.draw.rect(SCREEN,'BLACK',(50,20,1180,160))
        MENU_TEXT = get_font(100).render("TEACHER MENU", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'BLACK',(650,300,600,600))
        
        MENU_TEXT = get_font(20).render("Average Time Use", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(840, 350))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(20).render(str(min_time), True, "green")
        MENU_RECT = MENU_TEXT.get_rect(center=(800, 400))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(20).render("Top student data", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(840, 450))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(20).render(Top_student_name+' : '+str(Top_student_score), True, "green")
        MENU_RECT = MENU_TEXT.get_rect(center=(840, 500))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(20).render("Bottom student data", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(875, 550))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(20).render(Bottom_student_name+' : '+str(Bottom_student_score), True, "green")
        MENU_RECT = MENU_TEXT.get_rect(center=(840, 600))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        ALL_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(320, 450), 
                            text_input="SHOW ALL DATA", font=get_font(25), base_color="black", hovering_color="White")
        ALL_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        ALL_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ALL_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    all_data()
        pygame.display.update()

# level button
def levels():
    global level_button
    while True:
        SCREEN.blit(BG, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        LEVEL1_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(420, 200), 
                            text_input="LEVEL1", font=get_font(25), base_color="GREEN", hovering_color="red")
        LEVEL1_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        LEVEL1_BUTTON.update(SCREEN)

        LEVEL2_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(850, 200), 
                            text_input="LEVEL2", font=get_font(25), base_color="Green", hovering_color="red")
        LEVEL2_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        LEVEL2_BUTTON.update(SCREEN)

        LEVEL3_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(420, 350), 
                            text_input="LEVEL3", font=get_font(25), base_color="GREEN", hovering_color="red")
        LEVEL3_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        LEVEL3_BUTTON.update(SCREEN)

        LEVEL4_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(850, 350), 
                            text_input="LEVEL4", font=get_font(25), base_color="Green", hovering_color="red")
        LEVEL4_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        LEVEL4_BUTTON.update(SCREEN)

        LEVEL5_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(635, 500), 
                            text_input="LEVEL5", font=get_font(25), base_color="Green", hovering_color="red")
        LEVEL5_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        LEVEL5_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 1
                    pygame.quit()
                    import Binary
                    
                if LEVEL2_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 2
                    pygame.quit()
                    import Binary

                if LEVEL3_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 3
                    pygame.quit()
                    import Binary

                if LEVEL4_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 4
                    pygame.quit()
                    import Binary

                if LEVEL5_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 5
                    pygame.quit()
                    import Binary

        pygame.display.update()

# Student menu
def student():
    logged=0
    fetc = """SELECT Loggedin FROM
    Student WHERE username ="""+"'"+use_username+"'"
    data = db.execute(fetc)
    for row in data:
        logged=int(''.join(row))
        
    insert = "UPDATE Student SET Loggedin = "+ str(logged+1) +" WHERE username =('{}')".format(use_username) 
    db.execute(insert)
    db.commit()

    list_of_scores=[]
    fetc = """SELECT * FROM
    HIGHSCORE
    """
    data = db.execute(fetc)
    for row in data:
        list_of_scores.append(str(row[0]))
        list_of_scores.append(''.join(row[1]))

    fetc = """SELECT * FROM
    Uhighscore
    """
    data = db.execute(fetc)
    for row in data:
        if row[0]==use_username:
            which_score=row[1]

    while True:
        SCREEN.blit(BG, (0, 0))
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("BINARY GAME", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        START_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(620, 300), 
                            text_input="START GAME", font=get_font(55), base_color="black", hovering_color="White")
        START_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        START_BUTTON.update(SCREEN)

        pygame.draw.rect(SCREEN,'black',(800,400,400,400))
        pygame.draw.rect(SCREEN,'black',(80,400,400,400))

        MENU_TEXT = get_font(20).render("HIGH SCORES:", True, "green")
        MENU_RECT = MENU_TEXT.get_rect(center=(220, 450))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        if len(list_of_scores)>=2:
            MENU_TEXT = get_font(20).render(str(list_of_scores[0])+', '+str(list_of_scores[1]), True, "green")
            MENU_RECT = MENU_TEXT.get_rect(center=(140, 490))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        if len(list_of_scores)>=4:
            MENU_TEXT = get_font(20).render(str(list_of_scores[2])+', '+str(list_of_scores[3]), True, "green")
            MENU_RECT = MENU_TEXT.get_rect(center=(140, 530))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        if len(list_of_scores)>=6:
            MENU_TEXT = get_font(20).render(str(list_of_scores[4])+', '+str(list_of_scores[5]), True, "green")
            MENU_RECT = MENU_TEXT.get_rect(center=(140, 570))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        if len(list_of_scores)>=8:
            MENU_TEXT = get_font(20).render(str(list_of_scores[6])+', '+str(list_of_scores[7]), True, "green")
            MENU_RECT = MENU_TEXT.get_rect(center=(140, 610))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        if len(list_of_scores)>=10:
            MENU_TEXT = get_font(20).render(str(list_of_scores[8])+', '+str(list_of_scores[9]), True, "green")
            MENU_RECT = MENU_TEXT.get_rect(center=(140, 650))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        if len(list_of_scores)>=12:
            MENU_TEXT = get_font(20).render(str(list_of_scores[10])+', '+str(list_of_scores[11]), True, "green")
            MENU_RECT = MENU_TEXT.get_rect(center=(140, 690))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        try:
            MENU_TEXT = get_font(20).render((which_score), True, "green")
            MENU_RECT = MENU_TEXT.get_rect(center=(1000, 550))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        except:
            pass

        MENU_TEXT = get_font(20).render("YOUR HIGH SCORE:", True, "green")
        MENU_RECT = MENU_TEXT.get_rect(center=(990, 450))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    levels()

        pygame.display.update()

# The boxes used in registering
class register_box:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
        self.text=''
        self.NameBox = pygame.Rect(self.a,self.b,300,40)

    def box(self,event):
        x,y = pygame.mouse.get_pos()
        key= pygame.key.get_pressed()
        print(event)
        if key[pygame.K_BACKSPACE] and self.NameBox.collidepoint(x,y):

            self.text=self.text[:-1]

        # Checking which key is pressed and converting it to alphabet
        if self.NameBox.collidepoint(x,y):
           self.text=self.text+event
        pygame.draw.rect(SCREEN,'white',self.NameBox,2)
        # self.text += event.unicode
        print(self.text)
        
        textSurf = get_font(20).render(self.text,True,(0,255,0))
        SCREEN.blit(textSurf,(self.NameBox[0]+5,self.NameBox[1]+10))


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

# Logging in
def login():
    global use_username
    box1=register_box(500,240)
    box2=register_box(500,300)
    usernames=[]
    password=[]
    T_usernames=[]
    T_password=[]
    fetc = """SELECT username FROM
    Student
    """
    data = db.execute(fetc)
    for row in data:
        usernames.append(''.join(row))
    fetc = """SELECT password FROM
    Student
    """
    data = db.execute(fetc)
    for row in data:
        password.append(''.join(row))

    fetc = """SELECT username FROM
    Teacher
    """
    data = db.execute(fetc)
    for row in data:
        T_usernames.append(''.join(row))
    fetc = """SELECT password FROM
    Teacher
    """
    data = db.execute(fetc)
    for row in data:
        T_password.append(''.join(row))

    # print(password)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        pygame.draw.rect(SCREEN,'black',(225,200,800,200))
        MENU_TEXT = get_font(100).render("BINARY GAME", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render("USERNAME:", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 260))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render("PASSWORD:", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 320))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BACK = Button(image=None, pos=(300, 700), 
                            text_input="BACK", font=get_font(35), base_color="black", hovering_color="Green")
        
        LOGIN_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                            text_input="LOGIN", font=get_font(55), base_color="black", hovering_color="White")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        LOGIN_BUTTON.changeColor(PLAY_MOUSE_POS)
        LOGIN_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if LOGIN_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if box1.text in usernames and box2.text in password:
                        student()
                    elif box1.text in T_usernames and box2.text in T_password:
                        teacher()
            if event.type == pygame.KEYDOWN: 
            
                box1.box(event.unicode) 
                box2.box(event.unicode)
        use_username = box1.text
        box1.box('')
        box2.box('')

        pygame.display.update()

# Registeration and saving
def register(T_OR_S):
    box1=register_box(540,240)
    box2=register_box(450,300)
    box3=register_box(550,360)
    box4=register_box(560,420)
    box5=register_box(400,480)
    box6=register_box(430,540)
    Password = register_box(570,360)
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        if T_OR_S == 'STUDENT' or Password.text=='9851':
            MENU_TEXT = get_font(100).render("BINARY GAME", True, "Black")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
            pygame.draw.rect(SCREEN,'black',(280,200,700,400))

            MENU_TEXT = get_font(15).render("ENTER USERNAME:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(420, 260))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("PASSWORD:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(375, 320))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("REPEAT PASSWORD:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(425, 380))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("TEACHER INITIALS:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(430, 440))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("CLASS:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(350, 500))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("TEACHER:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(365 , 560))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            
            REGISTER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 660), 
                                text_input="REGISTER", font=get_font(55), base_color="black", hovering_color="White")
             
            REGISTER_BUTTON.changeColor(OPTIONS_MOUSE_POS)
            REGISTER_BUTTON.update(SCREEN)

        OPTIONS_BACK = Button(image=None, pos=(250, 700), 
                                text_input="BACK", font=get_font(35), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                try:
                    if REGISTER_BUTTON.checkForInput(OPTIONS_MOUSE_POS) and len(box2.text)>=8 and len(box3.text)>=8 :
                        if T_OR_S=='TEACHER':
                            insert = "INSERT INTO Teacher(username,password,INITIAL,CLASS,TEACHER) VALUES ('{}','{}','{}','{}','{}')".format(box1.text,box2.text,box4.text,box5.text,box6.text)
                            db.execute(insert)
                            db.commit()
                            login()
                        else:
                            insert = "INSERT INTO Student(username,password,INITIAL,CLASS,TEACHER,Loggedin) VALUES ('{}','{}','{}','{}','{}','{}')".format(box1.text,box2.text,box4.text,box5.text,box6.text,str(0))
                            db.execute(insert)
                            db.commit()
                            login()
                    elif  REGISTER_BUTTON.checkForInput(OPTIONS_MOUSE_POS) and len(box2.text)<8 and len(box3.text)<8:
                        MENU_TEXT = get_font(15).render("Minimum password length should be 8 characters", True, "Red")
                        MENU_RECT = MENU_TEXT.get_rect(center=(630, 585))
                        SCREEN.blit(MENU_TEXT, MENU_RECT)
                except:
                    pass
                    # time.sleep(2)
    
            if event.type == pygame.KEYDOWN: 
                if T_OR_S=='STUDENT' or Password.text=='9851':
                    box1.box(event.unicode) 
                    box2.box(event.unicode) 
                    box3.box(event.unicode) 
                    box4.box(event.unicode) 
                    box5.box(event.unicode) 
                    box6.box(event.unicode) 
                if T_OR_S=='TEACHER'and Password.text!='9851':
                    Password.box(event.unicode)
                

        if T_OR_S=='STUDENT' or Password.text=='9851':
            box1.box('')
            box2.box('')
            box3.box('')
            box4.box('')
            box5.box('')
            box6.box('')
        

        if T_OR_S=='TEACHER' and Password.text!='9851':
            SCREEN.fill("black")
            MENU_TEXT = get_font(15).render("TYPE TEACHER CODE:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(425, 380))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
            Password.box('')

        pygame.display.update()

# Button for student or teacher
def student_or_teacher():
    
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("REGISTER AS", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        STUDENT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                            text_input="STUDENT", font=get_font(55), base_color="black", hovering_color="White")

        TEACHER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                            text_input="TEACHER", font=get_font(55), base_color="black", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [STUDENT_BUTTON, TEACHER_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STUDENT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    register('STUDENT')
                if TEACHER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    register('TEACHER')
                    


        pygame.display.update()

# Main function that begins everything      
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        # SCREEN.fill('white')

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("BINARY GAME", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                            text_input="LOGIN", font=get_font(55), base_color="black", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                            text_input="REGISTER", font=get_font(55), base_color="black", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    login()
             
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    student_or_teacher()

        pygame.display.update()


main_menu()