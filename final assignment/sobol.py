from SALib.analyze import sobol
from ema_workbench import Policy
from ema_workbench.em_framework.evaluators import SOBOL
from ema_workbench import (MultiprocessingEvaluator, SequentialEvaluator)
from ema_workbench.em_framework.salib_samplers import get_SALib_problem
from ema_workbench.analysis import prim
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from ema_workbench import ema_logging
from ema_workbench import Model, RealParameter, ScalarOutcome, CategoricalParameter, IntegerParameter, BooleanParameter
from ema_workbench.em_framework.samplers import sample_uncertainties
# from ema_workbench.em_framework.evaluators import MC
from dike_model_function import DikeNetwork
from problem_formulation import get_model_for_problem_formulation
ema_logging.log_to_stderr(ema_logging.INFO)

dike_model, planning_steps = get_model_for_problem_formulation(5)


    

policies_0 = [Policy('no policy', **{l.name: 0 for l in dike_model.levers})]

n_scen = 1000
print(n_scen)
with MultiprocessingEvaluator(dike_model) as evalu:
    sa_results = evalu.perform_experiments(n_scen, policies=policies_0, uncertainty_sampling='sobol', reporting_interval=400)

from ema_workbench import save_results
save_results(sa_results, './data/exp/sobolnopol40000scen.tar.gz')

uncertainty = dike_model.uncertainties
levers = dike_model.levers

dike_model.levers = uncertainty
dike_model.uncertainty = levers

n_scen = 10
print(n_scen)
with MultiprocessingEvaluator(dike_model) as evalu:
    sa_results = evalu.perform_experiments(n_scen, policies=25, uncertainty_sampling='sobol', reporting_interval=400)

from ema_workbench import save_results
save_results(sa_results, './data/exp/sobolpol40000scen.tar.gz')