'''
author: Xaver Funk
purpose: power analysis for https://osf.io/ap2eg/
'''

from statsmodels.stats.power import TTestPower
from math import ceil

# instantiate test
power_test = TTestPower()

alpha = 0.05 # significance level: probability of rejecting the null, even though it is true
r = 1 # effect size
beta = 0.2 # probability of accepting the null, even though it is false
power = 1 - beta # probability of rejecting the null when real difference is equal to minimum effect size
effect_size = .47 # this is the smallest effect size we aim to replicate, reported in Daws et al. 2022 for modularity chnages after psilocybin

# calculate required N
N = power_test.solve_power(effect_size = effect_size, alpha=alpha, power=power, 
                     alternative='two-sided')

print(f"We expect to detect the desired effect size (Cohen's d \u2265 {effect_size}) at an alpha level of \u03B1 < {alpha} and an achieved power of \u03B2 = {power}, assuming two-sided t-tests and paired samples, with a sample size of {ceil(N)}")