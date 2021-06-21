# %%
from segmentation.instantiator.instantiate_utils import ObjectGetter


class OptimGetter:
    def __init__(self, module_name, name, param_dict):
        self.optim = ObjectGetter(module_name, name)()
        self.param_dict = param_dict

    def __call__(self, model_params):
        return self.optim(model_params, **self.param_dict)
