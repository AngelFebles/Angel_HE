from scipy.stats import chisquare
import numpy as np

chi_stat = chisquare([16, 18, 16, 14, 12, 12], f_exp=[16, 16, 16, 16, 16, 8])

print()
