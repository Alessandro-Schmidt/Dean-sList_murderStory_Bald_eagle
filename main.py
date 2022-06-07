""" Neste código existem bibliotecas que precisam ser instaladas no python. São elas a pyfiglet e a tabulate. Sugerimos baixar na máquina com os comandos pip ou rodar este código no Replit. 
Você pode fazer a inserção dessas bibliotecas no visual studio code como mostra nesse vídeo: 
https://www.youtube.com/watch?v=-Wvt7lWxzf4
trilha sonora recomendada: https://www.youtube.com/watch?v=ytw6ivAjkig&t=122s """
import pyfiglet
from tabulate import tabulate
import time
import dialogos
titulo = pyfiglet.figlet_format('DEANS LIST', font='banner3-D')
sub_title = pyfiglet.figlet_format('Um misterio de ASSASSINATO', font='standard')
print(titulo)

print(sub_title)

# início da história
print('--- Contexto ---\nNo auge da Guerra Fria, uma semana após a crise dos mísseis de Cuba e início do bloqueio continental, a América Latina vive um momento de tensão sem igual.\n\nNa PUCPR não é diferente.\n\nEspiões andam disfarçados entres os alunos, com o objetivo de roubar os postits dos requisitos do projeto da Bomba de Hidrogênio.\n\nO prédio da Escola Politécnica é o mais vigiado do Paraná. Não é permitida a entrada de pessoas não autorizadas nas aulas de BES.\n\nO assassinato da reitora veio como um choque para os estudantes, e está sendo abafado pela mídia e pela Universidade.\n\nVocê foi designado pelo Governo Federal para solucionar o mistério. A justiça está nas suas mãos. Descubra o autor do crime, o local do crime e a arma do crime. SEJA RÁPIDO! O responsável pode estar fugindo.\n\n')
print('-'*len('Vítima: Andreia Malucelli, decâna da Escola Politécnica'))
print('RELATÓRIO DA INVESTIGAÇÃO\nData do crime: 20/10/1962\nVítima: Andreia Malucelli, decâna da Escola Politécnica.\nLocal: Sigiloso.\nArma: Sigiloso.\nAutor do crime: em investigação.')
print('-'*len('Vítima: Andreia Malucelli, decâna da Escola Politécnica'))
print('\n\n-- HIPÓTESES --\n\n')
print('LOCAL -- \n\na) O assassinato em uma sala fechada, pois não há testemunhas\n\nb) Foram encontrados documentos queimados da Decâna no lixo antes da saída da PUCPR.\n\nc) Ela fazia encontros semanais com a CIA e a KGB para acalmar os ânimos, sempre em lugares secretos\n\nd) A CIA fechou o campûs, em especial o bloco amarelo.\n\n')
print('ARMA --\n\na) Uma fita cassete pequena foi encontrada junto aos documentos no lixo. Nesta fita, haviam instruções de como fugir do país.\n\nb) O General da CIA dentro da PUCPR possui uma arma no seu escritório\n\nc) Espiões da KGB usam armas pouco convencionais para evitar suspeitas.\n\nd) Aquilo que constrói, também destrói.\n\ne) Todos os computadores da PUCPR foram desligados no momento do assassinato.\n\n')
print('SUSPEITO --\n\na) Se sabe da existência de no mínimo uma espiã da KGB na Universidade.\n\nb) Não era do interesse americano, a morte da Decâna.\n\nc) O assassino não era neutro.\n\nd) É conhecido o envolvimento de pelo menos um dos monitores com a KGB.\n\ne) Quem cometeu o crime, estava acompanhado de alguém do sexo oposto.')
print('\n\nFATOS IMPORTANTES\n\nf) Você investigar alguém pode causar a sua morte.\n\ng) Cuidado com pistas falsas...\n\nh) A seguência com que investiga os personagens pode mudar as dicas que recebe!\n\ni) Você pode investigar alguns personagens novamente depois de outras revelação!\n\nBOA SORTE!')
lados = [['Nome:', 'Lado:', 'Pistas:'], ['Franklin Vieira', '?', ''], ['Alessandro', '?', ''], ['Marco Paludo', 'General da CIA dentro da PUC', ''], ['Professora Rafaela', 'Espiã da CIA', ''], ['Giulia Carvalho', '?', ''], ['Sheila Reinehr', 'Espiã da CIA', '']]

while True: 
  print(tabulate(lados,headers='firstrow', tablefmt='grid'))
  while True: 
    tool = False
    nomes = [['Código', 'Nome', 'Código', 'Nome'],['1', 'Franklin', '2', 'Alessandro'], ['3', 'Marco Paludo', '4', 'Professora Rafaela'],['5','Giulia Carvalho', '6', 'Sheila Reinehr']]
    armas = [['Código', 'Arma'], ['1', 'Estrangulamento'], ['2', 'Martelo'], ['3','Agulha'], ['4','Compasso'], ['5', 'Machado']]
    locais = [['Código','Locais suspeitos'], ['1','Sala dos monitores'], ['2', 'Biblioteca'], ['3', 'Sala secreta da CIA'], ['4', 'Ponte Escola\nPolitécnica']]
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
      print(tabulate(nomes, headers='firstrow', tablefmt='grid'))
      while True:
        try: 
          p = int(input('Digite o número de quem deseja investigar: '))
          if p not in range(1,7):
            print('\033[31m\nDigite apenas opções válidas\n\033[m')
          else:
            break
        except:
          print('\033[31m\nDigite apenas opções válidas\n\033[m')
      if p == 1:
        print('\n\nVocê chega para investigar Franklin...\n\n')
        time.sleep(1.5)
        print('Ele olha para os dois lados, e quando descobre suas intenções, pede que aja naturalmente, enquanto põe uma arma na sua cintura.')
        time.sleep(2)
        print("Ele manda você andar até a sala dos monitores. Chegando lá. Ele lhe entrega uma chave de ponta triangular. E diz para você não se desfazer dela")
        time.sleep(2)
        print('FRANKLIN: "Não confie em ninguém. É apenas isso que me permitiram dizer."')
        lados[1][2] = 'Chave de ponta triangular'
        tool = True
      elif p == 2: 
          print('\nAlessadro:')
          time.sleep(2) 
          print('Ele é difícil de desembuchar, provavelmente recebeu treinamento para isso\n\nA única coisa que diz: "Me proibiram de falar sobre esse tema... Se disser algo, corro sério risco de vida. O que posso dizer, o crime foi feito em duas pessoas, uma delas, não tinha nada haver com a PUCPR. A arma foi manual."')
          lados[2][2] ='"Estavam em dois."\nArma manual (?)'    
          lados[2][1] ="(Espião da CIA) v (Espião da KGB)"
          time.sleep(10)  
      elif p == 3:
            if tool==True:
              print('PALUDO: Eu não auxiliaria você regularmente. Mas você contém a chave de formato triangular que nos faltava... Nesta caixa aqui, que foi roubada da KGB, há o que eles sabem do caso...')
              print("PALUDO: Veja só o que encontramos!\nUm bilhete escrito: 'Tudo o que a Sheila lhe disse, é mentira.'\nUm machado cheio de sangue...? Pra que será que foi usado?")
              lados[3][2] = 'Tudo que a Sheila disser é mentira.\nMachado ensanguentado.'
              lados[6][2] = '~'
              time.sleep(5)
            else: 
              print('Não consegue me ajudar. As informações do caso estão nesta caixa super protegida... Apenas uma chave com a ponta triangular é capaz de abrir a caixa. Investigue mais pessoas até achar a chave.')
              time.sleep(4)            
      elif p == 4:
            print('Professora Rafaela.')
            print('Com muita pressa, a professora olha nos seus olhos atordoada e diz: ')
            time.sleep(2)           
            print('RAFAELA: "Vou te dizer tudo que eu sei ok? Franklin é um espião da CIA, ele e o Alessandro trabalham pra mim, infelizmente o Alessandro é Neutro. Mas vê se para de se preocupar com isso! Já aconteceu, não há mais o que eu possa fazer! Preciso ir!"')
            time.sleep(9)
            lados[4][2] = 'Dispersou o assunto,\nmuita pressa'
            lados[1][1] = 'Espião da CIA'
            lados[2][1] = 'Neutro'
      elif p ==5:
        morte_em_acao = True
        print('Giulia Carvalho...')
        print('GIULIA: Por que quer tanto investigar esse caso?')
        time.sleep(2)
        print('Tirando da bolsa um compasso e encostando em seu pescoço, ela revela sua identidade. Uma genuina espiã da KGB.\nEla lhe leva até a sala secreta, junto com outros espiões.')
        time.sleep(5)
        print('Chegando lá, você reconhece um rosto. Sheila Reinehr. Uma surpresa para todos.')
        time.sleep(3)
        print('GIULIA: Se eliminarmos você assim, vai ficar muito suspeito. Vamos ajudar na investigação, afinal, também queremos a cabeça de quem fez isso. Nós queríamos apenas sequestrar e torturar a decâna por informações sobre a bomba de Hidrogênio, nunca matar ela. Agora, a única que conhecia o projeto todo se foi.')
        time.sleep(7)
        print('A última vez que vimos a Decâna foi enquanto ela ia para a sala secreta da CIA. Achamos estranho ela ter reunião lá, todas as reuniões da Decâna com a CIA eram feitas em locais aleatórios. ')
        time.sleep(7)
        print('SHEILA: "Os maiores interessados na morte da Decâna eram aqueles que foram preteridos na mudança de gerência "')
        print('')
        lados[5][1] = 'Espiã da KGB'
        lados[6][1] += '^ (Espiã KGB)'    
      elif p == 6:
        if morte_em_acao == False: 
          print('Sheila Reinehr...')
          print('SHEILA: "O assassinato foi cometido por uma pessoa solteira."\nSHEILA: "Eu não sei muito sobre o caso, mas sei que foi cometido ao ar livre e em um local público!"')
          lados[6][2] = '(Assassino solteiro)'
        else: 
          lados[6][1] = 'Morta durante a operação.'
          print('Você chega para investigar Sheila Reinehr...')
          time.sleep(2)
          print('Ao chegar perto da sala secreta da CIA, você percebe um certo tumulto... Alguns gritos, e depois silêncio.')
          time.sleep(2)
          print('Você escuta Marco Paludo falando com alguém... Giulia Carvalho, espiã da KGB... QUE CONFUSÃO!\n')
          time.sleep(3)
          print('PALUDO: Você eu treinei pra ser dupla espiã. A Sheila não. Ninguém mente para a Águia Careca e fica impune!')
          time.sleep(4)
          print('GIULIA: Então quer que vá atrás da responsável do assassinato da Decânca?')
          time.sleep(3)
          print('PALUDO: Ela já está fugindo do país nessa altura do campeonato... ou se escondido em uma montanha! Sei lá!')
          time.sleep(3)
          print('Você não entende muita coisa, escutando através da janela da sala, você se levanta e tenta ver o que está acontecendo... A conversa entre Giulia e Paludo acontece sobre o corpo gelado de Sheila. O seu envolvimento não supervisionado com a KGB não foi perdoado...')
          time.sleep(9)
          print('A causa da morte? Cortaram a garganta dela com um Postit muito afiado! Que crueldade!')
          time.sleep(2)
          print('Você anota tudo, e sai de fininho para não ser pego.')
          time.sleep(4)
          lados[6][2] = 'Assassina nas montanhas...'
    elif option == '2' or option == 'ACUSAR':
      result_set = [False,False, False]
      print(tabulate(nomes, headers='firstrow', tablefmt='grid'))
      opt_1 = str(input('\nDigite o código ou o nome de quem deseja acusar: ')).upper()
      if opt_1 == '4' or opt_1 in 'RAFAELA':
        result_set[0] =True
      else: 
          result_set[0] = False
      print(tabulate(armas,headers='firstrow', tablefmt='grid'))
      opt_2 = str(input('\nDigite o código ou o nome da arma que cometeu o crime: ')).upper()
      if opt_2 == '5' or opt_2 in 'COMPASSO':
          result_set[1] = True
      else: 
          result_set[1] = False
      print(tabulate(locais,headers='firstrow', tablefmt='grid'))
      opt_3 = str(input('Digite o local onde acha que ocorreu o assassinato: ')).upper()
      if opt_3 == '3' or opt_3 in 'SALA SECRETA':
          result_set[2]=True
      else: 
          result_set[2] = False
      while True:   
          print('Analisando suas escolhas...')
          if  (result_set[0] and result_set[1] and result_set[2]) == True:
              sub_ = pyfiglet.figlet_format('CONSEGUIU! VINGOU A MORTE DA ÂNA!', font='standard')
              print(sub_)
              dialogos.dialogo_final()
              break
          else:
              print(f'\nSua investigação é falha. Corra antes que o tempo acabe.\nVocê sabe {result_set.count(True)}/3 informações corretas.')
              break
      if (result_set[0] and result_set[1] and result_set[2]) == True:
            break