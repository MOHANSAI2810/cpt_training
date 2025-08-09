import pickle

a = [1, 2, 3, 'hgdsc', False]

# Save list 'a' into data.pkl
with open('data.pkl', 'wb') as f:
    pickle.dump(a, f)

# Load the list from data.pkl
with open('data.pkl', 'rb') as f:
    load = pickle.load(f)
print("The data which is being loaded is:", load)

# Save loaded data into data1.pkl again using pickle
with open('data1.pkl', 'wb') as f:
    pickle.dump(load, f)

print("Successfully loaded the data into data1.pkl")
