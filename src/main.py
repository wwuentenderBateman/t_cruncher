from scipy.stats import t

# Parameters
alpha = 0.05        # Significance level
df = 8              # Degrees of freedom
tail = 'two-tailed' # Choose 'one-tailed' or 'two-tailed'

# t-critical calculation
if tail == 'two-tailed':
    t_crit = t.ppf(1 - alpha / 2, df)
else:
    t_crit = t.ppf(1 - alpha, df)

print(f"t-critical value: ±{round(t_crit, 3)}")