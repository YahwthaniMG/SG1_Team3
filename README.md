# SG1_Team3 - Laptop Manufacturing Simulation

## Project Overview

This repository contains a comprehensive simulation of a laptop manufacturing process, developed as part of a simulation and visualization course. The project utilizes Python and SimPy to model a complex manufacturing line, analyzing production efficiency, bottlenecks, and potential improvements.

## Table of Contents
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Running the Simulation](#running-the-simulation)
- [Simulation Parameters](#simulation-parameters)
- [Output and Metrics](#output-and-metrics)
- [Team Members](#team-members)

## Installation

### Prerequisites
- Python 3.13 or higher
- pip package manager

### Clone the Repository
```bash
git clone https://github.com/YahwthaniMG/SG1_Team3.git
cd SG1_Team3/Simulator
```

### Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Dependencies
- SimPy
- NumPy
- Matplotlib

## Project Structure
```
SG1_Team3/
│
└── Simulator/
    ├── main.py         # Main simulation runner
    ├── simulation.py   # Core simulation logic
    ├── metrics.py      # Metrics collection and analysis
    ├── README.md       # Project documentation
    └── requirements.txt# Dependency list
```

## Running the Simulation

### Basic Execution
```bash
python main.py
```

### Custom Simulation Parameters
You can modify simulation parameters in `main.py`:
- Number of runs
- Simulation time
- Specific station configurations

## Simulation Parameters

### Workstation Configuration
- 6 specialized workstations
- Initial material capacity: 25 units per station
- 3 resupply devices

### Failure Probabilities
- Station 1 (Motherboard): 2%
- Station 2 (CPU): 1%
- Station 3 (GPU): 5%
- Station 4 (Memory): 15%
- Station 5 (Case): 7%
- Station 6 (Screen): 6%

## Output and Metrics

The simulation generates comprehensive console output including:
- Total production
- Defect rates
- Station occupancy
- Downtime analysis
- Economic impact estimation

## Team Members
- Andrés López Álvarez
- Omar Vidaña Rodríguez
- Yahwthani Morales Gómez
- Hector Manuel Eguiarte Carlos

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments
- Professor Gabriel Castillo
- Simulation & Visualization Course
- SimPy Documentation

---

**Note**: This simulation is a computational model and requires validation in real-world manufacturing environments.
