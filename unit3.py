# class ABC:
#   def __init__(self):
#     self.i = 12
#     i = 34


# a = ABC()
# print(a.i)
# a.i = 78
# print(a.i)

# class Calc:
 
#   def __init__(self):
#     self.numOfCalcs = 0

#   def add(self,x,y):
#     self.numOfCalcs +=1
#     return x + y
 
#   def sub(self,x,y):
#     self.numOfCalcs +=1
#     return x - y
  

# calculator = Calc()

# calculator.add(3,1)
# calculator.sub(3,1)

# print(calculator.numOfCalcs)


# class Planet:
#   def __init__(self, name):
#     self.name = name
#     self.orbits_a_star = True
#     self.mass_enough_to_form_a_sphere = True
#     self.cleared_neighborhood_around_orbit = True
  
#   def show_name(self):
#     return f'I am planet {self.name}'
 
# class Moon(Planet):
#   def __init__(self, name, num_Moons):
#     super().__init__(name)
#     self.moons = num_Moons
 
#   def show_moons(self):
#     return f'I have {self.moons} moons'
 
# P8wM = Moon('Jupiter', 79)

# help(Moon)


# f = open('/myfile.txt', 'w')
# f.write('Two-Level\nText')
# f = open('myfile.txt', 'r')
# for line in f:
#   print(repr(line)) 
# f.close()

# class ABC:
#  def __init__(self,x):
#   self.x = x
#  x = 56
#  i = 34
# a = ABC(12)

# print(a.x)


# my_string = 'Python\\nIs\\nfun'

# print(repr(my_string))

class SolarSystem: 
 def __init__(self, name): 
  self.name = 'Sun' 
 def show_ss_name(self): 
  return f'The only star in our solar system is the {self.name}'
class Planet(SolarSystem): 
 def __init__(self, name): 
  self.name = name 
  self.orbits_a_star = True
  self.mass_enough_to_form_a_sphere = True
  self.cleared_neighborhood_around_orbit = True 
 def show_name(self): 
  return f'I am planet {self.name}' 
class Atm_Moon(Planet): 
 def __init__(self, name, atm_type, num_Moons):
  super().__init__(name) 
  self.moons = num_Moons 
  self.atmosphere = atm_type 
 def show_moons(self): 
  return f'I have {self.moons} moons' 
 def show_atmosphere(self): 
  return f'My atmosphere is mostly {self.atmosphere}' 
P4wAM = Atm_Moon('Mars', 'carbon dioxide',2)

help(Atm_Moon)