ac = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"];
#acm = ["Am", "Bm", "Cm", "Dm", "Em", "Fm", "Gm"];
T = input("Acorde: \n");

while T not in ac:
  print("Acorde não reconhecido, faz de novo ai op.");
  T = input("Acorde: \n");

m = int(input("Responda 1 para acorde maior ou 2 para menor: \n"));
while m != 1 and m != 2:
  print("Valor não reconhecido, digita oq eu to falando desgraça.");
  m = int(input("Responda 1 para acorde maior ou 2 para menor: \n"));
  
#acorde maior = T 3° 5°:  T 3°=T+2tons; 5°= 3° + 1+1/2ton

#Ré menor = [estado fundantal=re fa la;  
#1° inversao=fa la re; 
#2° inversao = la re fa]
if m == 1:
  ter = ac[ac.index(T)+4];
  qui = ac[ac.index(T)+7];
  print(f'''Estado fundamental = {T} {ter} {qui}
1º inversão = {ter} {qui} {T}
2º inversão = {qui} {T} {ter}''');
elif m == 2:
  ter = ac[ac.index(T)+3];
  qui = ac[ac.index(T)+7]
  print(f'''Estado fundamental = {T} {ter} {qui}
1º inversão = {ter} {qui} {T}
2º inversão = {qui} {T} {ter}''');
  
