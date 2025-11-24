import sys
import pprint

pprint.pprint(sys.path, indent=4)


import sys
import pprint

from hello import hello

pprint.pprint(sys.modules, indent=4)
