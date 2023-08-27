import os
import re

folder_path = r"C:\Users\willian.frankoski\OneDrive - RADIX ENGENHARIA E DESENVOLVIMENTO DE SOFTWARE S A\Documents\DataCamp\Joining Data with pandas"  # Substitua pelo caminho da sua pasta

def remove_suffix(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.ipynb'):
            new_filename = filename[:-6]
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")

remove_suffix(folder_path)





