import pandas as pd

# Constants
PROMPT = """
## Task: Emotion Expressivity Evaluation

**Emotion expressivity evaluation** is a task that involves assessing how well a speaker conveys emotions through their voice in an audio clip.

You are given two speech clips, in the following order:

1. Audio A
2. Audio B

**Your task:**  
Ignore background noise and content — focus only on emotion conveyed by the speech. Decide which speech sounds more {emotion}? (a) Audio A (b) Audio B.
"""

STRICT_OUTPUT = """
**Output format:**
Respond with either **(a)** or **(b)** only.
"""

def getPrompt(strict: bool = False, id: str = None, csv_path: str = "emotion_tts_assigned_by_distribution.csv"):
    if id is None:
        raise ValueError("You must provide a UUID.")

    df = pd.read_csv(csv_path)

    match = df[df["id"] == id]
    if match.empty:
        raise ValueError(f"UUID {id} not found in CSV.")

    emotion = match.iloc[0]["emotions"]

    filled_prompt = PROMPT.format(emotion=emotion)

    return filled_prompt + STRICT_OUTPUT if strict else filled_prompt
