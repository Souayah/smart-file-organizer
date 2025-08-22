# Smart File Organizer

## Project Description

Smart File Organizer is a Python-based utility designed to automatically organize files in a specified directory into subfolders based on their file types. This helps in maintaining a clean and organized file system, especially for directories like 'Downloads' that tend to accumulate various file types.

## Features

- **Organize by File Extensions**: Automatically categorizes files (e.g., PDFs, images, archives) into designated subfolders.
- **Custom Rules**: Supports flexible organization rules defined via JSON or YAML configuration files.
- **Command-Line Interface (CLI)**: Easy-to-use CLI with options for specifying target paths, configuration files, and organization intervals.
- **Automated Scheduling**: Can be configured to run automatically at specified intervals (e.g., every X minutes).
- **Detailed Logging**: Keeps a log of all moved files and organization activities for easy tracking and auditing.
- **Unit Tests**: Comprehensive unit tests ensure the reliability and correctness of core functionalities.
- **Optional Dockerfile**: Provides a Dockerfile for containerized deployment, ensuring consistent environments.
- **GitHub Actions Workflow**: Includes a GitHub Actions workflow to automate testing upon code pushes.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Souayah/smart-file-organizer.git
   cd smart-file-organizer
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples

### Basic Organization

To organize files in your default downloads folder (`~/Downloads`):

```bash
python3 -m organizer.cli
```

### Organizing a Specific Path

To organize files in a different directory (e.g., `/path/to/my/documents`):

```bash
python3 -m organizer.cli --path /path/to/my/documents
```

### Using a Custom Configuration File

To use a custom set of rules defined in `my_custom_rules.json`:

```bash
python3 -m organizer.cli --config examples/my_custom_rules.json
```

### Automated Organization

To run the organizer automatically every 30 minutes:

```bash
python3 -m organizer.cli --interval 30
```

### Combining Options

```bash
python3 -m organizer.cli --path /path/to/organize --config my_custom_rules.json --interval 60
```

## Contributing Guidelines

We welcome contributions to the Smart File Organizer! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and ensure tests pass.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a Pull Request.

