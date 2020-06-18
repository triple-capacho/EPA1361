# EPA1361 Hand-in final assignment
This is the hand in for the final assignment of EPA1361 - Model-based decision-making. </br>

## File structure
The file structure is as seen in the structure format below.
```bash
EPA1361
│   .gitignore
│   README.md
│
├───final assignment
│   │   .gitattributes
│   │   50pol10000scen.py
│   │   dike_model_function.py
│   │   ExplanationOrInformation.ipynb
│   │   ExploringModel.ipynb
│   │   FinalRunNeat.ipynb
│   │   FinalRunNeatOptimization.ipynb
│   │   funs_dikes.py
│   │   funs_economy.py
│   │   funs_generate_network.py
│   │   funs_hydrostat.py
│   │   helper.py
│   │   PerformingExperiments.ipynb
│   │   ProblemFormulationSelf.py
│   │   problem_formulation.py
│   │   README.md
│   │   sobol.py
│   │   test.py
│   │   __init__.py
│   │
│   ├───data
│   │   │   dikeIjssel.xlsx
│   │   │   dikeIjssel_alldata.xlsx
│   │   │   EWS.xlsx
│   │   │   rfr_strategies.xlsx
│   │   │
│   │   ├───exp
│   │   │       200Scenario_20Policy.tar.gz
│   │   │       500Scenario_NoPolicy.tar.gz
│   │   │       a4-5_10000nfemoea
│   │   │       baseRequest-80years.tar.gz
│   │   │       baseRequest.tar.gz
│   │   │       baseRequest1-80years.tar.gz
│   │   │       baseRequest1.tar.gz
│   │   │       baseRequest4-80years.tar.gz
│   │   │       baseRequest4.tar.gz
│   │   │       Gelderland.tar.gz
│   │   │       mc10pol10000scen.tar.gz
│   │   │       mc10pol1000scen.tar.gz
│   │   │       MOEA100k.tar.gz
│   │   │       moro1k.tar.gz
│   │   │       moro1k_NoCostLimit.tar.gz
│   │   │       nopol1000scen.tar.gz
│   │   │       noPol1000ScenVul.tar.gz
│   │   │       requestbridges-80years.tar.gz
│   │   │       requestbridges.tar.gz
│   │   │       requestbridges1-80years.tar.gz
│   │   │       requestbridges1.tar.gz
│   │   │       requestbridges4-80years.tar.gz
│   │   │       requestbridges4.tar.gz
│   │   │       requestbridgestry2.tar.gz
│   │   │       sobol1pol4000scen.tar.gz
│   │   │       sobolnopol40000scen.tar.gz
│   │   │       sobolnopol4000scen.tar.gz
│   │   │       sobolpol40000scen.tar.gz
│   │   │       solTest1.tar.gz
│   │   │       solTest2.tar.gz
│   │   │       solTestworstcase.tar.gz
│   │   │       solTestworstcase100.tar.gz
│   │   │       TransportBridges.tar.gz
│   │   │       worstcaseopt.tar.gz
│   │   │       worstcaseoptv2.tar.gz
│   │   │
│   │   ├───figs
│   │   ├───fragcurves
│   │   │       calfactors_pf1250.xlsx
│   │   │       frag_curves.xlsx
│   │   │
│   │   ├───hydrology
│   │   │       Qpeak_unisamples125_12500.txt
│   │   │       wave_shapes.xls
│   │   │       werklijn_params.xlsx
│   │   │
│   │   ├───losses_tables
│   │   │       A.1_lossestable.xlsx
│   │   │       A.2_lossestable.xlsx
│   │   │       A.3_lossestable.xlsx
│   │   │       A.4_lossestable.xlsx
│   │   │       A.5_lossestable.xlsx
│   │   │
│   │   ├───muskingum
│   │   │       params.xlsx
│   │   │
│   │   └───rating_curves
│   │           A.1_ratingcurve_new.png
│   │           A.1_ratingcurve_new.txt
│   │           A.2_ratingcurve_new.png
│   │           A.2_ratingcurve_new.txt
│   │           A.3_ratingcurve_new.png
│   │           A.3_ratingcurve_new.txt
│   │           A.4_ratingcurve_new.png
│   │           A.4_ratingcurve_new.txt
│   │           A.5_ratingcurve_new.png
│   │           A.5_ratingcurve_new.txt
│   │           Ijsseldischarges_16000.csv
│   │           Ijsseldischarges_19000.csv
│   │           Ijsselwaterlevels_16000.csv
│   │           Ijsselwaterlevels_19000.csv
│   │
│   ├───Figures
│   │       10000scenplot.png
│   │       boxplot_damage_NoPolicy.png
│   │       boxplot_deaths_NoPolicy.png
│   │       boxplot_NoPolicy.png
│   │       distributions_10policies.png
│   │       distributions_NoPolicy.png
│   │       FeatureScoring.png
│   │       feature_scoring_10policie.png
│   │       feature_scoring_10policies.png
│   │       prim_1.png
│   │       rfr_IJssel.PNG
│   │       rfr_wlreduction.PNG
│   │       ScatterPlotting.png
│   │       ScatterPlotting2.png
│   │       ScatterPlottingAvgExp.png
│   │       ScatterPlottingworstExp.png
│   │       ScatterPlotting_aggregated.png
│   │
│   ├───Tables
│   │       averge of outcomes_normaluncertainty.csv
│   │       averge of outcomes_worstscenrio.csv
│   │
│   └───__pycache__
│           dike_model_function.cpython-38.pyc
│           funs_dikes.cpython-38.pyc
│           funs_economy.cpython-38.pyc
│           funs_generate_network.cpython-38.pyc
│           funs_hydrostat.cpython-38.pyc
│           helper.cpython-38.pyc
│           ProblemFormulationSelf.cpython-38.pyc
│           problem_formulation.cpython-38.pyc
│
└───Report
    │   EPA1361_Group15_finalAssignment.pdf
    │
    └───source
            EPA1361_Group15_finalAssignment.docx
```

The final assignment folder contains the code and everything that the code generated, which is later used in the report. 
