print('Olá, seja bem vindo! Para realizar o cadastro iremos precisar de alguns dados, ok? \n')
primeiro_nome = input('Digite o seu primeiro nome: ')
sobrenome = input('Digite o seu sobrenome: ')

idade = int(input('Nos informe a sua idade, por gentileza: '))

if idade < 18:
  responsavel = input(f'\n{primeiro_nome}, como você é menor de idade iremos precisar do nome do seu responsável para realizar o cadastro! \nResponsável: ')

telefone = int(input('Digite o seu número de telefone com o dígito: '))

if len(str(telefone)) < 10 or len(str(telefone)) > 11:
  print(f'\n{primeiro_nome}, não foi possível realizar o cadastro, número de telefone inválido!\n')
else:
  print(f'Seu cadastro foi realizado com sucesso, {primeiro_nome}!')