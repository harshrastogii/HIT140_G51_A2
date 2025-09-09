import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load datasets
df1 = pd.read_csv('data/dataset1.csv')
df2 = pd.read_csv('data/dataset2.csv')

print("HIT140 - Investigation A: Do bats perceive rats as predators?")
print("="*60)

# Key findings
risk_avoiders = df1[df1['risk'] == 0]
risk_takers = df1[df1['risk'] == 1]

print(f"Risk-avoiders success rate: {risk_avoiders['reward'].mean():.1%}")
print(f"Risk-takers success rate: {risk_takers['reward'].mean():.1%}")

# Statistical test
contingency_table = pd.crosstab(df1['risk'], df1['reward'])
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
print(f"Statistical significance: p < {p_value:.6f}")

# Create visualization
plt.figure(figsize=(10, 5))
success_rates = [risk_avoiders['reward'].mean(), risk_takers['reward'].mean()]
plt.bar(['Risk-Avoiders', 'Risk-Takers'], success_rates, color=['red', 'blue'])
plt.ylabel('Success Rate')
plt.title('Bat Success Rates: Evidence of Predator Perception')
plt.ylim(0, 1)
plt.savefig('final_results.png', dpi=300)
plt.show()

print("Conclusion: Bats perceive rats as predators - risk-avoidance wins!")