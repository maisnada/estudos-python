#impressão de float
#"R$ {:f}".format(1.59)

#impressão de float limitando casas decimais para 2
#"R$ {:.2f}".format(1.59)

#impressão de float limitando casas decimais para 2, considerando o total de caracteres como 7. Respeitará o ldap
#"R$ {:7.2f}".format(1.59)
#R$   1.50
#R$  12.69

#complementa com 0 a esquerda lpad
#"R$ {:07.2f}".format(1.59)
#R$0001.50
#R$0012.69

#para formatar inteiros
#"R$ {:07d}".format(4)
#R$0000004

#para formatar inteiros
#"R$ {:7d}".format(46)
#R$    46

#"Data {:2d}/{:2d}".format(9,4)
#Data  9/ 4

#"Data {:02d}/{:02d}".format(9,4)
#Data 09/04
