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