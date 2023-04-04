import requests
from time import sleep
import os
#Developed by Phant0m The Great
vd='\033[32m'
am='\033[33m'
vm='\033[31m'
az='\033[36m'
ng='\033[1m'
f='\033[m'
lz='\033[34m'   
def info():
  print(f"""
{am}    	
 ██▒   █▓ █    ██  ██▓     ███▄ ▄███▓
▓██░   █▒ ██  ▓██▒▓██▒    ▓██▒▀█▀ ██▒
 ▓██  █▒░▓██  ▒██░▒██░    ▓██    ▓██░
  ▒██ █░░▓▓█  ░██░▒██░    ▒██    ▒██ 
   ▒▀█░  ▒▒█████▓ ░██████▒▒██▒   ░██▒
   ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ░  ░
   ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░░  ░      ░
     ░░   ░░░ ░ ░   ░ ░   ░      ░   
      ░     ░         ░  ░       ░   
     ░                               
{f}

  """)
  print('O programa Vulm, foi criado com a intensão de facilitar o encontro de dados pela web. \n-------------------------------------------------\n                    Dúvidas↓\n\n[?] Estou colocando o ip, porém não consigo localizar os dados, o que fazer ? \n[✓] Isso ocorre quando o programa não reconhece o ip com base na ferramenta selecionada, é por isso que existe a opção de ultilizar mais de uma ferramenta, isso também pode acontecer com as outras consultas (CEP, CNPJ)\n\n[?] Em qual versão está o programa ?\n[✓]Está na versão beta.')
  
def ip():  
    n1 = str(input(f'{f}>>>{az} [CONSULTA IP]{f} - Escolha a ferramenta\n\n- {az}[{f}01{az}]{f} Ip{f}\n- {az}[{f}02{az}]{f} Ipgeolocation{f}  \n- {am}>{f} '))         
    if n1=='2' or n1=='02':
        ip1=input(f'{f}- >>>{am}[{f}Fonte Ipgeolocation {am}]{f} \n Ip >> ')
        url1 = "https://api.ipgeolocation.io/ipgeo?apiKey=9313e7887bad45cea6d4b5845f085464&ip={}".format(ip1)
        res = requests.get(url1)
        req=res.json()
        br="\n{}-------------------------------------------------\nby: Phant0m The Great{}{} \n[Ip]:{}\n[Código do continente]:{}\n[Nome do continente]:{}\n[Código do país 2]:{}\n[Código do país 3]:{}\n[Nome do país]:{}\n[Capital do país]:{}\n[Prov do estado]:{}\n[Distrito]:{}\n[Cidade]:{}\n[CEP]:{}\n[Latitude]:{}\n[Longitude]:{}\n[Is_eu]:{}\n[Código de chamada]:{}\n[País tld]:{}\n[Languages]:{}".format(ng,f,az,req['ip'],req['continent_code'],req['continent_name'],req['country_code2'],req['country_code3'],req['country_name'],req['country_capital'],req['state_prov'],req['district'],req['city'],req['zipcode'],req['latitude'],req['longitude'],req['is_eu'],req['calling_code'],req['country_tld'],req['languages'],req['country_flag'],req['geoname_id'])
        print(br)
        print(f'{f}-------------------------------------------------')
        


    elif n1=='1' or n1=='01':            
        ip2=input(f'{f}- >>>{am}[{f}Fonte IP {am}]{f} \n Ip >> ')      
        url2='http://ip-api.com/json/{}'.format(ip2)
        res2=requests.get(url2);req1=res2.json()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        br2="\n{}-------------------------------------------------\n by: Phant0m The Great{}\n {}[Status]:{}\n [País]:{}\n [Código do país]:{}\n [Região]:{}\n [Nome da região]:{}\n [Cidade]:{}\n [Zip]:{}\n [Lat]:{}\n [Lon]:{}\n [Fuso horário]:{}\n [Isp]:{}\n [Org]:{}\n [As]:{} {}\033[m\n-------------------------------------------------".format(ng,f,az,req1['status'],req1['country'],req1['countryCode'],req1['region'],req1['regionName'],req1['city'],req1['zip'],req1['lat'],req1['lon'],req1['timezone'],req1['isp'],req1['org'],req1['as'],req1['query'],f)       
        print(br2)
      
    
def cep():    
    n1 = str(input(f'>>> {az}[CONSULTA CEP] {f}- Escolha a ferramenta{f}\n\n- {az}[{f}1{az}]{f} Apicep{f}\n- {az}[{f}2{az}]{f} Viacep{f}  \n- {am}>{f} '))
                                     
    if n1=='2' or n1=='02':
        cep2=input(f'{f}- >>>{am}[{f}Fonte Viacep {am}]{f} \n CEP >> ')
        if len(cep2)==8:
            url2='https://viacep.com.br/ws/{}/json/'.format(cep2)
            res2 = requests.get(url2);req2=res2.json()
            resl2="\n{}-------------------------------------------------\nby: Phant0m The Great{} \n{}[Cep]:{}\n[Logradouro]:{}\n[Complemento]:{}\n[Bairro]:{}\n[Localidade]:{}\n[Uf]:{}\n[Ibge]:{}\n[Gia]:{} {}\n-------------------------------------------------".format(ng,f,az,req2['cep'],req2['logradouro'],req2['complemento'],req2['bairro'],req2['localidade'],req2['uf'],req2['ibge'],req2['gia'],f)        
            print(resl2)
        else:
            print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')
    elif n1=='1' or n1=='01':
        cep3=input(f'{f}- >>>{am}[{f}Fonte Apicep {am}]{f} \n CEP >> ')
        if len(cep3) == 8:            
            url3='https://ws.apicep.com/cep/{}.json'.format(cep3) 
            res3 = requests.get(url3);req3=res3.json()
            resl3="\n{}-------------------------------------------------\nby: Phant0m The Great{} \n{}[Status]:{}\n[Ok]:{}\n[Código]:{}\n[Estado]:{}\n[Cidade]:{}\n[Distrito]:{}\n[Endereço]:{}\n[StatusText]:{} {}\n-------------------------------------------------".format(ng,f,az,req3['status'],req3['ok'],req3['code'],req3['state'],req3['city'],req3['district'],req3['address'],req3['statusText'],f)
            print(resl3)
        else:
            print(f' {vm}[!] valor invalido \n digite apenas numeros \n {f}ex: {ng}01001000 {f}')            
def cnpj():    
    cpnj1=input(f'{f}- >>>{am}[{f}Fonte Receita Federal {am}]{f} \n CNPJ >> ')                           
    url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
    res=requests.get(url1);req1=res.json()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    br="\n{}-------------------------------------------------\nby: Phant0m The Great {}\n{}[Data situação]:{}\n[Motivo situação]:{}\n[Complemento]:{}\n[Tipo]:{}\n[Nome]:{}\n[Telefone]:{}\n[Situação]:{}\n[Bairro]:{}\n[Logradouro]:{}\n[Número]:{}\n[Cep]:{}\n[Municipio]:{}\n[Fantasia]:{}\n[Porte]:{}\n[Abertura]:{}\n[Natureza juridica]:{}\n[Uf]:{}\n[Cnpj]:{}\n[Ultima atualização]:{}\n[Status]:{}\n[Email]:{}\n[Efr]:{}\n[Situação especial]:{}\n[Data situação especial]:{}".format(ng,f,az,req1['data_situacao'],req1['motivo_situacao'],req1['complemento'],req1['tipo'],req1['nome'],req1['telefone'],req1['situacao'],req1['bairro'],req1['logradouro'],req1['numero'],req1['cep'],req1['municipio'],req1['fantasia'],req1['porte'],req1['abertura'],req1['natureza_juridica'],req1['uf'],req1['cnpj'],req1['ultima_atualizacao'],req1['status'],req1['email'],req1['efr'],req1['situacao_especial'],req1['data_situacao_especial'],f)                  
    print(br)
    print(f'{f}-------------------------------------------------')
def ban():
    print(f"""
{am}    	
 ██▒   █▓ █    ██  ██▓     ███▄ ▄███▓
▓██░   █▒ ██  ▓██▒▓██▒    ▓██▒▀█▀ ██▒
 ▓██  █▒░▓██  ▒██░▒██░    ▓██    ▓██░
  ▒██ █░░▓▓█  ░██░▒██░    ▒██    ▒██ 
   ▒▀█░  ▒▒█████▓ ░██████▒▒██▒   ░██▒
   ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ░  ░
   ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░░  ░      ░
     ░░   ░░░ ░ ░   ░ ░   ░      ░   
      ░     ░         ░  ░       ░   
     ░                               
{f}

  """)
os.system('clear');
def menu():
    os.system('clear')
    print(f"""
{am}    	
 ██▒   █▓ █    ██  ██▓     ███▄ ▄███▓
▓██░   █▒ ██  ▓██▒▓██▒    ▓██▒▀█▀ ██▒
 ▓██  █▒░▓██  ▒██░▒██░    ▓██    ▓██░
  ▒██ █░░▓▓█  ░██░▒██░    ▒██    ▒██ 
   ▒▀█░  ▒▒█████▓ ░██████▒▒██▒   ░██▒
   ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ░  ░
   ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░░  ░      ░
     ░░   ░░░ ░ ░   ░ ░   ░      ░   
      ░     ░         ░  ░       ░   
     ░                               
{f}
Discord Tag: 𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150	 
Perfil no Replit: https://replit.com/@phant0m007 
-------------------------------------------------
[{az}01{f}]{f} Consultar CEP{f}
[{az}02{f}]{f} Consultar CNPJ{f}
[{az}03{f}]{f} Consultar IP {f}
[{az}04{f}]{f} Informações
[{az}05{f}]{f} Sair{f}
    """)
try:
    menu()
    inpu=str(input('Digite sua escolha: '))
except KeyboardInterrupt:
    exit()
except:
    print(f'{vm}- [!] error valor invalido {f}')
try:    
    if inpu=='3' or inpu=='03':   
        os.system('clear');ban();ip()
    elif inpu=='1' or inpu=='01':
        os.system('clear');ban();cep()
    elif inpu=='2' or inpu=='02':
        os.system('clear');ban();cnpj()
    elif inpu=='4' or inpu=='04':
        os.system('clear');info()
    elif inpu=='5' or inpu=='05':
        print('Até a próxima !')
        exit()
    else:
        print(f'{vm}- [!] valor invalido !! {f}');exit()                                                                                          
except:
    exit()
