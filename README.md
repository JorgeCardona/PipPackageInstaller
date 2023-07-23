# PipPackageCustomInstaller

The PipPackageCustomInstaller module is a tool for installing Python packages from PyPI (Python Package Index) in a simple way. It allows you to check if a package is available on PyPI, install the latest version or a specific version, and also provides information about the locally installed version.

## Installation

To use PipPackageCustomInstaller, you need to have Python and pip installed. There are no additional dependencies required.

## Usage

Import the `PipPackageCustomInstaller` class and create an instance for the desired package. Then, use the following methods:

### 1. Check if a package exists on PyPI:

```python
from pip_custome_package_installer import PipPackageCustomInstaller

package_name = "package_name"  # Replace "package_name" with the desired package name
installer = PipPackageCustomInstaller(package_name)
package_info = installer.package_exists_on_pypi()

if package_info[0]:
    package_to_install = package_info[0]
    available_versions = package_info[1]
    print(f"The package {package_name} is available on PyPI in the following versions: {available_versions}.")
    print(f"Latest available version: {package_to_install}")
else:
    print(f"The package {package_name} is not available on PyPI.")
```

### 2. Get the locally installed version of a package:

```python
from pip_custome_package_installer import PipPackageCustomInstaller

package_name = "package_name"  # Replace "package_name" with the desired package name
installer = PipPackageCustomInstaller(package_name)
local_version = installer.get_local_version_package()

if local_version == "Package not found":
    print(f"The package {package_name} is not installed locally.")
elif local_version == "Version not found":
    print(f"The version of package {package_name} was not found.")
else:
    print(f"The package {local_version} is installed locally.")
```

### 3. Install a package from PyPI:
```python
from pip_custome_package_installer import PipPackageCustomInstaller

package_name = "package_name"  # Replace "package_name" with the desired package name
version_to_install = "desired_version"  # Replace "desired_version" with the specific version you want to install

installer = PipPackageCustomInstaller(package_name, version_to_install)
installation_result = installer.install_package()

if installation_result is None:
    print("The package is already installed or not found on PyPI.")
elif installation_result.startswith("The package"):
    print(installation_result)  # Installation success message
else:
    print(f"Error installing the package: {installation_result}")
```

Contribution
If you want to contribute to this project, you can do so through pull requests. Your help is welcome and appreciated.


# DOCUMENTACION ESPANOL

El módulo PipPackageCustomInstaller es una herramienta para instalar paquetes de Python desde PyPI (Python Package Index) de manera sencilla. Permite verificar si un paquete está disponible en PyPI, instalar la última versión o una versión específica, y también muestra información sobre la versión instalada localmente.

## Instalación

Para utilizar PipPackageCustomInstaller, es necesario tener Python y pip instalados. No se requieren dependencias adicionales.

## Uso

Importar la clase `PipPackageCustomInstaller` y crear una instancia para el paquete deseado. Luego, utilizar los siguientes métodos:

### 1. Verificar si un paquete existe en PyPI:

```python
from pip_custome_package_installer import PipPackageCustomInstaller

package_name = "nombre_paquete"  # Reemplazar "nombre_paquete" por el nombre del paquete deseado
installer = PipPackageCustomInstaller(package_name)
package_info = installer.package_exists_on_pypi()

if package_info[0]:
    package_to_install = package_info[0]
    available_versions = package_info[1]
    print(f"El paquete {package_name} está disponible en PyPI en las siguientes versiones: {available_versions}.")
    print(f"Última versión disponible: {package_to_install}")
else:
    print(f"El paquete {package_name} no está disponible en PyPI.")
```

### 2. Obtener la versión instalada localmente de un paquete:
```python
from pip_custome_package_installer import PipPackageCustomInstaller

package_name = "nombre_paquete"  # Reemplazar "nombre_paquete" por el nombre del paquete deseado
installer = PipPackageCustomInstaller(package_name)
local_version = installer.get_local_version_package()

if local_version == "Package not found":
    print(f"El paquete {package_name} no está instalado localmente.")
elif local_version == "Version not found":
    print(f"La versión del paquete {package_name} no se encontró.")
else:
    print(f"El paquete {local_version} está instalado localmente.")
```

### 3. Instalar un paquete desde PyPI:
```python
from pip_custome_package_installer import PipPackageCustomInstaller

package_name = "nombre_paquete"  # Reemplazar "nombre_paquete" por el nombre del paquete deseado
version_to_install = "version_deseada"  # Reemplazar "version_deseada" por la versión específica que deseas instalar

installer = PipPackageCustomInstaller(package_name, version_to_install)
installation_result = installer.install_package()

if installation_result is None:
    print("El paquete ya está instalado o no se encontró en PyPI.")
elif installation_result.startswith("The package"):
    print(installation_result)  # Éxito en la instalación
else:
    print(f"Error al instalar el paquete: {installation_result}")
```

Contribución
Si deseas contribuir a este proyecto, puedes hacerlo a través de pull requests. Tu ayuda es bienvenida y apreciada.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.