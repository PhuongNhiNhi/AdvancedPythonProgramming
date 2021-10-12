class Country:
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area

  def is_larger(self, objCountry):
    if self.area > objCountry.area:
      return True
    else:
      return False
    
  def population_density(self):
    return self.population/self.area

  #def __str__(self):
  #  return .format(self.name, self.population, self.area)