from pythonforandroid.recipe import PythonRecipe

class BleakRecipe(PythonRecipe):
    version = '0.8.11'
    call_hostpython_via_targetpython = False
   
    
    url = 'https://github.com/google/mediapipe/archive/v0.8.11.tar.gz'
    name = 'mediapipe'

recipe = BleakRecipe()
