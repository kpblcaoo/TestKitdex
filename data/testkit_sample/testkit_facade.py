"""
Фасад для TestKit
Аналог TestKit.Facade.cs
"""
from .testkit_main import *
from .testkit_specialized import Specialized

class TestKitFacade:
    def __init__(self):
        self.specialized = Specialized()
    
    def create_user(self, **kwargs):
        return create_user(**kwargs)
    
    def create_message(self, **kwargs):
        return create_message(**kwargs)

# Глобальный фасад
TK = TestKitFacade()
