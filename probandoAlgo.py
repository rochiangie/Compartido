import tkinter as tk

class Cuestionario:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuestionario para Conocerse Mejor")

        self.preguntas = [
            "1. ¿Cuál es tu película favorita?",
            "2. ¿Qué tipo de música te gusta?",
            "3. ¿Cuál es tu lugar favorito para relajarte?",
            "4. ¿Tienes alguna habilidad o pasatiempo que te apasione?",
            "5. ¿Qué significa el éxito para ti?",
        ]

        self.respuestas = []

        self.label_pregunta = tk.Label(root, text=self.preguntas[0], font=("Arial", 12))
        self.label_pregunta.pack(pady=10)

        self.entry_respuesta = tk.Entry(root, width=50)
        self.entry_respuesta.pack(pady=10)

        self.boton_siguiente = tk.Button(root, text="Siguiente Pregunta", command=self.siguiente_pregunta)
        self.boton_siguiente.pack(pady=10)

    def siguiente_pregunta(self):
        respuesta_actual = self.entry_respuesta.get()
        self.respuestas.append(respuesta_actual)
        self.entry_respuesta.delete(0, tk.END)  # Limpiar la entrada

        if len(self.respuestas) < len(self.preguntas):
            # Mostrar la siguiente pregunta
            self.label_pregunta.config(text=self.preguntas[len(self.respuestas)])
        else:
            # Se han respondido todas las preguntas, mostrar las respuestas
            self.mostrar_respuestas()

    def mostrar_respuestas(self):
        self.label_pregunta.config(text="¡Gracias por responder!")

        for i, pregunta in enumerate(self.preguntas):
            respuesta = self.respuestas[i]
            tk.Label(self.root, text=f"{pregunta}\nRespuesta: {respuesta}", font=("Arial", 10)).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    cuestionario = Cuestionario(root)
    root.mainloop()
