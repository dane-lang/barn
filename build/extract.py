"""Extract the eight baseline PNG sheets embedded in index.html into ./sheets/ (needed by build.py for the H10S crop and the two Kilby truss references)."""
import re, base64, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(root, 'index.html')).read()
os.makedirs(os.path.join(root, 'sheets'), exist_ok=True)
for i, b in enumerate(re.findall(r'data:image/png;base64,([A-Za-z0-9+/=]+)', html)):
    open(os.path.join(root, 'sheets', f'{i:02d}.png'), 'wb').write(base64.b64decode(b))
print('extracted', i + 1, 'sheets')
