# Cellular Automaton -> Fire Propagation

<!-- PROJECT GIF -->
<br />
<div align="center">
  <a href="https://github.com/albertojc6/CA-HEURISTICS">
    <img src="ForestFireModel/layer_evolutions/fire_propagation.gif" alt="Fire Propagation Demo" width="400">
  </a>

  <h3 align="center">Cellular Automaton Forest Fire Model</h3>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#repo-structures">Repository Structures</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

In the first part of the practice, we will focus on the implementation of a cellular automaton based on Wolfram's rules. The main objective will be to create this automaton and understand the concepts that define it: the update rule, the combination rule, the neighborhood, among others. <br>

In a second part of the practice, once the basic concepts of cellular automata have been internalized, we will want to model the spread of a forest fire. Thus, the main objective will be the simulation of this system, since studying its behavior in a real experiment is unfeasible. In this sense, we will be able to analyze the results of the interactions between the different layers. In short, this second part will serve to give a more practical and real approach to our cellular automata.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites


* Python
  ```sh
  pip install pygame
  pip install matplotlib
  ```

### Installation

1. Clone the repo
  ```sh
  git clone https://github.com/albertojc6/CA-Heuristics.git
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

```python
from ForestFireCA import ForestFireCA

forest_fire = ForestFireCA(rows = 100, columns = 100, random_state = 42)
steps_fire, steps_fuel, steps_humidity = forest_fire.simulate(t = 100)

visualize_gif(steps_fire, layer = 'fire', name = 'fire_propagation.gif')
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Repository Structures

    .
    ├── CellularAutomaton.ipynb              # Generalized Wolfram's CA
    ├── ForestFireModel                      
    |    ──> data                            # Simulation data examples 
    |    ──> data_generator.py               # Function to generate artificial forest data
    |    ──> ForestFireCA.py                 # Model
    |    ──> Forest_fire_model.ipynb.py      # Use-case example, with visualizations      
    └── README.md

<p align="right">(<a href="#repo-structures">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Jordi Granja Bayot - jordi.granja.i@estudiantat.upc.edu - @jordigb4  
Alberto Jerez Cubero - alberto.jerez@estudiantat.upc.edu - @albertojc6

Project Link: [https://github.com/albertojc6/CA-Heuristics](https://github.com/albertojc6/CA-Heuristics)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
