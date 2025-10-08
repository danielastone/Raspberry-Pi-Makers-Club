```python name=tests/test_soil_moisture_model.py
import unittest
import numpy as np

# Replicate key functions and logic from SoilMoistureModel.ipynb for testing

def surface_evaporation(moisture, field_capacity, evap_rate, dt):
    surface_dryness = moisture[0] / field_capacity
    effective_evap = evap_rate * min(1.0, surface_dryness) * dt
    new_surface = max(0.0, moisture[0] - effective_evap)
    return new_surface

def percolation_step(moisture, nz, field_capacity, percolation_coeff, dt, saturation):
    new_moisture = moisture.copy()
    for z in range(nz-1):
        excess_water = max(0.0, moisture[z] - field_capacity)
        if excess_water > 0:
            flow = percolation_coeff * excess_water * dt
            new_moisture[z] -= flow
            new_moisture[z+1] += flow
            if new_moisture[z+1] > saturation:
                overflow = new_moisture[z+1] - saturation
                new_moisture[z+1] = saturation
                if z+2 < nz:
                    new_moisture[z+2] += overflow
    return new_moisture

class TestSoilMoistureModel(unittest.TestCase):
    def setUp(self):
        # Parameters matching notebook defaults
        self.DEPTH = 20.0
        self.CELL_SIZE = 1.0
        self.SENSOR_DEPTH = 7.6
        self.SATURATION = 0.6
        self.FIELD_CAPACITY = 0.35
        self.WILTING_POINT = 0.12
        self.INITIAL_MOISTURE = 0.35
        self.EVAP_RATE = 0.002
        self.PERCOLATION_COEFF = 0.08
        self.TIME_STEPS = 168
        self.DT = 1.0

        self.nz = int(self.DEPTH / self.CELL_SIZE)
        self.sensor_cell = int(self.SENSOR_DEPTH / self.CELL_SIZE)
        self.moisture = np.full(self.nz, self.INITIAL_MOISTURE)

    def test_surface_evaporation(self):
        # At initial moisture, should reduce only the first cell
        moisture = np.full(self.nz, self.INITIAL_MOISTURE)
        new_surface = surface_evaporation(moisture, self.FIELD_CAPACITY, self.EVAP_RATE, self.DT)
        self.assertLess(new_surface, self.INITIAL_MOISTURE)
        self.assertGreaterEqual(new_surface, 0.0)

    def test_percolation_no_excess(self):
        # No excess, no flow
        moisture = np.full(self.nz, self.FIELD_CAPACITY)
        new_moisture = percolation_step(moisture, self.nz, self.FIELD_CAPACITY, self.PERCOLATION_COEFF, self.DT, self.SATURATION)
        np.testing.assert_array_almost_equal(new_moisture, moisture)

    def test_percolation_with_excess(self):
        # Give excess water to top cell
        moisture = np.full(self.nz, self.FIELD_CAPACITY)
        moisture[0] = self.SATURATION
        new_moisture = percolation_step(moisture, self.nz, self.FIELD_CAPACITY, self.PERCOLATION_COEFF, self.DT, self.SATURATION)
        self.assertLess(new_moisture[0], moisture[0])
        self.assertGreater(new_moisture[1], moisture[1])

    def test_moisture_nonnegative(self):
        # Evaporation cannot make moisture negative
        moisture = np.zeros(self.nz)
        new_surface = surface_evaporation(moisture, self.FIELD_CAPACITY, self.EVAP_RATE, self.DT)
        self.assertGreaterEqual(new_surface, 0.0)

    def test_simulation_sensor_moisture(self):
        # Simulate several steps and check sensor cell moisture is reasonable
        moisture = np.full(self.nz, self.INITIAL_MOISTURE)
        for _ in range(10):
            moisture[0] = surface_evaporation(moisture, self.FIELD_CAPACITY, self.EVAP_RATE, self.DT)
            moisture = percolation_step(moisture, self.nz, self.FIELD_CAPACITY, self.PERCOLATION_COEFF, self.DT, self.SATURATION)
        self.assertGreaterEqual(moisture[self.sensor_cell], 0.0)
        self.assertLessEqual(moisture[self.sensor_cell], self.SATURATION)

if __name__ == '__main__':
    unittest.main()
```
**How to use:**  
- Save this file as `simulation/test_soil_moisture_model.py` in your repo.
- Run with `python -m unittest simulation/test_soil_moisture_model.py`.

Tests included:
- Surface evaporation reduces moisture, but never negative.
- Percolation does not flow when at field capacity.
- Excess water drains downward.
- Sensor cell moisture remains within physical limits after simulation steps.

Extend these tests for more scenarios or add plant/root/evaporation logic as needed.
