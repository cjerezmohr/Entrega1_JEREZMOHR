# mohtstore
El motivo de la pagina es una platafomra de consulta de equipos de informatica ya sea pc de escritorio como tambien perifericos y monitores.
primero genere uno proyecto llamado Hardstore y la aplicacion "productos".
genere 3 clases models : Desktop_notebook, Perifericos y Monitores.
cree el index.html, el base.html y luego las respectivas paginas para cada clase.
mediante la herencia comparti el diseño del html base a las las demas paginas para incluir el navbar importado de bootstrap.
controle que las info que generaba en los models se guardaba correctamente en la base de datos.
dentro de views genere funciones que muestren en las htmls respectivas y la info de cada modelo.
creando el archivo forms.py genere en su interior 3 formularios para poder crear un objeto nuevo de cada modelo haciendo la carga desde la html.
al completar y enviar un formulario este se mostrara en pantalla los datos cargados.
lo siguiente fue configurar el motor de busqueda creando una funcion dentro de views.py llamada Search_views para realizar busquedas con el metodo filter.
todos los archivos.html los guarde en una carpeta llamada "Templates"
***********************************************************************************************************************************************************
Guia de prueba de mi sitio
clonar desde github mediante el codigo https://github.com/cjerezmohr/mohtstore.git
luego de clonar hace un : CD hardstore para acceder a la carpeta del proyecto y ejecutar un "python manage.py runserver" para activar el sitio

en la pantalla principal tendremos un index de "bienvenida" 
en la nav bar tenemos un boton MohrStore y Home que nos retornaran a esta pantalla de inicio desde cualquier lugar del sitio
el desplegable Producto permite ir a las web de los 3 modelos en donde se muestra un ejemplo de productos cargados.
si deseamos crear o añadir un nuevo producto podemos hacerlo desde el desplegable crear y luego seleccionando una categoria y despues de completar el formulario
el nuevo producto se mostrara en pantalla
para buscarlo o buscar cuaquiera de los productos que integran la base de datos se puede usar el boton buscador a la derecha de la pantalla.

eso seria todo.
