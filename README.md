# Bash File Management Toolkit

A collection of powerful bash scripts for efficient file management, organization, and maintenance.

## Overview

This toolkit provides a comprehensive set of bash scripts designed to simplify file management tasks. From organizing cluttered directories to finding storage-hungry files, encrypting sensitive data, and maintaining backups, these utilities help you take control of your file system.

## Scripts Included

### 1. `file_sorter`

Automatically organizes files in a directory based on their types, moving them into categorized subfolders.

- Creates logical folder structure (Documents, Images, Videos, etc.)
- Handles various file extensions
- Preserves original file timestamps
- Option for recursive sorting through subdirectories

### 2. `file_renamer`

Powerful batch file renaming utility with flexible pattern matching.

- Add prefixes/suffixes
- Replace text using regular expressions
- Sequential numbering
- Date-based naming formats
- Preview changes before execution

### 3. `duplicate_file_finder`

Identifies and manages duplicate files to reclaim valuable disk space.

- Fast detection using file size and hash comparison
- Interactive management of duplicates
- Options to delete, move, or symlink duplicate files
- Export results to log file

### 4. `file_backup_system`

Robust backup solution to protect your important data.

- Full and incremental backup strategies
- Configurable compression options
- Scheduled backups via cron integration
- Retention policy management
- Backup verification

### 5. `disk_space_analyzer`

Visualizes disk usage to quickly identify space-consuming files and directories.

- Tree-like visualization of directory structure
- Sorting by size, date, or name
- Filtering options for specific file types
- Export results to various formats

### 6. `file_encryption_tool`

Secures sensitive files with strong encryption.

- AES-256 encryption standard
- Secure password handling
- Batch encryption/decryption
- Optional secure deletion of originals

### 7. `file_sync`

Keeps directories synchronized across different locations.

- Two-way synchronization
- Conflict detection and resolution
- Detailed logging of operations
- Dry-run mode for preview

## Installation/Running

```bash
# Clone the repository
git clone https://github.com/kistlerk19/linux-file-management.git

# Navigate to the project directory
cd linux-file-management

# Make scripts executable
chmod +x file_sorter file_renamer file_renamer duplicate_file_finder file_backup_system disk_space_analyzer file_encryption_tool file_sync
```

## Usage

### File Sorter

```bash
./file_sorter /path/to/directory [options]
```

### File Renamer

```bash
./file_renamer /path/to/files pattern [options]
```

### Duplicate File Finder

```bash
./duplicate_file_finder /path/to/search [options]
```

### File Backup System

```bash
./file_backup_system source destination [options]
```

### Disk Space Analyzer

```bash
./disk_space_analyzer /path/to/analyze [options]
```

### File Encryption Tool

```bash
./file_encryption_tool [encrypt|decrypt] file [options]
```

### File Sync

```bash
./file_sync source_dir target_dir [options]
```

## Dependencies

- Bash 4.0+
- Standard Unix utilities (find, sort, grep, etc.)
- Optional: OpenSSL (for encryption)
- Optional: rsync (for file sync)


## Author

Ishmael Gyamfi (May 2025)