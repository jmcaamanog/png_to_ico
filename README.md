# Nemo ICO Maker - Conversor a Windows 🖼️➡️🪟

| 🏗️ Perfil & ConTech | 📈 Repositorio & Enlaces |
| :--- | :--- |
| ![Profesión](https://img.shields.io/badge/Profesi%C3%B3n-Arquitectos%20T%C3%A9cnicos-2e7d32?logo=micro%3Abit&logoColor=white&style=plastic) <br> ![Role](https://img.shields.io/badge/Role-BIM%20%26%20ConTech-007ACC?logo=bim360&style=plastic) <br> ![Location](https://img.shields.io/badge/Location-A%20Coru%C3%B1a%20%F0%9F%8C%8A-005B94?logo=lighthouse&logoColor=white&style=plastic) <br> ![Maker](https://img.shields.io/badge/Maker-Software-red?logo=makerbot&style=plastic) <br> ![Hardware](https://img.shields.io/badge/Hardware---grey?style=plastic) <br> ![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&style=plastic) <br> ![Language](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white&style=plastic) | ![Stars](https://img.shields.io/github/stars/jmcaamanog/png_to_ico?style=plastic&color=yellow&logo=github) <br> ![License](https://img.shields.io/github/license/jmcaamanog/png_to_ico?style=plastic&color=green) |

| 🏗️ Perfil & ConTech | 📈 Repositorio & Enlaces |
| :--- | :--- |

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

**Jose Manuel Caamaño González** | Arquitecto Técnico & BIM Manager
Digital Product Lead | ConTech & Digital Twin SaaS | Data Analytics (SQL, Power BI)

Hecho con código y café desde A Coruña. ☕
[LinkedIn](https://www.linkedin.com/in/jmcaamanog/) · [Web](https://jmcaamanog.pages.dev)
