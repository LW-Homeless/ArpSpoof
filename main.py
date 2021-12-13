from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from os import name, system

from model.ArpSpoof import ArpSpoof
from model.ArpSpoofException import ArpSpoofException
from colorama import Fore, init


class Main:

    @staticmethod
    def main():
        init()

        try:
            if name == "posix":
                system("clear")
            elif name == "nt" or name == "ce" or name == "dos":
                system("cls")

            parser = ArgumentParser(prog="Arpspoof",
                                    description="ArpSpoof herramienta para realizar pruebas de "
                                                "envenenamiento de tablas arp",
                                    formatter_class=RawTextHelpFormatter)

            parser.add_argument("-t", type=str, metavar="", help="Host (target) a realizar arpspoof")
            parser.add_argument("-g",  type=str, metavar="", help="Host (Gateway) a realizar arpspoof")

            args = parser.parse_args()

            if args.t is None:
                print(Fore.RED + "[X] No ha ingresado ip host")
            elif args.g is None:
                print(Fore.RED + "[X] No ha ingresado ip Gateway")
            else:
                spoof = ArpSpoof(args.t, args.g)

                print(Fore.GREEN + "*" * 100)
                print(Fore.GREEN + "Iniciando ArpSpoof")
                print(Fore.GREEN + "*" * 100)
                for x in spoof.spoof():
                    print(Fore.RED + x)

        except KeyboardInterrupt:
            spoof.stop_spoof()
            print(Fore.GREEN + "*" * 100)
            print(Fore.GREEN + "[!] Deteniendo ArpSpoof")
            print(Fore.GREEN + "[!] Reversando ArpSpoof")
            print(Fore.GREEN + "*" * 100)
            for x in spoof.reverse_spoof():
                print(Fore.RED + x)

        except ArpSpoofException as exArp:
            print(exArp)


if __name__ == "__main__":
    Main.main()
