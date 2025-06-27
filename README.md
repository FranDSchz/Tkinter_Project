# Tkinter\_Project: WorldTime+

Bienvenido al repositorio del proyecto "WorldTime+". Esta es una aplicación de escritorio desarrollada en Python con Tkinter que permite a los usuarios obtener información útil sobre diferentes países del mundo, como la hora local, datos culturales y conversión de divisas.

### Tecnologías Principales

  * **Lenguaje:** Python 3
  * **Interfaz Gráfica:** Tkinter (ttk)
  * **Manejo de Zonas Horarias:** `pytz`
  * **Control de Versiones:** Git y GitHub
  * **Gestión de Proyecto:** Trello (Kanban)

-----

## 🚀 Gestión del Proyecto y Frameworks Ágiles

Para organizarnos de manera eficiente, hemos adoptado varias prácticas inspiradas en frameworks ágiles. Esto nos permite colaborar de forma ordenada, mantener la calidad y ser flexibles ante los cambios.

### Nuestro Tablero Kanban en Trello

Toda la planificación de tareas se centraliza en nuestro tablero de Trello. Es nuestra única fuente de verdad sobre qué hay que hacer, quién lo está haciendo y qué está terminado.

➡️ **[Accede a nuestro tablero en Trello aquí](https://trello.com/invite/b/685dfa8ef7e05b50776f18bb/ATTI84e33f78c0bf6bb7457acfc162af4fca0B8E15A5/worldtime-tkinter-project)**

#### Reglas de Uso del Tablero:

1.  **Fuente Única de Tareas:** Si una tarea no está en el tablero, no existe. Antes de empezar a programar, crea una tarjeta en la columna `Backlog`.
2.  **Asignación Clara:** Cada persona se asigna a la tarjeta en la que va a trabajar. **Una persona por tarjeta** para evitar duplicación de esfuerzos.
3.  **Visualiza el Progreso:** Cuando comiences a trabajar en una tarjeta, muévela a la columna `En Proceso`.
4.  **Conexión con Git:** El nombre de tu rama de Git debe estar relacionado con la tarjeta (ej: `feature/T10-widgets-conversor`).
5.  **Tarea Terminada:** Una vez que tu Pull Request es aprobado y fusionado en `main`, mueve la tarjeta a la columna `Finalizado`. ¡Celebra\!
6.  **Usa los Comentarios:** Si tienes dudas sobre una tarea o quieres dejar una nota, usa los comentarios de la tarjeta de Trello.

### Nuestras Prácticas Ágiles

  * **Kanban:** Usamos un tablero Kanban para visualizar nuestro flujo de trabajo. Esto nos ayuda a limitar el "trabajo en proceso" y a identificar cuellos de botella.
  * **Desarrollo Iterativo:** En lugar de intentar construir todo de golpe, trabajamos en pequeñas funcionalidades (cada tarjeta es una iteración) que se integran de forma continua en el proyecto principal.
  * **Feature Branching:** Cada nueva funcionalidad o arreglo se desarrolla en su propia rama de Git. Esto mantiene la rama `main` siempre estable y funcional.
  * **Pull Requests (PRs) y Revisión de Código (Code Review):** Ningún código llega a `main` sin ser revisado por al menos otro miembro del equipo a través de un Pull Request. Esto asegura la calidad, comparte conocimiento y reduce errores.

-----

## 💻 Cómo Instalar y Ejecutar el Proyecto

Sigue estos pasos para configurar el entorno de desarrollo en tu máquina.

**1. Clonar el Repositorio**

```bash
git clone https://github.com/FranDSchz/Tkinter_Project.git
cd Tkinter_Project
```

**2. Crear y Activar el Entorno Virtual**
Usamos un entorno virtual para mantener las dependencias del proyecto aisladas. El nuestro se llama `venv-tk-project`.

```bash
# Crear el entorno (solo la primera vez)
python -m venv venv-tk-project

# Activar el entorno (debes hacerlo cada vez que abras una nueva terminal para trabajar)
# En Windows (cmd/PowerShell):
.\venv-tk-project\Scripts\activate
# En macOS / Linux:
source venv-tk-project/bin/activate
```

*Verás `(venv-tk-project)` al inicio de la línea de tu terminal si está activo.*

**3. Instalar las Dependencias**
Con el entorno virtual activado, instala todas las librerías del proyecto con un solo comando:

```bash
pip install -r requirements.txt
```

**4. Ejecutar la Aplicación**
¡Ya está todo listo\! Para lanzar el programa, ejecuta:

```bash
python main.py
```

-----

## 📦 Cómo Añadir Nuevas Dependencias

Si tu tarea requiere una nueva librería que no está en el proyecto (por ejemplo, `Pillow` para imágenes), el proceso es el siguiente:

1.  **Activa tu entorno virtual** (`venv-tk-project`).
2.  Instala la nueva librería con `pip`:
    ```bash
    pip install nombre-de-la-libreria
    ```
3.  **¡Paso Crucial\!** Inmediatamente después de instalarla, actualiza el archivo `requirements.txt` para que el resto del equipo pueda instalarla también.
    ```bash
    pip freeze > requirements.txt
    ```
4.  Añade a tu commit (`git add`) tanto los archivos de código que has modificado como el archivo `requirements.txt` actualizado.
5.  En la descripción de tu Pull Request, menciona que has añadido una nueva dependencia.

-----

## 📂 Estructura del Proyecto

El proyecto está organizado en una estructura modular para facilitar la colaboración:

```
Tkinter_Project/
├── .gitignore         # Ignora archivos innecesarios para Git.
├── README.md          # Este archivo.
├── requirements.txt   # Lista de dependencias de Python para el proyecto.
├── datos.py           # Módulo para centralizar todos los datos.
├── ui.py              # Módulo con la clase de la App y la lógica de la interfaz.
├── main.py            # Punto de entrada de la aplicación (el archivo que se ejecuta).
└── venv-tk-project/   # Carpeta del entorno virtual (ignorada por Git).
```

-----

### **Recordatorio sobre el `.gitignore`**

Finalmente, asegúrate de que tu archivo `.gitignore` incluya el nombre de vuestro entorno virtual para que nunca se suba al repositorio.

Abre `.gitignore` y verifica que tienes esta línea:

```gitignore
# ... otras líneas ...

# Virtual Environments
venv-tk-project/
```

Si no está, añádela.
