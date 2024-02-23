import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:
apellido:
---
Ejercicio: for_01
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        '''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''




    def btn_mostrar_on_click(self):
        continuar = True
        Flag = True
        minimo = 0
        contador_tecnologia_IOT = 0
        Contador_tecno_IA = 0
        Contador_tecno_RV_RA = 0
        Contador_tecno_IOT = 0
        tecno_mayor_votada = 0
        contador_masculino = 0
        contador_femenino = 0 
        contador_otro = 0
        contador_IOT_edad = 0
        contador_fem_IA = 0
        acumuolador_edad_fem = 0
        nombre_min = ""
        genero_min = ""
        while continuar == True:
            nombre = input("ingrese nombre")

            edad = input("ingrese su edad")
            edad = int(edad)
            while edad < 18:
                edad = input("Reingrese su edad ")
                edad = int(edad)
            genero = input("ingrese genero")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Reingrese genero porfavor ")

            tecnologia = input("ingrese tecnologia ")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia =input("Ingrese la tecnologia nuevamente ")

            #1
            if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
                contador_tecnologia_IOT += 1

            #2
            if tecnologia == "IA":
                Contador_tecno_IA += 1
            #4
            elif tecnologia == "IOT":
                Contador_tecno_IOT += 1
                if edad >= 18 and edad <= 25 or edad >= 33 and edad <= 42:
                    contador_IOT_edad += 1
            else:
                Contador_tecno_RV_RA += 1
            if Contador_tecno_IA > Contador_tecno_IOT and Contador_tecno_IA > Contador_tecno_RV_RA:
                tecno_mayor_votada = "IA"
            elif Contador_tecno_IOT > Contador_tecno_IA and Contador_tecno_IOT > Contador_tecno_RV_RA:
                tecno_mayor_votada = "IOT"
            else:
                tecno_mayor_votada = "RV/RA"
                if edad < minimo or Flag == True:
                    minima = edad
                    nombre_min = nombre
                    genero_min = genero
                    Flag == False   

            
            #3
            if genero == "Masculino":
                contador_masculino += 1
            elif genero == "Femenino":
                contador_femenino += 1
                if tecnologia == "IA":
                    contador_fem_IA += 1
                    acumuolador_edad_fem += edad
            else:
                contador_otro += 1
            continuar = question("mensaje","Desea continuar?")

        total_empleados = contador_masculino + contador_femenino + contador_otro
        
        porcentaje_masculinos = (contador_masculino * 100) / total_empleados
        porcentaje_femeninos = (contador_femenino * 100) / total_empleados
        porcentaje_otro  = (contador_otro * 100) / total_empleados
        
        #4
        porcentaje_IOT_edad = (contador_IOT_edad * 100) / total_empleados #PUEDE DIVIDIRSE POR EL CONTA DE IOT DE ARRIBA
        #5
        if contador_fem_IA != 0:
            promedio_edad_fem = acumuolador_edad_fem / contador_fem_IA

        if Contador_tecno_RV_RA == True:
            print(f"{minima} {genero_min}, {nombre_min}")
        else:
            print("Nadie eligio RV/RA")


        print(f"cantidad de empleados de género masculino que votaron por IOT o IA entre 25 y 50 años: {contador_tecnologia_IOT} \n Tecnologia mas votada: {tecno_mayor_votada} \n Porcentajes \n\t Porcentaje masculino{porcentaje_masculinos} \t Porcentaje femenino: {porcentaje_femeninos} \t Porcentaje Otro: {porcentaje_otro} \t Porcentaje de los que votaron IOT y el rango de edad (18-25 o 33-42) {porcentaje_IOT_edad} \n Promedio de edad del genero femenino {promedio_edad_fem}. " )

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()