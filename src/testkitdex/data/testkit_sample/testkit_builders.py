"""
Fluent API builders
Аналог TestKit.Builders.cs
"""
class MessageBuilder:
    def __init__(self):
        self._message = {}
    
    def with_text(self, text):
        self._message["text"] = text
        return self
    
    def from_user(self, user_id):
        self._message["user_id"] = user_id
        return self
    
    def in_chat(self, chat_id):
        self._message["chat_id"] = chat_id
        return self
    
    def build(self):
        return self._message
