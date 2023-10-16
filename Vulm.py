import os, sys, cores as c, banners, uteis
from pystyle import Colorate, Colors
try:
  uteis.wifi()
  os.system('clear')
  print(banners.banner3)
  banners.Carreg()
  while True:
    os.system('clear')
    print(Colorate.Vertical(Colors.blue_to_green, banners.banner1))
    print(
      f'{c.rblue}Creatd By: Phant0m The Great{c.white}\n{c.rblue}Version: {uteis.Versão}{c.white}\n'
    )
    print('─' * 54)
    print(banners.opc)
    esc = input(f'''[{c.bwhite}?{c.white}] Digite a sua escolha: ''')
    if esc == '01' or esc == '1':
      os.system("clear")
      print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
      print(f'''{c.bwhite}({c.white}[ENTER] para voltar ao menu{c.bwhite})''')
      print('Formato: XXXXXXXX')
      n1 = str(
        input(
          f'>>> {c.blue}[CONSULTA CEP] {c.white}- Escolha a ferramenta{c.white}\n\n- {c.blue}[{c.white}1{c.blue}]{c.white} Apicep\n- {c.blue}[{c.white}2{c.blue}]{c.white} Viacep  \n- {c.bwhite}>{c.white} '
        ))
      if n1 == '2' or n1 == '02':
        uteis.cep_viacep()
      elif n1 == '1' or n1 == '01':
        uteis.cep_apicep()
    elif esc == '02' or esc == '2':
      os.system("clear")
      print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
      uteis.cnpj()
    elif esc == '03' or esc == '3':
      os.system("clear")
      print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
      print(f'''{c.bred}({c.white}[ENTER] para voltar ao menu{c.bred})''')
      n1 = str(
        input(
          f'{c.white}>>>{c.blue} [CONSULTA IP]{c.white} - Escolha a ferramenta\n\n- {c.blue}[{c.white}01{c.blue}]{c.white} Ip\n- {c.blue}[{c.white}02{c.blue}]{c.white} Ipgeolocation  \n- {c.yellow}>{c.white} '
        ))
      if n1 == '1' or n1 == '01':
        os.system('clear')
        print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
        uteis.ip()
      elif n1 == '2' or n1 == '02':
        os.system('clear')
        print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
        uteis.ipg()
    elif esc == '04' or esc == '4':
      os.system('clear')
      print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
      uteis.numer()
    elif esc == '05' or esc =='5':
      os.system('clear')
      print(Colorate.Vertical(Colors.blue_to_green, banners.banner2))
      uteis.placa_fipeplaca()
    elif esc == '06' or esc == '6':
      os.system("clear")
      print(Colorate.Vertical(Colors.blue_to_green, banners.banner1))
      print(
        f'{c.rblue}Creatd By: Phant0m The Great{c.white}\n{c.rblue}Version: 3.0{c.white}\n'
      )
      print('─' * 54)
      print(
        f'\n{c.bcyan}Sobre{c.white}: Vulm, é uma ferramenta com o objetivo de otimizar o processo de coleta de informações.\n\n[{c.bwhite}©{c.white}] → Ferramenta criada por: Phant0m The Great\n\n[{c.bblue}©d{c.white}] → Discord do criador: phant0mthegreat\n\n[{c.green}V{c.white}] Versão: {uteis.Versão}\n\n[{c.bred}☠{c.white}] → Bugs: Caso encontre algum bug na ferramenta, entre em contato com o criador para reportar o bug.\n'
      )
      input(f"""[ENTER] Para voltar ao menu.""")
    elif esc == 'S' or esc == 's':
      os.system("clear")
      print(Colorate.Vertical(Colors.blue_to_green, banners.banner4))
      print('')
      print(f'''[{c.bcyan}#{c.white}] Até a próxima !''')
      sys.exit()
except KeyboardInterrupt:
  print(f'\n[{c.bcyan}#{c.white}] O programa foi interrompido.')
        
