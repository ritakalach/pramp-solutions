"""
Drone Flight Planner

You’re an engineer at a disruptive drone delivery startup and your CTO asks you to come up with an efficient algorithm that calculates 
the minimum amount of energy required for the company’s drone to complete its flight. 
You know that the drone burns 1 kWh (kilowatt-hour is an energy unit) for every mile it ascends, and it gains 1 kWh for every mile it descends. 
Flying sideways neither burns nor adds any energy.

Given an array route of 3D points, implement a function calcDroneMinEnergy that computes and returns the minimal amount of energy the drone would need 
to complete its route. Assume that the drone starts its flight at the first point in route. That is, no energy was expended to place the drone at the starting point.

For simplicity, every 3D point will be represented as an integer array whose length is 3. 
Also, the values at indexes 0, 1, and 2 represent the x, y and z coordinates in a 3D point, respectively.


input:  route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

output: 5 # less than 5 kWh and the drone would crash before the finish
          # line. More than `5` kWh and it’d end up with excess e

"""


# O(n) time
# O(1) space
def calc_drone_min_energy(route):
  energy_balance = 0
  energy_deficit = 0
  
  prev_altitude = route[0][2]
  for i in range(1, len(route)):
    curr_altitude = route[i][2]
    energy_balance += prev_altitude - curr_altitude
    if energy_balance < 0:
      energy_deficit += abs(energy_balance)
      energy_balance = 0
    prev_altitude = curr_altitude
    
  return energy_deficit
  
  
  def calc_drone_min_energy(route):
  max_altitude = route[0][2]
  
  for i in range(1, len(route)):
    if route[i][2] > max_altitude:
      max_altitude = route[i][2]
    
  return max_altitude - route[0][2]
