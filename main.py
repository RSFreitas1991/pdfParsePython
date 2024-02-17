import camelot

# Read the PDF file
tables = camelot.read_pdf('classificacao.pdf', pages='all')

# Create a list to store the objects
objects = []

# Iterate over each table
for table in tables:
    # Convert the table to a pandas DataFrame
    df = table.df

    # Iterate over each row
    for i in range(len(df)):
        # Get the inscription and name
        inscription = df.iloc[i, 0]
        name = df.iloc[i, 1]

        # Check if a space exists in the inscription
        if ' ' in inscription:
            # Split the inscription into inscription and name
            inscription, name = inscription.split(' ', 1)

        # Remove leading and trailing spaces from the name
        name = name.strip()

        # Create an object with the specified columns
        obj = {
            'inscription': inscription,
            'name': name,
            'classification': df.iloc[i, 14]
        }
        # Add the object to the list
        objects.append(obj)

# Print the list of objects
for obj in objects:
    print(obj)