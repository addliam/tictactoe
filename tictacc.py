from itertools import permutations
import os
import time
brd={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
win = ['123','456','789','147','258','369','753','951']
u1=[]
u2=[]
used=[]
cont=0
t='\t'*2
def main():
    def restart():
        global brd 
        global cont
        global u1
        global u2
        global used
        x=brd.keys
        brd={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
        cont=0
        u1=[]
        u2=[]
        used=[]      
    def p():
        os.system('clear') 
        show(brd)
    def digit(n):
        if n.isdigit() and int(n) in range(1,10):
            return True
        else:
            return False    
    def show(board):
        print('\n'*2)
        print(t+board['1'] + '|' + board['2'] + '|' + board['3'])
        print(t+'-+-+-')
        print(t+board['4'] + '|' + board['5'] + '|' + board['6']) 
        print(t+'-+-+-')
        print(t+board['7'] + '|' + board['8'] + '|' + board['9'])
    #show(brd)   
    def test(b):
        perm=list(permutations(b))
        per=[]
        for i in perm:
            per.append(''.join(i))
        if any([j[:3] in win for j in per]):  
           return True   
        else:
           return False
    def p1():
        global brd 
        global cont 
        p()   
        x = str(input('User1: '))
        if digit(x) and x not in used:      
            u1.append(x)
            used.append(x)
            brd[x]='X'
            cont+=1
            #print(u1)        
        else:
            print('Entrada invalida')
            time.sleep(1)       
            p1()                   
    def p2(): 
        global brd 
        global cont
        p()               
        y = str(input('User2: ')) 
        if digit(y) and y not in used:     
            u2.append(y)
            used.append(y)
            brd[y]='0'
            cont+=1       
        else:
            print('Entrada invalida')
            time.sleep(1)   
            p2()
                         
    while True:           
        p1()    
        if test(u1)==True:
            p()
            print('Ganador user1')
            break      
        if cont>=9:
            p()
            print('Es un empate')
            break                 
        p2()     
        if test(u2)==True:
            p()
            print('Ganador user2')
            break
    n=input('Desea jugar de nuevo?: ')
    if n == '1':
        restart()
        main()           
    else:
        exit()                             
if __name__=='__main__':
    main()      
  