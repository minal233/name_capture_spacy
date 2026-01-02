
## Setup & Running Locally

### Prerequisites
- Python 3.8+
- spaCy English model: `en_core_web_md`

### Installation

```bash
# Clone or navigate to project
git clone https://github.com/minal233/name_capture_spacy.git
cd name_capture_spacy

# Create virtual environment (recommended)
python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate

# Install dependencies
pip install rasa spacy
python -m spacy download en_core_web_md

## First-Time Setup

```bash
# Build custom spaCy model for better Indian name detection
python custom_spacy.py
```

## Train & Run

```bash
# Terminal 1: Start action server
rasa run actions

# Terminal 2: Train model
rasa train

# Terminal 3: Interactive testing
rasa shell --endpoints endpoints.yml
```