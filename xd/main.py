import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle

class DiagnosticoApp:
    def __init__(self, master):
        self.master = master
        master.title("Proyecto CARRS versión 2.4")

        self.label = ttk.Label(master, text="Responde un breve cuestionario para resolver tu falla")
        self.label.pack()

        self.respuesta_label = ttk.Label(master, text="")
        self.respuesta_label.pack()

        self.realizar_test_button = ttk.Button(master, text="Realizar test", command=self.botones)
        self.realizar_test_button.pack()

        self.salir_button = ttk.Button(master, text="SALIR", command=master.quit)
        self.salir_button.pack()

        # Aplicar un tema de ttkthemes
        style = ThemedStyle(master)
        style.set_theme("arc")

    def botones(self):
        self.limpiar()
        falla = self.fallas()
        self.respuesta_label.config(text="La solución es:\n" + falla)
        self.mostrar_mas_info_button()

    def fallas(self):
        motor = self.preguntar("¿Tienes problemas de motor?")
        if motor:
            combustible = self.preguntar("¿Tu automóvil gasta más combustible de lo debido?")
            ruidoso = self.preguntar("¿Tu motor se escucha muy ruidoso?")
            arranque = self.preguntar("¿Tienes problemas para arrancar el vehículo en frío?")
            fuerza = self.preguntar("¿Sientes que tu motor tiene menos fuerza que antes?")
            if combustible and ruidoso and arranque and fuerza:
                return "Hacer un cambio de aceite: Para resolver este problema, te recomiendo que realices un cambio completo de aceite y filtro. Asegúrate de utilizar el tipo de aceite recomendado por el fabricante de tu vehículo y sigue las instrucciones del manual del propietario."

        suspension = self.preguntar("¿Tienes problemas de suspensión?")
        if suspension:
            gira = self.preguntar("¿Tu volante neutral y el auto gira?")
            desgaste = self.preguntar("¿Has notado que alguna llanta se desgasta más?")
            movimiento = self.preguntar("¿Tu volante se mueve bastante y tiembla?")
            if gira and desgaste and movimiento:
                return "Realizar una alineación y balanceo: Te recomiendo que lleves tu vehículo a un taller especializado para realizar una alineación y balanceo de las llantas. Esto ayudará a mejorar la estabilidad y el manejo del vehículo."

        electrico = self.preguntar("¿Tienes problemas eléctricos?")
        if electrico:
            faros = self.preguntar("¿Tus faros titilan o encienden con poca fuerza?")
            estereo = self.preguntar("¿El estéreo no enciende?")
            crack = self.preguntar("¿El auto emite un crack cuando lo enciendes?")
            arranque_auto = self.preguntar("¿El auto no arranca de ninguna manera?")
            bateria_vieja = self.preguntar("¿Tu batería es muy vieja?")
            if faros and estereo and crack and arranque_auto and bateria_vieja:
                return "Verificar el estado actual de la batería: Puede ser que la batería esté descargada o en mal estado. Te sugiero que revises la batería y, si es necesario, la recargues o reemplaces por una nueva."

        frenos = self.preguntar("¿Tienes problemas con tus frenos?")
        if frenos:
            chillido = self.preguntar("¿Cuando frenas escuchas un chillido agudo?")
            tardanza = self.preguntar("¿Al frenar sientes que tarda más?")
            if chillido and tardanza:
                return "Llegó la hora de cambiar tus pastillas de freno: Es posible que las pastillas de freno estén desgastadas y necesiten ser reemplazadas. Te recomiendo que lleves tu vehículo a un taller para cambiar las pastillas de freno."

        check_engine = self.preguntar("¿La luz check engine se encendió en tu tablero?")
        if check_engine:
            permanente = self.preguntar("¿La luz se mantiene encendida todo el tiempo?")
            if permanente:
                return "Posiblemente tu auto pasará a mejor vida: La luz de check engine puede indicar problemas graves en el motor. Te sugiero que lleves tu vehículo a un mecánico profesional para un diagnóstico más detallado."

        bocina = self.preguntar("¿Tienes problemas con alguna bocina?")
        if bocina:
            no_se_escucha = self.preguntar("¿La bocina no se escucha nada?")
            suficiente_bateria = self.preguntar("¿Tu auto tiene suficiente batería?")
            if no_se_escucha and suficiente_bateria:
                return "Seguro subes demasiado el volumen: Puede ser que la bocina esté dañada o que los cables estén sueltos. Te recomiendo que revises la conexión de la bocina y, si es necesario, la reemplaces."

        return "Sin resultados. Si los problemas persisten, vaya a un mecánico."

    def preguntar(self, pregunta):
        respuesta = messagebox.askyesno("Pregunta", pregunta)
        return respuesta

    def limpiar(self):
        self.respuesta_label.config(text="")
        self.mostrar_mas_info_button(False)

    def mostrar_mas_info_button(self, mostrar=True):
        if mostrar:
            self.mas_info_button = ttk.Button(self.master, text="Más información", command=self.mostrar_mas_informacion)
            self.mas_info_button.pack()
        else:
            if hasattr(self, 'mas_info_button'):
                self.mas_info_button.pack_forget()

    def mostrar_mas_informacion(self):
        if self.respuesta_label.cget("text").startswith("La solución es:"):
            mensaje = self.respuesta_label.cget("text").split("\n", 1)[-1]
            messagebox.showinfo("Más información", mensaje)
        else:
            messagebox.showinfo("Más información", "Aquí puedes agregar un diagnóstico más profesional y específico")

def main():
    root = tk.Tk()
    app = DiagnosticoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
