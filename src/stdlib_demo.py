from __future__ import annotations

import random
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

# 1. datetime
now = datetime.now()
print("現在:", now.isoformat(timespec="seconds"))
print("7 日後:", (now + timedelta(days=7)).strftime("%Y-%m-%d %H:%M"))

# 2. random
rolls = [random.randrange(1, 7) for _ in range(100)]
freq = Counter(rolls)
print("サイコロ出目頻度:", freq)

# 3. pathlib
py_files = list(Path("src").glob("*.py"))
print("このディレクトリの .py", [p.name for p in py_files])
