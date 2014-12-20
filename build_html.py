import os
import sys

subdir = sys.argv[1]
dirpath = '../' + subdir
if len(sys.argv) > 2:
    dirpath = sys.argv[2]

if not os.path.isdir(subdir):
    os.mkdir(subdir)

if subdir != '.':
    os.system('del /Q %s\\*' % subdir)

for fn in os.listdir(dirpath):
    if not fn.endswith('.md'):
        continue
    fp = os.path.join(dirpath, fn)
    fphtml = os.path.join(subdir, fn[:-3] + '.html')
    fpcss = '../styles.css'
    print fphtml
    try:
        # if os.system('python -m markdown -x markdown.extensions.sane_lists -x markdown.extensions.def_list %s > %s' % (fp, fphtml)):
        #     break
        # if os.system('python utf8_to_ansi.py %s %s' % (fphtml, fphtml)):
        #     break
        if os.system('python md2html.py %s > %s' % (fp, fphtml)):
            break
        if os.system('python fix_html.py %s %s %s' % (fphtml, fphtml, fpcss)):
            break
        if os.system('cp %s/*.png %s' % (dirpath, subdir)):
            break        
        if os.system('cp %s/*.pdf %s' % (dirpath, subdir)):
            break        
    except:
        import traceback
        traceback.print_exc()
        break
    
    
    
    