import boto
from boto import ec2



connection=ec2.connect_to_region("us-west-2")
reservations=connection.get_all_instances();
for res in reservations:
  for inst in res.instances:
   if 'travis' in inst.tags:
    if inst.state == "running":
     print "%s" % (inst.ip_address)

     with open("inventory", "r") as in_file:
      buf = in_file.readlines()

     with open("inventory", "w") as out_file:
      for line in buf:
        out_file.write(line)
        if '[webservers]' in line:
  	 out_file.write("\n%s" % (inst.ip_address))
