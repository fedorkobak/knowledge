import tkinter as tk
import pyscreenshot as ImageGrab

def take_screenshot(root:tk.Tk):
    '''
    Taking screeshot of the given
    tkinter application. And displays
    it using jupyter funciton `display`.

    Parameters
    ----------
    root:tk.Tk
        tkinter application instalce;
    '''
    root.update()
    
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = x + root.winfo_width()
    h = y + root.winfo_height()
    
    screenshot = ImageGrab.grab(bbox=(x, y, w, h))
    
    root.destroy()
    display(screenshot)
