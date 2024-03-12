import pickle

# Replace 'your_file.pkl' with the path to your actual file
filename = 'train_data.pkl'

# Using a context manager to ensure the file gets closed
with open(filename, 'rb') as file:
    data = pickle.load(file)

# Now you can use your data object as needed
print(data)