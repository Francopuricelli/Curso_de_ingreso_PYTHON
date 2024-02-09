import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = str(self.combobox_marca.get())
        cantidad =int(self.combobox_cantidad.get())
        valor_lamparas = 800
        importe_final = valor_lamparas * cantidad
        if cantidad >= 6:
            valor_total_ejercicio_1 = valor_lamparas * cantidad
            valor_lamparas_A = valor_total_ejercicio_1 - (valor_total_ejercicio_1 * 0.50)
            alert("mensaje",f"el valor total con el 50% de descuento es: {valor_lamparas_A}")
        elif cantidad == 5 and marca == "ArgentinaLuz":
            valor_total_ejercicio_2 = valor_lamparas * 5
            valor_lamparas_B = valor_total_ejercicio_2 - (valor_total_ejercicio_2 * 0.40)
            alert("mensaje",f"su valor total con el 40% de descuento por comprar la marca ArgentinaLuz es: {valor_lamparas_B}")
        if not marca == "ArgentinaLuz" and cantidad == 5:
                valor_total_ejercicio_b = valor_lamparas * 5
                valor_no_ArgentinaLuz = valor_total_ejercicio_b - (valor_total_ejercicio_b * 0.30)
                alert("mensaje",f"su valor total con el 30% de descuento es: {valor_no_ArgentinaLuz}")
        elif cantidad == 4 and (marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
            valor_total_ejercicio_c = valor_lamparas * 4 
            valor_con_descuento_felipelamparas = valor_total_ejercicio_c - (valor_total_ejercicio_c * 0.25)
            alert("mensaje",f"su valor total con el 25 % de descuento es de {valor_con_descuento_felipelamparas}")
        elif not (marca == "FelipeLamparas" and marca == "Argentina luz") and cantidad == 4:
            valor_total_ejercicio_3 = valor_lamparas * 4 
            valor_sin_felipelamparas = valor_total_ejercicio_3 - (valor_total_ejercicio_3 * 0.20)
            alert("mensaje",f"el valor total con el 20% es {valor_sin_felipelamparas}")
        if marca == "ArgentinaLuz" and cantidad == 3:
            valor_total_ejercicio_4 = valor_lamparas * 3
            valor_descuento_3 = valor_total_ejercicio_4 - (valor_total_ejercicio_4 * 0.15)
            alert("mensaje",f"su valor total con el 15% de descuento es {valor_descuento_3}")
        elif marca == "FelipeLamparas" and cantidad == 3:
            valor_total_ejercicio_4b = valor_lamparas * 3
            valor_descuento_felipe_3 = valor_total_ejercicio_4b - (valor_total_ejercicio_4b * 0.10)
            alert("mensaje",f"el valor total con el 10% de descuento es {valor_descuento_felipe_3}")
        elif not (marca == "FelipeLamparas" and marca == "Argentina luz") and cantidad == 3:
            valor_total_ejercicio_4c = valor_lamparas * 3
            valor_descuento_otras = valor_total_ejercicio_4c - (valor_total_ejercicio_4c * 0.05)
            alert("mensaje",f"el valor total con el 5% de descuento es de {valor_descuento_otras}")
        
            
        if valor_lamparas_A > 4000:
            descuento_adicional = valor_lamparas_A - (valor_lamparas_A * 0.05)
            alert("mensaje",f"debido a que su compra supero un valor de 4000 se le adicionara un descuento de 5% por lo que el valor total a pagar es de: {descuento_adicional}")
        elif valor_lamparas_B > 4000:
            descuento_adicional_b = valor_lamparas_B - (valor_lamparas_B * 0.05)
            alert("mensaje",f"debido a que su compra supero un valor de 4000 se le adicionara un descuento de 5% por lo que el valor total a pagar es de: {descuento_adicional_b}")
        elif valor_no_ArgentinaLuz > 4000:
            descuento_adicional_c = valor_no_ArgentinaLuz - (valor_no_ArgentinaLuz * 0.05)
            alert("mensaje",f"debido a que su compra supero un valor de 4000 se le adicionara un descuento de 5% por lo que el valor total a pagar es de: {descuento_adicional_c}")
        elif valor_con_descuento_felipelamparas > 4000:
            descuento_adicional_d = valor_con_descuento_felipelamparas - (valor_con_descuento_felipelamparas * 0.05)
            alert("mensaje",f"debido a que su compra supero un valor de 4000 se le adicionara un descuento de 5% por lo que el valor total a pagar es de: {descuento_adicional_d}")
        elif valor_sin_felipelamparas > 4000:
            descuento_adicional_e = valor_sin_felipelamparas - (valor_sin_felipelamparas * 0.05)
            alert("mensaje",f"debido a que su compra supero un valor de 4000 se le adicionara un descuento de 5% por lo que el valor total a pagar es de: {descuento_adicional_e}")
        elif valor_descuento_3 > 4000:
            descuento_adicional_f = valor_descuento_3 - (valor_descuento_3 * 0.05)
            alert("mensaje",f"debido a que su compra supero un valor de 4000 se le adicionara un descuento de 5% por lo que el valor total a pagar es de: {descuento_adicional_f}")
        elif valor_descuento_felipe_3 > 4000:
            descuento_adicional_g = valor_descuento_felipe_3 - (valor_descuento_felipe_3 * 0.05)
            alert("mensaje",f"debido a que su compra supero un valor de 4000 se le adicionara un descuento de 5% por lo que el valor total a pagar es de: {descuento_adicional_g}")
        elif valor_descuento_otras > 4000:
            descuento_adicional_h = valor_descuento_otras - (valor_descuento_otras * 0.05)
            alert("mensaje",f"debido a que su compra supero un valor de 4000 se le adicionara un descuento de 5% por lo que el valor total a pagar es de: {descuento_adicional_h}")
        
        
        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()