import pygame
import random
import matplotlib.pyplot as plt

# Resource 1: CDC / World Health Organization Influenza Guidelines
# Insight: Influenza has a transmission probability of ~15% per contact.
FLU_TRANSMISSION_PROB = 0.15

# Resource 2: "Time Lines of Infection" (Oxford Academic)
# Insight: Most adults are contagious for 5-7 days.
# We map 1 day to 30 frames in Pygame, so 6 days = 180 frames.
FLU_RECOVERY_TIME = 180

# Simulation Settings
WIDTH, HEIGHT = 800, 600
POPULATION_SIZE = 150
BALL_RADIUS = 5


class Person:
    def __init__(self, start_status="S"):
        self.x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        self.y = random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS)
        self.vel_x = random.uniform(-2, 2)
        self.vel_y = random.uniform(-2, 2)
        self.status = start_status  # S, I, or R
        self.timer = 0

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x <= 0 or self.x >= WIDTH: self.vel_x *= -1
        if self.y <= 0 or self.y >= HEIGHT: self.vel_y *= -1

    def update_health(self):
        if self.status == "I":
            self.timer += 1
            if self.timer > FLU_RECOVERY_TIME:
                self.status = "R"


def run_simulation(scenario_name, vaccination_rate):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Scenario: {scenario_name}")
    clock = pygame.time.Clock()

    # Create Population
    people = []
    num_vaccinated = int(POPULATION_SIZE * vaccination_rate)

    for i in range(POPULATION_SIZE):
        if i < num_vaccinated:
            people.append(Person(start_status="R"))  # Vaccinated/Immune
        else:
            people.append(Person(start_status="S"))  # Susceptible

    # Patient Zero
    people[-1].status = "I"

    stats = {"S": [], "I": [], "R": []}
    running = True

    while running:
        screen.fill((255, 255, 255))
        s_count, i_count, r_count = 0, 0, 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Logic Loop
        for p in people:
            p.move()
            p.update_health()

            # Stats Counting
            if p.status == "S":
                s_count += 1
            elif p.status == "I":
                i_count += 1
            else:
                r_count += 1

            # Drawing
            color = (0, 0, 255) if p.status == "S" else (255, 0, 0) if p.status == "I" else (0, 255, 0)
            pygame.draw.circle(screen, color, (int(p.x), int(p.y)), BALL_RADIUS)

            # Infection Logic
            if p.status == "I":
                for other in people:
                    if other.status == "S":
                        dist = ((p.x - other.x) ** 2 + (p.y - other.y) ** 2) ** 0.5
                        if dist < BALL_RADIUS * 2:
                            if random.random() < FLU_TRANSMISSION_PROB:
                                other.status = "I"

        stats["S"].append(s_count)
        stats["I"].append(i_count)
        stats["R"].append(r_count)

        pygame.display.flip()
        clock.tick(60)

        if i_count == 0:  # Simulation ends when virus dies out
            running = False

    pygame.quit()
    return stats


# --- 2. EXECUTION & VISUAL PRESENTATION ---

print("Running Scenario A: Flu with 0% Vaccination...")
data_a = run_simulation("Flu (No Vaccine)", 0.0)

print("Running Scenario B: Flu with 50% Vaccination...")
data_b = run_simulation("Flu (50% Vaccinated)", 0.5)

# Final Plots
plt.figure(figsize=(12, 5))

# Plot Scenario A
plt.subplot(1, 2, 1)
plt.plot(data_a["I"], color="red", label="Infected")
plt.plot(data_a["S"], color="blue", label="Susceptible")
plt.title("Scenario A: No Vaccine")
plt.legend()

# Plot Scenario B
plt.subplot(1, 2, 2)
plt.plot(data_b["I"], color="red", label="Infected")
plt.plot(data_b["S"], color="blue", label="Susceptible")
plt.title("Scenario B: 50% Vaccine")
plt.legend()

plt.tight_layout()
plt.show()