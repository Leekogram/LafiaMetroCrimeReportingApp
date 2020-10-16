import numpy as np
import pandas as pd

try:
    # module exists
    import seaborn as sns
    seaborn_exists = True
except ImportError:
    # module doesn't exist
    seaborn_exists = True

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
