# Lab V: Control Flow and Functions in Python 

 # --- Part A: making decisions ----------------------------------------------

# Exercise 1: classify a star by temperature (O B A F G K M)
temperature = 5778 
if temperature >= 30000:
    print ("Class O")
elif temperature >= 10000: 
    print ("Class B")
elif temperature >= 7500:
    print ("Class A")
elif temperature >= 6000:
    print ("Class F")
elif temperature >= 5200:
    print ("Class G")
elif temperature >= 3700: 
    print ("Class K")
else :
    print ("Class M")

# Exercise 2: boolean logic -- can you see it?
magnitude = 1.25
naked_eye = magnitude < 6.0
city_visible = magnitude < 3.0
if naked_eye and city_visible:
    print ("The star is visible in the city and visible to the human eye ")
elif not city_visible:
    print ("The star is visible to the naked eye but not visible in the city")
elif not naked_eye:
    print ("The star is visible in the city but not visible to the Human eye")
else :
    print ("The star is not visible in the city and also not visible to the naked eye ")


 # --- Part B: repeating things ----------------------------------------------



# Exercise 3: a for loop with range()
print("--- Light-travel table ---")
for distance in range(1, 11):
    year_left = 2026 - distance
    print(f"{distance} ly  ->  light left in {year_left}")

print ("--- Light_travel table ---")
for distance in range (0, 21, 5):
    year_left = 2026 - distance 
    print (f"{distance}ly  -> light left in {year_left}")



# Exercise 4: a while loop
brightness = 100.0
steps = 0
while brightness >= 1.0:
    brightness = brightness / 2
    steps = steps + 1

print ("It took: ", steps, "steps")

# --- Part C: functions -----------------------------------------------------


# Exercise 5: turn the classifier into a function that RETURNS the letter
def spectral_class(temperature):
    if temperature >= 30000:
        return "O"
    elif temperature >= 10000: 
        return "B"
    elif temperature >= 7500:
        return "A"
    elif temperature >= 6000:
        return "F"
    elif temperature >= 5200:
        return "G"
    elif temperature >= 3700: 
        return "K"
    else :
        return "M"

print (spectral_class(5778))
print (spectral_class(25000))


# Exercise 6: a function with a default argument
def light_left_year(distance_ly, now=2026):
    return now - distance_ly

print(light_left_year(8.6))          
print(light_left_year(8.6, 2000))    