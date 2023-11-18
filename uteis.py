import requests, cores as c, os, re, banners, time, sys, phonenumbers as phn
from pystyle import Colorate, Colors
from rich.panel import Panel
from rich.console import Console
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from pystyle import Colorate, Colors
from datetime import datetime
console=Console()
Versão='6.0'
def wifi():
  print(f'\nSe conectando ao {c.bblue}Vulm{c.white}...')
  url = 'https://www.google.com'
  timeout = 5
  time.sleep(2)
  try:
        requests.get(url, timeout=timeout)
  except:
        print(f'\nNão foi possível se conectar ao {c.blue}Vulm{c.white}.\nTente novamente mais tarde')
        sys.exit()
def placa_fipeplaca():
    print('Formato: ABC1234')
    placa = input(f'{c.white}- >>>{c.yellow}[ {c.white}Fonte: FipePlaca {c.yellow}]{c.white} \n Placa >> ')
    pattern = re.compile(r'\s+')    
    placa = re.sub(pattern, '', placa)
    url = f"https://www.fipeplaca.com.br/_next/data/dpgLQgwe3OL_eJHYZALg7/search/{placa}.json?plate={placa}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get('pageProps') and data['pageProps'].get('vehicle'):
            vehicle_info = data['pageProps']['vehicle']
            print(f'{c.white}\n{"─"*47}{c.white}\n'
                  f'{c.bwhite}[Marca]: {c.cyan}{vehicle_info["marca"]}\n'
                  f'{c.bwhite}[Modelo]: {c.cyan}{vehicle_info["modelo"]}\n'
                  f'{c.bwhite}[Ano Modelo]: {c.cyan}{vehicle_info["anoModelo"]}\n'
                  f'{c.bwhite}[Código Fipe]: {c.cyan}{vehicle_info["codigoFipe"]}\n'
                  f'{c.bwhite}[Cilindradas]: {c.cyan}{vehicle_info["cilindradas"]}\n'
                  f'{c.bwhite}[Potência]: {c.cyan}{vehicle_info["potencia"]}\n'
                  f'{c.bwhite}[Cor]: {c.cyan}{vehicle_info["cor"]}\n'
                  f'{c.bwhite}[UF]: {c.cyan}{vehicle_info["uf"]}\n'
                  f'{c.bwhite}[Município]: {c.cyan}{vehicle_info["municipio"]}\n'
                  f'{c.bwhite}[Renavam]: {c.cyan}{vehicle_info["renavam"]}\n'
                  f'{c.bwhite}[Chassi]: {c.cyan}{vehicle_info["chassi"]}\n'
                  f'{c.bwhite}[IPVA]: {c.cyan}{vehicle_info["ipva"]}\n'
                  f'{c.bwhite}[Placa]: {c.cyan}{vehicle_info["placa"]}')

            if vehicle_info.get('fipe'):
                for fipe_entry in vehicle_info['fipe']:
                    print(f'{c.bwhite}[Valor]: {c.cyan}{fipe_entry["Valor"]}\n'
                          f'{c.bwhite}[Marca]: {c.cyan}{fipe_entry["Marca"]}\n'
                          f'{c.bwhite}[Modelo]: {c.cyan}{fipe_entry["Modelo"]}\n'
                          f'{c.bwhite}[Ano Modelo]: {c.cyan}{fipe_entry["AnoModelo"]}\n'
                          f'{c.bwhite}[Combustível]: {c.cyan}{fipe_entry["Combustivel"]}\n'
                          f'{c.bwhite}[Código Fipe]: {c.cyan}{fipe_entry["CodigoFipe"]}\n'
                          f'{c.bwhite}[Mês Referência]: {c.cyan}{fipe_entry["MesReferencia"]}\n'
                          f'{c.bwhite}[Autenticação]: {c.cyan}{fipe_entry["Autenticacao"]}\n'
                          f'{c.bwhite}[Tipo Veículo]: {c.cyan}{fipe_entry["TipoVeiculo"]}\n'
                          f'{c.bwhite}[Sigla Combustível]: {c.cyan}{fipe_entry["SiglaCombustivel"]}\n'
                          f'{c.bwhite}[Data Consulta]: {c.cyan}{fipe_entry["DataConsulta"]}\n'
                          f'{c.bwhite}[IPVA]: {c.cyan}{fipe_entry["ipva"]}\n{c.white}{"─"*47}')   
            input(f'{c.white}\n[ENTER] para voltar ao menu.')
        else:
            print(f'''\n[{c.red}!{c.white}] {c.red}Placa inválida.{c.white}\n''')
            input('[ENTER] para voltar ao menu.')
    except:
        print(f'''\n[{c.red}!{c.white}] {c.red}Placa inválida.{c.white}\n''')
        input('[ENTER] para voltar ao menu.')
def cep_viacep():
        os.system("clear")
        print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
        cep2=input(f'{c.white}- >>>{c.yellow}[{c.white} Fonte Viacep {c.yellow}]{c.white} \n CEP >> ')
        pattern = re.compile(r'\s+')    
        cep2 = re.sub(pattern, '', cep2)
        try:
            url2='https://viacep.com.br/ws/{}/json/'.format(cep2)
            res2 = requests.get(url2);req2=res2.json()
            resl2="\n{}{}\n{}[Cep]: {}{}\n{}[Logradouro]: {}{}\n{}[Complemento]: {}{}\n{}[Bairro]: {}{}\n{}[Localidade]: {}{}\n{}[Uf]: {}{}\n{}[Ibge]: {}{}\n{}{}".format(c.white,'─'*47,c.bwhite,c.cyan, req2['cep'],c.bwhite,c.cyan,req2['logradouro'],c.bwhite,c.cyan,req2['complemento'],c.bwhite,c.cyan,req2['bairro'],c.bwhite,c.cyan,req2['localidade'],c.bwhite,c.cyan,req2['uf'],c.bwhite,c.cyan,req2['ibge'],c.white,'─'*47)        
            print(resl2)
            input('[ENTER] para voltar ao menu.')
        except:
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
            resl3="\n{}{}\n{}[Status]: {}{}\n{}[Ok]: {}{}\n{}[Código]: {}{}\n{}[Estado]: {}{}\n{}[Cidade]: {}{}\n{}[Distrito]: {}{}\n{}[Endereço]: {}{}\n{}[StatusText]: {}{} {}\n{}".format(c.white,'─'*47,c.bwhite,c.cyan,req3['status'],c.bwhite,c.cyan,req3['ok'],c.bwhite,c.cyan,req3['code'],c.bwhite,c.cyan,req3['state'],c.bwhite,c.cyan,req3['city'],c.bwhite,c.cyan,req3['district'],c.bwhite,c.cyan,req3['address'],c.bwhite,c.cyan,req3['statusText'],c.white,'─'*47)
            print(resl3)
            input('[ENTER] para voltar ao menu.')
        except:
          print(f'''\n[{c.red}!{c.white}] {c.red}CEP inválido.{c.white}\n''')
          input('[ENTER] para voltar ao menu.')
def cnpj():
    print('Formato: XXXXXXXXXXXXXX')
    cpnj1=input(f'{c.white}- >>>{c.yellow}[ {c.white}Fonte: Receita Federal {c.yellow}]{c.white} \n CNPJ >> ')
    try:
      url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
      res=requests.get(url1);req1=res.json()
      br="{}\n{}\n{}[Data situação]: {}{}\n{}[Motivo situação]: {}{}\n{}[Complemento]: {}{}\n{}[Tipo]: {}{}\n{}[Nome]: {}{}\n{}[Telefone]: {}{}\n{}[Situação]: {}{}\n{}[Bairro]: {}{}\n{}[Logradouro]: {}{}\n{}[Número]: {}{}\n{}[Cep]: {}{}\n{}[Municipio]: {}{}\n{}[Fantasia]: {}{}\n{}[Porte]: {}{}\n{}[Abertura]: {}{}\n{}[Natureza juridica]: {}{}\n{}[Uf]: {}{}\n{}[Cnpj]: {}{}\n{}[Ultima atualização]: {}{}\n{}[Status]: {}{}\n{}[Email]: {}{}\n{}[Efr]: {}{}\n{}[Situação especial]: {}{}\n{}[Data situação especial]: {}{}{}".format(c.white,'─'*47,c.bwhite,c.cyan,req1['data_situacao'],c.bwhite,c.cyan,req1['motivo_situacao'],c.bwhite,c.cyan,req1['complemento'],c.bwhite,c.cyan,req1['tipo'],c.bwhite,c.cyan,req1['nome'],c.bwhite,c.cyan,req1['telefone'],c.bwhite,c.cyan,req1['situacao'],c.bwhite,c.cyan,req1['bairro'],c.bwhite,c.cyan,req1['logradouro'],c.bwhite,c.cyan,req1['numero'],c.bwhite,c.cyan,req1['cep'],c.bwhite,c.cyan,req1['municipio'],c.bwhite,c.cyan,req1['fantasia'],c.bwhite,c.cyan,req1['porte'],c.bwhite,c.cyan,req1['abertura'],c.bwhite,c.cyan,req1['natureza_juridica'],c.bwhite,c.cyan,req1['uf'],c.bwhite,c.cyan,req1['cnpj'],c.bwhite,c.cyan,req1['ultima_atualizacao'],c.bwhite,c.cyan,req1['status'],c.bwhite,c.cyan,req1['email'],c.bwhite,c.cyan,req1['efr'],c.bwhite,c.cyan,req1['situacao_especial'],c.bwhite,c.cyan,req1['data_situacao_especial'],c.white)
      print(br)
      print(f'''{c.white}─''' * 47)
      input('[ENTER] para voltar ao menu.')
    except:
      print(f'''\n[{c.red}!{c.white}] {c.red}CNPJ inválido.{c.white}\n''')
      input('[ENTER] para voltar ao menu.')
def ip():
      ip2=input(f'{c.white}- >>>{c.yellow}[ {c.white}Fonte IP {c.yellow}]{c.white} \n Ip >> ')
      if ip2 == '':
        print(f'''\n[{c.red}!{c.white}] {c.red}IP inválido.{c.white}\n''')
        input('[ENTER] para voltar ao menu.')
      else:
        try:
        
          url2='http://ip-api.com/json/{}'.format(ip2)
          res2 = requests.get(url2)
          req1=res2.json()
          br2="\n{}{}\n{}[Status]: {}{}\n{}[País]: {}{}\n{}[Código do país]: {}{}\n{}[Região]: {}{}\n{}[Nome da região]: {}{}\n{}[Cidade]: {}{}\n{}[Zip]: {}{}\n{}[Lat]: {}{}\n{}[Lon]: {}{}\n{}[Fuso horário]: {}{}\n{}[Isp]: {}{}\n{}[Org]: {}{}\n{}[As]: {}{} {}{}\033[m\n{}".format(c.white,'─'*47,c.bwhite,c.cyan,req1['status'],c.bwhite,c.cyan,req1['country'],c.bwhite,c.cyan,req1['countryCode'],c.bwhite,c.cyan,req1['region'],c.bwhite,c.cyan,req1['regionName'],c.bwhite,c.cyan,req1['city'],c.bwhite,c.cyan,req1['zip'],c.bwhite,c.cyan,req1['lat'],c.bwhite,c.cyan,req1['lon'],c.bwhite,c.cyan,req1['timezone'],c.bwhite,c.cyan,req1['isp'],c.bwhite,c.cyan,req1['org'],c.bwhite,c.cyan,req1['as'],req1['query'],c.white,'─'*47)
          print(br2)
          input('[ENTER] para voltar ao menu.')
        except:
          print(f'''\n[{c.red}!{c.white}] {c.red}IP inválido.{c.white}\n''')
          input('[ENTER] para voltar ao menu.')
def ipg():
      ip1=input(f'- >>>{c.yellow}[{c.white} Fonte Ipgeolocation {c.yellow}]{c.white} \n Ip >> ')
      if ip1 == '':
        print(f'''\n[{c.red}!{c.white}] {c.red}IP inválido.{c.white}\n''')
        input('[ENTER] para voltar ao menu.')
      else:
        try:
          url1 = "https://api.ipgeolocation.io/ipgeo?apiKey=9313e7887bad45cea6d4b5845f085464&ip={}".format(ip1)
          res = requests.get(url1)
          req=res.json()
          br="\n{}{}\n{}[Ip]: {}{}\n{}[Código do continente]: {}{}\n{}[Nome do continente]: {}{}\n{}[Código do país 2]: {}{}\n{}[Código do país 3]: {}{}\n{}[Nome do país]: {}{}\n{}[Capital do país]: {}{}\n{}[Prov do estado]: {}{}\n{}[Distrito]: {}{}\n{}[Cidade]: {}{}\n{}[CEP]: {}{}\n{}[Latitude]: {}{}\n{}[Longitude]: {}{}\n{}[Is_eu]: {}{}\n{}[Código de chamada]: {}{}\n{}[País tld]: {}{}\n{}[Languages]: {}{}{}{}".format(c.white,'─'*47,c.bwhite,c.cyan,req['ip'],c.bwhite,c.cyan,req['continent_code'],c.bwhite,c.cyan,req['continent_name'],c.bwhite,c.cyan,req['country_code2'],c.bwhite,c.cyan,req['country_code3'],c.bwhite,c.cyan,req['country_name'],c.bwhite,c.cyan,req['country_capital'],c.bwhite,c.cyan,req['state_prov'],c.bwhite,c.cyan,req['district'],c.bwhite,c.cyan,req['city'],c.bwhite,c.cyan,req['zipcode'],c.bwhite,c.cyan,req['latitude'],c.bwhite,c.cyan,req['longitude'],c.bwhite,c.cyan,req['is_eu'],c.bwhite,c.cyan,req['calling_code'],c.bwhite,c.cyan,req['country_tld'],c.bwhite,c.cyan,req['languages'],req['country_flag'],req['geoname_id'])
          print(br)
          print(f'''{c.white}─''' * 47)
          input('[ENTER] para voltar ao menu.')
        except:
          print(f'''\n[{c.red}!{c.white}] {c.red}IP inválido.{c.white}\n''')
          input('[ENTER] para voltar ao menu.')
def numer():
  print(f'Formato: +XXXXXXXXXXXXX\n- >>>{c.yellow}[{c.white} Fonte: Phonenumbers {c.yellow}]{c.white}')
  numero = input(" Número >> ")
  if len(numero)!=14:
    print(f'''\n[{c.red}!{c.white}] {c.red}Número inválido.{c.white}\n''')
    input('[ENTER] para voltar ao menu.')
  else:
    try:
      parsing = parse(numero)
      loc = geocoder.description_for_number(parsing,"id")
      isp = carrier.name_for_number(parsing,"id")
      tz = timezone.time_zones_for_number(parsing) 
      print(f"{'─'*47}\n{c.bwhite}[Info]: {c.cyan}{parsing}\n{c.bwhite}[Formato Nacional]: {c.cyan}{phn.national_significant_number(parsing)}\n{c.bwhite}[Formato Internacional]: {c.cyan}{phn.normalize_digits_only(parsing)}\n{c.bwhite}[Pode ser contatado internacionalmente ?]: {c.cyan}{phn.can_be_internationally_dialled(parsing)}\n{c.bwhite}[Localização]: {c.cyan}{loc}\n{c.bwhite}[Código de área]: {c.cyan}{phn.region_code_for_number(parsing)}\n{c.bwhite}[Operadora original do número]: {c.cyan}{isp}\n{c.bwhite}[Fuso Horário]: {c.cyan}{tz}\n{c.white}{'─'*47}")
      input('[ENTER] para voltar ao menu.')
    except:
      print(f'''\n[{c.red}!{c.white}] {c.red}Número inválido.{c.white}\n''')
      input('[ENTER] para voltar ao menu.')

def CT():
  os.system('clear')
  print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
  print(f'{c.white}- >>>{c.yellow}[{c.white} Fonte: Token {c.yellow}]{c.white}')
  token=input(' Token >> ')
  head = {'Authorization': str(token)}
  src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
  if src.status_code != 200:
    print(f'''\n[{c.red}!{c.white}] {c.red}Token inválido.{c.white}''')
    input('\n[ENTER] para voltar ao menu.')
  else:
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    if r.status_code == 200:
       os.system('clear')
       print(Colorate.Vertical(Colors.blue_to_green, banners.banner1))
       print('\n[💉] Hackeado com sucesso !')
       def get_server_names(token):
         headers = {'Authorization': token, 'Content-Type': 'application/json'}
         response = requests.get('https://discord.com/api/v10/users/@me/guilds', headers=headers)

         server_names = [server['name'] for server in response.json()] if response.status_code == 200 else []


         return server_names
       name_servers=get_server_names(token)
       def get_friend_names(token):
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        response = requests.get('https://discord.com/api/v10/users/@me/relationships', headers=headers)

        friend_names = [friend['user']['username'] for friend in response.json() if 'user' in friend] if response.status_code == 200 else []

        return friend_names
       friend_names = get_friend_names(token)
       def get_badges(flags):
         badge_flags = {
      1: "Staff",
      2: "Partner",
      4: "Hypesquad Events",
      8: "Bug Hunter Level 1",
      16: "House Bravery",
      32: "House Brilliance",
      64: "House Balance",
      128: "Early Supporter",
      256: "Team User",
      512: "System",
      1024: "Bug Hunter Level 2",
      4096: "Verified Bot",
      16384: "Early Verified Bot Developer",
      65536: "Discord Certified Moderator"
  }
         badges = [badge_flags[flag] for flag in badge_flags if flag & flags]
         return ', '.join(badges) if badges else "Sem flags"
       linguagens = {
  'da'    : 'Dinamarquês, Dinamarca',
  'de'    : 'Alemão, Alemanha',
  'en-GB' : 'Inglês, Reino Unido',
  'en-US' : 'Inglês, Estados Unidos',
  'es-ES' : 'Espanhol, Espanha',
  'fr'    : 'Francês, França',
  'hr'    : 'Croata, Croácia',
  'lt'    : 'Lituano, Lituânia',
  'hu'    : 'Húngaro, Hungria',
  'nl'    : 'Holandês, Holanda',
  'no'    : 'Norueguês, Noruega',
  'pl'    : 'Polonês, Polônia',
  'pt-BR' : 'Português Brasil, Brasil',
  'ro'    : 'Romeno, Romênia',
  'fi'    : 'Finlandês, Finlândia',
  'sv-SE' : 'Sueco, Suécia',
  'vi'    : 'Vietnamita, Virtna',
  'tr'    : 'Turco, Turquia',
  'cs'    : 'Tcheco, República Tcheca',
  'el'    : 'Grego, Grécia',
  'bg'    : 'Búlgaro, Bulgária',
  'ru'    : 'Russo, Russia',
  'uk'    : 'Ucraniano, Ucrânia',
  'th'    : 'Tailandês, Tailândia',
  'zh-CN' : 'Chinês, China',
  'ja'    : 'Japonês, Japão',
  'zh-TW' : 'Chinês, Taiwan',
  'ko'    : 'Coreano, Coreia'
           }
       friend_names_text = '\n'.join(friend_names) if friend_names else '  [cyan]Nenhum amigo encontrado.[white]'
       server_names_text = '\n'.join(name_servers) if name_servers else '  [cyan]Nenhum servidor encontrado.[white]'
       userName = r.json()['username'] + '#' + r.json()['discriminator']
       userID = r.json()['id']
       name = r.json()['global_name']
       vatar = r.json()['avatar']
       avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{vatar}.webp'
       accent_color = r.json()['accent_color']
       phone = r.json()['phone']
       email = r.json()['email']
       mfa = r.json()['mfa_enabled']
       flags = r.json()['flags']
       verem = r.json()['verified']
       locale = r.json()['locale']
       pl = linguagens.get(locale)
       badges = get_badges(flags)
       nitro = r.json()['premium_type']
       Cdate = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d/%m/%Y %H:%M:%S UTC')
       print(f'\n[🧪] Token: {token}\n')
       if mfa==True:
        mfa='Sim'
       else:
         mfa='Não'
       if verem==True:
         verem='Sim'
       else:
         verem='Não'
       if nitro==1:
         nitro='Nitro Classic'
       elif nitro==2:
          nitro='Nitro'
       elif nitro==3:
         nitro='Nitro Basic'
       else:
         nitro='Sem nitro'
       if vatar==None:
         avatar_url='Sem foto de perfil (ícone padrão do Discord)'
       console.print(Panel.fit(f'''
<<───────────Info básicas 🧾───────────>>

[blue]ID do usuário :[white] {userID}

[blue]Nome de usuário :[white] {userName}
[blue]Nome exebido :[white] {name}

[blue]Ícone do perfil :[white] {avatar_url}

[blue]Entrou no discord em :[white] {Cdate}

[blue]Língua :[white] {locale} ({pl})

[blue]Cor do banner :[white] {'(HEX) '+str(accent_color) if accent_color else "Automático"}

[blue]↓ Amigos ↓[white]

{friend_names_text}

[blue]↓ Servidores que o usuário participa ↓[white]

{server_names_text}


<<──────────────Nitro 🚀──────────────>>

[blue]Nitro :[white] {nitro}

<<────────────Seguraça 🔐────────────>>

[blue]Possui verificação de 2 fatores ? :[white] {mfa}

[blue]O email é verificado pelo discord ? :[white] {verem}

 <<──────────Flags ⛳───────────>>

[blue]Flags : [white]{badges}

 <<────────────Contato 📫────────────>>

[blue]Email :[white] {email}

[blue]Número de telefone :[white] {phone if phone else "[cyan]Não registrado[white]"}

''', title='🛰️'))
       input('\n[ENTER] para voltar ao menu.')
