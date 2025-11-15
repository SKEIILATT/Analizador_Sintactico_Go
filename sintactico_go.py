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
# CONTRIBUCIÓN: Leonardo Macías (leodamac)
# Sección: Arrays - Acceso e Inicialización
# ============================================================================

def p_expresion_array_acceso(p):
    '''expresion : ID LBRACKET expresion RBRACKET'''
    pass

def p_array_literal(p):
    '''expresion : LBRACKET INT_LITERAL RBRACKET tipo LBRACE lista_expresiones RBRACE
                 | LBRACKET INT_LITERAL RBRACKET tipo LBRACE RBRACE
                 | LBRACKET INT_LITERAL RBRACKET LBRACKET INT_LITERAL RBRACKET tipo LBRACE lista_filas_matriz RBRACE'''
    pass

def p_lista_filas_matriz(p):
    '''lista_filas_matriz : lista_filas_matriz COMMA fila_matriz
                          | fila_matriz'''
    pass

def p_fila_matriz(p):
    '''fila_matriz : LBRACE lista_expresiones RBRACE'''
    pass

# ============================================================================
# FIN CONTRIBUCIÓN: Leonardo Macías
# ============================================================================
