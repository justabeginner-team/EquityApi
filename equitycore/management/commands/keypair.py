import os,sys,subprocess
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = """Generates a Public/Public RSA Key Pair which is store in the current User's
            **current working** directory  under the **.JengaAPI/keys/** Directory
            """

    def add_arguments(self,parser):
        parser.add_argument('-gk','--genkey',type=str,help='defines generating key pairs',required=True,)


    def handle(self,*args,**kwargs):
        if kwargs['genkey']:
            self.stdout.write(self.style.SUCCESS('Generating key pairs'))
            #get current working  directory
            current_dir=os.getcwd()

            if not os.path.exists(current_dir + "/.JengaApi"):
                    os.mkdir(current_dir + "/.JengaApi")

            keypath = os.path.join(current_dir, ".JengaApi", "keys")
            if not os.path.exists(keypath):
                os.mkdir(keypath)
            os.system(
                f"cd {keypath};openssl genrsa -out privatekey.pem 2048;openssl rsa -in privatekey.pem -outform PEM -pubout -out publickey.pem"
                )
            self.stdout.write(self.style.WARNING('keys are saved in:'))
            os.system(f"ls {keypath}")

        else:
            self.stdout.write(self.style.ERROR('error while generating key pairs'))


       
