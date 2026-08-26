<<<<<<< HEAD
# Lab V: A Gentle Introduction to Python
# Programming Essentials for Astronomy I - Python
#
# Fill in the TODOs below. Run this file (no compiling needed!) with:
#     python3 intro_to_python.py

# --- Part A: first steps ---------------------------------------------------

# Exercise 1: Hello, Universe
print("Hello, Universe!")
# TODO: also print your name and your favourite celestial object.


# Exercise 2: variables and types
name = "Sirius"           # str
distance_ly = 8.6         # float
num_planets = 0           # int
naked_eye_visible = True  # bool

# TODO: print each variable together with its type, e.g.
#       print(name, "has type", type(name))


# --- Part B: arithmetic with astronomy -------------------------------------

# Exercise 3: unit conversions (1 parsec ~= 3.26 ly, 1 ly ~= 9.46e12 km)
# TODO: convert distance_ly to parsecs and to kilometres, and print both
#       using f-strings.

# Exercise 4: we see the past
# TODO: print the year the light we see now left Sirius (use 2026 as "now").
# TODO: print 8.6 / 3 and 8 // 3 and notice the difference.

# Exercise 5: the power operator (**) -- volume of a sphere
pi = 3.14159
radius_km = 696000  # the Sun
# TODO: compute volume = (4/3) * pi * radius_km ** 3 and print it with {volume:.3e}


# --- Part C: talking to the user -------------------------------------------

# Exercise 6: reading input
# NOTE: input() returns TEXT -- convert it with float(...) before doing maths.
# Uncomment the two lines below once you are ready to try it:
# text = input("Enter a distance in light-years: ")
# print(f"That is {float(text) / 3.26:.2f} parsecs.")


# --- Optional extension ----------------------------------------------------
# import math
# TODO: distance modulus  mu = 5 * math.log10(d) - 5  for d in parsecs.
=======
# PART A
# Exercise 1 
print ("Hello, My name is Mudalo")
print ("My favourite celestrial object is the Moon")

# Exercise 2 
name = "Sirius"          
distance_ly = 8.6        
num_planets = 0          
naked_eye_visible = True 

print(name, "has type", type(name))
print(distance_ly, "has type", type(distance_ly))
print(num_planets, "has type", type(num_planets))
print(naked_eye_visible, "has type", type(naked_eye_visible))

# PART B
# Exercise 3
distance_pc = distance_ly / 3.26
distance_km = distance_ly/ 9.46e12
print(f"Sirius is {distance_pc} parsecs away.")
print(f"Sirius is {distance_km} kilometers away.")

# Exercise 4
current_year = 2026
actual_year = current_year - 8.6
print ("Light from Sirius which can be observed on Earth in 2026 left Sirius in : " , actual_year )
print(8.6 / 3)    
print(8 // 3)     


# Exercise 5 
pi = 3.14159
radius_km = 696000
volume = (4 / 3) * pi * radius_km ** 3
print(f"The Sun's volume is about {volume:.3e} cubic km.")

# Exercise 6
text = input("Enter a distance in light-years: ")
distance_ly = float(text)   
print(f"That is {distance_ly / 3.26:.2f} parsecs.")


>>>>>>> ce7c9ea (Completed Week 1 activities)
