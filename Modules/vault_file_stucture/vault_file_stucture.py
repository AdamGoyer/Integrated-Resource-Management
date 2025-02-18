import os
import sys
from typing import Dict, List
from folder_config import FOLDER_STRUCTURE

def validate_path(path: str) -> bool:
    """
    Check if the provided folder path is valid.
    
    This function ensures that:
    1. The path is not empty
    2. The path is an absolute path (starts from the root directory)
    """
    if not path:
        return False
    if not os.path.isabs(path):
        return False
    return True

def create_file_structure(base_dir: str, structure: Dict[str, List[str]], dry_run: bool = False) -> List[str]:
    """
    Creates a standardized folder structure at the specified location.
    
    How it works:
    1. Validates the provided path
    2. Creates the main folder if it doesn't exist
    3. Creates all subfolders based on the structure defined in folder_config.py
    
    Args:
        base_dir: The main folder where everything will be created
        structure: The folder structure blueprint (from folder_config.py)
        dry_run: If True, just shows what would be created without actually creating anything
    
    Returns:
        A list of all folders that were (or would be) created
    """
    created_paths = []

    # Make sure the provided path is valid
    if not validate_path(base_dir):
        raise ValueError("Please provide a valid absolute path")

    # Create the main folder if this isn't a dry run
    if not dry_run and not os.path.exists(base_dir):
        try:
            os.makedirs(base_dir)
            created_paths.append(base_dir)
        except PermissionError:
            raise PermissionError(f"No permission to create directory at {base_dir}")

    # Create each main folder and its subfolders
    for folder, subfolders in structure.items():
        # Create the main folder path
        folder_path = os.path.join(base_dir, folder)
        created_paths.append(folder_path)
        
        # Create the main folder if not a dry run
        if not dry_run:
            os.makedirs(folder_path, exist_ok=True)
            
        # Create all subfolders for this main folder
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            created_paths.append(subfolder_path)
            
            # Create the subfolder if not a dry run
            if not dry_run:
                os.makedirs(subfolder_path, exist_ok=True)

    return created_paths

def main():
    """
    Main program that handles:
    1. Getting the folder path from the user
    2. Showing what folders will be created
    3. Getting user confirmation
    4. Creating the folder structure
    5. Handling any errors that occur
    """
    # Get the folder path either from command line or user input
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = input("Please enter the absolute path where you want to create the folder structure: ")

    # Check if the path is valid
    if not validate_path(base_dir):
        print("Error: Please provide a valid absolute path")
        return

    # Show the user what folders will be created
    print("\nThe following folders will be created:")
    paths = create_file_structure(base_dir, FOLDER_STRUCTURE, dry_run=True)
    for path in paths:
        print(f"  {path}")

    # Get user confirmation before proceeding
    confirm = input("\nDo you want to proceed? (y/N): ")
    if confirm.lower() != 'y':
        print("Operation cancelled")
        return

    # Create the folders and handle any errors
    try:
        create_file_structure(base_dir, FOLDER_STRUCTURE)
        print("\nFolder structure created successfully!")
    except (PermissionError, OSError) as e:
        print(f"\nError creating folders: {e}")

# This is where the program starts when run
if __name__ == "__main__":
    main()
