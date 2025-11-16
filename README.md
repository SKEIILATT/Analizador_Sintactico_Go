# Analizador Sintáctico para Go

Implementación de un analizador sintáctico (parser) para el lenguaje de programación Go, desarrollado en Python utilizando PLY (Python Lex-Yacc). Este proyecto representa la segunda fase de un compilador educativo.

## Autores

- **Jair Palaguachi** ([@JairPalaguachi](https://github.com/JairPalaguachi))
- **Javier Gutiérrez** ([@SKEIILATT](https://github.com/SKEIILATT))
- **Leonardo Macías** ([@leodamac](https://github.com/leodamac))

## Descripción

El analizador sintáctico valida que la secuencia de tokens generada por el analizador léxico cumpla con las reglas gramaticales del lenguaje Go. Utiliza una gramática libre de contexto implementada con PLY yacc para construir y validar la estructura sintáctica de programas Go.

## Características Implementadas

### Estructuras de Datos
- **Arrays**: Declaración y acceso a arreglos de tamaño fijo
- **Slices**: Arreglos dinámicos con operaciones de slicing
- **Maps**: Diccionarios con inicialización literal y operaciones

### Estructuras de Control
- **IF-ELSE**: Condicionales simples, anidados y con inicialización
- **FOR**: Bucles tradicionales, estilo while, y for-range
- **SWITCH**: Switch con expresión, sin expresión, y con inicialización

### Declaraciones
- **Variables**: `var`, declaración corta (`:=`), múltiple, y bloques
- **Constantes**: `const` simple y en bloques
- **Funciones**: Con parámetros, retornos simples, múltiples y nombrados
- **Funciones variádicas**: Soporte para parámetros variables (`...`)

### Expresiones
- **Aritméticas**: Suma, resta, multiplicación, división, módulo
- **Lógicas**: AND, OR, NOT con precedencia correcta
- **Relacionales**: Comparaciones (==, !=, <, <=, >, >=)
- **Bit a bit**: AND, OR, XOR, desplazamientos
- **Punteros**: Operadores `&` (dirección) y `*` (desreferencia)

### Funciones Built-in
- `make()`: Creación de slices, maps y channels
- `append()`: Agregar elementos a slices
- `len()`: Longitud de colecciones
- `delete()`: Eliminar elementos de maps

### Características Especiales
- **Blank identifier** (`_`): En asignaciones y for-range
- **Imports múltiples**: Con sintaxis de paréntesis
- **Literal nil**: Para punteros y valores nulos
- **Operadores de asignación compuesta**: `+=`, `-=`, `*=`, etc.

## Requisitos

- Python 3.7 o superior
- PLY (Python Lex-Yacc) 3.11 o superior

## Instalación
```bash
# Instalar dependencias
pip install ply

# Clonar el repositorio
git clone <url-del-repositorio>
cd Analizador_Sintactico_Go
```

## Uso

### Análisis Sintáctico Básico
```bash
python sintactico_go.py <archivo.go>
```

### Ejemplos
```bash
# Analizar variables y operadores básicos
python sintactico_go.py algoritmo1.go

# Analizar estructuras de control
python sintactico_go.py algoritmo2.go

# Analizar estructuras de datos y funciones avanzadas
python sintactico_go.py algoritmo3.go
```

## Salida y Logs

El analizador genera automáticamente un archivo de log en la carpeta `logs/` con el formato:
```
sintactico-{usuario}-{archivo}-{fecha}-{hora}.txt
```

### Ejemplo de Log
```
================================================================================
ANÁLISIS SINTÁCTICO - LENGUAJE GO
================================================================================
Archivo analizado: algoritmo1.go
Fecha y hora: 15/11/2025 18:14:01
Usuario: leodamac
================================================================================

ERRORES SINTÁCTICOS ENCONTRADOS (0)
--------------------------------------------------------------------------------
No se encontraron errores sintácticos.

================================================================================
FIN DEL ANÁLISIS SINTÁCTICO
================================================================================
```

### Con Errores
```
ERRORES SINTÁCTICOS ENCONTRADOS (4)
--------------------------------------------------------------------------------
Error de sintaxis en '&' (Token: BITAND, Línea: 103)
Error de sintaxis en 'int' (Token: ID, Línea: 141)
...
```
## Gramática Implementada

### Ejemplo de Reglas
```python
# Declaración de variables
declaracion_var : VAR ID tipo
                | VAR ID tipo ASSIGN expresion
                | ID DECLARE_ASSIGN expresion

# Estructura IF-ELSE
if_statement : IF condicion bloque
             | IF condicion bloque ELSE bloque
             | IF condicion bloque ELSE if_statement

# Bucle FOR con range
for_statement : FOR ID COMMA ID DECLARE_ASSIGN RANGE expresion bloque
```

## Precedencia de Operadores
```python
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
    ('right', 'ADDRESS', 'POINTER'),
)
```


## Estructura del Proyecto
```
Analizador_Sintactico_Go/
├── lexico_go.py              # Analizador léxico
├── sintactico_go.py          # Analizador sintáctico ⭐
├── algoritmo1.go             # Prueba: variables y operadores
├── algoritmo2.go             # Prueba: estructuras de control
├── algoritmo3.go             # Prueba: estructuras de datos avanzadas
├── logs/                     # Logs de análisis
│   ├── sintactico-usuario-algoritmo1-fecha.txt
│   ├── sintactico-usuario-algoritmo2-fecha.txt
│   └── sintactico-usuario-algoritmo3-fecha.txt
├── parser.out                # Tabla de parsing de PLY
└── parsetab.py               # Cache del parser
```

## Mantenimiento

### Limpiar Archivos Cache
```bash
# Borrar cache de PLY (necesario después de modificar la gramática)
rm -f parser.out parsetab.py

# Borrar cache de Python
rm -rf __pycache__
```

### Regenerar Parser

Después de modificar `sintactico_go.py`, es importante limpiar el cache:
```bash
rm -f parser.out parsetab.py
python sintactico_go.py algoritmo1.go
```


## Tecnologías

- **Python 3**: Lenguaje de implementación
- **PLY (Python Lex-Yacc)**: Framework para construcción de parsers
- **Git**: Control de versiones


