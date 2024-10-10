from tkinter import *
from tkinter import messagebox as msg
from sqlite3 import *


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Database Root Manager")
        self.conn = connect("ambition-db.sql")