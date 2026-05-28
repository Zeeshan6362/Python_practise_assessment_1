import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    """
    Copies files from the source directory to the destination directory.
    Appends a timestamp to the filename if a file with the same name already exists.
    """
    # 1. Validate the source directory
    if not os.path.exists(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        sys.exit(1)
    if not os.path.isdir(source_dir):
        print(f"Error: '{source_dir}' is a file, not a directory.")
        sys.exit(1)

    # 2. Validate (or create) the destination directory
    if not os.path.exists(dest_dir):
        print(f"Destination directory '{dest_dir}' not found. Creating it...")
        try:
            os.makedirs(dest_dir)
        except Exception as e:
            print(f"Error creating destination directory: {e}")
            sys.exit(1)
    elif not os.path.isdir(dest_dir):
        print(f"Error: Destination '{dest_dir}' is a file, not a directory.")
        sys.exit(1)

    # 3. Iterate through items in the source directory
    print(f"\nScanning source: {source_dir}")
    print("-" * 40)
    
    files_copied = 0
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        
        # We only want to backup files, skip sub-directories for this basic script
        if os.path.isfile(source_path):
            dest_path = os.path.join(dest_dir, filename)
            
            # 4. Check for naming collisions in the destination
            if os.path.exists(dest_path):
                # Split the filename and its extension (e.g., "data", ".txt")
                name, ext = os.path.splitext(filename)
                
                # Generate a timestamp (e.g., 20231025_143005)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # Reassemble the new unique filename
                new_filename = f"{name}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, new_filename)
                print(f"Collision detected. Renaming '{filename}' to '{new_filename}'")
            
            # 5. Perform the file copy gracefully
            try:
                shutil.copy2(source_path, dest_path)
                print(f"Copied: {filename}")
                files_copied += 1
            except Exception as e:
                print(f"Error copying '{filename}': {e}")

    print("-" * 40)
    print(f"Backup Complete! Successfully backed up {files_copied} file(s).")

if __name__ == "__main__":
    # Ensure the user provided exactly two arguments (plus the script name itself)
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        print("Example: python backup.py /var/log/myapp /backup/myapp_logs")
        sys.exit(1)
        
    # Grab the arguments provided in the terminal
    src = sys.argv[1]
    dest = sys.argv[2]
    
    print("--- Starting DevOps Backup Process ---")
    backup_files(src, dest)