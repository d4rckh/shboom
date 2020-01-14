# **shboom**
✨ *Oh, life could be a dream* ✨

Shboom (ha**shboom**) with a hash dictionary attack script made in python3.

## Supported types
- md5
## Downloading
Make sure you have `git`, `python3` and `python3-pip` packages installed.
```bash
git clone https://github.com/m4d-d0x/shboom/ # clone the master branch
cd shboom/ # change the directory in the shboom folder
```
And it's there! There are no thirdparty python dependencies!
## Using
```bash
python3 main.py -h # this will print the help screen
```
It should look at like this:
```
usage: main.py [-h] [-f F] [-t T] [-w W]

optional arguments:
  -h, --help  show this help message and exit
  -f F        The file to takes the hashes from, one on each line.
  -t T        Hash type md5 is the only one supported right now.
  -w W        The file containg the wordlist.
```

`-f` is used to specify the file with the hashes to crack, make sure you put one on each line. Also make sure there are no blank lines.

`-t` is used to specify the hash type. 

`-w` is used to specify the wordlist file.
