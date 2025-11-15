# Analizador Léxico y Sintáctico para Go

Proyecto educativo que implementa un analizador léxico y sintáctico para el lenguaje de programación Go, desarrollado en Python utilizando la biblioteca PLY (Python Lex-Yacc).

## Autores

- **Jair Palaguachi** ([@JairPalaguachi](https://github.com/JairPalaguachi))
- **Javier Gutiérrez** ([@SKEIILATT](https://github.com/SKEIILATT))
- **Leonardo Macías** ([@leodamac](https://github.com/leodamac))

## Descripción

Este proyecto implementa las primeras fases de un compilador para el lenguaje Go:

- **Analizador Léxico (Lexer)**: Tokeniza código fuente de Go, identificando palabras reservadas, operadores, literales, identificadores y delimitadores.
- **Analizador Sintáctico (Parser)**: Valida la estructura gramatical del código Go según las reglas del lenguaje.

El analizador es capaz de procesar archivos `.go` y generar reportes detallados de los tokens encontrados, así como identificar errores léxicos.

## Características

- Reconocimiento de **62 tipos de tokens** diferentes
- Soporte completo para palabras reservadas de Go
- Detección de literales: enteros, flotantes, strings, runes y booleanos
- Identificación de operadores: aritméticos, lógicos, de comparación, bit a bit y de asignación
- Manejo de comentarios de línea (`//`) y de bloque (`/* */`)
- Generación automática de logs con timestamp
- Reporte detallado de errores léxicos con línea y columna

## Requisitos

- Python 3.7 o superior
- PLY (Python Lex-Yacc) 3.11 o superior

## Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd Analizador_Sintactico_Go
```

2. Instala las dependencias:
```bash
pip install ply
```

## Uso

Para analizar un archivo de código Go:

```bash
python lexico_go.py <archivo.go>
```

### Ejemplos

El proyecto incluye tres archivos de prueba con diferentes características del lenguaje Go:

```bash
# Analizar algoritmo básico (variables y operadores)
python lexico_go.py algoritmo1.go

# Analizar estructuras de control (if, for, switch)
python lexico_go.py algoritmo2.go

# Analizar estructuras de datos (arrays, slices, maps, punteros)
python lexico_go.py algoritmo3.go
```

## Salida

El analizador genera un archivo de log en la carpeta `logs/` con el siguiente formato:

```
lexico-{usuario}-{archivo}-{fecha}-{hora}.txt
```

El log contiene:
- Lista completa de tokens reconocidos con línea y columna
- Total de tokens procesados
- Lista de errores léxicos encontrados (si los hay)
- Estadísticas del análisis

### Ejemplo de salida:

```
TOKENS RECONOCIDOS (288)
========================================
Token: PACKAGE    | Valor: package  | Línea: 5  | Columna: 1
Token: ID         | Valor: main     | Línea: 5  | Columna: 9
Token: FUNC       | Valor: func     | Línea: 7  | Columna: 1
...

ERRORES LÉXICOS (0)
========================================
No se encontraron errores léxicos.
```

## Estructura del Proyecto

```
Analizador_Sintactico_Go/
├── lexico_go.py          # Analizador léxico principal
├── sintactico_go.py      # Analizador sintáctico
├── algoritmo1.go         # Ejemplo: variables y operadores
├── algoritmo2.go         # Ejemplo: estructuras de control
├── algoritmo3.go         # Ejemplo: estructuras de datos
├── parsetab.py           # Tabla de parsing generada por PLY
├── parser.out            # Salida del parser generada por PLY
├── logs/                 # Carpeta con logs de análisis
└── __pycache__/          # Cache de Python
```

## Tokens Reconocidos

### Palabras Reservadas
`package`, `import`, `func`, `var`, `const`, `if`, `else`, `for`, `switch`, `case`, `default`, `return`, `break`, `continue`, `goto`, `fallthrough`, `type`, `struct`, `interface`, `map`, `chan`, `go`, `defer`, `select`, `range`

### Operadores

#### Aritméticos
`+`, `-`, `*`, `/`, `%`, `++`, `--`

#### Lógicos
`&&`, `||`, `!`

#### Comparación
`==`, `!=`, `<`, `<=`, `>`, `>=`

#### Bit a Bit
`&`, `|`, `^`, `<<`, `>>`, `&^`

#### Asignación
`=`, `:=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`, `&^=`

### Literales
- Enteros: `42`, `0x2A`, `0o52`, `0b101010`
- Flotantes: `3.14`, `1.5e10`
- Strings: `"hello"`, `` `raw string` ``
- Runes: `'a'`, `'\n'`
- Booleanos: `true`, `false`
- Nulo: `nil`

### Delimitadores
`(`, `)`, `{`, `}`, `[`, `]`, `;`, `,`, `.`, `:`, `...`

## Ejemplos de Código Analizado

### algoritmo1.go
- Declaración de variables con distintos métodos
- Operadores aritméticos básicos
- Funciones simples

### algoritmo2.go
- Condicionales (if-else, if-else if)
- Bucles (for tradicional, while-style, range)
- Switch statements
- Operadores lógicos compuestos

### algoritmo3.go
- Arrays y slices
- Maps (diccionarios)
- Punteros
- Funciones con múltiples retornos
- Funciones variádicas
- Operadores bit a bit

## Tecnologías Utilizadas

- **Python 3**: Lenguaje de implementación
- **PLY (Python Lex-Yacc)**: Framework para construcción de lexers y parsers
- **Go**: Lenguaje objetivo del análisis

## Desarrollo

### Distribución del Trabajo

- **Jair Palaguachi**: Palabras reservadas y tokens básicos
- **Javier Gutiérrez**: Expresiones regulares para tokens simples
- **Leonardo Macías**: Tokens complejos (literales e identificadores)
- **Equipo completo**: Manejo de comentarios, espacios y generación de logs

## Limitaciones Conocidas

- El analizador sintáctico aún está en desarrollo
- No soporta todas las características avanzadas de Go (genéricos, etc.)
- Los comentarios no generan tokens (se ignoran)

## Futuras Mejoras

- [ ] Completar el analizador sintáctico
- [ ] Implementar generación de árbol de sintaxis abstracta (AST)
- [ ] Agregar análisis semántico
- [ ] Crear interfaz gráfica para visualización de tokens
- [ ] Soporte para más características de Go 1.20+

## Licencia

Este es un proyecto educativo desarrollado con fines académicos.

## Contacto

Para preguntas o sugerencias, contacta a cualquiera de los autores a través de sus perfiles de GitHub.
