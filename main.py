import pygame 

print('Setup Start')
pygame.init()
windows =pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
     # check for all events
     for event in pygame.event.get():
         if event.type == pygame.QUIT: 
            print('Quitting...')  
            pygame.quit()   # Close Window
            quit()   # end pygame
<<<<<<< HEAD
=======
      
>>>>>>> c32c3d97d7a1ea39678cecd906506a1b3f319e77

