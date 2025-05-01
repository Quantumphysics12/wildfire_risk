def resource_allocation(vCrewA, vCrewB, vCrew_Evac, vCrew_Lookout, vHeliA, vHeliB, vHeli_Evac, vHeli_Lookout, vDroneA, vDroneB, vDrone_Evac, vDrone_Lookout):
  import pyqubo
  from pyqubo import Binary, Constraint, Placeholder
  import matplotlib.pyplot as plt
  import seaborn as sns
  # Resources and tasks
  resources = ["Crew", "Heli", "Drone"]
  tasks = ["ZoneA", "ZoneB", "Evac", "Lookout"]
  # Effectiveness (higher = better)
  effectiveness = {
      ("Crew", "ZoneA"): vCrewA,
      ("Crew", "ZoneB"): vCrewB,
      ("Crew", "Evac"): vCrew_Evac,
      ("Crew", "Lookout"): vCrew_Lookout,
      ("Heli", "ZoneA"): vHeliA,
      ("Heli", "ZoneB"): vHeliB,
      ("Heli", "Evac"): vHeli_Evac,
      ("Heli", "Lookout"): vHeli_Lookout,
      ("Drone", "ZoneA"): vDroneA,
      ("Drone", "ZoneB"): vDroneB,
      ("Drone", "Evac"): vDrone_Evac,
      ("Drone", "Lookout"): vDrone_Lookout
  }

  # Binary variables: one for each (resource, task) pair
  x = {(r, t): Binary(f"x_{r}_{t}") for r in resources for t in tasks}

  # Objective: maximize effectiveness → minimize negative effectiveness
  objective = -sum(effectiveness[(r, t)] * x[(r, t)] for r in resources for t in tasks)

  # Constraint: each resource assigned to at most one task
  resource_constraints = sum(
      Constraint((sum(x[(r, t)] for t in tasks) - 1) ** 2, label=f"OneTask_{r}")
      for r in resources
  )

  # Combine objective and constraint
  H = objective + Placeholder("lambda") * resource_constraints

  # Compile model
  model = H.compile()
  qubo, offset = model.to_qubo(feed_dict={"lambda": 5.0})  # You can tune this weight
  variables = sorted({v for pair in qubo.keys() for v in pair})
  # Print QUBO matrix
  print("QUBO Matrix:")
  for term, coeff in qubo.items():
      print(f"{term}: {coeff}")
  import numpy as np
  variables = sorted({v for pair in qubo.keys() for v in pair})
  var_index = {var: i for i, var in enumerate(variables)}
  qubo_matrix = np.zeros((len(variables), len(variables)))

  for (i, j), value in qubo.items():
    i_idx, j_idx = var_index[i], var_index[j]
    qubo_matrix[i_idx, j_idx] = value
    if i != j:
            qubo_matrix[j_idx, i_idx] = value  # symmetry
  print("\nOffset:", offset)
  plt.figure(figsize=(8, 6))
  sns.heatmap(qubo_matrix, annot=True, fmt=".1f", cmap="coolwarm", xticklabels=variables, yticklabels=variables)
  plt.title("QUBO Matrix Heatmap")
  plt.xlabel("Variables")
  plt.ylabel("Variables")
  plt.tight_layout()
  plt.show()
8
def get_input(prompt):
    while True:
        try:
            # Ask for input
            value = int(input())

            # Check if the value is within the valid range
            if 1 <= value <= 10:
                value = 10 - value
                return value
            else:
                print("Please enter an integer between 1 and 10.")
        except ValueError:
            # If the input is not an integer
            print("Invalid input! Please enter an integer between 1 and 10.")

print("Please report the Public Protection Classification rating (PPC) for the following subjects. The number should be an integer between 1 and 10. Please not that '1' is the most effective, and '10' is the least effective in accordance with the Insurance Services Office (ISO)\n")
print("Effectiveness of Ground Fire-Fighting Crew in Zone A (high-fire-risk area): ")
[vCrewA, vCrewB, vCrew_Evac, vCrew_Lookout, vHeliA, vHeliB, vHeli_Evac, vHeli_Lookout, vDroneA, vDroneB, vDrone_Evac, vDrone_Lookout] = [1] * 12
get_input(vCrewA)
print("Effectiveness of Ground Fire-Fighting Crew in Zone B (moderate-fire-risk area): ")
get_input(vCrewB)
print("Effectiveness of Ground Fire-Fighting Crew in Town Evacuation: ")
get_input(vCrew_Evac)
print("Effectiveness of Ground Fire-Fighting Crew in Lookout duties: ")
get_input(vCrew_Lookout)

print("Effectiveness of Helicopter in Zone A (high-fire-risk area): ")
get_input(vHeliA)
print("Effectiveness of Helicopter in Zone B (moderate-fire-risk area): ")
get_input(vHeliB)
print("Effectiveness of Helicopter in Town Evacuation: ")
get_input(vHeli_Evac)
print("Effectiveness of Helicopter in Lookout duties: ")
get_input(vHeli_Lookout)

print("Effectiveness of Drone in Zone A (high-fire-risk area): ")
get_input(vDroneA)
print("Effectiveness of Drone in Zone B (moderate-fire-risk area): ")
get_input(vDroneB)
print("Effectiveness of Drone in Town Evacuation: ")
get_input(vDrone_Evac)
print("Effectiveness of Drone in Lookout duties: ")
get_input(vDrone_Lookout)


resource_allocation(vCrewA, vCrewB, vCrew_Evac, vCrew_Lookout, vHeliA, vHeliB, vHeli_Evac, vHeli_Lookout, vDroneA, vDroneB, vDrone_Evac, vDrone_Lookout);