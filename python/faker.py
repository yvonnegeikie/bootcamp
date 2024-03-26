[09:32] Nick O'Rourke
!pip install faker
 
from faker import Faker

import pandas as pd

import numpy as np
 
fake = Faker()

Faker.seed(42)

np.random.seed(42)
 
# Define sample size

sample_size = 100
 
# Generate synthetic data

data = {

    'FacilityName': [f"Facility {i}" for i in range(sample_size)],

    'Type': np.random.choice(['Park', 'Library', 'Museum', 'School', 'Hospital'], sample_size),

    'Address': [fake.address() for _ in range(sample_size)],

    'Latitude': np.round(np.random.uniform(40.5, 40.9, sample_size), 6),  # Approximate coordinates for New York City

    'Longitude': np.round(np.random.uniform(-74.0, -73.7, sample_size), 6)

}
 
df_synthetic_new_york = pd.DataFrame(data)
 like 1