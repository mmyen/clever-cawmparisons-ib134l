# Calculate Log Bayes Factors for each pair of models.

order = ["JC 69", "F81", "HKY", "GTR", "GTR + Gamma"] # Stores the names of the models in the order of the values presented

# All values were hard-coded into the Python script because there were only five of them, 
# 	and I am not planning on frequently updating the below values.
# 	The values were taken from the average_powp_log_likelihoods.csv
# If I were comparing more values, I would use the read_csv method to read in the data.
ss_likelihoods = [-11062.07, -10867.75, -10239.37, -10115.56, -9125.816]
ps_likelihoods = [-11061.46, -10865.66, -10235.17, -10113.58, -9125.033]

num_models = len(order)

# This assertion was put here to ensure that there were no issues in data entry
assert len(order) == len(ss_likelihoods) == len(ps_likelihoods)

# Calculate log Bayes Factors for log likelihoods generated using stepping-stone sampling method.
print("Stepping Stone")
for i in range(num_models):
	for j in range(num_models):
		print(order[i], order[j], ss_likelihoods[i] - ss_likelihoods[j])

# Calculate log Bayes Factors for log likelihoods generated using path-sampling method.
print("Path Sampling")
for i in range(num_models):
	for j in range(num_models):
		print(order[i], order[j], ps_likelihoods[i] - ps_likelihoods[j])