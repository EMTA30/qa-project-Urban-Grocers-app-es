# Proyecto Urban Grocers qa-project-Urban-Grocers-app-es

## Descripción del Proyecto
Este proyecto tiene como objetivo automatizar la creación de un nuevo usuario y la creación de un kit vacío en una aplicación, utilizando el encabezado Authorization para la autenticación.

## Documentación de Referencia
- **apiDoc**: Utilizado para documentar las APIs del proyecto. [apiDoc](https://apidocjs.com/)
- **Tutorial de Python**: [Tutorial Oficial de Python](https://docs.python.org/es/3/tutorial/index.html)
- **Pytest Documentation**: Documentación completa de pytest para pruebas en Python. [Pytest](https://docs.pytest.org/en/7.1.x/contents.html)
- **PEP 8**: Guía de estilo para el código Python. [PEP](https://peps.python.org/pep-0008/)

## Tecnologías y Técnicas Utilizadas

### Python
Python es un lenguaje de programación de alto nivel, interpretado y con una fuerte orientación a objetos. Es ampliamente apreciado por su sintaxis clara y legible, lo que facilita tanto el aprendizaje para los nuevos programadores como el desarrollo rápido de aplicaciones complejas para los más experimentados. Python es muy popular en la automatización de tareas, el análisis de datos, la inteligencia artificial, y el desarrollo web, entre otros campos.

### PyCharm
PyCharm es un entorno de desarrollo integrado (IDE) utilizado en la programación de computadoras, específicamente para el lenguaje Python. Desarrollado por JetBrains, PyCharm ofrece varias características útiles como análisis de código, un depurador gráfico, un probador integrado, integración con sistemas de control de versiones, y soporte para el desarrollo web con Django. PyCharm facilita el desarrollo de software en Python mediante la automatización de varias tareas rutinarias y ofreciendo una interfaz cómoda para escribir, probar y depurar código.

## Comandos para Usar el Proyecto

### Clonar el Repositorio
Para obtener una copia del código fuente en tu máquina local, utiliza el siguiente comando:

```bash
git clone git@github.com:tu-usuario/qa-project-Urban-Grocers-app-es.git
```

Asegúrate de clonar el repositorio correcto. El nombre de usuario debe ser tu propio nombre de usuario, no tripleten-com.

## Configuración en PyCharm
Para abrir el proyecto en PyCharm:

1. Abre PyCharm.
2. Selecciona Archivo → Abrir.
3. Navega hasta la carpeta qa-project-Urban-Grocers-app-es que clonaste y selecciona la carpeta para abrirla como un proyecto.

## Configurar Entorno de Pruebas
Para instalar Pytest y Requests, ejecuta los siguientes comandos:

```bash
pip install pytest
pip install requests
```

## Ejecutar el Proyecto
Antes de ejecutar las pruebas, asegúrate de que el servidor está desplegado y la URL está accesible. Luego, realiza los siguientes pasos:

1. Copia la URL del servidor (sin la "/" final).
2. Establece esta URL en la variable URL_SERVICE dentro del archivo configuration.

Para ejecutar las pruebas, usa el siguiente comando:

```bash
pytest create_kit_name_kit_test.py
```

Asegúrate de revisar y modificar cualquier detalle específico que pueda variar según tu configuración o requisitos del proyecto.
