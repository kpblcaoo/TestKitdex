"""
Моки сервисов
Аналог TestKit.Mocks.cs
"""
class MockService:
    def __init__(self, name="MockService"):
        self.name = name
    
    def mock_method(self):
        return f"Mock result from {self.name}"

def create_mock_service(service_type, **kwargs):
    return MockService(**kwargs)
