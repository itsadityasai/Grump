try:
    from sys import argv, stdin
    from hashlib import md5, sha1, sha256, sha384, sha512
    from psutil import sensors_battery as battery
    from time import sleep
    from sys import exit as die
    from colorama import Fore, Style, init
    init()

    print()

    if len(argv) == 1:
        argv.append('--help')

    if argv[1] in ['--help', 'help', '-h']:
        print("""

        Grr - A battery sensitive hash cracker.
        Made by Mateo Cruz (linktr.ee/mateo.xz).

        See README.md for detailed instructions.

        Format : grr.py hash type
        Example : grr.py 900150983cd24fb0d6963f7d28e17f72 md5


        """)
        die()

    class hash:
        hash = argv[1]
        type = argv[2].lower()

    class stats:
        tried = 0
        errors = 0

    for line in stdin:

        stats.tried += 1
        testKey = line.replace('\n', '')

        if stats.tried % 100000 == 0:
            print(f"{Fore.GREEN}{stats.tried / 1000}K tries, {Fore.RED}{stats.errors / 1000}K errors {Style.RESET_ALL}")

        if stats.tried % 1000000 == 0:
            if not battery().power_plugged:
                print(f"{Fore.YELLOW}On battery power.. Pausing {Style.RESET_ALL}")
                while True:
                    sleep(60)
                    if battery().power_plugged:
                        print(f"{Fore.GREEN}Plugged in.. Resuming {Style.RESET_ALL}")
                        break

        try:

            if hash.type == 'md5':
                if (md5(testKey.encode()).hexdigest() == hash.hash):
                    print(f"\n{Fore.YELLOW}MD5({Fore.BLUE}{testKey}{Fore.YELLOW}){Fore.YELLOW} = {Fore.YELLOW}{hash.hash}{Style.RESET_ALL}\n")
                    die()
            elif hash.type == 'sha1':
                if (sha1(testKey.encode()).hexdigest() == hash.hash):
                    print(f"\n{Fore.YELLOW}SHA1({Fore.BLUE}{testKey}{Fore.YELLOW}){Fore.YELLOW} = {Fore.YELLOW}{hash.hash}{Style.RESET_ALL}\n")
                    die()
            elif hash.type == 'sha256':
                if (sha256(testKey.encode()).hexdigest() == hash.hash):
                    print(f"\n{Fore.YELLOW}SHA256({Fore.BLUE}{testKey}{Fore.YELLOW}){Fore.YELLOW} = {Fore.YELLOW}{hash.hash}{Style.RESET_ALL}\n")
                    die()
            elif hash.type == 'sha384':
                if (sha384(testKey.encode()).hexdigest() == hash.hash):
                    print(f"\n{Fore.YELLOW}SHA384({Fore.BLUE}{testKey}{Fore.YELLOW}){Fore.YELLOW} = {Fore.YELLOW}{hash.hash}{Style.RESET_ALL}\n")
                    die()
            elif hash.type == 'sha512':
                if (sha512(testKey.encode()).hexdigest() == hash.hash):
                    print(f"\n{Fore.YELLOW}SHA512({Fore.BLUE}{testKey}{Fore.YELLOW}){Fore.YELLOW} = {Fore.YELLOW}{hash.hash}{Style.RESET_ALL}\n")
                    die()
            else:
                print(f"{Fore.RED}Invalid hash type. Please see README.md\n")
                die()

        except UnicodeEncodeError:

            stats.errors += 1
            stats.tried -= 1

except KeyboardInterrupt:
    print(f"{Fore.RED}Interrupted.. Exiting with {stats.tried} tries and {stats.errors} errors {Style.RESET_ALL}")
