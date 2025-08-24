#!/bin/bash

# Download spaCy model if not available
python -m spacy download en_core_web_sm --quiet

# Run the Streamlit app
streamlit run Home.py --server.port=$PORT --server.address=0.0.0.0
