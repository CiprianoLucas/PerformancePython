import timeit
from functools import reduce

base = "{$1}{$2}{$3}{$4}{$5}{$6}{$7}{$8}{$9}{$10}{$11}{$12}{$13}{$14}{$15}{$16}{$17}{$18}{$19}{$20}"
print(base)

def normal():
 # Texto original
 texto = "LoremipsumdolorsitametconsecteturadipisicingelitEosnostrumaccusamusipsaeaquefugiatisteabsimiliqueeiusarchitectodoloribus"
 return texto

def f_string():
 # Texto original
 texto = f"{'Lorem'}{'ipsum'}{'dolor'}{'sit'}{'amet'}{'consectetur'}{'adipisicing'}{'elit'}{'Eos'}{'nostrum'}{'accusamus'}{'ipsa'}{'eaque'}{'fugiat'}{'iste'}{'ab'}{'similique'}{'eius'}{'architecto'}{'doloribus'}"
 return texto

def usando_join():
 lista = []
 lista.append("Lorem")
 lista.append("ipsum")
 lista.append("dolor")
 lista.append("sit")
 lista.append("amet")
 lista.append("consectetur")
 lista.append("adipisicing")
 lista.append("elit")
 lista.append("Eos")
 lista.append("nostrum")
 lista.append("accusamus")
 lista.append("ipsa")
 lista.append("eaque")
 lista.append("fugiat")
 lista.append("iste")
 lista.append("ab")
 lista.append("similique")
 lista.append("eius")
 lista.append("architecto")
 lista.append("doloribus")
 texto = "".join(lista)  # Adicionando espaço entre as palavras
 return texto

def usando_concat():
 texto = ""
 texto += "Lorem"
 texto += "ipsum"
 texto += "dolor"
 texto += "sit"
 texto += "amet"
 texto += "consectetur"
 texto += "adipisicing"
 texto += "elit"
 texto += "Eos"
 texto += "nostrum"
 texto += "accusamus"
 texto += "ipsa"
 texto += "eaque"
 texto += "fugiat"
 texto += "iste"
 texto += "ab"
 texto += "similique"
 texto += "eius"
 texto += "architecto"
 texto += "doloribus"
 return texto

def usando_replace_com_reduce():
 dicionario = {
     "{$1}": "Lorem",
     "{$2}": "ipsum",
     "{$3}": "dolor",
     "{$4}": "sit",
     "{$5}": "amet",
     "{$6}": "consectetur",
     "{$7}": "adipisicing",
     "{$8}": "elit",
     "{$9}": "Eos",
     "{$10}": "nostrum",
     "{$11}": "accusamus",
     "{$12}": "ipsa",
     "{$13}": "eaque",
     "{$14}": "fugiat",
     "{$15}": "iste",
     "{$16}": "ab",
     "{$17}": "similique",
     "{$18}": "eius",
     "{$19}": "architecto",
     "{$20}": "doloribus"
 }
 texto = reduce(lambda acc, k: acc.replace(k, dicionario[k]), dicionario, base)
 return texto

def usando_replace_com_for():
 dicionario = {
     "{$1}": "Lorem",
     "{$2}": "ipsum",
     "{$3}": "dolor",
     "{$4}": "sit",
     "{$5}": "amet",
     "{$6}": "consectetur",
     "{$7}": "adipisicing",
     "{$8}": "elit",
     "{$9}": "Eos",
     "{$10}": "nostrum",
     "{$11}": "accusamus",
     "{$12}": "ipsa",
     "{$13}": "eaque",
     "{$14}": "fugiat",
     "{$15}": "iste",
     "{$16}": "ab",
     "{$17}": "similique",
     "{$18}": "eius",
     "{$19}": "architecto",
     "{$20}": "doloribus"
 }
 texto = base
 for k in dicionario:
     texto = texto.replace(k, dicionario[k])
 return texto

# Medindo o tempo de execução
tempo_normal = timeit.timeit(normal)
tempo_f_string = timeit.timeit(f_string)
tempo_join = timeit.timeit(usando_join)
tempo_concat = timeit.timeit(usando_concat)
tempo_replace_reduce = timeit.timeit(usando_replace_com_reduce)
tempo_replace_for = timeit.timeit(usando_replace_com_for)

print(normal())
print(f_string())
print(usando_join())
print(usando_concat())
print(usando_replace_com_reduce())
print(usando_replace_com_for())

print(f"Tempo normal: {tempo_normal:.5f} segundos")
print(f"Tempo f-string: {tempo_f_string:.5f} segundos")
print(f"Tempo usando join: {tempo_join:.5f} segundos")
print(f"Tempo usando += : {tempo_concat:.5f} segundos")
print(f"Tempo usando replace com reduce: {tempo_replace_reduce:.5f} segundos")
print(f"Tempo usando replace com for: {tempo_replace_for:.5f} segundos")
