import sys, time, cores as c
def Carreg():
	l = ['|', '-', '|', '-']
	for i in l+l+l:
		sys.stdout.write('\r' + f'''Iniciando {c.bblue}Vulm{c.white}...'''+i)
		sys.stdout.flush()
		time.sleep(0.1)

banner1="""            __     __     _                
            \ \   / /   _| |_ __ ___  
             \ \ / / | | | | '_ ` _ \ 
              \ V /| |_| | | | | | | |
               \_/  \__,_|_|_| |_| |_|
                           """
opc=f"""{c.bwhite}Bem vindo(a) ao Vulm !\nescolhas as opções a seguir ↓\n\n{c.white}[{c.blue}01{c.white}]{c.white} - Consultar CEP
{c.white}[{c.blue}02{c.white}]{c.white} - Consultar CNPJ
{c.white}[{c.blue}03{c.white}]{c.white} - Consultar IP
{c.white}[{c.blue}04{c.white}]{c.white} - Consultar Número de telefone


{c.white}[{c.cyan}05{c.white}]{c.white} - Informações
{c.white}[{c.cyan}S{c.white}]{c.white} - Sair\n"""
banner2="""               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--'"""
banner3="""─────█─▄▀█──█▀▄─█─────
────▐▌──────────▐▌────
────█▌▀▄──▄▄──▄▀▐█────
───▐██──▀▀──▀▀──██▌───
──▄████▄──▐▌──▄████▄──"""
banner4="""                   | 
              .   ]#[   . 
               \_______/ 
            .    ]###[    . 
             \___________/ 
          .     ]#####[     . 
           \_______________/ 
        .      ]#######[      . 
         \___________________/ 
      .       ]#########[       . 
       \_____]##.-----.##[_____/ 
        |__|__|_|     |_|__|__| 
        |__|__|_|_____|_|__|__| 
        ########/_____\######## 
               |_______| 
"""
