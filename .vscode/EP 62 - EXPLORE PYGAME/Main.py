import pygame

"""INIT"""
pygame.init()

# variabel running game
isRun = True

"""MEMBUAT DISPLAY SURFACE OBJECT"""
window = pygame.display.set_mode((600,600))

# object game
# posisi
x = 300
y = 300

# ukuran
panjang = 30
lebar = 30

# kecepatan gerak
speed = 5

while isRun:
    pygame.time.delay(10)
    """USER INPUT, DATABASE INPUT"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    # ambil ke kanan
    if keys[pygame.K_RIGHT] and x < 600 - lebar:
        x += speed

    # ambil ke atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # ambil ke bawah
    if keys[pygame.K_DOWN] and y < 600 - panjang:
        y += speed

    """UPDATE ASSET"""
    window.fill((200,200,200))
    pygame.draw.rect(window,(255,124,0),(x,y,lebar,panjang))

    """RENDER KE DISPLAY"""
    pygame.display.update()

pygame.quit()