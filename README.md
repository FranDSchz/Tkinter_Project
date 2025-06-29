# Tkinter_Project: WorldTime+
### Grupo N°: 4

### Integrantes del Equipo
* 👩‍💻 Lorena Beatriz Vargas
* 👨‍💻 Franco Damián Sánchez
* 👩‍💻 Oriana Aguilar
* 👨‍💻 Nelson Agustin Sotelo
* 👨‍💻 Leandro Goncebat

---

## 📝 Descripción del Proyecto

**WorldTime+** es una aplicación de escritorio desarrollada en Python utilizando la librería Tkinter. El objetivo principal del proyecto es ofrecer a los usuarios una herramienta interactiva para consultar información útil de diferentes países del mundo.

Las características principales implementadas son:

* **Reloj Mundial:** Muestra la hora actual del país seleccionado, actualizada en tiempo real.
* **Panel Informativo:** Proporciona datos útiles como el idioma oficial, la estación del año actual, un dato curioso y la bandera del país.
* **Diferencia Horaria:** Calcula y muestra la diferencia horaria entre el país seleccionado y Argentina.
* **Conversor de Divisas:** Permite convertir un monto desde Pesos Argentinos (ARS) a la moneda local del país seleccionado utilizando tasas de cambio fijas.
* **Interfaz Personalizable:** Incluye un interruptor para cambiar entre un tema visual claro y uno oscuro.

---

## 💻 Procedimiento de Ejecución

Para corregir y ejecutar la aplicación, por favor, sigue estos pasos. El archivo principal de ejecución es `main.py`.

**1. Clonar el Repositorio**
```bash
git clone [https://github.com/FranDSchz/Tkinter_Project.git](https://github.com/FranDSchz/Tkinter_Project.git)
cd Tkinter_Project
```

**2. Crear y Activar el Entorno Virtual**
El proyecto utiliza un entorno virtual para aislar sus dependencias.

```bash
# Crear el entorno (solo la primera vez)
python -m venv venv-tk-project

# Activar el entorno
# En Windows (cmd/PowerShell):
.\venv-tk-project\Scripts\activate
# En macOS / Linux:
source venv-tk-project/bin/activate
```
*La terminal mostrará `(venv-tk-project)` al inicio de la línea si la activación fue exitosa.*

**3. Instalar las Dependencias**
Con el entorno activado, instala todas las librerías necesarias con un solo comando:
```bash
pip install -r requirements.txt
```

**4. Ejecutar la Aplicación**
Una vez instaladas las dependencias, lanza el programa ejecutando el archivo `main.py`:
```bash
python main.py
```

---

## 🚀 Metodología Utilizada

Para la organización del equipo y el trabajo colaborativo, adoptamos un marco de trabajo inspirado en metodologías ágiles, combinando principios de **Kanban** y buenas prácticas de desarrollo de software.

### Nuestro Tablero Kanban en Trello
La planificación y seguimiento de tareas se centralizó en un tablero de Trello, que actuó como nuestra única fuente de verdad sobre el estado del proyecto.

➡️ **[Acceso al Tablero Kanban del Proyecto en Trello](https://trello.com/invite/b/685dfa8ef7e05b50776f18bb/ATTI84e33f78c0bf6bb7457acfc162af4fca0B8E15A5/worldtime-tkinter-project)**

#### Flujo de Trabajo en el Tablero:
1.  **Fuente Única de Tareas:** Todas las funcionalidades se desglosaron en tarjetas en la columna `Backlog`.
2.  **Asignación y Límite de WIP (Work In Progress):** Cada miembro del equipo se asignaba una única tarjeta para moverla a `En Proceso`, limitando el trabajo en curso y fomentando el enfoque.
3.  **Transparencia:** El tablero ofreció una visión clara y en tiempo real del progreso de cada tarea y del proyecto en general.
4.  **Finalización:** Al fusionar el código correspondiente en la rama principal, la tarjeta se movía a `Finalizado`.

### Prácticas Clave de Colaboración
* **Desarrollo Iterativo:** Construimos la aplicación de forma incremental, añadiendo pequeñas funcionalidades (cada tarjeta del tablero) en ciclos cortos.
* **Modularización del Código:** El proyecto se dividió en módulos (`datos.py`, `ui.py`, `main.py`) para permitir el trabajo en paralelo y reducir conflictos.
* **Control de Versiones (Git Flow):**
    * **Feature Branching:** Cada tarea se desarrolló en su propia rama de Git, protegiendo la estabilidad de la rama `main`.
    * **Pull Requests (PRs) y Code Review:** Se adoptó como regla que ningún código podía ser fusionado a `main` sin un Pull Request y la revisión de al menos otro miembro del equipo. Esto garantizó la calidad del código, la transferencia de conocimiento y la detección temprana de errores.

---

## 📦 Cómo Añadir Nuevas Dependencias (Guía para el equipo)

Si una tarea futura requiere una nueva librería, el proceso es:
1.  Activar el entorno virtual (`venv-tk-project`).
2.  Instalar la librería con `pip`.
3.  Actualizar el archivo `requirements.txt` con el comando: `pip freeze > requirements.txt`.
4.  Añadir a un `commit` tanto los cambios en el código como el `requirements.txt` actualizado.

---

## 📂 Estructura del Proyecto

```
Tkinter_Project/
├── .gitignore         # Ignora archivos innecesarios para Git.
├── README.md          # Este archivo.
├── requirements.txt   # Lista de dependencias de Python para el proyecto.
├── datos.py           # Módulo para centralizar todos los datos.
├── ui.py              # Módulo con la clase de la App y la lógica de la interfaz.
├── main.py            # Punto de entrada de la aplicación.
└── venv-tk-project/   # Carpeta del entorno virtual (ignorada por Git).
```