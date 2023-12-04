OBJECTIVE: Use genomic data from the family *Corvidae* to compare the performance of different models in the Bayesian approach to phylogeny

ASSETS:
- data folder: a folder containing two file:
    - data/corvids_and_losh_2.nex (rename in final clean repo): a Nexus file containing the gene sequences for the cytochrome b (cytb) gene for 29 species of corvid, plus 1 outgroup (*Lanius ludovicianus*)
    - data/average_powp_log_likelihoods.csv: a comma-separated values file containing the average log likelihoods calculated under the path sampling and stepping-stone sampling methods for the power posteriors
- scripts folder: a folder containing 11 scripts.
    - scripts/calculate_log_bf.py: A Python3 script for calculating log Bayes Factors.
    - scripts/corvid_F81_powp.Rev: A RevBayes script using power posteriors to calculate average log marginal likelihoods for the Felsenstein 1981 nucleotide substitution model (F81)
    - scripts/corvid_F81.Rev: A RevBayes script that finds the maximum *a posteriori* non-clock tree under the F81 model
    - scripts/corvid_GTR_Gamma_powp.Rev: A RevBayes script using power posteriors to calculate average log marginal likelihoods for the General Time-Reversible nucleotide substitution model with Discrete Gamma (GTR + Γ)
    - scripts/corvid_GTR_Gamma.Rev: A RevBayes script that finds the maximum *a posteriori* non-clock tree under the GTR + Γ model
    - scripts/corvid_GTR_powp.Rev: A RevBayes script using power posteriors to calculate average log marginal likelihoods for the General Time-Reversible nucleotide substitution model (GTR)
    - scripts/corvid_GTR.Rev: A RevBayes script that finds the maximum *a posteriori* non-clock tree under the GTR model
    - scripts/corvid_HKY_powp.Rev: A RevBayes script using power posteriors to calculate average log marginal likelihoods for the Hasegawa-Kishino-Yano 1985 nucleotide substitution model (HKY85/HKY)
    - scripts/corvid_HKY.Rev: A RevBayes script that finds the maximum *a posteriori* non-clock tree under the HKY85 model
    - scripts/corvid_JC_powp.Rev: A RevBayes script using power posteriors to calculate average log marginal likelihoods for the Jukes-Cantor 1969 nucleotide substitution model (JC69/JC)
    - scripts/corvid_HKY.Rev: A RevBayes script that finds the maximum *a posteriori* non-clock tree under the JC69 model
- (gitignore proposal in final repo)
- (placeholder for report)
- README.md: a file with instructions on how to run the scripts.

REQUIREMENTS/CONSTRAINTS:
- The code should be ran on a machine able to install and run python3.
- The code should be ran on a machine able to install and run RevBayes. The scripts can be run through the terminal.
- The code takes time in the magnitude of hours to run. The computer must be able to keep running the code even when the screen shuts off.
- The filepaths at the beginning of each Rev script should be updated as needed.

If you have any questions about how to run the scripts, you can email me at \*\*\*\*\*@berkeley.edu