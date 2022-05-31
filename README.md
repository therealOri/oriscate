# oriscate
A python code obfuscator. 
__ __

<br />
<br />


# How To Use
```
#Install.
git clone https://github.com/therealOri/oriscate.git
cd oriscate

#Set up enviroment.
virtualenv oscENV
source oscENV/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

#Run code.
python main.py -i file1.py -o file2.py -s 100 -r
```
__ __


<br />
<br />

# Make your code a `.so`/`.pyd` file.
> Usning cython

```
python setup.py build_ext --inplace
```
> You should get a .so file if on linux or a .pyd file if on windows. (Rename the file to whatever you want).
__ __
