# 🌍 Project Terra

> An artificial ecosystem simulation where complex behaviors emerge from simple rules.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20development-orange?style=for-the-badge)

---

## 📖 About

Project Terra is an ecosystem simulation engine written in Python. It models an artificial world populated by autonomous agents that interact with each other and with their environment.

Every organism follows its own set of rules to survive, search for food, reproduce, and adapt to changing environmental conditions. Rather than scripting every possible behavior, the simulation is designed so that **complex ecosystem dynamics naturally emerge from simple local interactions**.

The project focuses on building a robust **Simulation Engine**, while visualization will be developed as a separate layer.

---

## ✨ Features

- 🌍 Grid-based world simulation
- 🌱 Dynamic environment
- 🐾 Autonomous agents
- ⚡ Energy-based survival system
- ❤️ Reproduction mechanics
- ☠️ Aging and death
- 🧠 Rule-based decision making
- ⏳ Tick-based simulation engine
- 🔧 Modular and scalable architecture

---

## 🌱 Initial Food Chain

```
🌳 Tree
    ↓
🐇 Rabbit
    ↓
🐍 Snake
    ↓
🦅 Hawk
```

Each organism has its own attributes and behaviors, including:

- Position
- Energy
- Age
- Perception
- Decision making
- Movement
- Reproduction
- Death

---

## 🌍 The World

The simulation takes place on a grid-based map.

Each cell can contain:

- Terrain
- Water
- Trees
- Animals
- Multiple entities

The initial world size is **16 × 16**, but the architecture allows future expansion.

---

## ⏳ Simulation Tick

Time advances through discrete **ticks**.

```
1 Tick = 3 Hours
```

Every tick executes the following pipeline:

1. Update world time
2. Update environment
3. Grow trees
4. Update animals
5. Resolve interactions
6. Update energy
7. Process reproduction
8. Remove dead entities

This deterministic execution order ensures consistent and reproducible simulations.

---

## 🏗️ Project Structure

```
Project-Terra/
│
├── app/                 # Camada da API (FastAPI)
│   ├── main.py          # Entrypoint do servidor e Rotas
│   └── engine/          # Motor da Simulação (Core)
│       ├── config/
│       ├── entities/
│       ├── world/
│       └── utils/
│
├── frontend/            # Interface em React + Bootstrap (Em breve)
├── docs/
├── tests/
├── README.md
└── pyproject.toml       # Gerenciamento de dependências com uv
```

### Engine

Controls the simulation loop and tick execution.

### World

Represents the environment, map, terrain, and world state.

### Entities

Contains every living organism and future entity types.

### Config

Stores simulation constants and configurable parameters.

### Utils

Utility modules shared across the project.

---

## 🚀 Roadmap

### Core Engine

- [x] Project architecture
- [x] Grid-based map
- [x] Cell system
- [x] Entity hierarchy
- [x] Tick engine
- [x] World scheduler

### Environment

- [x] Water generation
- [ ] Resource system
- [ ] Climate
- [ ] Seasons

### Flora

- [ ] Tree growth
- [ ] Tree lifecycle
- [ ] Environmental influence

### Fauna

- [ ] Rabbit behavior
- [ ] Snake behavior
- [ ] Hawk behavior
- [ ] Hunting system
- [x] Reproduction system

### Future

- [ ] PostgreSQL persistence
- [ ] Real-time visualization
- [ ] Artificial Intelligence agents
- [ ] Genetics
- [ ] Multiple biomes
- [ ] Parallel simulation

---

### Future / Web Integration
- [x] API with FastAPI and JSON serialization
- [ ] Visual interface with React and Bootstrap
- [ ] PostgreSQL persistence
- [ ] Artificial Intelligence agents

## 💻 Technologies

- Python 3.11+
- Object-Oriented Programming
- FastAPI (Backend API)
- React & Bootstrap (Frontend)
- uv (Package & Environment Manager)
- PostgreSQL *(planned)*

---

## 🎯 Goals

Project Terra was created to explore concepts such as:

- Software Architecture
- Object-Oriented Design
- Agent-Based Systems
- Simulation Engineering
- Artificial Intelligence
- Emergent Behavior
- Algorithms and Data Structures
- Backend Development

The long-term objective is to build a modular simulation framework capable of supporting increasingly sophisticated ecosystems.

---
## ▶️ Getting Started

Clone the repository:

```bash

git clone [https://github.com/RaphaelMota-bit/project-terra.git](https://github.com/RaphaelMota-bit/project-terra.git)
cd project-terra
Set up the environment and dependencies (using uv):

Bash
uv venv
uv sync
Run the API server:

Bash
uv run uvicorn app.main:app --reload
Access the interactive API documentation in your browser:
http://localhost:8000/docs

## 📈 Future Vision

Project Terra is designed to evolve far beyond a simple ecosystem simulation.

Planned future features include:

- Multiple ecosystems
- Rivers and terrain generation
- Weather and climate
- Disease simulation
- Evolution and genetics
- Social behaviors
- Machine Learning agents
- Distributed simulations
- Real-time visualization

---

## 🤝 Contributing

Contributions, ideas, and discussions are always welcome.

Feel free to open an issue or submit a pull request.


> *"The goal is not to program complex behaviors, but to create the rules from which complexity naturally emerges."*
