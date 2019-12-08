from marl.tools import ClassSpec, _std_repr

class Policy(object):
    policy = {}
    
    def __call__(self, state):
        raise NotImplementedError
    
    def load(self, filename):
        raise NotImplementedError

    def save(self, filename):
        raise NotImplementedError
    
    def __repr__(self):
        return _std_repr(self)
    
    @classmethod
    def make(cls, id, **kwargs):
        if isinstance(id, cls):
            return id
        else:
            return Policy.policy[id].make(**kwargs)
    
    @classmethod
    def register(cls, id, entry_point, **kwargs):
        if id in Policy.policy.keys():
            raise Exception('Cannot re-register id: {}'.format(id))
        Policy.policy[id] = ClassSpec(id, entry_point, **kwargs)
        
    @classmethod
    def available(cls):
        return Policy.policy.keys()

def register(id, entry_point, **kwargs):
    Policy.register(id, entry_point, **kwargs)
    
def make(id, **kwargs):
    return Policy.make(id, **kwargs)
    
def available():
    return Policy.available()