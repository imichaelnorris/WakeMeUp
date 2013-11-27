import time
from datetime import date

#Wake me up when September ends
time.sleep((date(date.today().year + (1 if date.today().month > 9 else 0), 10, 1) - date.today()).total_seconds())
