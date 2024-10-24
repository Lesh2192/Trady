# Tradi

Tradi is an interactive command-line translator that allows you to translate text from a source language to a destination language. The project uses the `googletrans` library for translation and `click` for handling command-line arguments.

## Features

- Translate text between different languages.
- Input language names in English (e.g., "English" for English).
- Use the `Ctrl + L` key to clear the screen.
- Command-line options to specify the text, source language, and destination language.

## Installation

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the repository**:

   ```sh
   git clone https://github.com/Mempa21/Tradi.git
   cd Tradi
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv myenv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```sh
     myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source myenv/bin/activate
     ```

4. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Command-line Options

- `--text`: Text to translate.
- `--src-lang`: Source language name (e.g., "English").
- `--dest-lang`: Destination language name (e.g., "French").

### Example Usage

```sh
python translator.py --text "Hello, world!" --src-lang "English" --dest-lang "French"
```

### Display Help

To display the help and available options, use:

```sh
python translator.py --help
```

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.
