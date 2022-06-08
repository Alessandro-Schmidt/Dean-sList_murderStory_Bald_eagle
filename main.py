""" Neste código existem bibliotecas que precisam ser instaladas no python. São elas a pyfiglet e a tabulate. Sugerimos baixar na máquina com os comandos pip ou rodar este código no Replit. 
Você pode fazer a inserção dessas bibliotecas no visual studio code como mostra nesse vídeo: 
https://www.youtube.com/watch?v=-Wvt7lWxzf4
trilha sonora recomendada: https://www.youtube.com/watch?v=UCAtGFQ4uLE&t=2046s """


import pyfiglet
from tabulate import tabulate
import time
import dialogos
titulo = pyfiglet.figlet_format('DEANS LIST', font='banner3-D')
sub_title = pyfiglet.figlet_format('Um misterio de ASSASSINATO', font='standard')
edition = pyfiglet.figlet_format('Bald Eagle Edition', font='digital')
print("\n\n")
time.sleep(3)
print(titulo)
time.sleep(3)
print(sub_title)
time.sleep(3)
print(edition)

# início da história
print('--- Contexto ---\nNo auge da Guerra Fria, uma semana após a crise dos mísseis de Cuba e início do bloqueio continental, a América Latina vive um momento de tensão sem igual.\n\nNa PUCPR não é diferente.\n\nEspiões andam disfarçados entres os alunos, com o objetivo de roubar o tão desejado elixir. Ninguém sabe o que é o elixir, só se sabe que URSS e EUA estão buscando ferozmente\n\nO prédio da Escola Politécnica é o mais vigiado do Paraná. Não é permitida a entrada de pessoas não autorizadas nas aulas de BES, BCC ou BSI.\n\nO assassinato do decâno veio como um choque para os estudantes, e está sendo abafado pela mídia e pela Universidade.\n\nVocê foi designado pelo Governo Federal para solucionar o mistério. A justiça está nas suas mãos. Descubra o autor do crime, o local do crime e a arma do crime. SEJA RÁPIDO! O responsável pode estar fugindo.\n\n')
#time.sleep(15)
print('-'*len('Vítima: Marco Paludo, decâno da Escola Politécnica'))
print('RELATÓRIO DA INVESTIGAÇÃO\nData do crime: 20/10/1962\nVítima: Marco Paludo, decâno da Escola Politécnica.\nLocal: Sigiloso.\nArma: Sigiloso.\nAutor do crime: em investigação.')
print('-'*len('Vítima: Marco Paludo, decâno da Escola Politécnica'))
#time.sleep(7)
print('\n\n-- HIPÓTESES --\n\n')
print('LOCAL -- \n\na) O assassinato foi um local aberto, mas não há testemunhas\n\nb) Foram encontrados documentos queimados do Decâno em um dos lixos da PUCPR.\n\nc) Ela fazia encontros semanais com a CIA e a KGB para acalmar os ânimos, sempre em lugares secretos\n\nd) A CIA fechou o câmpus, em especial o bloco amarelo.\n\n')
print('ARMA --\n\na) Uma fita cassete pequena foi encontrada junto aos documentos no lixo. Nesta fita, haviam instruções de como fugir do país.\n\nb) O General da CIA dentro da PUCPR possui uma arma no seu escritório\n\nc) Espiões da KGB usam armas pouco convencionais para evitar suspeitas.\n\nd) Aquilo que constrói, também destrói.\n\ne) Todos os computadores da PUCPR foram desligados no momento do assassinato.\n\n')
print('SUSPEITO --\n\na) Se sabe da existência de no mínimo uma espiã da KGB na Universidade.\n\nb) Não era do interesse Sovitético, a morte do Decâno.\n\nc) O assassino não era neutro.\n\nd) É conhecido o envolvimento de pelo menos um dos alunos de BCC com a KGB.\n\ne) Quem cometeu o crime, estava acompanhado de alguém do sexo oposto.\n\nf) Alguém de fora do círculo comum, é provavelmente um agente duplo')
print('\n\nFATOS IMPORTANTES\n\nf) Você investigar alguém pode causar a sua morte.\n\ng) Cuidado com pistas falsas...\n\nh) A seguência com que investiga os personagens pode mudar as dicas que recebe!\n\ni) Você pode investigar alguns personagens novamente depois de outras revelação!\n\nBOA SORTE!')
lados = [['Nome:', 'Lado:', 'Pistas:'], ['Fernando', '?', ''], ['Alessandro', '?', ''], ['Vilmar', 'General da CIA dentro da PUC', ''], ['Professora Rafaela', 'Espiã da CIA', ''], ['Stephany Ferrão', '?', ''], ['Julien', 'Espião da CIA', '']]
#time.sleep(20)
while True:
  print(tabulate(lados,headers='firstrow', tablefmt='grid'))
  result_set = [False,False, False]
  tool = False
  while True: 
    nomes = [['Código', 'Nome', 'Código', 'Nome'],['1', 'Fernando', '2', 'Alessandro'], ['3', 'Vilmar', '4', 'Professora Rafaela'],['5','Stephany Ferrão', '6', 'Julien']]
    armas = [['Código', 'Arma'], ['1', 'Estrangulamento'], ['2', 'Martelo'], ['3','Porrada'], ['4','Compasso'], ['5', 'Machado'], ['6', 'Veneno']]
    locais = [['Código','Locais suspeitos'], ['1','Sala dos monitores'], ['2', 'Biblioteca'], ['3', 'Sala secreta da CIA'], ['4', 'Ponte Escola\nPolitécnica'],['5', 'Campo de bocha da PUCPR'], ['6', 'Havana']]
    escolhas_possiveis = [['Número da ação','Ação'], ['1','Investigar'], ['2', 'Acusar'], ['3', 'Consultar pistas']]
    print(tabulate(escolhas_possiveis, headers='firstrow', tablefmt='grid'))
    option = str(input('Digite sua escolha: ')).upper()
    if option =='3' or option in 'CONSULTAR':
      print('+'+'-'*90+'+')
      print('+--SUSPEITOS--+')
      print(tabulate(nomes,headers='firstrow', tablefmt='grid'))
      print(tabulate(armas,headers='firstrow', tablefmt='grid'))
      print(tabulate(locais,headers='firstrow', tablefmt='grid'))
      print('+'+'-'*90+'+')
      break
    elif option == '1' or option == 'INVESTIGAR':
      print('-'*len('INVESTIGAÇÃO')+'\nINVESTIGAÇÃO\n'+'-'*len('INVESTIGAÇÃO'))
      print(tabulate(lados,headers='firstrow', tablefmt='grid'))
      print(tabulate(nomes, headers='firstrow', tablefmt='grid'))
      while True:
        morte_em_acao = False
        try: 
          p = int(input('Digite o número de quem deseja investigar: '))
          if p not in range(1,7):
            print('\033[31m\nDigite apenas opções válidas\n\033[m')
          else:
            break
        except:
          print('\033[31m\nDigite apenas opções válidas\n\033[m')
      if p == 1:
        tool = True
        print('\n\nVocê chega para investigar Fernando...\n\n')
        time.sleep(1.5)
        print('Ele olha para os dois lados, e quando descobre suas intenções, pede que aja naturalmente, enquanto põe uma arma na sua cintura.')
        time.sleep(2)
        print("Ele manda você andar até a sala dos monitores. Chegando lá. Ele lhe entrega uma chave de ponta triangular. E diz para você não se desfazer dela")
        time.sleep(2)
        print('FERNANDO: "Não confie em ninguém. É apenas isso que me permitiram dizer."')
        lados[1][2] = 'Chave de ponta triangular'
      elif p == 2: 
          print('\nAlessadro:')
          time.sleep(2) 
          print('Ele é difícil de desembuchar, provavelmente recebeu treinamento para isso\n\nA única coisa que diz: "Me proibiram de falar sobre esse tema... Se disser algo, corro sério risco de vida. O que posso dizer, o crime foi feito em duas pessoas, uma delas, quem realmente matou, fiquei sabendo que descobriu o que era o tal do "Elixir", por isso matou o Paludo."')
          lados[2][2] ='"Estavam em dois."\n matou por causa do elixir(?)'    
          lados[2][1] ="(Espião da CIA) v (Espião da KGB)"
          time.sleep(10)  
      elif p == 3:
            if tool==True:
              print('VILMAR: Eu não auxiliaria você regularmente. Mas você possui a chave de formato triangular que nos faltava... Nesta caixa aqui, que foi roubada da KGB, mas recuperada, há o que eles sabem do caso...')
              print("VILMAR: Veja só o que encontramos!\nUm bilhete escrito: 'Tudo o que o Julien lhe disse, é mentira.'\nUm machado cheio de sangue...? Pra que será que foi usado?")
              lados[3][2] = 'Tudo que o Julian disser é mentira.\nMachado ensanguentado.'
              lados[6][2] = '~'
              time.sleep(5)
            else: 
              print('Não consegue me ajudar. As informações do caso estão nesta caixa super protegida... Apenas uma chave com a ponta triangular é capaz de abrir a caixa. Investigue mais pessoas até achar a chave.')
              time.sleep(4)            
      elif p == 4:
            print('Professora Rafaela.')
            print('Com muita pressa, a professora olha nos seus olhos atordoada e diz: ')
            time.sleep(2)           
            print('RAFAELA: "Vou te dizer tudo que eu sei ok? Fernando é um espião da CIA, ele e o Julien trabalham pra mim. Mas vê se para de se preocupar com isso! Acho que nem tudo que vemos é assassinato, pode ter sido um acidente."')
            print('RAFAELA: Confesso que me decepcionei com ele.')
            time.sleep(9)
            lados[4][2] = 'Dispersou o assunto\n "Acidente"?'
            lados[1][1] = 'Espião da CIA'
            lados[6][1] = 'Espião da CIA'
      elif p ==5:
        morte_em_acao = True
        print('Stephany Ferrão...')
        print('STEPHANY: Por que quer tanto investigar esse caso?')
        time.sleep(2)
        print('Tirando da bolsa um compasso sujo e encostando em seu pescoço, ela revela sua identidade. Uma genuina espiã da KGB.\nEla lhe leva até a sala secreta, junto com outros espiões.')
        time.sleep(5)
        print('Chegando lá, você reconhece um rosto. Julien. Uma surpresa para todos.')
        time.sleep(3)
        print('STEPHANY: Se eliminarmos você assim, vai ficar muito suspeito. Vamos ajudar na investigação, afinal, também queremos a cabeça de quem fez isso. Nós queríamos apenas sequestrar e torturar o decâno por informações sobre o tal do Elixir, nunca matar ele. Somos pessoas civilizadas. Agora, o único que sabia o que era se foi.')
        time.sleep(7)
        print('A última vez que vimos o Decâno foi enquanto espionávamos ele durante o jogo de bocha. Vimos ele sair apressado... Provavelmente enfurecido')
        time.sleep(7)
        print('JULIEN: "Os maiores interessados na morte do Decâno eram aqueles que foram aqueles que ganhariam com a descoberta do elixir"')
        print('')
        lados[5][1] = 'Espiã da KGB'
        lados[5][2] = 'Brabo na bocha?'
        lados[6][1] += '^ (Espião KGB)'    
      elif p == 6:
        if morte_em_acao == False: 
          print('Julien...')
          print('JULIEN: O paludo sofria com alcoolismo. Passava o dia todo bebendo Skol no Havana.')
          print('JULIEN: "O decâno foi morto durante um jogo de bocha."\nJULIEN: "Sei também que o assassino foi com a intenção de matar"')
          time.sleep(3)
          lados[6][2] = '(Morto na Bocha) ^ (Intenção de matar) ^ (Skol no Havana)?'
        else: 
          lados[6][1] = 'Morto durante a operação.'
          print('Você chega para investigar Julien...')
          time.sleep(2)
          print('Ao chegar perto da sala secreta da CIA, você percebe um certo tumulto... Alguns gritos, e depois silêncio.')
          time.sleep(2)
          print('Você escuta Vilmar, coordenador de BCC, falando com alguém... Stephany Ferrão, espiã da KGB... QUE CONFUSÃO!\n')
          time.sleep(3)
          print('VILMAR: Você eu treinei pra ser dupla espiã. O Julian não. Ninguém mente para mim e fica impune!')
          time.sleep(4)
          print('STEPHANY: Então quer que vá atrás do responsável do assassinato da Decânca?')
          time.sleep(3)
          print('VILMAR: Ele já deve estar fugindo do país nessa altura do campeonato... ou se escondido em uma montanha! Sei lá!')
          time.sleep(2)
          print('VILMAR: Teve notícias da Rafaela? Desde que ofereci a recompensa caso ela descobrisse o que era o Elixir, ela sumiu e nunca mais deu notícia...')
          time.sleep(61)
          print('\nVocê não entende muita coisa, escutando através da janela da sala, você se levanta e tenta ver o que está acontecendo... A conversa entre Stephany e Vilmar acontece sobre o corpo gelado de Julien. O seu envolvimento não supervisionado com a KGB não foi perdoado...')
          time.sleep(9)
          print('A causa da morte? Deram uma machadada no bingolin dele! Que crueldade!')
          time.sleep(2)
          print('Você anota tudo, e sai de fininho para não ser pego.')
          time.sleep(4)
          lados[6][2] = 'Assassina nas montanhas...\n(Saber O que é o elixir -> $$$)'
          lados[5][1] = '(Espiã da CIA)'
    elif option == '2' or option == 'ACUSAR':
      print(tabulate(nomes, headers='firstrow', tablefmt='grid'))
      opt_1 = str(input('\nDigite o código ou o nome de quem deseja acusar: ')).upper()
      time.sleep(1)
      if opt_1 == '4' or opt_1 in 'RAFAELA':
        result_set[0] =True
      else: 
          result_set[0] = False
      print(tabulate(armas,headers='firstrow', tablefmt='grid'))
      opt_2 = str(input('\nDigite o código ou o nome da arma que cometeu o crime: ')).upper()
      if opt_2 == '3' or opt_2 in 'PORRADA':
          result_set[1] = True
      else: 
          result_set[1] = False
      print(tabulate(locais,headers='firstrow', tablefmt='grid'))
      opt_3 = str(input('Digite o local onde acha que ocorreu o assassinato: ')).upper()
      if opt_3 == '6' or opt_3 in 'HAVANA':
          result_set[2]=True
      else: 
          result_set[2] = False
      while True:   
          print('Analisando suas escolhas...')
          time.sleep(3)
          if  (result_set[0] and result_set[1] and result_set[2]) == True:
              sub_ = pyfiglet.figlet_format('CONSEGUIU! VINGOU A MORTE DO DECÂNO!', font='standard')
              print(sub_)
              dialogos.dialogo_final()
              break
          else:
              print(f'\nSua investigação é falha. Corra antes que o tempo acabe.\nVocê sabe {result_set.count(True)}/3 informações corretas.')
              break
      if (result_set[0] and result_set[1] and result_set[2]) == True:
          break
      