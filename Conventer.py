# Day 3: ECE Unit Converter
print("--- Thanu's ECE Converter ---")

# Input: Current in Milliamps (mA)
milli_amps = 1500 

# Process: Convert to Amps (A) by dividing by 1000
amps = milli_amps / 1000

print("Current in mA: " + str(milli_amps))
print("Current in Amps: " + str(amps) + "A")

# A quick logic check
if amps > 1.0:
    print("Status: High Current Device")
else:
    print("Status: Low Current Device")
  
