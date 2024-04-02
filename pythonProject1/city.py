class City:
  def __init__(self, city_name, region_name, number_of_citizens):
         self.city_name = city_name
         self.region_name = region_name
         self.number_of_citizens = number_of_citizens

  def __str__(self):
    return f"""Name:{self.city_name},
region_name:{self.region_name}, number_of_citizens:{self.number_of_citizens}"""
  def __eq__(self, other):
      return self.region_name == other.region_name, self.number_of_citizens == other.number_of_citizens


c1 = City("Prague", "Praha", "2000000")
c2 = City("Berlin", "Berlin","5000000")
print(c1)
print(c1 == c2)
