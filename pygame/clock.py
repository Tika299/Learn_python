import pygame

pygame.init()
#tạo ra một màn hình
screen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
font = pygame.font.Font(None,50)


running = True
text_1 = font.render("+",True,BLACK)
text_2 = font.render("-",True,BLACK)
text_3 = font.render("Start",True,BLACK)
text_4 = font.render("Reset",True,BLACK)

total_secs = 0
start = False

while running:
    #tô màu cho màn hình
    screen.fill(GREY)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.rect(screen,WHITE, (100,50,50,50))
    pygame.draw.rect(screen,WHITE, (100,200,50,50))
    pygame.draw.rect(screen,WHITE, (200,200,50,50))
    pygame.draw.rect(screen,WHITE, (200,50,50,50))
    pygame.draw.rect(screen,WHITE, (300,50,150,50))
    pygame.draw.rect(screen,WHITE, (300,200,150,50))

    screen.blit(text_1,(100,50))
    screen.blit(text_2,(100,200))
    screen.blit(text_1,(200,50))
    screen.blit(text_2,(200,200))
    screen.blit(text_3,(300,50))
    screen.blit(text_4,(300,200))

    pygame.draw.rect(screen,BLACK,(50,520,400,50))
    pygame.draw.rect(screen,WHITE,(60,530,380,30))
    pygame.draw.circle(screen,BLACK,(250,400),110)
    pygame.draw.circle(screen,WHITE,(250,400),100)

    pygame.draw.circle(screen,BLACK,(250,400),5)
    pygame.draw.line(screen,BLACK,(250,400),(250,310))
    pygame.draw.line(screen,BLACK,(250,400),(250,360))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if(mouse_x>100 and mouse_x<150 and mouse_y>50 and mouse_y <100):
                    total_secs+=60
                    print("+")
                elif (mouse_x>100 and mouse_x<150 and mouse_y>200 and mouse_y <250):
                    total_secs-=60
                    print("-")
                elif (mouse_x>200 and mouse_x<250 and mouse_y>50 and mouse_y <100):
                    total_secs+=1
                    print("+")
                elif (mouse_x>200 and mouse_x<250 and mouse_y>200 and mouse_y <250):
                    total_secs-=1
                    print("-")
                elif (mouse_x>300 and mouse_x<450 and mouse_y>50 and mouse_y <100):
                    start = True
                    print("start")
                elif (mouse_x>300 and mouse_x<450 and mouse_y>200 and mouse_y <250):
                    total_secs = 0
                    print("reset")


    if start:
        total_secs-=1
        if total_secs==0:
            start = False
        
    
    if total_secs <0:
        total_secs=0

    mins = int(total_secs/60)
    secs = total_secs - mins*60

    time_now = str(mins) + " : " +str(secs)

    text_time = font.render(time_now,True,BLACK)
    screen.blit(text_time,(120,120))

    #áp dụng màu cho màn hình
    pygame.display.flip()

pygame.quit()