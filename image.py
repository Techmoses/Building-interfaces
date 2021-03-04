from tkinter import *
window =Tk()
window.title('Image Example')
img = ( 'lotto.gif')
label =Label(window, bg='yellow')
btn = Button( window)
txt = Text( window, width=25, height=7)
txt.insert('1.1','Python Fun!')
can =\
Canvas( window, width =100,height=100, bg='cyan')
can.create_line(0,0,100,100,width =25, fill = 'yellow')
label.pack( side =TOP )
btn.pack( side = LEFT, padx = 10)
txt.pack( side = LEFT)
can.pack( side = LEFT, padx = 10)
window.mainloop()
           
