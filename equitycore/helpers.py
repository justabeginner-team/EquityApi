import os
import random


def pk_path():
    """
    :returns:: path to the directory privatekey.pem is 
    :as defined by running  command "python manage.py keypair --genkey GENKEY" 

    : ""path to .pem "" :: your current_working_dir/.JengaApi/keys/privatekey.pem

    """
    return os.path.join(os.getcwd(), ".JengaApi", "keys", "privatekey.pem")


def reference_id_generator():
    reference_id = "%0.12d" % random.randint(0, 999999999999)
    return reference_id
