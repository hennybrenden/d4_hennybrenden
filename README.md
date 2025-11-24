# 🧮 INF201 – Deliverable 4  
### Walking home from AudMax  

Dette prosjektet er koblet til GitHub via SSH og satt opp fra terminalen.
Her ligger deliverable 4, som jeg leverer alene.  

**👩‍💻 Author:** Henny Brenden  
**🌐 GitHub Profile:** [@hennybrenden](https://github.com/hennybrenden)  
**Repository:** <https://github.com/hennybrenden/d4_hennybrenden>
**📅 Date:** November 2025

---

## 🧠 Overview  
This project implements the *Deliverable 4* assignment for INF201.  
The goal is to build a complete and documented Python package, including:

- A simulation of a student (Alex) walking home from AudMax  
- A structured package layout using modules and classes  
- A test suite using `pytest`  
- Automatic test execution with GitHub Actions  
- Packaging using `pyproject.toml` and wheel-building  
- A Jupyter notebook exploring how probabilities affect the outcome  
- Git development workflow (issues, milestone, branches, PR)

The simulation models a random walk on a 1D axis from 0–100, with:
- Pentagon  
- AudMax  
- Kaia  

Alex walks randomly each second, and may be absorbed at Pentagon or Kaia based on:
- `p_pentagon`
- `p_kaia`

---


## 📦 Project structure

walk/                      # Python package
  __init__.py
  model.py                 # AlexWalk and SimulationResult
  simulation.py            # run_many() helper for many simulations

tests/                     # Test suite (pytest)
  test_model.py
  test_simulation.py

examples/
  run_example.py           # Simple script that runs many simulations
  walk_experiments.ipynb   # Jupyter notebook for Task 3

.github/workflows/
  tests.yml                # GitHub Actions workflow running tox

pyproject.toml             # Packaging configuration
tox.ini                    # Tox configuration for running tests
README.md                  # This file 

---


## ⚙️ Files Included
| File | Description |
|------|-------------|
| `model.py` | AlexWalk + SimulationResult implementation |
| `simulation.py` | Function for running many simulations + statistics |
| `test_model.py` | Unit tests for model logic |
| `test_simulation.py` | Tests for aggregated simulation results |
| `run_example.py` | Example that prints summary statistics |
| `walk_experiments.ipynb` | Notebook exploring p-values graphically |
| `pyproject.toml` | Package definition & build config |
| `tox.ini` | Test automation config |
| `tests.yml` | GitHub Actions workflow for CI |
| `d4.log` | Git log (created before submission) |
| `*.whl` | Wheel file created using `python -m build` |
| `video` | ≤3 minute project explanation video |
---


## 🧪 Test Coverage  
Tests include:

- Correct termination at Pentagon/Kaia  
- Handling of deterministic probabilities (`p = 1` or `0`)  
- `run_many()` structure and output fields  
- Validity of `SimulationResult`  

Run all tests using:

'''bash
tox

---

## ▶️ How to run the example

'''bash
python examples/run_example.py

---

## 🧬 Task 3 — Jupyter Notebook
examples/walk_experiments.ipynb contains:
- Multiple simulations over a grid of p-values
- DataFrame summarising results
- Heatmap visualisation
- Short discussion of observations

Open it using:
jupyter notebook examples/walk_experiments.ipynb

---

## 🏗️ How to build the wheel

'''bash
pip install build
python -m build

The wheel is created inside:
dist/walk-0.1.0-py3-none-any.whl

---

## 📝 Git Log
git log > d4.log

---

## 🎥 Video
A three minute long video, explaining the code. 

---

## ✅ Summary

This project demonstrates:
- Proper Python package structure
- Unit testing with pytest
- Continuous Integration
- Packaging and wheel-building
- Random walk simulation
- Jupyter exploration and visualization
- GitHub workflow with issues, milestone, branch and PR

Deliverable 4 completed with all required components.

---



