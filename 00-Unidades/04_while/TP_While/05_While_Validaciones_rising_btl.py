import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador = 0
        edad = 0
        legajo_a = 0
        while True:
            apellido = prompt("mensaje","Ingrese su apellido: ")
            if apellido == None:
                break
            edad = int(edad)

            while True:
                edad = prompt ("mensaje"," Porfavor ingrese su edad: ")
                edad = int(edad)
                if edad >= 18 and edad <= 90:
                    break
                alert("error","la edad debe ser entre 18 años y 90 años")
                edad = prompt("mensaje","ingrese la edad nuevamente")

            while True:
                legajo = prompt("mensaje","Ingrese su numero de legajo")
                legajo= int(legajo)
                if legajo >= 1000 and legajo <= 9000:
                    break
                else:
                    alert("error","Su numero de legajo debe tener 4 cifras y no debe tener dos ceros a la izquierda")
                legajo = prompt("mensaje","reingrese su numero de legajo porfavor")




            self.txt_apellido.delete(0, "end")
            self.txt_apellido.insert(0, apellido)

            self.txt_edad.delete(0, "end")
            self.txt_edad.insert(0, edad)

            self.txt_legajo.delete(0, "end")
            self.txt_legajo.insert(0, legajo)
            break
                
                    
                    
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        edad = int(edad)
        apellido = prompt("iNGRESO DE DATOS", "Ingrese su apellido: ")
        apellido = str(apellido)
        while apellido != edad:
            edad = prompt("ingreso", "ingrese su edad")
            edad = int(edad)
            if edad > 90 or edad < 17:
                edad = prompt("ERROR","REINGRESAR EDAD")
            while not edad or apellido:
                estado = prompt(self.combobox_tipo.get(),"ingrese estado")
                estado = str (estado)
                if estado != "Soltero" and estado != "Casado" and estado != "Divorciado" and estado != "Viudo":
                    estado = prompt("ERROR","REINGRESAR ESTADO")
                '''
             




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
