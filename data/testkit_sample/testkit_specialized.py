"""
Специализированные генераторы
Аналог TestKit.Specialized.cs
"""
class Specialized:
    def __init__(self):
        self.captcha = CaptchaSpecialized()
        self.moderation = ModerationSpecialized()
        self.admin = AdminSpecialized()

class CaptchaSpecialized:
    def bait(self):
        return {"type": "captcha", "action": "bait"}
    
    def valid(self):
        return {"type": "captcha", "action": "valid"}

class ModerationSpecialized:
    def allow(self):
        return {"action": "allow"}
    
    def ban(self):
        return {"action": "ban"}

class AdminSpecialized:
    def approve_callback(self):
        return {"type": "callback", "action": "approve"}
