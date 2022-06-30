TODO: Reflect on what you learned this week and what is still unclear.

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime

%matplotlib inline

plt.rcParams['figure.figsize'] = (10, 5)

saved_style_state = matplotlib.rcParams.copy() #give us a style state to go back to
