# Nemo ICO Maker - Conversor a Windows 🖼️➡️🪟

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-2fa5d6.svg)
![Pillow](https://img.shields.io/badge/Image-Pillow-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

(Arquitecto Técnico_JMC) Herramienta de escritorio ligera diseñada específicamente para la conversión rápida de imágenes PNG a iconos de Windows (`.ico`). Pensada para desarrolladores y creadores de herramientas (como las aplicaciones de la *Nemo Suite*) que necesitan generar iconos multiresolución o empaquetar ejecutables sin depender de servicios web ni perder calidad en el proceso.

## 🚀 La Filosofía de la Herramienta (Fricción Cero)

Cuando estás desarrollando interfaces o compilando ejecutables de tus propios proyectos, perder tiempo configurando resoluciones de iconos rompe el flujo de trabajo. Esta utilidad nace para hacer una sola cosa y hacerla bien: seleccionas un PNG, te genera las carpetas de exportación automáticas y te da exactamente los archivos que necesitas, ya sea para personalizar una carpeta de Windows o para inyectarlo en tu próximo `.exe`.

## 🧠 Características del Software (v2.0)

*   **Exportación Dual:**
    *   **Icono Windows (`_export/`):** Empaqueta automáticamente los tamaños `256x256`, `128x128`, `64x64`, `48x48`, `32x32` y `16x16` en un solo archivo `.ico` para carpetas y accesos directos.
    *   **Icono App (`_export_app/`):** Genera el `.ico` optimizado para compiladores (como PyInstaller) y extrae un `.png` limpio a 256px ideal para usar dentro de la interfaz (UI) de tu aplicación.
*   **Interfaz Dinámica y Proporcionada:** UI limpia con `customtkinter` (Dark Mode nativo). Los botones ofrecen feedback visual (cambian de gris neutro a azul vibrante cuando están listos para usarse).
*   **Acción Rápida:** Mensajes emergentes interactivos que te permiten abrir directamente el explorador de Windows con el nuevo icono ya seleccionado o te chivan el comando exacto de PyInstaller.
*   **Branding Integrado:** La propia aplicación luce su icono nativo en la barra de título de Windows y cuenta con una sección "Acerca de..." con información del creador.

## 📂 Estructura del Repositorio

*   📁 **`CAPTURAS/`**: Galería visual del proyecto. Incluye capturas de pantalla de la interfaz de usuario en funcionamiento.
*   📁 **`EJECUTABLE/`**: Contiene el programa compilado (`.exe`) listo para descargar y usar en Windows, sin necesidad de instalar nada.
*   📄 **`png_to_ico_converter.py`**: El código fuente de la interfaz gráfica y la lógica de conversión.
*   📄 **`app_icon.ico`**: El icono nativo de la aplicación necesario para la compilación.

## ⚙️ Requisitos para el Código Fuente

Si prefieres ejecutar o modificar el software desde el código fuente, necesitarás:

1. Clonar el repositorio y navegar a la carpeta.
2. Instalar las dependencias necesarias:
   ```bash
   pip install customtkinter Pillow
3. Ejecutar el programa:
   ```bash
   python png_to_ico_converter.py

## 🛠️ ¿Cómo compilar tu propio .exe?

1. Si modificas el código y quieres generar tu propio ejecutable con el icono incrustado en la ventana, usa este comando con PyInstaller:
   ```bash
   pyinstaller --noconsole --onefile --icon="app_icon.ico" --add-data "app_icon.ico;." png_to_ico_converter.py
## 👨‍💻 Autor

Jose Manuel Caamaño González | Arquitecto Técnico & BIM Manager.
Digital Product Lead | ConTech & Digital Twin SaaS | BIM, Energy Modeling & Sustainability | Data Analytics (SQL, Power BI)

Hecho con código y café desde A Coruña. ☕

Jose Manuel Caamaño González | [LinkedIn](https://www.linkedin.com/in/jmcaamanog/)isual del proyecto. Incluye capturas de pantalla de la interfaz de usuario en funcionamiento.
*   📁 **`EJECUTABLE/`**: Contiene el programa compilado (`.exe`) listo para descargar y usar en Windows, sin necesidad de instalar Python ni librerías adicionales.
*   📄 **`png_to_ico_converter.py`**: El código fuente de la interfaz gráfica y la lógica de conversión.

## ⚙️ Requisitos para el Código Fuente

Si prefieres ejecutar o modificar el software desde el código fuente, necesitarás:

1. Clonar el repositorio y navegar a la carpeta.
2. Instalar las dependencias necesarias:
   ```bash
   pip install customtkinter Pillow
3. Ejecutar el programa::
   ```bash
   python png_to_ico_converter.py
## 👨‍💻 Autor

Jose Manuel Caamaño González | Arquitecto Técnico & BIM Manager.
Digital Product Lead | ConTech & Digital Twin SaaS | BIM, Energy Modeling & Sustainability | Data Analytics (SQL, Power BI)

Hecho con código y café desde A Coruña. ☕

Jose Manuel Caamaño González | [LinkedIn](https://www.linkedin.com/in/jmcaamanog/)
