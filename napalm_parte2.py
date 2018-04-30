#!/usr/bin/python

import napalm

#Router diccionario
R1={'so':'ios','hostname':'R1','ip':'1.1.1.1','username':'napalm','password':'napalm','secret':'cisco','alterfile':'/home/jose/Automatizacao/R1_snmp.conf'}
R2={'so':'junos','hostname':'R2','ip':'2.2.2.2','username':'napalm','password':'napalm123','alterfile':'/home/jose/Automatizacao/R2_snmp.conf'}

#Listado dos meus roteadores
routers=[R1,R2]


#BEGIN


#Loop para fazer varredura
for router in routers:
 #Caso seja um roteador IOS, utilizar o parametro optional_args com a senha de enable
 if router['so'] == 'ios':
  optional_args={'secret':router['secret']}
 else:
  optional_args={}
 #Selecctiona o driver
 driver = napalm.get_network_driver(router['so'])
 #Coneta ao roteador, dentro de um try..execpt, caso de algum erro o erro eh printado
 try:
  device = driver (hostname=router['ip'], username=router['username'], password=router['password'],optional_args=optional_args)
  device.open()
  #Carrega o arquivo das atualizacoes a serem feitas
  device.load_merge_candidate(filename=router['alterfile'])
  #Fecha a conexao
  device.close()
 except Exception as error:
  print "Problemas com driver/sessao do roteador %s" % router['ip']
  print error

#FIM
 
