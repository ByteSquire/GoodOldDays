$Env:PYTHONPATH = "C:\Users\green\AppData\Local\Programs\GIMP 2\lib\python2.7"
if (!$Env:Path.Contains("C:\Users\green\AppData\Local\Programs\GIMP 2\bin")) {$Env:Path += "C:\Users\green\AppData\Local\Programs\GIMP 2\bin"}
gimp-console-2.10 -idf --batch-interpreter python-fu-eval -b "import sys;sys.path=['.']+sys.path;import icon_generator;icon_generator.run('../../source/TexturesSVG','../../source/GODTextures')" -b "pdb.gimp_quit(1)"
