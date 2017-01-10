# -*- coding: utf-8 -*-
import os
import sys
from osax import *
from filter.Filter import Filter

DEBUG = False
sa = OSAX()

if DEBUG is False:
    DATA_ROOT = '../../../'
else:
    DATA_ROOT = '../'
xls_file = os.path.join(DATA_ROOT, 'tournee-totems.xls')

if os.path.isdir(DATA_ROOT) is False:
    sa.display_dialog(u"Répértoire contenant les fichiers non trouvé (chemin attendu: %s)" % (os.path.abspath(DATA_ROOT)), buttons=["OK"])
    sys.exit(-1)

if os.path.isfile(xls_file) is False:
    sa.display_dialog(u"Fichier excel introuvable (chemin attendu: %s)" % (os.path.abspath(xls_file)), buttons=["OK"])
    sys.exit(-1)

if DEBUG:
    filter = Filter(xls_file, os.path.abspath(DATA_ROOT))
    filter.parse()
    filter.filter()
else:
    try:
        filter = Filter(xls_file, os.path.abspath(DATA_ROOT))
        filter.parse()
        filter.filter()
    except:
        import sys
        ex = sys.exc_info()[1]
        sa.display_dialog(ex.__str__(), buttons=["OK"])
        sys.exit(-1)
