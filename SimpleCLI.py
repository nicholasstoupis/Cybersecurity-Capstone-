from argparse import ArgumentParser, Namespace
#These imports are the py files. Such as the scanner and the whois 
import scanner
import wrapper

parser = ArgumentParser()

#These arguments are used to call functons. There is a default incase of invalid statement (will change later)
parser.add_argument('echo', help= 'echos string', type=str, default='thank you')

#Takes arguments from the above line and makes them usable.
args: Namespace = parser.parse_args()

#The echo function
print(args.echo)