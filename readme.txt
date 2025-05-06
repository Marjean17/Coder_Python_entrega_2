1.- crea archivos .py para trabajarlos desde módulos (ej. clases.py, funciones.py, main.py).

2.- importa los módulos en donde sean utilizados ( 
    por ej en main.py importamos al inicio...
        from modelo_clientes import Persona, Cliente, Empleado
        from funciones_cliente import no_numeric, only_numeric, ingresa_datos_cliente)

3.- Creamos la carpeta mi_paquete y movemos allí todos los archivos menos el main
4.- Creamos dentro de mi_paquete un archivo vacío llamado __init__.py dentro de la carpeta mi_paquete. (Esto le indica a Python que la carpeta es un paquete).
5.- Creamos FUERA de mi_paquete un archivo vacío llamado setup.py 
    Dentro de setup.py ponemos

        from setuptools import setup, find_packages

        setup(
            name='mi_paquete',
            version='0.1',
            packages=find_packages(),
            install_requires=[],  # Agrega aquí las dependencias si las hay
        )

6.- Abrimos una terminal en VSC y navegamos hasta el directorio que contiene la carpeta mi_paquete usando cd.

7.- Abre la paleta de comandos (Ctrl + Shift + P).
    Busca "Python: Select Interpreter".
    Selecciona la opción "Create Environment".
    Elige el tipo de entorno (Venv o Conda). Venv es mas simple y ligero. Conda admite mas lenguajes y mas paquetes
    Selecciona la ubicación para el entorno virtual.
    VSC creará el entorno virtual y lo activará automáticamente.
    Instalar tu paquete en el entorno virtual:

    Una vez creado el entorno virtual, asegúrate de que está activado (lo verás en la barra de estado de VSC). 
    Luego, ejecuta el comando pip install dist/mi_paquete-0.1-py3-none-any.whl dentro de la terminal integrada de VSC. 
    Esto instalará tu paquete en el entorno virtual, aislado del entorno global.

    Recomendación:
    Es una buena práctica siempre usar entornos virtuales para tus proyectos de Python, especialmente si utilizas diferentes paquetes o versiones. 
    Esto te ayudará a evitar conflictos y a mantener tus proyectos organizados.

8.- Al crear un entorno virtual, solo las bibliotecas de Python que se instalan en él se almacenarán en la carpeta .venv. 
    Tu código fuente y otros archivos del proyecto deben almacenarse fuera de la carpeta .venv, en la raíz del proyecto o en subcarpetas dentro de la raíz.

    Para usar el entorno virtual, debes activarlo primero:

    Abre una terminal en la carpeta raíz de tu proyecto.
    Ejecuta el siguiente comando:
    
        source .venv\Scripts\activate
    si es linux (.venv/bin/activate)

    Ahora deberías ver el nombre del entorno virtual entre paréntesis en tu prompt de terminal. Esto indica que el entorno virtual está activo.
    Una vez que el entorno virtual está activo, puedes instalar bibliotecas de Python usando pip y ejecutar tu código usando python. 
    Cuando hayas terminado, puedes desactivar el entorno virtual ejecutando el siguiente comando:

    deactivate

9.- Ejecutamos 

        pip install wheel==0.40.0
        pip install ipython==8.14.0
        
    luego, si ya está instalado

        python setup.py sdist bdist_wheel

        Este comando crea los archivos necesarios para distribuir tu paquete, incluyendo el archivo .whl (wheel) que contiene el código compilado 
        y los metadatos del paquete. Estos archivos se generan en la carpeta dist.

10.- Ejecutamos 
        pip install dist/paquete-0.1-py3-none-any.whl (mi_paquete = el nombre de la carpeta que le hayamos dado)


build/: Esta carpeta es utilizada por setuptools para almacenar archivos temporales durante el proceso de construcción del paquete. Es seguro eliminarla después de que la construcción se haya completado.
dist/: Esta carpeta es donde se almacenan los archivos de distribución generados, como los archivos .tar.gz, .whl y .zip. Estos son los archivos que se utilizan para instalar el paquete en otros entornos.
paquete/: Esta carpeta contiene el código fuente de tu paquete. Debe tener un archivo __init__.py para que Python lo reconozca como un paquete.
paquete.egg-info/: Esta carpeta contiene metadatos sobre tu paquete, como su nombre, versión, dependencias y otros detalles. Es generada por setuptools durante el proceso de construcción.
main.py: Es el archivo principal de tu proyecto, donde se ejecuta el código principal.
setup.py: Es el archivo de configuración para la distribución de tu paquete. Contiene información sobre el paquete, como su nombre, versión, descripción, autor, dependencias, etc.
En resumen, la estructura que describes es la esperada después de ejecutar comandos como python setup.py sdist bdist_wheel o similares.

Posibles problemas:

Aunque la estructura es correcta, hay algunos puntos que vale la pena revisar:

Instalaciones redundantes: Si has instalado el paquete varias veces en modo editable (con pip install -e .), es posible que tengas varias carpetas paquete.egg-info con diferentes nombres. Esto puede causar confusión, pero generalmente no es un problema grave. Puedes eliminar las carpetas egg-info antiguas si lo deseas.
Archivos residuales: Las carpetas build y dist pueden contener archivos de distribuciones anteriores. Si quieres asegurarte de tener una distribución limpia, puedes eliminar estas carpetas antes de generar una nueva distribución.
Recomendaciones:

Limpieza: Elimina las carpetas build, dist y paquete.egg-info antes de generar una nueva distribución para asegurarte de que no haya archivos residuales de versiones anteriores.
.gitignore: Asegúrate de incluir las carpetas build, dist y paquete.egg-info en tu archivo .gitignore para que no se suban al control de versiones.
Instalación editable: Si estás desarrollando el paquete, utiliza pip install -e . para instalarlo en modo editable. Esto te permitirá realizar cambios en el código fuente y ver los cambios reflejados inmediatamente sin tener que reinstalar el paquete.
Espero que esta información te sea útil.



11.- ejecuta en powershell

      pip install dist/paquete.whl


11Bis.- Instalación en modo editable:** Si estás desarrollando activamente el paquete, es más conveniente instalarlo en modo editable. 
Esto te permite realizar cambios en el código fuente y ver los cambios reflejados inmediatamente sin tener que reinstalar el paquete. 
Para instalarlo en modo editable, ejecuta:

powershell
      pip install -e .

Este comando instalará tu paquete desde la carpeta actual (donde se encuentra tu archivo `setup.py`)

12.- Ahora si...

    python main.py