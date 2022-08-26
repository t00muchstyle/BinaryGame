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

WIDTH,HEIGHT=1080,620

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")
BG = pygame.transform.scale(BG,(1080,620))

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
        MENU_RECT = MENU_TEXT.get_rect(center=(self.x+740, self.y))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render(str(self.st_logged)+"  TIMES", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(self.x+960, self.y))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

# Checking data of which class is needed
def which_class_student(txt):
    global w,g
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
        MENU_TEXT = get_font(12).render("STUDENT NAME", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(100, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'black',(230,50,20,1300))
        MENU_TEXT = get_font(12).render("HIGH SCORE", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(350, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'black',(430,50,20,1300))
        MENU_TEXT = get_font(12).render("TEACHER", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(550, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'black',(650,50,20,1300))
        MENU_TEXT = get_font(12).render("CLASS INITIAL", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(780, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        pygame.draw.rect(SCREEN,'black',(870,50,20,1300))
        MENU_TEXT = get_font(12).render("TIMES LOGGED IN", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(990, 80))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        OPTIONS_BACK = Button(image=None, pos=(70, 40), 
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
                    w=-300
                    g=0
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
        pygame.draw.rect(SCREEN,'BLACK',(0,20,1180,60))
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
        pygame.draw.rect(SCREEN,'BLACK',(0,20,1180,160))
        MENU_TEXT = get_font(80).render("TEACHER MENU", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))
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

        PLAY_BACK = Button(image=None, pos=(90, 300), 
                            text_input="BACK", font=get_font(35), base_color="black", hovering_color="Green")
        PLAY_BACK.changeColor(OPTIONS_MOUSE_POS)
        PLAY_BACK.update(SCREEN)


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
                    SCREEN.fill('white')
                    main()

                    
                if LEVEL2_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 2
                    SCREEN.fill('white')
                    main()

                if LEVEL3_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 3
                    SCREEN.fill('white')
                    main()

                if LEVEL4_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 4
                    SCREEN.fill('white')
                    main()

                if LEVEL5_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    level_button = 5
                    SCREEN.fill('white')
                    main()

                if PLAY_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    student()

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
        MENU_TEXT = get_font(80).render("BINARY GAME", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        START_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(620, 300), 
                            text_input="START GAME", font=get_font(55), base_color="black", hovering_color="White")
        START_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        START_BUTTON.update(SCREEN)

        pygame.draw.rect(SCREEN,'black',(700,400,400,400))
        pygame.draw.rect(SCREEN,'black',(0,400,400,400))

        MENU_TEXT = get_font(20).render("HIGH SCORES:", True, "green")
        MENU_RECT = MENU_TEXT.get_rect(center=(160, 450))
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
            MENU_RECT = MENU_TEXT.get_rect(center=(950, 550))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        except:
            pass

        MENU_TEXT = get_font(20).render("YOUR HIGH SCORE:", True, "green")
        MENU_RECT = MENU_TEXT.get_rect(center=(910, 450))
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
    
    
    global use_username,SCREEN
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
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
        MENU_TEXT = get_font(80).render("BINARY GAME", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render("USERNAME:", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 260))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        MENU_TEXT = get_font(15).render("PASSWORD:", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 320))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BACK = Button(image=None, pos=(90, 300), 
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
    box1=register_box(540,180)
    box2=register_box(450,240)
    box3=register_box(550,300)
    box4=register_box(560,360)
    box5=register_box(400,420)
    box6=register_box(430,480)
    Password = register_box(570,360)
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        if T_OR_S == 'STUDENT' or Password.text=='9851':
            MENU_TEXT = get_font(80).render("BINARY GAME", True, "Black")
            MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
            pygame.draw.rect(SCREEN,'black',(280,140,700,400))

            MENU_TEXT = get_font(15).render("ENTER USERNAME:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(420, 200))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("PASSWORD:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(375, 260))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("REPEAT PASSWORD:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(425, 320))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("TEACHER INITIALS:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(430, 380))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("CLASS:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(350, 440))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            MENU_TEXT = get_font(15).render("TEACHER:", True, "white")
            MENU_RECT = MENU_TEXT.get_rect(center=(365 , 500))
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            
            REGISTER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 590), 
                                text_input="REGISTER", font=get_font(55), base_color="black", hovering_color="White")
             
            REGISTER_BUTTON.changeColor(OPTIONS_MOUSE_POS)
            REGISTER_BUTTON.update(SCREEN)

        OPTIONS_BACK = Button(image=None, pos=(90, 300), 
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
                        MENU_RECT = MENU_TEXT.get_rect(center=(630, 555))
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

        MENU_TEXT = get_font(80).render("REGISTER AS", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))
        STUDENT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(590, 300), 
                            text_input="STUDENT", font=get_font(55), base_color="black", hovering_color="White")

        TEACHER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(590, 500), 
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

        MENU_TEXT = get_font(80).render("BINARY GAME", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(590, 300), 
                            text_input="LOGIN", font=get_font(55), base_color="black", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(590, 500), 
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

import pygame,sys
import random as r
import time
import sqlite3 as sq

# from menu import use_username,level_button




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
# WIDTH, HEIGHT = 600,600
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
G_9=False

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

Game_BG = pygame.transform.scale(Game_BG,(600,600))
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
        global Box_y,G_1,G_2,G_3,G_4,G_5,G_6,G_7,G_8,G_9
        # Checking which key pressed
        key=pygame.key.get_pressed()
        x,y = pygame.mouse.get_pos()
        self.NameBox = pygame.Rect(700,self.Box_y,90,50)
        
            
        if self.NameBox.collidepoint(x,y):

            if event.type== pygame.KEYUP:
                G_9=False
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
            WIN.blit(textSurf,(700,self.Box_y+10))
            pygame.draw.rect(WIN,'orange',self.NameBox,2)

        pygame.draw.rect(WIN,'orange',(208,self.animate_box+5,45,45))
        Binary_num1 = Binary_font.render(str(self.a),1,"White")
        WIN.blit(Binary_num1,(220,self.animate_box))

        pygame.draw.rect(WIN,'orange',(268,self.animate_box+5,45,45))
        Binary_num2 = Binary_font.render(str(self.b),1,"White")
        WIN.blit(Binary_num2,(280,self.animate_box))

        pygame.draw.rect(WIN,'orange',(328,self.animate_box+5,45,45))
        Binary_num3 = Binary_font.render(str(self.c),1,"White")
        WIN.blit(Binary_num3,(340,self.animate_box))

        pygame.draw.rect(WIN,'orange',(388,self.animate_box+5,45,45))
        Binary_num4 = Binary_font.render(str(self.d),1,"White")
        WIN.blit(Binary_num4,(400,self.animate_box))

        pygame.draw.rect(WIN,'orange',(448,self.animate_box+5,45,45))
        Binary_num5 = Binary_font.render(str(self.e),1,"White")
        WIN.blit(Binary_num5,(460,self.animate_box))

        pygame.draw.rect(WIN,'orange',(508,self.animate_box+5,45,45))
        Binary_num6 = Binary_font.render(str(self.f),1,"White")
        WIN.blit(Binary_num6,(520,self.animate_box))

        pygame.draw.rect(WIN,'orange',(568,self.animate_box+5,45,45))
        Binary_num7 = Binary_font.render(str(self.g),1,"White")
        WIN.blit(Binary_num7,(580,self.animate_box))

        pygame.draw.rect(WIN,'orange',(628,self.animate_box+5,45,45))
        Binary_num8 = Binary_font.render(str(self.h),1,"White")
        WIN.blit(Binary_num8,(640,self.animate_box))
        
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
            G_9=True
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
            G_9=True
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
            G_9=True
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
            G_9=True
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
            G_9=True
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
            G_9=True
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
            G_9=True
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
            G_9=True
            self.text=''
            self.G=True
            Box_y+=60
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/win.wav'))

        if G_9:
            self.text=''
        
# # Driver code
# NameBox = pygame.Rect(50,70,250,50)
# textBox = pygame.Rect(225,150,250,50)
# selectBox = 0
# text = ''

# Window function displays everything
def window(event,first,second,Third,fourth,fifth,sixth,seventh,eighth):
    global text,selectBox,Milliseconds,Time,score
    # WIN.fill('orange')
    WIN.blit(Game_BG,(200,0))
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
    WIN.blit(Time_text,(700,0))

    score_text = Binary_font.render(str(score),1,"Green")
    WIN.blit(score_text,(720,550))

    # Allows to update screen everysecond
    pygame.display.update()

# Function which saves data at the end and the gameover screen
def gameover(No_times,realtime):
    No_times+=1
    clock=pygame.time.Clock()
    clock.tick(8)
    Over_text = Binary_font.render("Game Over!",1,"WHITE")
    WIN.blit(Over_text,(350,280))
    pygame.display.update()
    clock.tick(8)
    Over_text = Binary_font.render("Game Over!",1,"RED")
    WIN.blit(Over_text,(350,280))
   
    pygame.display.update()
    if No_times==10:
        Score_text = Binary_font.render("You score is",1,'RED')
        WIN.blit(Score_text,(350,340))
        pygame.display.update()
        pygame.draw.rect(WIN,"BLACK",(400,400,120,50))
        Score_text = Binary_font.render(str(realtime),1,'RED')
        WIN.blit(Score_text,(450,400))
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
        # pygame.quit()
        restart()
        
    gameover(No_times,realtime)

def restart():
 
    levels()

# Main function which begins everything
def main():
    # Globalising time and second to change according to game
    global G_1,G_2,G_3,G_4,G_5,G_6,G_7,G_8,Box_y,score,G_9,Milliseconds,list_scores,Time,level
    clock=pygame.time.Clock()
    Box_y=1040
    G_1=False
    G_2=False
    G_3=False
    G_4=False
    G_5=False
    G_6=False
    G_7=False
    G_8=False
    G_9=False
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
        # Using random binary or hex numbers 
        if first.G:
            if level<=4:
                first = Binary_boxes(r.randint(0,level4),r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                first = Binary_boxes(0,0,0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            first.G=False
            interval=Time
            interval-=inter_range
            
        if second.G and Time==interval:
            if level <= 4:
                second = Binary_boxes(r.randint(0,level4),r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                second = Binary_boxes(0,0,0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            second.G=False
            interval=Time
            interval-=inter_range

        elif Third.G and Time==interval:
            if level <= 4:
                Third = Binary_boxes(r.randint(0,level4),r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                Third = Binary_boxes(0,0,0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            Third.G=False
            interval=Time
            interval-=inter_range

        elif Fourth.G and Time==interval:
            if level <= 4:
                Fourth = Binary_boxes(r.randint(0,level4),r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                Fourth = Binary_boxes(0,0,0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            Fourth.G=False
            interval=Time
            interval-=inter_range

        elif Fifth.G and Time==interval:
            if level <= 4:
                Fifth = Binary_boxes(r.randint(0,level4),r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                Fifth = Binary_boxes(0,0,0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            Fifth.G=False
            interval=Time
            interval-=inter_range

        elif sixth.G and Time==interval:
            if level <= 4:
                sixth = Binary_boxes(r.randint(0,level4),r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                sixth = Binary_boxes(0,0,0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            sixth.G=False
            interval=Time
            interval-=inter_range

        elif seventh.G and Time==interval:
            if level <= 4:
                seventh = Binary_boxes(r.randint(0,level4),r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                seventh = Binary_boxes(0,0,0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
            seventh.G=False
            interval=Time
            interval-=inter_range

        elif eighth.G and Time==interval:
            if level <= 4:
                eighth = Binary_boxes(r.randint(0,level4),r.randint(0,level3),r.randint(0,level2),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1),r.randint(0,1))
            elif level == 5:
                eighth = Binary_boxes(0,0,0,0,0,0,list_of_hex[r.randint(0,15)],list_of_hex[r.randint(0,15)])
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

main_menu()

