import re
import csv
import os
import sys

def parse_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    transcript = []
    current_timestamp = None
    current_text = []
    current_speaker = None

    timestamp_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})')
    speaker_pattern = re.compile(r'^([\w\s]+):')
    number_pattern = re.compile(r'^\d+$')  # Pattern to match lines that are just numbers

    for line in lines:
        line = line.strip()
        if number_pattern.match(line):
            continue  # Skip lines that are just numbers
        if timestamp_pattern.match(line):
            if current_timestamp:
                transcript.append((current_timestamp, current_speaker, ' '.join(current_text)))
                current_text = []
                current_speaker = None
            current_timestamp = line
        elif line and not line.startswith('WEBVTT'):
            speaker_match = speaker_pattern.match(line)
            if speaker_match:
                current_speaker = speaker_match.group(1)
                line = line[len(current_speaker)+1:].strip()  # Remove speaker name from the line
            current_text.append(line)

    if current_timestamp:
        transcript.append((current_timestamp, current_speaker, ' '.join(current_text)))

    return transcript

def save_transcript_to_csv(transcript, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Speaker", "Text"])
        for timestamp, speaker, text in transcript:
            writer.writerow([timestamp, speaker, text])

def process_directory(input_directory, output_directory=None):
    if output_directory is None:
        output_directory = input_directory

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".vtt"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.csv")
            
            transcript = parse_vtt(input_path)
            save_transcript_to_csv(transcript, output_path)
            
            print(f"Processed {filename} and saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vtt_to_csv_directory.py <input_directory> [output_directory]")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else None
    
    process_directory(input_directory, output_directory)
