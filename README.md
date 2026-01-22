# FluSpread-Sim-A Data-Driven Kinetic SIR Model of Influenza Transmission

FluSpread-Sim is a Python-based epidemiological simulation that utilizes a kinetic "billiard-ball" model to visualize the spread of Influenza (flu) within a closed population. This project moves beyond naive assumptions by using empirical data from the CDC and Oxford Academic to define transmission probabilities and recovery timelines.

## 🔬 Scientific Foundation & Insights

This simulation is built upon core parameters extracted from the following external resources:

1.  **CDC / World Health Organization Influenza Guidelines** * **Insight:** Research indicates that the transmission probability of Influenza is approximately 15% per contact between a susceptible and an infected individual.
    * **Implementation:** The model uses `FLU_TRANSMISSION_PROB = 0.15` during collision detection.

2.  **"Time Lines of Infection" (Oxford Academic)** * **Insight:** Most healthy adults remain contagious for a duration of 5 to 7 days.
    * **Implementation:** Mapping time to frames (30 frames = 1 day), the model sets a recovery window of 180 frames (`FLU_RECOVERY_TIME`) to represent a 6-day infectious period.

## 🛠️ Model Mechanics

The simulation utilizes the **SIR Model** (Susceptible, Infected, Recovered):
* **Blue (Susceptible):** Individuals who can contract the virus.
* **Red (Infected):** Individuals currently spreading the virus.
* **Green (Recovered/Immune):** Individuals who have either recovered from infection or were pre-vaccinated, making them immune to further spread.


## 📊 Scenarios & Visualization

The project simulates two distinct scenarios to demonstrate the impact of public health interventions:

* **Scenario A: 0% Vaccination Rate** – A "natural" spread scenario where a single infected individual enters a completely susceptible population.
* **Scenario B: 50% Vaccination Rate** – A scenario demonstrating herd immunity, where half the population starts in the 'Recovered' (immune) state.

### Visual Presentation
1.  **Pygame Animation:** A real-time visual representation of particle collision and infection spread.
2.  **Matplotlib Analysis:** A dual-plot comparison showing the "flattening of the curve" and total susceptible depletion across both scenarios.

### Results
The simulation clearly illustrates that even a 50% vaccination rate significantly reduces the peak number of concurrent infections and prevents the total exhaustion of the susceptible population, effectively "breaking" the chain of transmission.
<img width="1498" height="704" alt="image" src="https://github.com/user-attachments/assets/952f299d-c54a-4c4e-a920-c203a0168689" />


## 🚀 Getting Started

### Prerequisites
* Python 3.x
* Pygame
* Matplotlib

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/FluSpread-Sim.git](https://github.com/GligorMaria/FluSpread-Sim.git)


2. Install dependencies:
   ```bash
   pip install pygame matplotlib

3. Run the simulation
   ```bash
   python main.py


