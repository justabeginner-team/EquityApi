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
    """
    generates a 12 digit random number with leading zeros 
    
    :returns: a string of 12 random unique digits from 000000000001 to 999999999999 with leading zeros i.e 000005678967
    """
    reference_id = "%0.12d" % random.randint(1, 999999999999)
    return reference_id
