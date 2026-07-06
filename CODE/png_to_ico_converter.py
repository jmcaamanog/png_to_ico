import os
import sys
import subprocess
import webbrowser  # <-- Necesario para abrir LinkedIn
from tkinter import filedialog, messagebox
from PIL import Image
import customtkinter as ctk

# Configuración básica de la ventana
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    """ Función mágica para que el .exe encuentre el icono de la ventana al compilarse """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("Conversor de iconos Nemo")
        self.geometry("420x480") # Un pelín más alto para alojar el botón Acerca de
        self.resizable(False, False)

        # --- ICONO DE LA VENTANA ---
        # Intenta cargar el icono app_icon.ico en la barra superior izquierda de Windows
        try:
            self.iconbitmap(resource_path("app_icon.ico"))
        except:
            pass # Si no existe, usa el de por defecto sin dar error

        self.image_path = None

        # --- DISEÑO DE LA INTERFAZ ---
        self.lbl_title = ctk.CTkLabel(self, text="Nemo ICO Maker", font=ctk.CTkFont(size=24, weight="bold"))
        self.lbl_title.pack(pady=(15, 10))

        self.btn_load = ctk.CTkButton(self, text="1. Cargar PNG", command=self.load_image, width=160, height=35)
        self.btn_load.pack(pady=5)

        self.preview_frame = ctk.CTkFrame(self, width=160, height=160)
        self.preview_frame.pack(pady=10)
        self.preview_frame.pack_propagate(False)

        self.lbl_preview = ctk.CTkLabel(self.preview_frame, text="Sin imagen")
        self.lbl_preview.pack(expand=True, fill="both")

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=15)

        self.btn_export_win = ctk.CTkButton(self.buttons_frame, text="Icono Windows", command=self.export_windows, state="disabled", width=120, height=35, fg_color="gray40", text_color_disabled="gray80", font=ctk.CTkFont(weight="bold"))
        self.btn_export_win.grid(row=0, column=0, padx=10)

        self.btn_export_app = ctk.CTkButton(self.buttons_frame, text="Icono App", command=self.export_app, state="disabled", width=120, height=35, fg_color="gray40", text_color_disabled="gray80", font=ctk.CTkFont(weight="bold"))
        self.btn_export_app.grid(row=0, column=1, padx=10)

        self.lbl_status = ctk.CTkLabel(self, text="", text_color="green", wraplength=380)
        self.lbl_status.pack(pady=5)

        # --- BOTÓN ACERCA DE ---
        self.btn_about = ctk.CTkButton(self, text="Acerca de...", font=ctk.CTkFont(underline=True), fg_color="transparent", hover_color="gray30", text_color="gray70", command=self.show_about)
        self.btn_about.pack(side="bottom", pady=10)

    # --- LÓGICA DE LA VENTANA "ACERCA DE" ---
    def show_about(self):
        about_win = ctk.CTkToplevel(self)
        about_win.title("Acerca de Nemo ICO Maker")
        about_win.geometry("450x320")
        about_win.resizable(False, False)
        
        # Bloquea la ventana principal hasta que cierres esta
        about_win.grab_set() 
        about_win.attributes('-topmost', True)
        
        try:
            about_win.iconbitmap(resource_path("app_icon.ico"))
        except:
            pass

        ctk.CTkLabel(about_win, text="Nemo ICO Maker", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=(20, 5))
        
        desc = ("Herramienta de escritorio ligera diseñada para convertir\n"
                "automáticamente imágenes PNG en iconos nativos de Windows (.ico).\n"
                "Garantiza la máxima nitidez sin depender de terceros.")
        ctk.CTkLabel(about_win, text=desc).pack(pady=10)
        
        author = ("Autor:\nJosé Manuel Caamaño González\n"
                  "Arquitecto Técnico & BIM Manager\n"
                  "Digital Product Lead | ConTech & Digital Twin SaaS")
        ctk.CTkLabel(about_win, text=author, font=ctk.CTkFont(weight="bold")).pack(pady=10)
        
        btn_linkedin = ctk.CTkButton(about_win, text="🔗 Conectar en LinkedIn", fg_color="#005BC4", hover_color="#004394", command=lambda: webbrowser.open("https://www.linkedin.com/in/jmcaamanog/"))
        btn_linkedin.pack(pady=15)

    # --- LÓGICA DEL PROGRAMA (Carga y Exportaciones) ---
    def load_image(self):
        file_path = filedialog.askopenfilename(title="Selecciona un archivo PNG", filetypes=[("Archivos PNG", "*.png")])
        if file_path:
            self.image_path = file_path
            self.lbl_status.configure(text="")
            try:
                img = Image.open(self.image_path)
                img.thumbnail((160, 160))
                ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
                self.lbl_preview.configure(image=ctk_img, text="")
                
                self.btn_export_win.configure(state="normal", fg_color="#005BC4", hover_color="#004394", text_color="white")
                self.btn_export_app.configure(state="normal", fg_color="#005BC4", hover_color="#004394", text_color="white")
            except Exception as e:
                messagebox.showerror("Error garrafal", f"No se ha podido cargar la imagen:\n{e}")
                self.image_path = None
                self.btn_export_win.configure(state="disabled", fg_color="gray40")
                self.btn_export_app.configure(state="disabled", fg_color="gray40")
                self.lbl_preview.configure(image="", text="Error al cargar")

    def export_windows(self):
        if not self.image_path: return
        try:
            original_dir = os.path.dirname(self.image_path)
            original_filename = os.path.basename(self.image_path)
            filename_without_ext = os.path.splitext(original_filename)[0]
            
            export_folder = os.path.join(original_dir, "_export")
            os.makedirs(export_folder, exist_ok=True)
            save_path = os.path.join(export_folder, f"{filename_without_ext}.ico")

            img = Image.open(self.image_path)
            img.save(save_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])

            self.lbl_status.configure(text=f"¡Listo! Guardado en: _export")
            self._ask_to_open_folder(save_path)
        except Exception as e:
            messagebox.showerror("Error", f"Problema al exportar: {e}")

    def export_app(self):
        if not self.image_path: return
        try:
            original_dir = os.path.dirname(self.image_path)
            original_filename = os.path.basename(self.image_path)
            filename_without_ext = os.path.splitext(original_filename)[0]
            
            export_folder = os.path.join(original_dir, "_export_app")
            os.makedirs(export_folder, exist_ok=True)

            ico_path = os.path.join(export_folder, f"app_icon.ico")
            img = Image.open(self.image_path)
            img.save(ico_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])

            png_path = os.path.join(export_folder, f"app_icon_256.png")
            img_resized = img.resize((256, 256), Image.Resampling.LANCZOS)
            img_resized.save(png_path, format='PNG')

            self.lbl_status.configure(text=f"Set de APP creado en: _export_app")
            
            mensaje = (
                f"¡Set de iconos para tu App generado con éxito!\n\n"
                f"Se han creado dos archivos en la carpeta _export_app:\n"
                f"1. app_icon.ico (Para compilar tu .exe)\n"
                f"2. app_icon_256.png (Por si lo necesitas dentro del código)\n\n"
                f"¿Quieres abrir la carpeta ahora?"
            )
            if messagebox.askyesno("¡Kit de App Exportado!", mensaje):
                ruta_absoluta = os.path.normpath(ico_path)
                subprocess.Popen(f'explorer /select,"{ruta_absoluta}"')
        except Exception as e:
            messagebox.showerror("Error", f"Problema al exportar el kit de app: {e}")

    def _ask_to_open_folder(self, file_path):
        mensaje = "¿Todo listo, jefe!\n\n¿Quieres abrir la carpeta ahora para verlo?"
        if messagebox.askyesno("¡Exportado con éxito!", mensaje):
            ruta_absoluta = os.path.normpath(file_path)
            subprocess.Popen(f'explorer /select,"{ruta_absoluta}"')

if __name__ == "__main__":
    app = App()
    app.mainloop()