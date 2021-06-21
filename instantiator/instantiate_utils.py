from importlib import import_module


class ObjectGetter:
    def __init__(self, module_name, object_name):
        self.module_name = module_name
        self.object_name = object_name

    def __call__(self):
        module = import_module(self.module_name)
        return getattr(module, self.object_name)
