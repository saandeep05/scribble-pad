from tkinter import Tk, Canvas, BOTH, Label, SUNKEN, Button, TOP


def begin(event):
    global oldx, oldy
    # starting points, just after the mouse is clicked
    oldx = event.x
    oldy = event.y


def draw(event):
    global oldx, oldy, canvas
    newx = event.x
    newy = event.y
    # We draw a line from (oldx, oldy) to (newx, newy)
    id = canvas.create_line(oldx, oldy, newx, newy)
    # id of each line is stored in last
    last.append(id)
    oldx = newx
    oldy = newy


def store_last(event):
    # Storing the last element into store
    global last
    if last:
        # Enter the last drawn item into store list
        store.append(last)
    # the same last element will not append to the store list multiple times while mouse is moving without drawing
    last = []


def undo(event):
    # last stores the last element that's been drawn on the screen.
    global last
    if store:
        # Since the last drawn element is always stored at last of the store list, we access it by store[-1]
        # the element is a result of various small lines that we created.
        for i in store[-1]:
            # each line of the element has unique id. So we iterate tha last element and delete each line.
            canvas.delete(i)
        # The element is erased from the screen, but still stored in the store list, so we pop it.
        store.pop(-1)


def clear_all(event):
    # when store is empty, we need not clear the screen since it doesnt have anything to clear
    if store:
        # We need to access all the elements stored in store from last,
        # so that it doesn't give out of index exception
        for i in range(len(store)-1, -1, -1):
            # in each element, we select the id of each line of the element in store[i]
            # for each iteration j has an id of the element in store[i]
            for j in store[i]:
                # deleting the id removes it from the screen
                canvas.delete(j)
            # after this loop, the whole element stored in store[i] is erased from the screen.
            # The element is erased from the screen, but still stored in the store list, so we pop it.
            store.pop(i)


def undo_btn():
    global last
    if store:
        for i in store[-1]:
            canvas.delete(i)
        store.pop(-1)


def clear_all_btn():
    if store:
        for i in range(len(store)-1, -1, -1):
            for j in store[i]:
                canvas.delete(j)
            store.pop(i)


root = Tk()
oldx = 0
oldy = 0
store = []  # this contains the list of all elements that are drawn on the screen
last = []  # this contains the list of id's of all the lines of the last drawn element

# Screen
canvas = Canvas(root, background='white', relief=SUNKEN, width=300, height=300)

# Header
title = Label(root, foreground='navy', background='lightblue', padx=10, font=('verdana', 17, 'italic bold'),
              text='Scribble Pad')
title.pack()

# Event Triggers
canvas.bind('<Button-1>', begin)
canvas.bind('<Button1-Motion>', draw)
canvas.bind('<Control-Button-1>', undo)
canvas.bind('<Motion>', store_last)
canvas.bind('<Control-Button-3>', clear_all)

undo_button = Button(root,
                     border=1,
                     background='#eab676',
                     font=('arial', 10, 'bold'),
                     text='Undo',
                     command=undo_btn)
undo_button.pack(side=TOP)

clear_all_button = Button(root,
                          border=1,
                          background='#eab676',
                          font=('arial', 10, 'bold'),
                          text='Clear Screen',
                          command=clear_all_btn)
clear_all_button.pack(side=TOP)

# Packing the canvas
canvas.pack(expand=True, fill=BOTH)

# Running infinite loop until the window's closed
root.mainloop()
