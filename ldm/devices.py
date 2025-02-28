import torch

def choose_torch_device() -> str:
    '''Convenience routine for guessing which GPU device to run model on'''
    if torch.cuda.is_available():
        return 'cuda'
    if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        return 'mps'
    return 'cpu'

def choose_autocast_device(device) -> str:
    '''Returns an autocast compatible device from a torch device'''
    device_type = device.type # this returns 'mps' on M1
    # autocast only supports cuda or cpu
    if device_type not in ('cuda','cpu'):
        return 'cpu'
    return device_type
