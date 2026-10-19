"""Set the contribution query's calendar window to the current Korean date."""
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

today = datetime.now(ZoneInfo('Asia/Seoul')).date()
first = today - timedelta(days=364)
source = Path('.profile-renderer/src/github-graphql.ts')
marker = 'contributionsCollection${yearArgs} {'
query = f'contributionsCollection(from:"{first}T00:00:00Z", to:"{today}T23:59:59Z") {{'
code = source.read_text(encoding='utf-8')
if code.count(marker) != 1:
    raise SystemExit('Contribution query changed upstream; refusing to patch.')
source.write_text(code.replace(marker, query), encoding='utf-8')
print(f'Contribution calendar: {first} through {today} (Korean calendar date).')
