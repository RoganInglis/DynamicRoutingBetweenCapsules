from models.base_model import BaseModel
from models.capsnet_model import CapsNetModel

__all__ = [
    "BaseModel",
    "CapsNetModel"
]


def make_model(config):
    if config['model_name'] in __all__:
        return globals()[config['model_name']](config)
    else:
        raise Exception('The model name %s does not exist' % config['model_name'])


def get_model_class(config):
    if config['model_name'] in __all__:
        return globals()[config['model_name']]
    else:
        raise Exception('The model name %s does not exist' % config['model_name'])
