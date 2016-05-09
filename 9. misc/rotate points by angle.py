from math  import *

def rotate(y, x, alpha):
            ''' calculate point coordination as rotation based on origin of coordination system;
            pivot point: x=0, y=0'''
            alpha = -alpha
            print('alpha:', alpha)
            print('x1,y1: ',x, y)
            if alpha != 0:
                r = sqrt(x*x + y*y)
                print('r: ', r)
                a1 = asin(y/r)
                a2 = a1 + radians(alpha)
                print('a2: ', degrees(a2))
                x = r * cos(a2)
                y = r * sin(a2)
                print('x2,y2: ',x, y)
            return [int(x),int(y)]


def rotate_2(x, y, alpha):
            ''' calculate point coordination as rotation based on origin of coordination system;
            pivot point: x=0, y=0
            x2 = x cos(a) - y sin(a)
            y2 = x sin(a) + y cos(a)
            (a) mierzone przeciwnie do ruchu wskazówek zegara
            '''
            print('alpha:', alpha)
            print('x1, y1:', x, y)
            ar = -radians(alpha)
            x2 = x * cos(ar) - y * sin(ar)
            y2 = x * sin(ar) + y * cos(ar)
            print('x2, y2:', int(x2), int(y2))
            return [int(x2),int(y2)]

def forward(x, y, dist, alpha):
            print('dist, alpha:', dist, alpha)
            print('x1, y1:', x, y)
            alpha = alpha
            x = x + int((dist * sin(radians(alpha))))
            y = y + int((dist * cos(radians(alpha))))
            print('x2, y2:', x, y)
            return [x,y]

print('rotate return:',rotate(10,0,0))
print('rotate return:',rotate(10,0,90))
print('rotate return:',rotate(10,0,180))

print()

print('rotate_2 return:',rotate_2(10,0,0))
print('rotate_2 return:',rotate_2(10,0,90))
print('rotate_2 return:',rotate_2(10,0,180))

##print('forward:', forward(0, 0, 10, 0))
##print('forward:', forward(0, 0, 10, 90))
##print('forward:', forward(0, 0, 10, 180))



def test (a, b):
    print(a)
    print(b)


test(1,2)

test((3,4))




