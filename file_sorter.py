import os
import shutil
import time
from pathlib import Path

def create_folder(directory, folder_name):
    """Create a folder if it doesn't exist."""
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_name}")
    return folder_path

def get_file_category(file_extension):
    """Determine the category of a file based on its extension."""
    extension = file_extension.lower()
    
    # Documents
    if extension in ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv']:
        return 'Documents'
    
    # Images
    elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']:
        return 'Images'
    
    # Videos
    elif extension in ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']:
        return 'Videos'
    
    # Audio
    elif extension in ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a']:
        return 'Audio'
    
    # Archives
    elif extension in ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2']:
        return 'Archives'
    
    # Code
    elif extension in ['.py', '.java', '.cpp', '.c', '.html', '.css', '.js', '.php', '.rb', '.go', '.json', '.xml']:
        return 'Code'
    
    # Executables
    elif extension in ['.exe', '.msi', '.app', '.bat', '.sh']:
        return 'Executables'
    
    # Others
    else:
        return 'Others'

def sort_files(directory_path):
    """Sort files in the given directory into appropriate subfolders."""
    try:
        # Convert to absolute path
        directory_path = os.path.abspath(directory_path)
        
        if not os.path.exists(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist.")
            return False
        
        print(f"\nScanning directory: {directory_path}\n")
        
        # Count for stats
        total_files = 0
        moved_files = 0
        
        # Create a set to track processed files to avoid duplicates
        processed_files = set()
        
        # Create a dictionary to keep track of files moved to each category
        category_counts = {}
        
        # Scan all files in the directory (not recursive)
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            
            # Skip directories and already processed files
            if os.path.isdir(item_path) or item in processed_files:
                continue
            
            total_files += 1
            
            # Get file extension and category
            _, file_extension = os.path.splitext(item)
            category = get_file_category(file_extension)
            
            # Create category folder if it doesn't exist
            category_folder = create_folder(directory_path, category)
            
            # Destination path for the file
            destination = os.path.join(category_folder, item)
            
            # Move the file if not already in its category folder
            if os.path.dirname(item_path) != category_folder:
                try:
                    # Handle file conflicts
                    if os.path.exists(destination):
                        base_name, extension = os.path.splitext(item)
                        timestamp = time.strftime("_%Y%m%d_%H%M%S")
                        new_filename = f"{base_name}{timestamp}{extension}"
                        destination = os.path.join(category_folder, new_filename)
                    
                    # Move the file
                    shutil.move(item_path, destination)
                    moved_files += 1
                    
                    # Update category count
                    category_counts[category] = category_counts.get(category, 0) + 1
                    
                    print(f"Moved: {item} → {category}/{os.path.basename(destination)}")
                    processed_files.add(item)
                except Exception as e:
                    print(f"Error moving {item}: {e}")
        
        # Display summary
        print("\n" + "="*50)
        print(f"File Sorting Complete!")
        print(f"Total files scanned: {total_files}")
        print(f"Files moved: {moved_files}")
        
        # Show category breakdown
        if category_counts:
            print("\nFiles organized by category:")
            for category, count in category_counts.items():
                print(f"  - {category}: {count} file(s)")
        
        print("="*50)
        return True
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    """Main function to run the file sorter."""
    print("="*50)
    print("       AUTOMATIC FILE SORTER")
    print("="*50)
    
    while True:
        # Get directory path from user
        directory = input("\nEnter the directory path to sort (or 'q' to quit): ").strip()
        
        if directory.lower() == 'q':
            print("\nExiting File Sorter. Goodbye!")
            break
        
        # Sort the files
        sort_files(directory)
        
        choice = input("\nDo you want to sort another directory? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nExiting File Sorter. Goodbye!")
            break

if __name__ == "__main__":
    main()