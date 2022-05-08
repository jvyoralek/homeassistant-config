from urllib.request import urlopen
import json
import re

url = urlopen("https://raw.githubusercontent.com/Templarian/MaterialDesign/master/meta.json")
meta = [('mdi-'+i['name'], i['codepoint']) for i in json.loads(url.read()) if re.search('^weather-', i['name'])]

print('''---
esphome:
  # ...
  includes:
    - weather_icon_map.h

# ...

font:
  - file: fonts/materialdesignicons-webfont.ttf
    id: ...
    size: ...
    glyphs:''')

for name, codepoint in meta:
    print('      - "\\U000%s" # %s' % (codepoint, name))

with open('weather_icon_map.h', 'w') as h:
    h.write('#include <map>\nstd::map<std::string, std::string> weather_icon_map\n')
    h.write('  {\n')
    for name, codepoint in meta:
        h.write('    {"%s", "\\U000%s"},\n' % (name.replace('weather-', ''), codepoint))
    h.write('  };')