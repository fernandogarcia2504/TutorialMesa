from Exercise import MoneyModel
import matplotlib.pyplot as plt
plt.show()

starter_model = MoneyModel(10)
for i in range(5):
    starter_model.step()

agent_wealth = [a.wealth for a in starter_model.schedule.agents]
# Create a histogram with seaborn
g = sns.histplot(agent_wealth, discrete=True)
g.set(title="Wealth distribution", xlabel="Wealth", ylabel="Number of agents"); 
 # The semicolon is just to avoid printing the object representation
