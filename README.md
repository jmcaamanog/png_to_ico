# Nemo ICO Maker - Conversor a Windows 🖼️➡️🪟

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-2fa5d6.svg)
![Pillow](https://img.shields.io/badge/Image-Pillow-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

(Arquitecto Técnico_JMC) Herramienta de escritorio ligera diseñada específicamente para la conversión rápida de imágenes PNG a iconos de Windows (`.ico`). Pensada para desarrolladores y creadores de herramientas (como las aplicaciones de la *Nemo Suite*) que necesitan generar iconos multiresolución sin depender de servicios web ni perder calidad en el proceso.

## 🚀 La Filosofía de la Herramienta (Fricción Cero)

Cuando estás desarrollando interfaces o compilando ejecutables de tus propios proyectos, perder tiempo configurando resoluciones de iconos rompe el flujo de trabajo. Esta utilidad nace para hacer una sola cosa y hacerla bien: seleccionas un PNG, te genera una carpeta de exportación automática en la misma ubicación y te empaqueta el archivo `.ico` con todos los tamaños estándar de Windows (desde 256x256 hasta 16x16) incrustados para que se vea nítido en cualquier parte del sistema operativo.

## 🧠 Características del Software (v1.0)

*   **Conversión Multiresolución:** Empaqueta automáticamente los tamaños `256x256`, `128x128`, `64x64`, `48x48`, `32x32` y `16x16` en un solo archivo.
*   **Gestión Inteligente de Directorios:** Crea automáticamente una subcarpeta `_export/` junto al archivo original para no ensuciar tu espacio de trabajo.
*   **Interfaz Minimalista y Dark Mode:** UI limpia con `customtkinter` que se adapta al tema de tu sistema, con previsualización en tiempo real de la imagen cargada.
*   **Acción Rápida:** Mensajes emergentes interactivos que te permiten abrir directamente el explorador de Windows con el nuevo icono ya seleccionado.

## 📂 Estructura del Repositorio

*   📁 **`CAPTURAS/`**: Galería visual del proyecto. Incluye capturas de pantalla de la interfaz de usuario en funcionamiento.
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
