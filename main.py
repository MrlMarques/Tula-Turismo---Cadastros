# main.py

from tkinter import Tk
from views.interface import App
from db.database import inicializar_db

def main():
    # Inicializando o banco de dados
    inicializar_db()

    # Inicializando a interface gráfica
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
