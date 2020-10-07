import os


def pk_path():
    """
    :returns:: path to the directory privatekey.pem is 
    :as defined by running  command "python manage.py keypair --genkey GENKEY" 

    : ""path to .pem "" :: your current_working_dir/.JengaApi/keys/privatekey.pem

    """   
    return os.path.join(os.getcwd(), ".JengaApi", "keys", "privatekey.pem")
