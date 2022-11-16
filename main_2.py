def my_function(fname): #do il nome a una funzione
  print(fname + " Refsnes") #stampo il nome della funzione 

my_function("Emil") #Gli argomenti sono specificati dopo il nome della funzione, all'interno delle parentesi.
my_function("Tobias") 
my_function("Linus")

print("##################")

def my_function(fname, lname): #Per impostazione predefinita, una funzione deve essere chiamata con il numero corretto di argomenti.
# Significa che se la tua funzione si aspetta 2 argomenti, devi chiamare la funzione con 2 argomenti, non di più e non di meno.
  print(fname + " " + lname) #stampo i due argomenti della funzione

my_function("Emil", "Refsnes")  
#Gli argomenti sono specificati dopo il nome della funzione, all'interno delle parentesi.

print("##################")
def my_function(*kids):  #Se non sai quanti argomenti verranno passati alla tua funzione, 
#aggiungi a *prima del nome del parametro nella definizione della funzione.
  print("The youngest child is " + kids[1])   #stampo gli argomenti della funzione

my_function("Emil", "Tobias", "Linus") 
my_function("Emil", "Tobias") 

print("##################")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3) 

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("##################")

def my_function(**kid):  #Se non sai quanti argomenti di parole chiave verranno passati nella tua funzione, 
#aggiungi due asterischi: **prima del nome del parametro nella definizione della funzione.
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print("##################")

def my_function(country = "Norway"): #valore di default del parametro
  print("I am from " + country)

my_function("Sweden")  #scrivo nome argomenti
my_function("India")
my_function() #se non c'è l'argomento stampa il nome messo nella funzione 
my_function("Brazil")

print("##################")

def my_function(food):   #do il nome a una funzione
  for x in food:
    print(x) #mi stamperà gli argomenti della lista

fruits = ["apple", "banana", "cherry"] #riempio una lista con dei nomi

my_function(fruits)  # come argomento metto il nome della lista

print("##################")

def my_function(x):  #do il nome a una funzione 
  return 5 * x  # compie la moltiplicazione

print(my_function(3))  # stampa la funzione 5x3
print(my_function(5))
print(my_function(9))

print("##################")

def myfunction(): #functionle definizioni non possono essere vuote, ma se per qualche motivo hai una functiondefinizione 
  pass #senza contenuto, inserisci l' passistruzione per evitare di ottenere un errore.
