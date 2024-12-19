class EventManager():
    def __init__(self):
        self.registered = []

    def register(self, user):
        if user in self.registered:
            return False
        else:
            self.registered.append(user)
            return True
    
    def deregister(self, user):
        if user in self.registered:
            self.registered.pop(self.registered.index(user))
            return True
        else:
            return False
        
    def get_num_registrations(self):
        return len(self.registered)
    
class LimitedEventManager(EventManager):
    def __init__(self,registration_limit):
        super().__init__()
        self.registration_limit = registration_limit

    def register(self, user):
        if len(self.registered) < self.registration_limit:
            if user in self.registered:
                return False
            else:
                self.registered.append(user)
                return True
        else:
            return False
    