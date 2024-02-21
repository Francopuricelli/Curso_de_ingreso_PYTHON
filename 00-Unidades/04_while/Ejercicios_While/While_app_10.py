import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_pos = 0
        acumulador_neg = 0
        Contador_pos = 0
        contador_neg = 0   
        contador_ceros = 0
        suma = 0
        num = 0
        while True:
            suma = prompt("mensaje","Ingrese numero: ")
            if suma != None and suma != "":
                suma = int(suma)
            else:
                break
            if suma > 0:
                acumulador_pos += suma
                Contador_pos += 1
            elif suma < 0:
                acumulador_neg += suma
                contador_neg += 1
            else:
                contador_ceros += 1
            
        diferencia = Contador_pos - contador_neg
        mensaje = f"resultado \n la suma acumulada de los positivos es {acumulador_pos} \n la suma acumulada de los      negativos es {acumulador_neg} \n la Cantidad de números positivos ingresados es {Contador_pos} \n la Cantidad de números negativos ingresados es {contador_neg } \n la cantidad de ceros es {contador_ceros} \n la diferencia es {diferencia}"
        alert("mensaje", mensaje)



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
