# helpers.py
# Utility helpers used by the Virtual-Ally project.

import json
import os
from datetime import datetime

def ensure_outputs():
    os.makedirs('outputs', exist_ok=True)

def save_package(pkg, out='outputs/package.json'):
    ensure_outputs()
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(pkg, f, indent=2, ensure_ascii=False)
    return out

def timestamped_filename(prefix='file', ext='png'):
    ts = int(datetime.now().timestamp())
    return f'outputs/{prefix}_{ts}.{ext}'
