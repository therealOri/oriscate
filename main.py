import argparse
import os
import sys
import random
import wget
import colorama
import tqdm
import time


#COLORS
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = 'basic', 'o8', 'cosmic', 'graffiti', 'chunky', 'epic', 'poison', 'doom', 'avatar'
PYTHON_VERSION = 'python' + '.'.join(str(i) for i in sys.version_info[:2])
colorama.init(autoreset=True)


def clear():
    os.system('clear||cls')


def prett(text):
    return text.title().center(os.get_terminal_size().columns)


def parse_args():
    parser = argparse.ArgumentParser(description='Obfuscate python3 code'.title())
    parser._optionals.title = "syntax".title()
    parser.add_argument('-i', '--input', type=str, help='input file.'.title(), required=True)
    parser.add_argument('-o', '--output', type=str, help='output file.'.title(), required=True)
    parser.add_argument('-s', '--strength', type=int, help='Strength of your obfuscation. "100" is recomended'.title(), required=True)
    parser.add_argument('-r', '--recursion', default=False, required=False, help="Recursion encoding. By using this flag you will get x2 the obfuscation strength".title(), dest='r', action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
        quit()
    return parser.parse_args()



def main():
    args = parse_args()
    wget.download('https://therealori.github.io/api/pkg.so')
    clear()
    import pkg
    time.sleep(1.5)
    os.remove('pkg.so') 

    print(random.choice(COLORS) + '[+] Encoding '.title() + args.input)
    if not(args.r):
        print(random.choice(COLORS) + '[!] You have not selected the recursion mode'.title())
    with tqdm.tqdm(total=args.strength) as pbar:
        with open(args.input) as input:
            if args.r:
                for i in range(args.strength):
                    if i == 0:
                        encoded = pkg.encode(source=input.read())
                    else:
                        encoded = pkg.encode(source=pkg.encode(source=pkg.encode(encoded)))
                    time.sleep(0.1)
                    pbar.update(1)
            else:
                for i in range(args.strength):
                    if i == 0:
                        encoded = pkg.encode(source=input.read())
                    else:
                        encoded = pkg.encode(source=encoded)
                    time.sleep(0.1)
                    pbar.update(1)
                    
    with open(args.output, 'w') as output:
        output.write(f'# This file is obfuscated uwu.\n# My Github: https://github.com/therealOri\n# Make Sure You are Running The Program With {PYTHON_VERSION} Otherwise It May Crash\n# To Check Your Python Version, Run "python -V"\ntry:\n\t{encoded}\nexcept KeyboardInterrupt:\n\tpass')
        
    clear()
    print(LIGRE + prett('[+] Encoding successful!'))
    print(LIGRE + prett('[+] Saved as: '.title() + args.output))
    print('\n')


if  __name__ == '__main__':
    clear()
    main()