import pygame
import time
import pygame.midi

pygame.midi.init()
player= pygame.midi.Output(0)
player.set_instrument(7, 1)

major=[0,4,7,12]
G3 = 55
A4 = 57
B4 = 59
C4 = 60
D4 = 62
E4 = 64
F4s = 66
G4 = 67

def go(note, duration):
    player.note_on(note, 127,1)
    time.sleep(duration)
    player.note_off(note,127,1)
    print(note, duration)

def arp(base,ints):
    for n in ints:
        go(base+n, 1, 127)

def chord(base, ints):
    player.note_on(base,127,1)
    player.note_on(base+ints[1],127,1)
    player.note_on(base+ints[2],127,1)
    player.note_on(base+ints[3],127,1)
    time.sleep(1)
    player.note_off(base,127,1)
    player.note_off(base+ints[1],127,1)
    player.note_off(base+ints[2],127,1)
    player.note_off(base+ints[3],127,1)
    
def end():
       pygame.quit()
       
def main():


    go(G3, 3.5)
    go(A4, .5)
    go(C4, .5)
    go(B4, .5)
    go(A4, .5)
    go(D4, 1.5)
    go(D4, 1.5)
    go(D4, .5)
    go(E4, .5)
    go(B4, .5)
    go(C4, .5)
    go(A4, 1.5)
    go(A4, 1.5)
    go(A4, .5)
    go(C4, .5)
    go(B4, .5)
    go(A4, .5)
    go(G3, .5)    
    go(G4, .5)
    go(F4s, .5)
    go(E4, .5)
    go(D4, .5)
    go(C4, .5)
    go(B4, .5)
    go(A4, .5)
    
    go(G3, 3.5)
    go(A4, .5)
    go(C4, .5)
    go(B4, .5)
    go(A4, .5)
    go(D4, 1.5)
    go(D4, 1.5)
    go(D4, .5)
    go(E4, .5)
    go(B4, .5)
    go(C4, .5)
    go(A4, 1.5)
    go(A4, 1.5)
    go(A4, .5)
    go(C4, .5)
    go(B4, .5)
    go(A4, .5)
    go(G3, .5)
    go(D4, .5)
    go(A4, .5)
    go(B4, .5)
    go(G3, 2.5)



main()