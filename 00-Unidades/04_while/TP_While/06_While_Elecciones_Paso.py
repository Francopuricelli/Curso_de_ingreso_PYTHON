import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        minimo = 0
        maximo = 0
        flag = True
        contador = 0
        edad = 0
        promedio_edad = 0
        acum_votos = 0
        edad_suma = 0
        cantidad_votos = 0
        candidato_mas_votos = ""
        candidato_menos_votos = ""
        while True:
            nombre_candidato = prompt("mensaje","ingrese el nombre del candidato:")
            nombre_candidato
            if nombre_candidato == None:
                break
            cantidad_votos = prompt("mensaje","ingrese cantidad de votos: ")
            cantidad_votos = int(cantidad_votos)
            if cantidad_votos > 0:
                acum_votos += cantidad_votos
            if flag == True:
                minimo = cantidad_votos
                maximo = cantidad_votos
                candidato_mas_votos = nombre_candidato
                candidato_menos_votos = nombre_candidato
                flag = False
            else:
                if cantidad_votos < minimo:
                    minimo = cantidad_votos
                    candidato_menos_votos = nombre_candidato
                elif cantidad_votos > maximo:
                    maximo = cantidad_votos
                    candidato_mas_votos = nombre_candidato
                    

            if edad != None or edad >= 25:
                edad = prompt("mensaje","Ingrese edad del candidato")
                edad = int(edad)
                if edad == None or edad < 25:
                    alert("mensaje","su edad debe ser de mas de 25 años")
                    edad = prompt("mensaje","reingrese edad")
                edad = int(edad)
                edad_suma += edad
            contador += 1
            promedio_edad = edad_suma / contador
        mensaje = f"{candidato_mas_votos} es el candidato con mas votos ({maximo}) .\n {candidato_menos_votos}, ({edad} años) es el candidato con menos votos ({minimo}) \n el promedio de edades es de: {promedio_edad} \n la cantidad de votos es de: {acum_votos} " 

        alert("mesnaje", mensaje)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()