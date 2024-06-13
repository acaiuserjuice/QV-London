import matplotlib.pyplot as plt
import numpy as np

# demonstrate the cost of voting using n squared
votes = np.arange(1, 21)
cost = votes**2

plt.figure(figsize=(10, 6))
plt.plot(votes, cost, marker='o')
plt.title('Quadratic Voting Cost Function')
plt.xlabel('Number of Votes')
plt.ylabel('Cost (in Credits)')
plt.grid(True)
plt.xticks(votes)
plt.yticks(range(0, 401, 20))              # extended to range to demonstrate uptick in cost
plt.axhline(y=100, color='r', linestyle='--', label='100 Credits Line')
plt.axvline(x=10, color='b', linestyle='--', label='10 Votes Line')
plt.legend()
plt.savefig('quadratic_voting_cost_function.png')
plt.show()










