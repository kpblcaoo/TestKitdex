"""
Основной модуль TestKit
Аналог TestKit.Main.cs
"""
from . import TK

# Основные методы
def create_user(**kwargs):
    return TK.create_user(**kwargs)

def create_message(**kwargs):
    return TK.create_message(**kwargs)

def create_chat(**kwargs):
    return TK.create_chat(**kwargs)
