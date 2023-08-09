import os

root_folder = './shakespeare-dataset/'
combined_shakespeare = 'combined-works'


def remove_meta(filepath: str) -> None:
    """
    Remove metadata from a Shakespeare play text file.
    Prunes out '=' and Character Information.

    Parameters:
        filepath (str): The path to the Shakespeare play text file.

    Returns:
        None
    """
    remove_on = "ACT 1"

    # Read the content of the file
    with open(filepath, 'r') as file:
        content = file.read()
        # Remove '=' characters
        content = content.replace('=', '')
        # Retain only content, while discarding metadata
        _, content = content.split(remove_on, 1)

    # Write the modified content back to the file
    with open(filepath, 'w') as file:
        file.write(content)


all_files = os.listdir(root_folder)

# Loop through files in the root folder and remove metadata from each file
for i, file in enumerate(all_files):
    try:
        remove_meta(os.path.join(root_folder, file))
        print(f'Completed {i} / {len(all_files)}')
    except ValueError:
        pass

# Loop through each file and combine them all
with open(combined_shakespeare, 'a') as combined_works:
    total_size = 0
    for i, file in enumerate(all_files):
        with open(os.path.join(root_folder, file), 'r') as fx:
            combined_works.write(fx.read())
            total_size += len(fx.read())

        print(f'Completed {i} / {len(all_files)}')
    print(f'Total Size: {total_size}')

with open(combined_shakespeare, 'r') as combined_works:
    print(f'Total Size: {len(combined_works.read())}')
