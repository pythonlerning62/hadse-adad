import random
import cv2
userChoise=int(input('az 1 ta chand shansi entekhab shavad????'))
com = random.randint(1,userChoise)
count=0
start=False
while not start:
    user =int(input('hadse khod ra vared konid>>>>'))
    if count==5:
        print(f'tedade talashe mojaze shoma tamam shod va adade morede nazar {com} bood')
        img1 = cv2.imread('losse2.jpg')
        cv2.imshow('opencv',img1)
        c = cv2.waitKey(0)
        cv2.destroyAllWindows()
        break
    if user==com:
        print(f'afarin shoma barande shodid va adade morede nazar {com} bood')
        count+=1
        print(f'talashe shomareye {count}')
        img = cv2.imread('won.jpg')
        cv2.imshow('opencv',img)
        c = cv2.waitKey(0)
        cv2.destroyAllWindows()
              
        start=True
    elif user>com:
        print('hadse shoma bishtar ast') 
        count+=1
        print(f'talashe shomareye {count}')
    else:
        print('hadse shoma kamtar ast')
        count+=1
        print(f'talashe shomareye {count}')

              