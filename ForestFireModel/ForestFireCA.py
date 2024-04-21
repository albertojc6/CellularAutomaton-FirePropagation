from data_generator import *

class ForestFireCA:

    def __init__(self, rows = 100, columns = 100, random_state = 42):
        
        self._num_layers = 3
        self._rows = rows
        self._columns = columns
        self.state = self._initialize_data(random_state=random_state)


    def _initialize_data(self, random_state):

        random.seed(random_state)
        initial_state = list()
        initial_state.append(initialize_fire_layer(self._rows, self._columns))
        initial_state.append(initialize_fuel_layer(self._rows, self._columns))
        initial_state.append(initialize_humidity_layer(self._rows, self._columns))
        
        layers = ['fire', 'fuel', 'humidity']
        for i, layer in enumerate(layers):
            write_img_file(f'Initialize_{layer}.img', initial_state[i])
        return np.array(initial_state)


    def get_hood_info(self, layer, i, j):
        """
        Method to get the 'layer's states of the (i, j)'s Moore Neighborhood cells
        """

        hood_states = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                ni = (i + y) if (i + y < self._rows) and (i + y >= 0) else None # Closed-Boundary Assumption
                nj = (j + x) if (j + x < self._columns) and (j + x >= 0) else None
                if ni and nj: hood_states.append(self.state[layer, ni, nj])
        return hood_states
    

    def evolve(self):
        """
        Method to evolve bi-dimensional cellular automaton from time (t) to (t + 1)
        """

        self._new_state = np.zeros((self._num_layers, self._rows, self._columns), dtype = int)
        self._evolve_humidity()
        self._evolve_fuel()
        self._evolve_fire()
        self.state = self._new_state
    
    
    def _evolve_humidity(self):
        """
        Method to update humidity's layer from time (t) to (t + 1)
        """

        for i in range(self._rows):
            for j in range(self._columns):

                cell_humidity = self.state[2, i, j]
                hood_fire = self.get_hood_info(0, i, j)
                self._new_state[2, i, j] = self._humidity_func(cell_humidity, hood_fire)
    

    def _evolve_fire(self):
        """
        Method to update fire's layer from time (t) to (t + 1)
        """

        for i in range(self._rows):
            for j in range(self._columns):

                cell_fire, cell_fuel, cell_humidity = self.state[:, i, j]
                hood_fire = self.get_hood_info(0, i, j)
                self._new_state[0, i, j] = self._fire_func(cell_fire, cell_fuel, cell_humidity, hood_fire)


    def _evolve_fuel(self):
        """
        Method to update fuel's layer from time (t) to (t + 1)
        """

        for i in range(self._rows):
                for j in range(self._columns):

                    cell_fire, cell_fuel, _ = self.state[:, i, j]  
                    self._new_state[1, i, j] = self._fuel_func(cell_fire, cell_fuel)   
        

    def simulate(self, t):
        """
        Method to carry out a simulation of t units of time

        Return: list with the bi-dimensional states of each generation step of each layer in the triplet (fire,fuel,humidity)
        """
        fire_steps = [self.state[0].copy()]
        fuel_steps = [self.state[1].copy()]
        humidity_steps = [self.state[2].copy()]

        for _ in range(t):
            self.evolve()
            fire_steps.append(self.state[0].copy())
            fuel_steps.append(self.state[1].copy())
            humidity_steps.append(self.state[2].copy())
        return fire_steps, fuel_steps, humidity_steps
    

    def _fire_func(self, cell_fire, cell_fuel, cell_humidity, hood_fire):
        """
        Method to calculate the next state of a fire's layer cell, combining information from multiple current layers

        Return: 0 if UnBurned, 1 if Burning or 2 if Burned
        """

        nghbrs_burning = sum(1 for state in hood_fire if state == 1)
        if cell_fire == -1: return -1
        elif cell_fire == 0:
            if nghbrs_burning > 0 and cell_fuel > 0 and cell_humidity == 0:
                return 1
            else:
                return 0
        elif cell_fire == 1:
            if cell_fuel > 1: return 1   
            else: return -1
              

    def _fuel_func(self, cell_fire, cell_fuel):
        """
        Method to calculate the next state of a fuel's layer cell, combining information from multiple current layers

        Return: number of hours that a cell can remain in Burning state
        """
        res = cell_fuel - 1 if cell_fire == 1 else cell_fuel
        return res if res > 0 else 0


    def _humidity_func(self, cell_humidity, hood_fire):
        """
        Method to calculate the next state of a humidity's layer cell, combining information from multiple current layers

        Return: number of hours that a cell can delay its Unburned state, when hood_fire is active
        """

        nghbrs_fire = sum(1 for state in hood_fire if state == 1)
        reduce_t = (1.5* np.log(nghbrs_fire)) + 1 if nghbrs_fire > 0 else 0 #Humity reduction caused by active hood fire
        res = cell_humidity - reduce_t
        return res if res > 0 else 0