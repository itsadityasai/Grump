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
        Made by Neptune (github.com/wolfrust/).

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

### Using --skip

*Before you jump in, let me just say that crunch is a wordlist generator, it is the program that is piping output in this scenario. The same logic applies if you're using `type wordlist.txt` or any other password supply method.*

Say you run this command and get an output like this:

```

crunch.exe 1 10 abcdefghijk | grr.py 5d41402abc4b2a76b9719d911017c592 md5

300000K tries
400000K tries
..
1000000K tries


```

And then for whatever reason, you have to stop the program. Just make note of the command you used and the number of tries done (so in this case, the number of tries is 1000000K).

The next time you start Grr, you would run a command like this:

``` [original pipe command] | grr.py [same hash] [same hash type] --skip [tries complete in last session] ```

To continue with the previous example, you would run:

``` crunch.exe 1 10 abcdefghijk | grr.py 5d41402abc4b2a76b9719d911017c592 md5 --skip 1000000000 ```

Note that you must enter the entire integer value. (So, not 1000000K, but 1000000000.)

### Using JTR

You can use <a href='http://www.openwall.com/john/'>John The Ripper</a> in the following manner to save progress.

``` john --session=foo --wordlist="path/to/your/wordlist" --stdout | grr.py hash type ```

John will pipe the wordlist to Grr. It makes note of where you stopped last, and the next time, it starts piping at the place you stopped. So you don't try passwords you've already tried before. And so, we have successfully mangaged to save progress.

To restore the session, run ``` john --restore=foo  | grr.py hash type ```. Note that this is assuming you named your session *foo*. Also, the session's details are saved in a file. In this case, *foo.rec*. This means that if you lose this file you lose your session.


# Contributing

Go ahead. GitHub offers lots of features for this. Just make sure you read <a href='https://github.com/Mate0xz/Grr/blob/main/LICENSE'>the license</a> first.


# License

This code is offered under <a href='https://github.com/Mate0xz/Grr/blob/main/LICENSE'>this license</a>. By using this software you agree to abide by it.
