from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    districts = models.TextField()  # List of districts in Tamil Nadu

    def __str__(self):
        return self.name

class TravelCost(models.Model):
    vehicle_type = models.CharField(max_length=50)
    distance = models.FloatField()  # Distance in km
    petrol_price = models.FloatField()  # Petrol price per liter
    fuel_efficiency = models.FloatField()  # km per liter
    total_cost = models.FloatField()

    def calculate_cost(self):
        # Calculate fuel cost based on distance, fuel_efficiency, and petrol price
        self.total_cost = (self.distance / self.fuel_efficiency) * self.petrol_price
        return self.total_cost

class Accommodation(models.Model):
    type = models.CharField(max_length=100)
    cost_per_night = models.FloatField()

    def __str__(self):
        return self.type

class FoodCost(models.Model):
    food_type = models.CharField(max_length=100)
    cost_per_day = models.FloatField()

    def __str__(self):
        return self.food_type
