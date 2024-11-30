import os
import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='backup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
SOURCE_DIR = "/path/to/source/directory"  # Directory to back up
REMOTE_USER = "remote_user"  # Remote server SSH username
REMOTE_HOST = "remote_host"  # Remote server IP or hostname
REMOTE_DIR = "/path/to/remote/backup/directory"  # Destination directory on the remote server
SSH_KEY = "/path/to/ssh/key"  # Path to your SSH private key

def backup_directory():
    """Perform the backup operation using rsync."""
    try:
        # Construct the rsync command
        rsync_command = [
            "rsync", "-avz", "--delete", "-e", f"ssh -i {SSH_KEY}",
            SOURCE_DIR, f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}"
        ]
        
        # Execute the rsync command
        result = subprocess.run(rsync_command, capture_output=True, text=True)
        
        # Check the result
        if result.returncode == 0:
            logging.info("Backup completed successfully.")
            print("Backup completed successfully.")
        else:
            logging.error(f"Backup failed: {result.stderr}")
            print(f"Backup failed: {result.stderr}")
    except Exception as e:
        logging.error(f"An error occurred during backup: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the source directory exists
    if not os.path.exists(SOURCE_DIR):
        logging.error(f"Source directory does not exist: {SOURCE_DIR}")
        print(f"Source directory does not exist: {SOURCE_DIR}")
    else:
        # Run the backup
        backup_directory()
