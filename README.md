# vtt2csv
python script to convert a folder of vtt files to csv format - useful for searching etc

### Introducing the VTT to CSV Conversion Script

#### Overview

The VTT to CSV Conversion Script is a simple tool designed to help you convert WebVTT (VTT) files into CSV files. WebVTT files are commonly used for subtitles and captions in videos. This script extracts the timestamps, speaker names, and text from VTT files and organizes them into a structured CSV format. This makes it easier to read, search, and analyse the content of your subtitles or captions.

#### How It Works

1. **Extracts Information**: The script reads each VTT file and extracts the timestamps, speaker names, and text.
2. **Organizes Data**: It organizes the extracted information into columns: Timestamp, Speaker, and Text.
3. **Saves as CSV**: The organized data is saved into a CSV file, which can be opened with spreadsheet software like Microsoft Excel or Google Sheets.

#### Use Cases

- **Transcription Analysis**: If you have transcriptions in VTT format, converting them to CSV makes it easier to analyse the text and identify patterns.
- **Content Search**: CSV files are easier to search and navigate, making it simpler to find specific parts of the transcription.
- **Data Integration**: CSV files can be easily integrated into other systems for further processing or analysis.

#### Getting Started

1. **Ensure Python is Installed**:
   Most macOS systems come with Python pre-installed. To check if Python is installed, open the Terminal and type:
   ```sh
   python3 --version
   ```
   If Python is not installed, download and install it from the [Python website](https://www.python.org/downloads/).

2. **Download the Script**:
   Save the provided script as `vtt2csv.py`.

3. **Open the Terminal**:
   Launch the Terminal application on your macOS.

4. **Navigate to the Script Directory**:
   Use the `cd` command to navigate to the directory where you saved `vtt2csv.py`. For example, if it's in your `Documents` folder, type:
   ```sh
   cd ~/Documents
   ```

5. **Run the Script**:
   To convert the VTT files, run the script using the following command. Replace `path_to_your_vtt_files_directory` with the path to your VTT files directory. Optionally, specify an output directory:
   ```sh
   python3 vtt2csv.py path_to_your_vtt_files_directory [path_to_output_csv_files_directory]
   ```
   If you don't specify an output directory, the CSV files will be saved in the same directory as the VTT files.

#### Example

Let's say you have a folder named `vtt_files` in your `Documents` directory containing your VTT files. To convert these files and save the CSVs in the same directory:

1. Open the Terminal.
2. Navigate to the `Documents` directory:
   ```sh
   cd ~/Documents
   ```
3. Run the script:
   ```sh
   python3 vtt2csv.py vtt_files
   ```

If you want to save the CSV files in a different directory, for example, a folder named `csv_files` in your `Documents` directory:
```sh
python3 vtt2csv.py vtt_files csv_files
```

#### Troubleshooting

- **Command Not Found**: If you see a "command not found" error when running `python3`, make sure Python is installed correctly.
- **Permissions Issues**: Ensure you have the necessary read and write permissions for the directories you are working with.

This tool simplifies the process of converting VTT files to CSV format, making it easier to work with your transcriptions or captions. If you have any questions or need further assistance, feel free to reach out!
