import re
import os

def convert_vtt_to_text(vtt_file, output_file):
    with open(vtt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    timestamp_pattern = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3} align:start position:0%$")
    seen_lines = set()
    text = []
    
    for line in lines:
        line = line.strip()
        if line.lower().startswith("webvtt") or line.lower().startswith("kind: captions") or line.lower().startswith("language: en"):
            continue
        if not timestamp_pattern.match(line) and "<c>" not in line:
            if line not in seen_lines:
                text.append(line)
                seen_lines.add(line) 
    paragraph = " ".join(text).lower()
    
    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(paragraph)
    print(f"Transcript saved to {output_file}")

folder_path = 'C:/Users/Administrator/Desktop/AI Agents'
vtt_files = [f for f in os.listdir(folder_path) if f.endswith('.vtt')]

for vtt_file in vtt_files:
    vtt_file_path = os.path.join(folder_path, vtt_file)
    output_file_path = os.path.join(folder_path, f"{os.path.splitext(vtt_file)[0]}.txt")
    convert_vtt_to_text(vtt_file_path, output_file_path)