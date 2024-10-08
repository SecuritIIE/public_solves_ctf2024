# Sneaky /Snakey_vm: setup (in solution's reverse order)

## 3d step: Write the constraints on the flag (cf easy_crackme)

Choose a flag, then edit and run

```bash
python flag_constraints.py 
```

## 2nd step: Write a code to check the flag and create its bytecode (using dis - python vm)

With our constraints printed, write `challenge_generator.py` and run:

```bash
echo 'a="""' > sneaky.py
python challenge_generator.py >> sneaky.py
echo '"""' >> sneaky.py
echo 'print("Maybe you need to go deeper :)")' >> sneaky.py
```

## 1st step: Pack the code with pyinstaller

```bash
pip install -U pyinstaller
pyinstaller --onefile sneaky.py 

mv dist/sneaky . && rm -rf build/ dist/ *.spec
```
