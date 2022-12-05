
# Run the below command to install dependencies
# !pip3 install pymc

import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import numpy as np
import arviz as az
from datetime import datetime

# Read in the data

df = pd.read_csv("samples.csv") 
n = len(df)-1
print(df)


true_sigma = 0.35      # Standard deviation of the error 
true_slope = 1.2      # The slope of the linear relationship (mm/year)

# When is low tide?
starttime = df.iloc[0][0]
starttime=starttime.split("T")[0]+" "+starttime.split("T")[1]
starttime=datetime.strptime(starttime, '%Y-%m-%d %H:%M')

hours_=[]
for hours in df["timestamp"].to_numpy():
  h=int(hours.split("T")[1][:2])
  if h>12:
    h-=12
  hours_.append(h)
hours_=np.array(hours_)

# print(hours_)

# Make seconds from lowtide using timestamps
seconds = starttime.timestamp() 
print("\nnumber of seconds since low tide.",seconds)

# Get the fish counts as a numpy array
fish_counts = df["jellyfish_entering"].to_numpy()

# print("\nfish counts in numpy array: ",fish_counts)

# How many seconds between lowtides?
period = 12.0 * 60.0 * 60.0

# Create a model
basic_model = pm.Model()
with basic_model:

    # Give priors for unknown model parameters
    magnitude = pm.Uniform("magnitude", lower=0, upper=200)
    sigma = pm.HalfNormal("sigma", sigma=12)

    # Create the model

    # Expected value of outcome
    expected_count = magnitude*pm.math.sin(0.000145444)*seconds

    # print(expected_count)

    Y_obs = pm.Normal("Y_obs", mu=expected_count, sigma=sigma)

    # Make chains
    # Due to high exceution time, Decrease the number_of_chains
    
    # trace = pm.sample(1000, chains=3,cores=1)
    # trace = pm.sample(500, return_inferencedata=True,tune=1000, chains=2000,cores=1)
    trace = pm.sample(500, chains=2000,cores=1)

# Find maximum a posteriori estimations
map_magnitude = pm.find_MAP(model=basic_model)
map_sigma = pm.find_MAP(model=basic_model)

# Let the user know the MAP values
print(f"Based on these {n} measurements, the most likely explanation:")
print(f"\tWhen the current is moving fastest, {map_magnitude['magnitude']:.2f} jellyfish enter the bay in 15 min.")
print(f"\tExpected residual? Normal with mean 0 and std of {map_sigma['sigma']:.2f} jellyfish.")

# Do a contour/density plot
fig, ax = plt.subplots(1, 1, figsize=(7, 7))
## Your code here
posterior = trace["posterior"]
p_magnitude = posterior["magnitude"]
p_sigma = posterior["sigma"]

ax = az.plot_kde(
    p_magnitude,
    p_sigma,
    hdi_probs=[0.3, 0.50, 0.8, 0.95], 
    contourf_kwargs={"cmap": "Blues"},
)

ax.vlines(true_slope, true_sigma - 0.1, true_sigma+0.1, linestyle="dashed")
ax.hlines(true_sigma, true_slope - 0.2, true_slope + 0.3, linestyle="dashed")
ax.set_xlabel("magnitude")
ax.set_ylabel("$\sigma$")
ax.set_title("Probability density of magnitude and $\sigma$")
fig.show()
fig.savefig("pdf.png")

# Plot your function and confidence against the observed data
fig, ax = plt.subplots(figsize=(8, 6))


## Your code here
ax.set_xlabel("Hours since low tides")
ax.set_ylabel("jellyfish entering in bay after 15 minutes")

ax.plot(hours_, fish_counts,"+", c='black', label='Obsereved')
ax.plot(fish_counts, c='r', linestyle="dashed", label='Prediction')
ax.plot(fish_counts,hours_, c='g', linestyle="dashed", label='95% Confidence')

plt.legend(loc='upper right')


fig.show()

fig.savefig("jellyfish.png")