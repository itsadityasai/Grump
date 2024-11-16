# Grr
Battery sensitive hash cracker.

---

# Prerequisites 

You will need <a href='https://www.python.org/'>Python</a> installed, along with pip, python's in built package manager. You can install it using the python installer.

After installation of python, you will need to install the following modules:

  - colorama
  - psutil
  - hashlib
  
To install these, run:

``` pip install colorama psutil hashlib ```


Once that's done, all you have to do is run ```grr.py``` . More on that below.

---

# Usage

## Overview

You can run ```grr.py --help``` to get a brief idea of what to do.

```

        Grr - A battery sensitive hash cracker.
        Made by Mateo Cruz (linktr.ee/mateo.xz).

        See README.md for detailed instructions.

        Format : printprogram wordlist | grr.py hash type
        Example : cat list.txt | grr.py 900150983cd24fb0d6963f7d28e17f72 md5
          
```

## Supplying passwords to try

Grr only supports piped input. Take a look at the example above.

Replace `list.txt` with your wordlist's path. If you're using Windows without Cygwin, then use `type` instead of `cat`.
You needn't supply a wordlist. Any pipe will do. You can even try one password like this : ``` echo p@sswd | grr.py 900150983cd24fb0d6963f7d28e17f72 md5 ```


## Hash types

Supported hash types are:

  - md5
  - sha1 
  - sha256 
  - sha384 
  - sha512
  

## Saving progress

There is no inbuilt method to save progress. However, you can use <a href='http://www.openwall.com/john/'>John The Ripper</a> in the following manner.

``` john --session=foo --wordlist="path/to/your/wordlist" --stdout | grr.py hash type ```

John will pipe the wordlist to Grr. It makes note of where you stopped last, and the next time, it starts piping at the place you stopped. So you don't try passwords you've already tried before. And so, we have successfully mangaged to save progress.

To restore the session, run ``` john --restore=foo  | grr.py hash type ```. Note that this is assuming you named your session *foo*. Also, the session's details are saved in a file. In this case, *foo.rec*. This means that if you lose this file you lose your session.


# Contributing

Go ahead. GitHub offers lots of features for this. Just make sure you read <a href='https://github.com/Mate0xz/Grr/blob/main/LICENSE'>the license</a> first.


# License

This code is offered under <a href='https://github.com/Mate0xz/Grr/blob/main/LICENSE'>this license</a>. By using this software you agree to abide by it.

