#!/usr/bin/env python
# coding: utf-8

# # Hola Gabriela!
# 
# Mi nombre es David Bautista, soy code reviewer de TripleTen y voy a revisar el proyecto que acabas de desarrollar.
# 
# Cuando vea un error la primera vez, lo señalaré. Deberás encontrarlo y arreglarlo. La intención es que te prepares para un espacio real de trabajo. En un trabajo, el líder de tu equipo hará lo mismo. Si no puedes solucionar el error, te daré más información en la próxima ocasión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres.**
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# 
# <div class="alert alert-block alert-danger">
#     
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
#     
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# 
# Puedes responderme de esta forma: 
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# </div
# 
# ¡Empecemos!

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General
#     
# ~~Hola Gabriela, te felicito por el desarrollo del proyecto hasta el momento. Ahora bien, he dejado diferentes comentarios para que los puedas temer en cuenta para la siguiente entrega.~~ </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #2
#     
# ~~Hola Gabriela, he dejado nuevos comentarios etiquetados con el #2 para que los puedas revisar. Te felicito por las modificaciones realizadas, vas muy bien.~~ </div>
# 
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #3
#     
# ~~Hola Gabriela, he dejado nuevos comentarios etiquetados con el #3 para que los puedas tener en cuenta para la sigiente entrega.~~ </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #4</b> <a class="tocSkip"></a>
#     
# # Comentario General #4
#     
# Hola, Gabriela, tendré en cuenta tu comentario de la sección final por si tengo que revisar uno de tus futuros proyectos. Gracias por el feedback y espero sigas enamorada de este maravilloso mundo. Te va a sorprender todo lo que se puede llegar a aprender. Por otro lado, te felicito por el desarrollo del proyecto, muchas veces tal como lo mencionaste tenías pequeños errores los cuales siento que también pueden llegar a enriquecer el aprendizaje, si lo piensas, este tipo de errores van a ser cada vez menos comunes porque ya vas a tener las pilas puestas sobre como evitarlos.  </div>

# Una empresa de comercio electrónico, Store 1, recientemente comenzó a recopilar datos sobre sus clientes. El objetivo final de Store 1 es comprender mejor el comportamiento de sus clientes y tomar decisiones basadas en datos para mejorar su experiencia online.
# 
# Como parte del equipo de análisis, tu primera tarea es evaluar la calidad de una muestra de datos recopilados y prepararla para futuros análisis.

# # Cuestionario
# 
# Store 1 tiene como objetivo garantizar la coherencia en la recopilación de datos. Como parte de esta iniciativa, se debe evaluar la calidad de los datos recopilados sobre los usuarios y las usuarias. Te han pedido que revises los datos recopilados y propongas cambios. A continuación verás datos sobre un usuario o una usuaria en particular; revisa los datos e identifica cualquier posible problema.

# In[1]:


user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']


# **Opciones:**
# 
# 1. El tipo de datos para `user_id` debe cambiarse de una cadena a un número entero.
#     
# 2. La variable `user_name` contiene una cadena que tiene espacios innecesarios y un guion bajo entre el nombre y el apellido.
#     
# 3. El tipo de datos de `user_age` es incorrecto.
#     
# 4. La lista `fav_categories` contiene cadenas en mayúsculas. En su lugar, deberíamos convertir los valores de la lista a minúsculas.

# Escribe en la celda Markdown a continuación el número de las opciones que has identificado como problemas. Si has identificado varios problemas, sepáralos con comas. Por ejemplo, si piensas que los números 1 y 3 son incorrectos, escribe 1, 3.

# # **Escribe tu respuesta y explica tu argumentación:**
# 2, 3.
# El nombre contiene espacios innecesarios y está separado por un guíon bajo, dificultando la escritura e intercambio de código.
# La edad se puede cambiar a número entero para facilitar la lectura y por el tipo de dato, la edad es más fácil leer en número entero.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo Gabriela. </div>

# # Ejercicio 1
# 
# Vamos a implementar los cambios que identificamos. Primero, necesitamos corregir los problemas de la variable `user_name`. Como vimos, tiene espacios innecesarios y un guion bajo como separador entre el nombre y el apellido; tu objetivo es eliminar los espacios y luego reemplazar el guion bajo con el espacio.

# In[2]:


user_name = ' mike_reed '
user_name = user_name.strip()# eliminar los espacios en la cadena original
user_name = user_name.replace("_", " ")# reemplazar el guion bajo con el espacio

print(user_name)
                              #aplicar strip() y replace() dentro de la misma variable sin crear una nueva, solo indicando las modificaciones ha realizar.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo aplicando los métodos ``strip()`` y ``replace()``. </div>

# # Ejercicio 2
# 
# Luego, debemos dividir el `user_name` (nombre de usuario o usuaria) actualizado en dos subcadenas para obtener una lista que contenga dos valores: la cadena para el nombre y la cadena para el apellido.

# In[3]:


user_name = 'mike reed'
name_split = user_name.split() #uso del metodo split para dividir

#crear una lista separando cada valor (nombre y apellido),  creando subcadenas.

print(name_split)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Recuerda que en este ejercicio la idea es usar el método ``split()`` para poder separar el string por un carácter específico. ~~</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo Gabriela.</div>

# # Ejercicio 3
# 
# ¡Genial! Ahora debemos trabajar con la variable `user_age`. Como ya mencionamos, esta tiene un tipo de datos incorrecto. Arreglemos este problema transformando el tipo de datos y mostrando el resultado final.

# In[4]:


user_age = 32.0
user_age = int(user_age)# cambia el tipo de datos para la edad de un usuario o usuaria

#cambio a número entero con int()

print(user_age)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo transformando el tipo de dato de la variable. </div>

# # Ejercicio 4
# 
# Como sabemos, los datos no siempre son perfectos. Debemos considerar escenarios en los que el valor de `user_age` no se pueda convertir en un número entero. Para evitar que nuestro sistema se bloquee, debemos tomar medidas con anticipación.
# 
# Escribe un código que intente convertir la variable `user_age` en un número entero y asigna el valor transformado a `user_age_int`. Si el intento falla, mostramos un mensaje pidiendo al usuario o la usuaria que proporcione su edad como un valor numérico con el mensaje: `Please provide your age as a numerical value.` (Proporcione su edad como un valor numérico.)

# In[5]:


user_age = 'treinta y dos' # aquí está la variable que almacena la edad como un string.


#no es posible convertir string a valor númerico con la función INT
#para evitar una falla en el error evidente usar el operador TRY, EXCEPT

try:
    user_age_int= int(user_age)
    print(user_age_int)
    
except:
    print("Please provide your age as a numerical value.")
       
    # escribe un código que intente transformar user_age en un entero y si falla, imprime el mensaje especificado


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, Gabriela. Buen trabajo aplicando el ``try`` - ``except`` para solucionar este ejercicio. </div>

# # Ejercicio 5
# 
# Finalmente, considera que todas las categorías favoritas se almacenan en mayúsculas. Para llenar una nueva lista llamada `fav_categories_low` con las mismas categorías, pero en minúsculas, itera los valores en la lista `fav_categories`, modifícalos y agrega los nuevos valores a la lista `fav_categories_low`. Como siempre, muestra el resultado final.

# In[1]:


fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

# escribe tu código aquí
for fav_categorie in fav_categories:
    fav_categorie = fav_categorie.lower()
 # creacion de un bucle para pasarlos a minúscula con lower
 #ya vi mi eror, en vez de imprimir poner la variable para dar la orden de poner minúsculas en esa variable   
    fav_categories_low.append(fav_categorie)
#unir nueva lista con los valores modificados

# no elimines la siguiente declaración print
print(fav_categories_low)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Recuerda que en este ejercicio el ideal es usar un bucle para poder modificar cada uno de los elementos de la lista original y agregarlos a la lista final. Un método clave podría ser ``append()``.~~ </div>
#     
#     
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# ~~Usas una buena lógica; sin embargo, no se está guardando de manera correcta la modificación sobre cada palabra. Podrías aplicar la siguiente estructura. ~~
#     
# ```python
# fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
# fav_categories_low = []
# 
# 
# for fav_categorie in fav_categories:
#     fav_categorie = fav_categorie.lower()
#     fav_categories_low.append(fav_categorie)
# print(fav_categories_low)    
# ```
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo Gabriela. </div>
#     

# # Ejercicio 6
# 
# Hemos obtenido información adicional sobre los hábitos de gasto de nuestros usuarios y usuarias, incluido el importe gastado en cada una de sus categorías favoritas. La gerencia está interesada en las siguientes métricas:
# 
# - Importe total gastado por el usuario o la usuaria.
# - Importe mínimo gastado.
# - Importe máximo gastado.
# 
# Vamos a calcular estos valores y mostrarlos en la pantalla:

# In[7]:


fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category) # escribe tu código aquí
max_amount = max(spendings_per_category)# escribe tu código aquí
min_amount = min(spendings_per_category)# escribe tu código aquí

#sacamos el total, máximo y mínimo de los gastos con dichas funciones.

# no elimines la siguiente declaración print
print(total_amount)
print(max_amount)
print(min_amount)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo realizando los cálculos con las funciones predeterminadas de suma, máximo y mínimo. </div>

# # Ejercicio 7
# 
# La empresa quiere ofrecer descuentos a sus clientes leales. Los clientes y las clientas que realizan compras por un importe total mayor a $1500 se consideran leales y recibirán un descuento.
# 
# Nuestro objetivo es crear un bucle `while` que compruebe el importe total gastado y se detenga al alcanzarlo. Para simular nuevas compras, la variable `new_purchase` genera un número entre 30 y 80 en cada iteración del bucle. Esto representa el importe de dinero gastado en una nueva compra y es lo que hay que sumar al total.
# 
# Una vez que se alcance el importe objetivo y se termine el bucle `while`, se mostrará la cantidad final.

# In[8]:


from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent >= target_amount: # escribe tu código aquí
    #compara, mientras total sea mayor o igual al importe mínimo deseado por la empresa (1500)
	new_purchase = randint(30, 80) # generamos un número aleatorio de 30 a 80
	total_amount_spent += new_purchase # escribe tu código aquí
#cuando el total y nuevas compras se vayan sumando se irá reflejando la cantidad de cada ususario para ver si son leales.En este caso no tenemos un valor para parar.

print(total_amount_spent)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo estructurando el bucle ``while``. </div>

# # Ejercicio 8
# 
# Ahora tenemos toda la información sobre un cliente o una clienta de la forma que queremos que sea. La gerencia de una empresa nos pidió proponer una forma de resumir toda la información sobre un usuario o una usuaria. Tu objetivo es crear una cadena formateada que utilice información de las variables `user_id`, `user_name` y `user_age`.
# 
# Esta es la cadena final que queremos crear: `User 32415 is mike who is 32 years old.` (El usuario 32415 es Mike, quien tiene 32 años).

# In[13]:


user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_info ="User {} is {} who is {} years old".format(user_id, user_name[0], user_age)# escribe tu código aquí

#añadí [] para seleccionar solo el índice del nombre del usuario, para mejorar la visibilidad de la info del cliente.

#aplica un método format para lograr la impresion deseada.
# no elimines la siguiente declaración print
print(user_info)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Buen trabajo con el formato de texto, sin embargo, recuerda que podrías acceder al primer elemento de la lista ``user_name`` para que la salida final se vea de mejor manera.~~ </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo. </div>

# Como sabes, las empresas recopilan y almacenan datos de una forma particular. Store 1 desea almacenar toda la información sobre sus clientes y clientas en una tabla.
# 
# | user_id | user_name | user_age | purchase_category | spending_per_category |
# | --- | --- | --- | --- | --- |
# | '32415' | 'mike', 'reed' | 32 | 'electronics', 'sport', 'books' | 894, 213, 173 |
# | '31980' | 'kate', 'morgan' | 24 | 'clothes', 'shoes' | 439, 390 |
# 
# En términos técnicos, una tabla es simplemente una lista anidada que contiene una sublista para cada usuario o usuaria.
# 
# Store 1 ha creado una tabla de este tipo para sus usuarios y usuarias. Se almacena en la variable `users`. Cada sublista contiene el ID del usuario o la usuaria, nombre y apellido, edad, categorías favoritas y el importe gastado en cada categoría.

# # Ejercicio 9
# 
# Para calcular los ingresos de la empresa, sigue estos pasos.
# 
# 1. Utiliza `for` para iterar sobre la lista `users`.
# 2. Extrae la lista de gastos de cada usuario o usuaria y suma los valores.
# 3. Actualiza el valor de los ingresos con el total de cada usuario o usuaria.
# 
# Así obtendrás los ingresos totales de la empresa que mostrarás en la pantalla al final.

# In[22]:


users = [
	  # este es el inicio de la primera sublista
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
        [894, 213, 173]
    ], # este es el final de la primera sublista

    # este es el inicio de la segunda sublista
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'shoes'],
        [439, 390]
    ] # este es el final de la segunda sublista
]

revenue = 0

for user in users:
    print(sum(user[4]))
    revenue += sum(user[4])#suma de los gastos de cada cliente
    # actualiza los ingresos
    #agrege la suma a revenue para sumar los gastos de los usuarios   
    
# no elimines la siguiente declaración print
print(revenue)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Gabriela, es importante que reconstruyas paso a paso el bucle, ya que hay un problema de identificación. Recuerda que al construir el bucle y dar enter, automáticamente se sitúa el cursor en la línea en la que debes seguir desarrollando cada parte del código. </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# ~~Te falta estructurar el código de manera que se pueda actualizar el valor de los ingresos. Intenta seguir la estructura del bucle de código anterior.~~ </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a>
#     
# Buen trabajo Gabriela. </div>
#     

# # Ejercicio 10
# 
# Recorre la lista de usuarios y usuarias que te hemos proporcionado y muestra los nombres de la clientela menor de 30 años.

# In[8]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]
young_users=[] #crear nueva lista para lo filtros

for user in users:
 if user [2]<30:#creando el filtro para la edad menores a 30
        young_users.append(user[1])
        
print(young_users)     ##imprimos usarios filtrados
        # escribe tu código aquí


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Desarrollas el bucle con una buena lógica, sin embargo, recuerda que el ideal es únicamente mostrar el nombre de los clientes que cumplen con la condición respectiva.~~ </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo. </div>

# # Ejercicio 11
# 
# Juntemos las tareas 9 y 10 e imprimamos los nombres de los usuarios y las usuarias que tengan menos de 30 años y un gasto total superior a 1000 dólares.

# In[14]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

select_users=[] #crear nueva lista para lo filtros

for user in users:
 if user [2]<30 and sum(user[4])>1000:#creando el filtro para la edad e ingresos 
        select_users.append(user[1])
        
print(select_users)  # escribe tu código a


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Recuerda que cuando accedes a user[4] deberías usar un ``sum()``, ya que estás accediendo a una lista. ~~

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo. </div>

# # Ejercicio 12
# 
# Ahora vamos a mostrar el nombre y la edad de todos los usuarios y todas las usuarias que han comprado ropa. Imprime el nombre y la edad en la misma declaración print.

# In[10]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

clothes_users=[]

for user in users:
    if "clothes" in user[3]:#creando el filtro para la ropa 
        clothes_users.append(user[1:3]) #aqui trate de pedir que incluya solo los indices 1 y 2 
        
print(clothes_users)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~En este ejercicio el ideal sería usar la sentencia ``in``. Esta te permite ver si un elemento se encuentra o no dentro de una lista~~.  </div>
#     
#     
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# ~~Perfecto, ahora solo debes tener en cuenta que el iedal es imprimir unicamente el nombre y la edad de los clientes~~. </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a>
#     
# ~~Aun no se ha terminado de tener en cuenta los comentarios anteriores Gabriela.~~ </div>

# Amo con toda locura esto, pero me decesperó sobre manera que muchas veces no da por errores de dedo, y es esta última vez fue un poco frustrante no tener una indicación que me guiará sobre donde estaba una S extra que tenía. Fuera de eso estoy enamorada del curso.
# Gracias por tu ayuda :)

# 

# #Escribe aquí cualquier comentario o reflexión final
