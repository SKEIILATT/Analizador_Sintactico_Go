"""
Analizador Sintáctico para el Lenguaje Go
Proyecto: Implementación de un Analizador Sintáctico en Go
Integrantes:
- Jair Palaguachi (JairPalaguachi)
- Javier Gutiérrez (SKEIILATT)
- Leonardo Macías (leodamac)
"""
import ply.yacc as yacc
from lexico_go import tokens, lexer
from datetime import datetime
import sys
import os

# Variables globales para logging
log_errors = []

# Definir precedencia de operadores
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

# ============================================================================
# REGLAS BÁSICAS DE ESTRUCTURA DEL PROGRAMA
# ============================================================================

def p_programa(p):
    '''programa : package_decl imports declaraciones'''
    print("Programa analizado correctamente")

def p_package_decl(p):
    '''package_decl : PACKAGE ID'''
    pass

# ============================================================================
# IMPORTS 
# ============================================================================

def p_imports(p):
    '''imports : import_decl imports
               | import_decl
               | empty'''
    pass

def p_import_decl(p):
    '''import_decl : IMPORT STRING_LITERAL
                   | IMPORT LPAREN lista_imports RPAREN
                   | empty'''
    pass

def p_lista_imports(p):
    '''lista_imports : lista_imports STRING_LITERAL
                     | STRING_LITERAL'''
    pass

# ============================================================================
# DECLARACIONES A NIVEL DE PROGRAMA EN GO
# ============================================================================

def p_declaraciones(p):
    '''declaraciones : declaraciones declaracion
                     | declaracion'''
    pass

def p_declaracion(p):
    '''declaracion : funcion
                   | declaracion_var_global
                   | bloque_var
                   | bloque_const
                   | declaracion_const
                   | empty'''
    pass

# ============================================================================
# CONTRIBUCIÓN: Leonardo Macías (leodamac)
# Sección: Declaraciones de Variables
# ============================================================================

def p_declaracion_var_global(p):
    '''declaracion_var_global : VAR ID tipo
                              | VAR ID tipo ASSIGN expresion
                              | VAR ID ASSIGN expresion'''
    pass

def p_bloque_var(p):
    '''bloque_var : VAR LPAREN lista_decl_bloque RPAREN'''
    pass

def p_lista_decl_bloque(p):
    '''lista_decl_bloque : lista_decl_bloque decl_var_bloque
                         | decl_var_bloque'''
    pass

def p_decl_var_bloque(p):
    '''decl_var_bloque : ID tipo
                       | ID tipo ASSIGN expresion
                       | ID ASSIGN expresion'''
    pass

def p_declaracion_var(p):
    '''declaracion_var : VAR ID tipo
                       | VAR ID tipo ASSIGN expresion
                       | VAR ID ASSIGN expresion
                       | ID DECLARE_ASSIGN expresion'''
    pass

def p_declaracion_var_multiple(p):
    '''declaracion_var_multiple : VAR lista_ids tipo
                                | VAR lista_ids tipo ASSIGN lista_expresiones
                                | lista_ids DECLARE_ASSIGN lista_expresiones'''
    pass

def p_lista_ids(p):
    '''lista_ids : lista_ids COMMA ID
                 | lista_ids COMMA UNDERSCORE
                 | ID
                 | UNDERSCORE'''
    pass

# ============================================================================
# FIN CONTRIBUCIÓN: Leonardo Macías
# ============================================================================

# ============================================================================
# CONTRIBUCIÓN: Javier Gutiérrez (SKEIILATT)
# Sección: Asignaciones
# ============================================================================

def p_asignacion(p):
    '''asignacion : ID ASSIGN expresion
                  | ID PLUS_ASSIGN expresion
                  | ID MINUS_ASSIGN expresion
                  | ID TIMES_ASSIGN expresion
                  | ID DIVIDE_ASSIGN expresion
                  | ID LBRACKET expresion RBRACKET ASSIGN expresion
                  | TIMES ID ASSIGN expresion'''
    pass

def p_asignacion_multiple(p):
    '''asignacion_multiple : lista_ids ASSIGN lista_expresiones'''
    pass


# ============================================================================
# DECLARACIONES DE CONSTANTES
# ============================================================================

def p_declaracion_const(p):
    '''declaracion_const : CONST ID ASSIGN expresion
                         | CONST ID tipo ASSIGN expresion'''
    pass

def p_bloque_const(p):
    '''bloque_const : CONST LPAREN lista_decl_const RPAREN'''
    pass

def p_lista_decl_const(p):
    '''lista_decl_const : lista_decl_const decl_const_bloque
                        | decl_const_bloque'''
    pass

def p_decl_const_bloque(p):
    '''decl_const_bloque : ID ASSIGN expresion
                         | ID tipo ASSIGN expresion'''
    pass

# ============================================================================
# FUNCIONES
# ============================================================================

def p_funcion(p):
    '''funcion : FUNC ID LPAREN parametros RPAREN tipo_retorno bloque
               | FUNC ID LPAREN parametros RPAREN bloque'''
    pass

def p_parametros(p):
    '''parametros : lista_parametros
                  | empty'''
    pass

def p_lista_parametros(p):
    '''lista_parametros : lista_parametros COMMA parametro
                        | parametro'''
    pass

def p_parametro(p):
    '''parametro : ID tipo
                 | ID COMMA ID tipo
                 | ID ELLIPSIS tipo
                 | TIMES ID
                 | UNDERSCORE tipo'''
    pass

def p_tipo_retorno(p):
    '''tipo_retorno : tipo
                    | LPAREN lista_tipos RPAREN'''
    pass

def p_lista_tipos(p):
    '''lista_tipos : lista_tipos COMMA tipo
                   | tipo'''
    pass

# ============================================================================
# TIPOS DE DATOS
# ============================================================================

def p_tipo(p):
    '''tipo : ID
            | LBRACKET INT_LITERAL RBRACKET tipo
            | LBRACKET RBRACKET tipo
            | MAP LBRACKET tipo RBRACKET tipo
            | TIMES tipo'''
    pass

# ============================================================================
# BLOQUES Y SENTENCIAS
# ============================================================================

def p_bloque(p):
    '''bloque : LBRACE sentencias RBRACE
              | LBRACE RBRACE'''
    pass

def p_sentencias(p):
    '''sentencias : sentencias sentencia
                  | sentencia'''
    pass

def p_sentencia(p):
    '''sentencia : declaracion_var
                 | bloque_var
                 | bloque_const
                 | declaracion_const
                 | asignacion
                 | asignacion_multiple
                 | declaracion_var_multiple
                 | if_statement
                 | for_statement
                 | switch_statement
                 | return_statement
                 | expresion
                 | impresion
                 | ID INCREMENT
                 | ID DECREMENT
                 | empty'''
    pass

# ============================================================================
# FIN CONTRIBUCIÓN: Javier Gutiérrez
# ============================================================================

# ============================================================================
# CONTRIBUCIÓN: Leonardo Macías (leodamac)
# Sección: Estructura de Control IF-ELSE
# ============================================================================

def p_if_statement(p):
    '''if_statement : IF condicion bloque
                    | IF condicion bloque ELSE bloque
                    | IF condicion bloque ELSE if_statement'''
    pass

def p_condicion(p):
    '''condicion : expresion
                 | declaracion_var_corta SEMICOLON expresion'''
    pass

def p_declaracion_var_corta(p):
    '''declaracion_var_corta : ID DECLARE_ASSIGN expresion
                             | lista_ids DECLARE_ASSIGN expresion'''
    pass

# ============================================================================
# FIN CONTRIBUCIÓN: Leonardo Macías
# ============================================================================

# ============================================================================
# CONTRIBUCIÓN: Javier Gutiérrez (SKEIILATT)
# Sección: Estructura de Control FOR
# ============================================================================

def p_for_statement(p):
    '''for_statement : FOR condicion bloque
                     | FOR bloque
                     | FOR inicializacion SEMICOLON condicion SEMICOLON incremento bloque
                     | FOR ID COMMA ID DECLARE_ASSIGN RANGE expresion bloque
                     | FOR ID DECLARE_ASSIGN RANGE expresion bloque
                     | FOR ID COMMA ID ASSIGN RANGE expresion bloque
                     | FOR UNDERSCORE COMMA ID DECLARE_ASSIGN RANGE expresion bloque
                     | FOR ID COMMA UNDERSCORE DECLARE_ASSIGN RANGE expresion bloque
                     | FOR UNDERSCORE COMMA UNDERSCORE DECLARE_ASSIGN RANGE expresion bloque'''
    pass

def p_inicializacion(p):
    '''inicializacion : declaracion_var
                      | asignacion
                      | empty'''
    pass

def p_incremento(p):
    '''incremento : asignacion
                  | ID INCREMENT
                  | ID DECREMENT
                  | empty'''
    pass

# ============================================================================
# FIN CONTRIBUCIÓN: Javier Gutiérrez
# ============================================================================


# ============================================================================
# CONTRIBUCIÓN: Jair Palaguachi (JairPalaguachi)
# Sección: Estructura de Control SWITCH
# ============================================================================


# ============================================================================
# FIN CONTRIBUCIÓN: Jair Palaguachi
# ============================================================================


# ============================================================================
# CONTRIBUCIÓN: Leonardo Macías (leodamac)
# Sección: Return Statement
# ============================================================================



# ============================================================================
# FIN CONTRIBUCIÓN: Leonardo Macías
# ============================================================================


# ============================================================================
# CONTRIBUCIÓN: Jair Palaguachi (JairPalaguachi)
# Sección: Expresiones Aritméticas y Lógicas
# ============================================================================

# ============================================================================
# FIN CONTRIBUCIÓN: Jair Palaguachi
# ============================================================================


# ============================================================================
# CONTRIBUCIÓN: Leonardo Macías (leodamac)
# Sección: Arrays - Acceso e Inicialización
# ============================================================================



# ============================================================================
# FIN CONTRIBUCIÓN: Leonardo Macías
# ============================================================================

# ============================================================================
# CONTRIBUCIÓN: Javier Gutiérrez (SKEIILATT)
# Sección: Slices
# ============================================================================

def p_slice_literal(p):
    '''expresion : LBRACKET RBRACKET tipo LBRACE lista_expresiones RBRACE
                 | LBRACKET RBRACKET tipo LBRACE RBRACE'''
    pass

def p_slice_operacion(p):
    '''expresion : ID LBRACKET expresion COLON expresion RBRACKET
                 | ID LBRACKET COLON expresion RBRACKET
                 | ID LBRACKET expresion COLON RBRACKET
                 | ID LBRACKET COLON RBRACKET'''
    pass

# ============================================================================
# FIN CONTRIBUCIÓN: Javier Gutiérrez
# ============================================================================


# ============================================================================
# CONTRIBUCIÓN: Jair Palaguachi (JairPalaguachi)
# Sección: Maps
# ============================================================================

# ============================================================================
# FIN CONTRIBUCIÓN: Jair Palaguachi
# ============================================================================

# ============================================================================
# MANEJO DE ERRORES SINTÁCTICOS - Leonardo
# ============================================================================

# ============================================================================
# FIN CONTRIBUCIÓN: Leonardo
# ============================================================================


# ============================================================================
# FUNCIONES DE ANÁLISIS Y LOGGING - Jair
# ============================================================================


# ============================================================================
# FIN CONTRIBUCIÓN: Jair
# ============================================================================

# ============================================================================
# MANEJO DE ERRORES SINTÁCTICOS - Leonardo
# ============================================================================


# ============================================================================
# FIN CONTRIBUCIÓN: Leonardo
# ============================================================================




# ============================================================================
# PUNTO DE ENTRADA - Javier
# ============================================================================
