import pygame
import time
import pygame.midi

pygame.midi.init()
player= pygame.midi.Output(0)
player.set_instrument(101, 1)

major=[0,4,7,12]
G3 = 54
A4 = 56
B4 = 58
C4 = 60
D4 = 62
E4 = 64
F4s = 65
G4 = 66


def go(note, duration):
    player.note_on(note, 127,1)
    time.sleep(duration)
    player.note_off(note,127,1)

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
    go(G3, 4)
    go(A4, 1)
    go(C4, 1)
    go(B4, 1)
    go(A4, 1)
    go(D4, 2)
    go(D4, 2)
    go(D4, 1)
    go(E4, 1)
    go(B4, 1)
    go(C4, 1)
    go(A4, 2)
    go(A4, 2)
    go(A4, 1)
    go(C4, 1)
    go(B4, 1)
    go(G3, 2)
    go(A4, 1)
    go(G4, 1)
    go(F4s, 1)
    go(E4, 1)
    go(D4, 1)
    go(C4, 1)
    go(B4, 1)
    go(A4, 1)
    go(G3, 4)
    go(A4, 1)
    go(C4, 1)
    go(B4, 1)
    go(A4, 1)
    go(D4, 2)
    go(D4, 2)
    go(D4, 1)
    go(E4, 1)
    go(B4, 1)
    go(C4, 1)
    go(A4, 2)
    go(A4, 2)
    go(A4, 1)
    go(C4, 1)
    go(B4, 1)
    go(A4, 1)
    go(G3, 1)
    go(D4, 1)
    go(A4, 1)
    go(B4, 1)
    go(G3, 3)



main()