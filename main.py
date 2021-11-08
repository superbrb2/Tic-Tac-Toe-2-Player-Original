from tkinter import *
import tkinter.messagebox 

player_turn = True
Tie = 0
#--------------------------------------FUNCTIONS---------------------

def Disable_buttons():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def Player_colour(p1, p2):
    if player_turn == True:
        p1['fg'] = '#93ff8f'
        p2['fg'] = '#b02a2a'


    if player_turn == False:
        p1['fg'] = '#b02a2a'
        p2['fg'] = '#93ff8f' 


def Clicked_button(buttons):
    global player_turn, Tie, p1, p2

    if player_turn == True and buttons['text'] == '':
        buttons['text'] = 'O'
        player_turn = False
        Tie += 1
        Check_for_win()


    elif player_turn == False and buttons['text'] == '':
        buttons['text'] = 'X'
        player_turn = True
        Tie += 1
        Check_for_win()

    else:
        tkinter.messagebox.showerror("Tic-Tac-Toe", "Someone's already gone there!")

    Player_colour(p1, p2)


def Check_for_win():
    

    if (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
   
        Disable_buttons()
        label['text'] = 'Player 1 wins!'
        label.place(rely=0.75, relx=0.05, relwidth=0.9, relheight=0.2)


    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):

            Disable_buttons()
            label['text'] = 'Player 2 wins!'
            label.place(rely=0.75, relx=0.05, relwidth=0.9, relheight=0.2)


    elif(Tie == 9):
        label['text'] = "It's a Tie!"
        label.place(rely=0.75, relx=0.05, relwidth=0.9, relheight=0.2)

#--------------------------------------ROOT--------------------------
root = Tk()
root.title('Tic Tac Toe')
#--------------------------------------CANVAS------------------------

canvas = Canvas(height=366,width=233, bg='#bfd9ff')
canvas.pack()

#--------------------------------------FRAMES------------------------
main_frame = Frame(canvas, bg='#b1cbf2')
main_frame.place(rely=0.05,relx=0.05, relheight=0.6, relwidth=0.9)

#---------------------------------------LINES------------------------

line1 = Frame(main_frame, bg='black')
line2 = Frame(main_frame, bg='black')
line3 = Frame(main_frame, bg='black')
line4 = Frame(main_frame, bg='black')

line1.place(rely=0.05, relx=0.33, relheight=0.9,relwidth=0.02)
line2.place(rely=0.05, relx=0.66, relheight=0.9,relwidth=0.02)
line3.place(rely=0.33, relx=0.05, relheight=0.02,relwidth=0.9)
line4.place(rely=0.66, relx=0.05, relheight=0.02,relwidth=0.9)

#--------------------------------------LABEL---------------------------

p1 = Label(canvas, font='Times 15 bold', text='Player 1', bg='#9dbcfa', bd=5)
p2 = Label(canvas, font='Times 15 bold', text='Player 2', bg='#9dbcfa', bd=5)

p1.place(rely=0.75, relx=0.05, relwidth=0.4, relheight=0.2)
p2.place(rely=0.75, relx=0.55, relwidth=0.4, relheight=0.2)

Player_colour(p1, p2)

label = Label(canvas,font='Times 20 bold', bg='#9dbcfa', bd=5, ) # SEE 'CHECK_FOR_WIN()
#-------------------------------------BUTTONS-------------------------

button1 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button1))
button2 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button2))
button3 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button3))
button4 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button4))
button5 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button5))
button6 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button6))
button7 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button7))
button8 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button8))
button9 = Button(main_frame, bg='#b1cbf2', font='Times 20 bold', command=lambda: Clicked_button(button9))

button1.place(rely=0.03, relx=0.03,relheight=0.3,relwidth=0.3)
button2.place(rely=0.03, relx=0.36,relheight=0.3,relwidth=0.3)
button3.place(rely=0.03, relx=0.69,relheight=0.3,relwidth=0.3)
button4.place(rely=0.36, relx=0.03,relheight=0.3,relwidth=0.3)
button5.place(rely=0.36, relx=0.36,relheight=0.3,relwidth=0.3)
button6.place(rely=0.36, relx=0.69,relheight=0.3,relwidth=0.3)
button7.place(rely=0.69, relx=0.03,relheight=0.3,relwidth=0.3)
button8.place(rely=0.69, relx=0.36,relheight=0.3,relwidth=0.3)
button9.place(rely=0.69, relx=0.69,relheight=0.3,relwidth=0.3)


root.mainloop()