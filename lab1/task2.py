#!/usr/bin/python3

import oci 

def create_compartment (parent_compartment_id, name, description): 

    # Create the compartment details object
    create_compartment_details = oci.identity.models.CreateCompartmentDetails(
       compartment_id=parent_compartment_id,
       name=name,
       description=description
    )
   
    try:
       # Create the compartment
       response = identity_client.create_compartment(create_compartment_details)
       compartment = response.data
   
       print(f"Compartment '{compartment.name}' created successfully!")
       print(f"Compartment OCID: {compartment.id}")
       print(f"Compartment Lifecycle State: {compartment.lifecycle_state}")
       return compartment.id
   
    except oci.exceptions.ServiceError as e:
       print(f"Error creating compartment: {e}")
       exit 

if __name__ == '__main__':

    #load configuration
    config = oci.config.from_file("~/.oci/config", "DEFAULT") 
    identity_client = oci.identity.IdentityClient(config)
    
    # Define EE279 compartment 
    parent_compartment_id = "ocid1.tenancy.oc1..aaaaaaaaxwlaxyenswxcwdnuvnfs6nmuvliub3uycbvmgaceff3atwxg7ifa"
    compartment_name = "EE279"
    compartment_description = "EE279 CIS (Computer Information Security) Landing Zone"

    # Create EE279 compartment 
    ee279_ocid = create_compartment (parent_compartment_id, compartment_name, compartment_description)
    ee279_ocid = "ocid1.compartment.oc1..aaaaaaaafzvzpakzxpleayn3ummg5pxdww62gld5z2xjseani3xnscwje5la"

    # Define E279 child compartments 
    child_complist = ["net", "sec", "app", "db", "bkp", "sto"] 
    child_compdesc = {
			"net": "for all network resources i.e. virtual cloud networks",
		      	"sec": "for all security resource i.e. bastions",
			"app": "for all common application resources i.e. app vms or PaaS", 
			"db": "for all common database resources i.e. db vms or PaaS", 
			"bkp": "for common backups (of app artifacts, databases, etc.)",
			"sto": "for common non-backup storage i.e. buckets or filesystems"
		     }

    for comp in child_complist: 
       ocid = create_compartment (ee279_ocid, f"EE279-{comp}", child_compdesc[comp])
       print(ocid)
