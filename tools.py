# tools.py
# Small tools: image placeholder and palette extraction (simulated)

import os
from datetime import datetime

def create_placeholder_image(name='mood'):
    os.makedirs('outputs', exist_ok=True)
    fname = f'outputs/{name}_{int(datetime.now().timestamp())}.png'
    # create a minimal binary file to represent an image placeholder
    with open(fname, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')  # PNG header only (not a viewable image, but a placeholder)
    return fname

def extract_palette_from_text(text):
    # very naive, returns a fixed palette if none found
    return ['#C9564E', '#FFD27F', '#3D2C8D']
