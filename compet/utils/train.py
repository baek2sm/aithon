import random
import numpy as np
import torch


def set_random_seed(seed=0):
    """Set a random seed for reproducibility
    :param seed: It is a number used to initialize a pseudorandom number generator.
    :return: None
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
