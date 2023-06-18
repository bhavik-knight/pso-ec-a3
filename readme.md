# Particle Swarm Optimization
## Evolutionary Computation

---

- This is a ubiquitos algorithm that solves optimization problems which are not necessarily differentiable
- Classical algorithm needs the problems to be differntiable
- Inspired by the social behavior of birds that are searching for food
- The swarm (group) as a whole search for global optima, while each particle search for local optima
- The particle have their own position, velocity and fitness value
- All particles communicate, hence their best fitness value and local optima is known all the time
- The important componets are `Inertia Component`, `Congnitive Component` and `Social Component`
- The parameters are `number of dimensions`, `lower bound` ans `upper bound`
- The hyperparameters can be tuned to get better performace.
- The algorithm iteratively look try to improve the candiate solution against the fitness value

---

---
- Python version: 3.10
- [Pyswarms library](https://pyswarms.readthedocs.io/en/latest/tutorials.html)
- [Matplotlib library](https://matplotlib.org/stable/users/installing/index.html)

## instructiosn to run:
1. create virtual environment to install all packages needed for to run the program locally
```python -m venv pso-env```
2. activate the virual environment
```source pso-env/bin/activate```
3. clone the repository:
4. install required files:
```pip install -r requirements.py```


---
references:
- PSO - [wikipedia](https://en.wikipedia.org/wiki/Particle_swarm_optimization)
- [geeks-for-geeks](https://www.geeksforgeeks.org/particle-swarm-optimization-pso-an-overview/)
