"""
módulo que implementa las siguientes funciones:
- segundos a minutos: recibe segundos y devuelve minutos y segundos
- segundos a horas: recibe segundos y regresa horas, minutos y segundos
- minutos a segundos: recibe minutos y segundos y regresa segundos
- minutos a horas: recibe minutos y segundos y regresa horas minutos y
segundos
"""
import os

def segundos_a_minutos(segundos):
    """
    convierte segundos a minutos
    argumentos: segundos -- los convierte a minutos
    """
    m = segundos // 60
    s = segundos % 60
    return m, s

def segundos_a_horas(segundos):
    """
    convierte segundos a horas
    argumentos: segundos -- los pasa a horas
    """
    h = segundos // 3600
    m = segundos // 60
    s = segundos % 60
    return h, m, s

def minutos_a_segundos(segundos, minutos):
    """
    convierte minutos a segundos
    argumentos: segundos, minutos -- convierte estos a minutos y segundos
    """
    s = minutos * 60 + segundos
    return s

def minutos_a_horas(segundos, minutos):
    """
    convierte minutos a horas
    argumentos: segundos, minutos -- convierte esto a la unidad deseada
    """
    h = minutos // 60
    m = segundos // 60
    s = segundos % 60
    return h, m, s
