#!/usr/bin/env python3
"""Register this checkout in the personal marketplace, preserving other entries."""
import argparse,json,shutil
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--home',type=Path,default=Path.home(),help='Home directory (override for isolated verification)')
a=p.parse_args();repo=Path(__file__).resolve().parents[1]
source=repo/'plugins/yori';name=json.loads((source/'.codex-plugin/plugin.json').read_text())['name']
# A stable owned directory; do not edit OpenAI's installed cache.
dest=a.home/'.codex/plugins/yori-chatgpt-source'
market=a.home/'.agents/plugins/marketplace.json'
data=json.loads(market.read_text()) if market.exists() else {'name':'personal','plugins':[]}
assert isinstance(data,dict) and isinstance(data.get('plugins'),list),'Invalid marketplace; left unchanged'
if market.exists():shutil.copy2(market,market.with_suffix('.json.yori-backup'))
# Copy only the reviewed plugin files; this never copies repository history or backend data.
shutil.copytree(source,dest,dirs_exist_ok=True)
entry={'name':name,'source':{'source':'local','path':str(dest.resolve())},'policy':{'installation':'AVAILABLE','authentication':'ON_INSTALL'},'category':'Productivity'}
data['plugins']=[e for e in data['plugins'] if e.get('name')!=name]+[entry]
market.parent.mkdir(parents=True,exist_ok=True)
temp=market.with_suffix('.json.tmp');temp.write_text(json.dumps(data,indent=2)+'\n');temp.replace(market)
print('Yori registered. Restart the desktop app, install/enable Yori from the personal local source, and connect your Yori account.')
