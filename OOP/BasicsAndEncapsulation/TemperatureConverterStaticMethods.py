"""
 this is for practising static methods and properties
"""

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahranheit(celcium_degree:float):
        return (celcium_degree*9/5)+32
    
    @staticmethod
    def celsius_to_kelvin(celcium_degree:float):
        return celcium_degree+273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin_degree:float):
        return kelvin_degree-273.15
    
    @staticmethod
    def faranheit_to_celsius(faranheit_degree:float):
        return (faranheit_degree-32)*5/9

print(TemperatureConverter.celsius_to_fahranheit(100))