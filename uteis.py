import requests, cores as c, os, re, banners, time, sys
from pystyle import Colorate, Colors
def wifi():
  print(f'\nSe conectando ao {c.bblue}Vulm{c.white}...')
  url = 'https://www.google.com'
  timeout = 5
  time.sleep(2)
  try:
        requests.get(url, timeout=timeout)
  except ConnectionError:
        print(f'\nNão foi possível se conectar ao {c.blue}Vulm{c.white}.\nTente novamente mais tarde')
        sys.exit()
def cep_viacep():
        os.system("clear")
        print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
        cep2=input(f'{c.white}- >>>{c.yellow}[{c.white} Fonte Viacep {c.yellow}]{c.white} \n CEP >> ')
        pattern = re.compile(r'\s+')    
        cep2 = re.sub(pattern, '', cep2)
        try:
            url2='https://viacep.com.br/ws/{}/json/'.format(cep2)
            res2 = requests.get(url2);req2=res2.json()
            resl2="\n{}-------------------------------------------------\n{}[Cep]: {}{}\n{}[Logradouro]: {}{}\n{}[Complemento]: {}{}\n{}[Bairro]: {}{}\n{}[Localidade]: {}{}\n{}[Uf]: {}{}\n{}[Ibge]: {}{}\n{}-------------------------------------------------".format(c.white,c.bwhite,c.cyan, req2['cep'],c.bwhite,c.cyan,req2['logradouro'],c.bwhite,c.cyan,req2['complemento'],c.bwhite,c.cyan,req2['bairro'],c.bwhite,c.cyan,req2['localidade'],c.bwhite,c.cyan,req2['uf'],c.bwhite,c.cyan,req2['ibge'],c.white)        
            print(resl2)
            input('[ENTER] para voltar ao menu.')
        except:
         96042656000128


          
         print(f'''\n[{c.red}!{c.white}] {c.red}CEP inválido.{c.white}\n''')
         input('[ENTER] para voltar ao menu.')
def cep_apicep():
        os.system('clear')
        print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
        cep3=input(f'{c.white}- >>>{c.yellow}[{c.white} Fonte Apicep {c.yellow}]{c.white} \n CEP >> ')
        pattern = re.compile(r'\s+')    
        cep3 = re.sub(pattern, '', cep3)
        try:       
          
            url3='https://ws.apicep.com/cep/{}.json'.format(cep3) 
            res3 = requests.get(url3);req3=res3.json()
            resl3="\n{}-------------------------------------------------\n{}[Status]: {}{}\n{}[Ok]: {}{}\n{}[Código]: {}{}\n{}[Estado]: {}{}\n{}[Cidade]: {}{}\n{}[Distrito]: {}{}\n{}[Endereço]: {}{}\n{}[StatusText]: {}{} {}\n-------------------------------------------------".format(c.white,c.bwhite,c.cyan,req3['status'],c.bwhite,c.cyan,req3['ok'],c.bwhite,c.cyan,req3['code'],c.bwhite,c.cyan,req3['state'],c.bwhite,c.cyan,req3['city'],c.bwhite,c.cyan,req3['district'],c.bwhite,c.cyan,req3['address'],c.bwhite,c.cyan,req3['statusText'],c.white)
            print(resl3)
            input('[ENTER] para voltar ao menu.')
        except:
          print(f'''[{c.red}!{c.white}] {c.red}CEP inválido.{c.white}\n''')
          input('[ENTER] para voltar ao menu.')
def cnpj():
    print('Fortamo: XXXXXXXXXXXXXX')
    cpnj1=input(f'{c.white}- >>>{c.yellow}[ {c.white}Fonte Receita Federal {c.yellow}]{c.white} \n CNPJ >> ')
    try:
      url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
      res=requests.get(url1);req1=res.json()
      br="{}\n-----------------------------------------------\n{}[Data situação]: {}{}\n{}[Motivo situação]: {}{}\n{}[Complemento]: {}{}\n{}[Tipo]: {}{}\n{}[Nome]: {}{}\n{}[Telefone]: {}{}\n{}[Situação]: {}{}\n{}[Bairro]: {}{}\n{}[Logradouro]: {}{}\n{}[Número]: {}{}\n{}[Cep]: {}{}\n{}[Municipio]: {}{}\n{}[Fantasia]: {}{}\n{}[Porte]: {}{}\n{}[Abertura]: {}{}\n{}[Natureza juridica]: {}{}\n{}[Uf]: {}{}\n{}[Cnpj]: {}{}\n{}[Ultima atualização]: {}{}\n{}[Status]: {}{}\n{}[Email]: {}{}\n{}[Efr]: {}{}\n{}[Situação especial]: {}{}\n{}[Data situação especial]: {}{}{}".format(c.white,c.bwhite,c.cyan,req1['data_situacao'],c.bwhite,c.cyan,req1['motivo_situacao'],c.bwhite,c.cyan,req1['complemento'],c.bwhite,c.cyan,req1['tipo'],c.bwhite,c.cyan,req1['nome'],c.bwhite,c.cyan,req1['telefone'],c.bwhite,c.cyan,req1['situacao'],c.bwhite,c.cyan,req1['bairro'],c.bwhite,c.cyan,req1['logradouro'],c.bwhite,c.cyan,req1['numero'],c.bwhite,c.cyan,req1['cep'],c.bwhite,c.cyan,req1['municipio'],c.bwhite,c.cyan,req1['fantasia'],c.bwhite,c.cyan,req1['porte'],c.bwhite,c.cyan,req1['abertura'],c.bwhite,c.cyan,req1['natureza_juridica'],c.bwhite,c.cyan,req1['uf'],c.bwhite,c.cyan,req1['cnpj'],c.bwhite,c.cyan,req1['ultima_atualizacao'],c.bwhite,c.cyan,req1['status'],c.bwhite,c.cyan,req1['email'],c.bwhite,c.cyan,req1['efr'],c.bwhite,c.cyan,req1['situacao_especial'],c.bwhite,c.cyan,req1['data_situacao_especial'],c.white)
      print(br)
      print(f'''{c.white}-''' * 47)
      input('[ENTER] para voltar ao menu.')
    except:
      print(f'''\n[{c.red}!{c.white}] {c.red}CNPJ inválido.{c.white}\n''')
      input('[ENTER] para voltar ao menu.')
def ip():
      ip2=input(f'{c.white}- >>>{c.yellow}[ {c.white}Fonte IP {c.yellow}]{c.white} \n Ip >> ')
      try:
        
        url2='http://ip-api.com/json/{}'.format(ip2)
        res2 = requests.get(url2)
        req1=res2.json()
        br2="\n{}-------------------------------------------------\n{}[Status]: {}{}\n{}[País]: {}{}\n{}[Código do país]: {}{}\n{}[Região]: {}{}\n{}[Nome da região]: {}{}\n{}[Cidade]: {}{}\n{}[Zip]: {}{}\n{}[Lat]: {}{}\n{}[Lon]: {}{}\n{}[Fuso horário]: {}{}\n{}[Isp]: {}{}\n{}[Org]: {}{}\n{}[As]: {}{} {}{}\033[m\n-------------------------------------------------".format(c.white,c.bwhite,c.cyan,req1['status'],c.bwhite,c.cyan,req1['country'],c.bwhite,c.cyan,req1['countryCode'],c.bwhite,c.cyan,req1['region'],c.bwhite,c.cyan,req1['regionName'],c.bwhite,c.cyan,req1['city'],c.bwhite,c.cyan,req1['zip'],c.bwhite,c.cyan,req1['lat'],c.bwhite,c.cyan,req1['lon'],c.bwhite,c.cyan,req1['timezone'],c.bwhite,c.cyan,req1['isp'],c.bwhite,c.cyan,req1['org'],c.bwhite,c.cyan,req1['as'],req1['query'],c.white)
        print(br2)
        input('[ENTER] para voltar ao menu.')
      except:
        print(f'''\n[{c.red}!{c.white}] {c.red}IP inválido.{c.white}\n''')
        input('[ENTER] para voltar ao menu.')
def ipg():
      ip1=input(f'- >>>{c.yellow}[{c.white} Fonte Ipgeolocation {c.yellow}]{c.white} \n Ip >> ')
      try:
        url1 = "https://api.ipgeolocation.io/ipgeo?apiKey=9313e7887bad45cea6d4b5845f085464&ip={}".format(ip1)
        res = requests.get(url1)
        req=res.json()
        br="\n{}-------------------------------------------------\n{}[Ip]: {}{}\n{}[Código do continente]: {}{}\n{}[Nome do continente]: {}{}\n{}[Código do país 2]: {}{}\n{}[Código do país 3]: {}{}\n{}[Nome do país]: {}{}\n{}[Capital do país]: {}{}\n{}[Prov do estado]: {}{}\n{}[Distrito]: {}{}\n{}[Cidade]: {}{}\n{}[CEP]: {}{}\n{}[Latitude]: {}{}\n{}[Longitude]: {}{}\n{}[Is_eu]: {}{}\n{}[Código de chamada]: {}{}\n{}[País tld]: {}{}\n{}[Languages]: {}{}{}{}".format(c.white,c.bwhite,c.cyan,req['ip'],c.bwhite,c.cyan,req['continent_code'],c.bwhite,c.cyan,req['continent_name'],c.bwhite,c.cyan,req['country_code2'],c.bwhite,c.cyan,req['country_code3'],c.bwhite,c.cyan,req['country_name'],c.bwhite,c.cyan,req['country_capital'],c.bwhite,c.cyan,req['state_prov'],c.bwhite,c.cyan,req['district'],c.bwhite,c.cyan,req['city'],c.bwhite,c.cyan,req['zipcode'],c.bwhite,c.cyan,req['latitude'],c.bwhite,c.cyan,req['longitude'],c.bwhite,c.cyan,req['is_eu'],c.bwhite,c.cyan,req['calling_code'],c.bwhite,c.cyan,req['country_tld'],c.bwhite,c.cyan,req['languages'],req['country_flag'],req['geoname_id'])
        print(br)
        print(f'''{c.white}-''' * 47)
        input('[ENTER] para voltar ao menu.')
      except:
        print(f'''\n[{c.red}!{c.white}] {c.red}IP inválido.{c.white}\n''')
        input('[ENTER] para voltar ao menu.')
