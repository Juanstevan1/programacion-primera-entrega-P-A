
# MyProject

## Introducción

**MyProject** es una plataforma de comercio electrónico desarrollada en Django que permite a los usuarios visualizar productos, agregarlos al carrito y realizar órdenes de compra. El proyecto implementa una arquitectura en capas y aplica tres patrones de diseño: **Builder**, **Strategy** y **Facade**.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **myproject/**: Directorio principal del proyecto.
  - **home/**: Aplicación que maneja la página de inicio y la navegación general.
  - **orders/**: Aplicación que gestiona la creación y seguimiento de órdenes.
  - **products/**: Aplicación que administra los productos disponibles en la plataforma.
  - **myproject/**: Configuraciones globales del proyecto Django.
  - **manage.py**: Archivo principal para ejecutar comandos de administración de Django.

## Requisitos Previos

- **Python 3.x** instalado en el sistema.
- **Virtualenv** o **venv** para crear un entorno virtual (opcional pero recomendado).
- **Pip** instalado para manejar las dependencias.
- **Django** (se instalará con las dependencias).

## Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/myproject.git
cd myproject
```

### 2. Crear y Activar un Entorno Virtual (Opcional pero Recomendado)

#### En Windows
```bash
python -m venv venv
venv\Scriptsctivate
```

#### En macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las Dependencias

Asegúrate de tener un archivo `requirements.txt` con las dependencias necesarias. Si no lo tienes, puedes crearlo con el siguiente contenido:

```bash
Django>=3.0,<4.0
```

Luego, instala las dependencias:

```bash
pip install -r requirements.txt
```

### 4. Aplicar Migraciones

```bash
python manage.py migrate
```

### 5. Crear un Superusuario (Opcional, para acceder al panel de administración de Django)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

### 7. Acceder a la Aplicación

Abre tu navegador y navega a [http://localhost:8000/](http://localhost:8000/) para ver la aplicación en funcionamiento.

---

## Explicación de la Arquitectura y Patrones de Diseño

### Arquitectura en Capas

El proyecto sigue una arquitectura en capas que separa las responsabilidades en tres niveles principales:

- **Capa de Presentación**: Contiene las vistas y plantillas que interactúan con el usuario. Maneja la interfaz gráfica y la comunicación con la capa de lógica de negocio.
- **Capa de Lógica de Negocio**: Incluye los servicios y facades que implementan las reglas de negocio, como el cálculo de precios y la gestión de órdenes.
- **Capa de Acceso a Datos**: Gestionada por los modelos y el ORM de Django, permite interactuar con la base de datos de forma eficiente.

Esta arquitectura facilita la separación de responsabilidades, mejora la mantenibilidad y permite escalar el sistema de manera más sencilla.

### Patrones de Diseño Implementados

#### 1. Patrón de Creación: Builder
- **Ubicación**: `products/builders.py`
- **Descripción**: El patrón Builder se utiliza para la creación flexible de productos con múltiples atributos opcionales o configuraciones específicas.
- **Justificación**:
  - **Flexibilidad en la Construcción**: Permite construir objetos complejos de manera incremental y flexible.
  - **Mantenibilidad**: Facilita la adición de nuevos tipos de productos sin alterar el código existente, siguiendo el principio abierto/cerrado.
  - **Integración en la Arquitectura**: Se ubica en la capa de lógica de negocio, permitiendo que la capa de presentación solicite productos personalizados sin conocer los detalles de su construcción.

#### 2. Patrón de Comportamiento: Strategy
- **Ubicación**: `products/strategies.py`
- **Descripción**: El patrón Strategy gestiona las diferentes políticas de precios según el tipo de usuario (regular, premium o mayorista).
- **Justificación**:
  - **Flexibilidad en el Comportamiento**: Permite cambiar las políticas de precios sin modificar el código del cliente, facilitando la adaptación a nuevas reglas de negocio.
  - **Reutilización de Código**: Las estrategias pueden ser reutilizadas y extendidas para nuevos tipos de usuarios.
  - **Integración en la Arquitectura**: Reside en la capa de lógica de negocio. La capa de presentación interactúa con esta capa para obtener los precios ajustados, sin necesidad de conocer cómo se calculan.

#### 3. Patrón Estructural: Facade
- **Ubicación**: `orders/facades.py`
- **Descripción**: El patrón Facade simplifica la interacción con el sistema de gestión de órdenes, proporcionando una interfaz unificada para un conjunto de interfaces en un subsistema.
- **Justificación**:
  - **Simplicidad**: Reduce la complejidad al ocultar las operaciones subyacentes de creación y gestión de órdenes.
  - **Aislamiento**: Permite aislar la capa de presentación de los detalles internos de la lógica de negocio, promoviendo un bajo acoplamiento.
  - **Integración en la Arquitectura**: Se sitúa entre la capa de presentación y la capa de lógica de negocio. La capa de presentación utiliza la fachada para interactuar con el sistema de órdenes sin manejar múltiples clases o métodos complejos.

---

## Funcionalidades Principales

- **Lista y Detalle de Productos**: Los usuarios pueden navegar y ver detalles de los productos disponibles.
- **Carrito de Compras**: Permite añadir productos al carrito y ver el resumen de la compra.
- **Creación de Órdenes**: Procesa las compras y genera órdenes con precios ajustados según el tipo de usuario.
- **Historial de Órdenes**: Permite a los usuarios visualizar órdenes pasadas y detalles de las compras realizadas.