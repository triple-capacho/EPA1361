import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from ema_workbench import save_results
from ema_workbench import ema_logging, MultiprocessingEvaluator
from ema_workbench import Model, RealParameter, ScalarOutcome, CategoricalParameter, IntegerParameter, BooleanParameter
from ema_workbench.em_framework.samplers import sample_uncertainties
# from ema_workbench.em_framework.evaluators import MC
from dike_model_function import DikeNetwork
from problem_formulation import get_model_for_problem_formulation
ema_logging.log_to_stderr(ema_logging.INFO)

dike_model, planning_steps = get_model_for_problem_formulation(5)

ema_logging.log_to_stderr(ema_logging.INFO)

# setup the policies
from ema_workbench import Policy

base_dict = {'0_RfR 0':1, 
               '0_RfR 1':1,
               '0_RfR 2':1,
               '1_RfR 0':0,
               '1_RfR 1':0,
               '1_RfR 2':0,
               '2_RfR 0':0,
               '2_RfR 1':0,
               '2_RfR 2':0,
               '3_RfR 0':0,
               '3_RfR 1':0,
               '3_RfR 2':0,
               '4_RfR 0':0,
               '4_RfR 1':0,
               '4_RfR 2':0,
               'EWS_DaysToThreat':0,
               'A.1_DikeIncrease 0':0,
               'A.1_DikeIncrease 1':0,
               'A.1_DikeIncrease 2':0,
               'A.2_DikeIncrease 0':0,
               'A.2_DikeIncrease 1':0,
               'A.2_DikeIncrease 2':0,
               'A.3_DikeIncrease 0':0,
               'A.3_DikeIncrease 1':0,
               'A.3_DikeIncrease 2':0,
               'A.4_DikeIncrease 0':0,
               'A.4_DikeIncrease 1':0,
               'A.4_DikeIncrease 2':0,
               'A.5_DikeIncrease 0':0,
               'A.5_DikeIncrease 1':0,
               'A.5_DikeIncrease 2':0}

pols = [Policy('RFR policy', **{'0_RfR 0':1,
                                  '0_RfR 1':1,
                                  '0_RfR 2':1}),
           Policy('policy 2', **{'4_RfR 0':1,
                                  '4_RfR 1':1,
                                  '4_RfR 2':1}),
           Policy('policy 3', **{'1_RfR 0':1,
                                  '2_RfR 1':1,
                                  '3_RfR 2':1})]

with MultiprocessingEvaluator(dike_model) as evaluator:
    results = evaluator.perform_experiments(scenarios=1000,               #500
                                            policies=[pols[0]],
                                            uncertainty_sampling='mc', reporting_interval=100)


save_results(results, './transport.tar.gz')