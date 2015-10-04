import csv

DHCPSERVER = "127.0.0.1"

data = []
cmds = []




#
# DEF
#

def build_add_scope(scope):

  # netsh dhcp server \\[server] 
  # add scope ScopeAddress SubnetMask ScopeName[ScopeComment]

  cmds = ('add scope ' + scope['subnet'] + ' ' + scope['netmask'] + ' ' + scope['descr'])
  return cmds

def build_netsh_dhcp():
  return('netsh dhcp server ' + DHCPSERVER + ' ')


def read(filename):

    out_dict = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(csvfile) # skip the first row
        for row in reader:
            if row[0][0] != "#":
               	out_dict['subnet'] = row[0]
               	out_dict['netmask']= row[1]
               	out_dict['gateway']= row[2]
               	out_dict['exclude_start']= row[3]
               	out_dict['exclude_end']= row[4]
               	out_dict['descr']= row[5]
               	data.append(out_dict)
    return data

def output_dhcp_create_cmd(scopes):
  for scope in scopes:
    print(build_netsh_dhcp() + build_add_scope(scope))
    

# 
# MAIN
#

scopes = read('scopes.txt')
output_dhcp_create_cmd(scopes)


#
# netsh
#
"""
add scope ScopeAddress SubnetMask ScopeName[ScopeComment]

"""