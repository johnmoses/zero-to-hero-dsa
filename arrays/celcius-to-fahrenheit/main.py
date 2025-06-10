""" 
Convert list of temperatures from celcius to fahrenheit
"""
def celcius_to_fahrenheit(temps):
    return [temp * 9/5 + 32 for temp in temps]

print(celcius_to_fahrenheit([0, 10, 20, 30, 40]))
