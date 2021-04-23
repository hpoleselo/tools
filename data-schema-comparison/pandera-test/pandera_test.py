import pandera as pa
import pandas as pd

data = pd.read_json('../user.json')
print(data)

# Defining the schema
schema = pa.DataFrameSchema({
    "email" : pa.Column(pa.String, nullable=False)
    "books" : pa.Column(pa.String, nullable=True),
    "title" : pa.Column(pa.String, pa.Check(len<=120), nullable=True),
    "isbn" : pa.Column(pa.String, nullable=False),
})

# Validating the data
schema.validate(data_sample)