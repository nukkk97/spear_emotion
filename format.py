import os
import csv
from pathlib import Path

BASE_DIR = Path("pairwise_outputs")
GITHUB_PREFIX = "https://github.com/nukkk97/spear_emotion/raw/refs/heads/main/pairwise_outputs"

def generate_csv(output_file="output.csv"):
    rows = []
    for idx, uuid_dir in enumerate(BASE_DIR.iterdir()):
        if uuid_dir.is_dir():
            wav_files = sorted(uuid_dir.glob("*.wav"))
            if len(wav_files) == 2:
                audio1 = f"{GITHUB_PREFIX}/{uuid_dir.name}/{wav_files[0].name}"
                audio2 = f"{GITHUB_PREFIX}/{uuid_dir.name}/{wav_files[1].name}"
                rows.append([idx, audio1, audio2])
            else:
                print(f"Skipping {uuid_dir} — expected 2 .wav files, found {len(wav_files)}")

    # Write to CSV
    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "audio1", "audio2"])
        writer.writerows(rows)

    print(f"CSV generated: {output_file}")

if __name__ == "__main__":
    generate_csv()