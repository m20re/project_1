"""
Name: Marvin Orellana
Email: marvinorellana@unomaha.edu
Date: 
Desc: 
"""
from gui import *



def main():
    window = Tk()
    window.title('CSV Reader')
    window.geometry('350x250')
    # makes window part of the GUI class
    GUI(window)

    window.mainloop()

if __name__ == "__main__":
    main()