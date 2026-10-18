from django.shortcuts import render

# "Base de datos" falsa: una lista de diccionarios en memoria.
# En un proyecto real esto vendría de un modelo (models.py) y una tabla,
# pero para ENTENDER qué es SSR no necesitamos base de datos: lo importante
# es que estos datos se insertan en el HTML *antes* de enviarlo al navegador.
PRODUCTOS = [
{"id":1,"nombre":"Pollo agridulce","categoria":"Platos al wok","precio":130,"stock":20,"imagen":"img/pollo-agridulce.webp"},
  {"id":2,"nombre":"Res con brócoli","categoria":"Platos al wok","precio":145,"stock":20,"imagen":"img/res-con-brocoli.webp"},
  {"id":3,"nombre":"Pollo kung pao","categoria":"Platos al wok","precio":135,"stock":20,"imagen":"img/pollo-kung-pao.webp"},
  {"id":4,"nombre":"Chow mein","categoria":"Platos al wok","precio":120,"stock":20,"imagen":"img/chow-mein.webp"},
  {"id":5,"nombre":"Arroz frito especial","categoria":"Platos al wok","precio":110,"stock":20,"imagen":"img/arroz-frito-especial.webp"},
  {"id":6,"nombre":"Rollos primavera (2)","categoria":"Entradas","precio":60,"stock":20,"imagen":"img/rollos-primavera.webp"},
  {"id":7,"nombre":"Wonton frito","categoria":"Entradas","precio":65,"stock":20,"imagen":"img/wonton-frito.webp"},
  {"id":8,"nombre":"Sopa wantán","categoria":"Entradas","precio":70,"stock":20,"imagen":"img/sopa-wantan.webp"},
  {"id":9,"nombre":"Costillas agridulces","categoria":"Entradas","precio":120,"stock":20,"imagen":"img/costillas-agridulces.webp"},
  {"id":10,"nombre":"Dumplings al vapor","categoria":"Entradas","precio":85,"stock":20,"imagen":"img/dumplings-vapor.webp"},
  {"id":11,"nombre":"Combo 1 (2 guisos + arroz)","categoria":"Combos y bebidas","precio":150,"stock":20,"imagen":"img/dos-guisos-arroz.webp"},
  {"id":12,"nombre":"Combo familiar","categoria":"Combos y bebidas","precio":420,"stock":20,"imagen":"img/combo-familiar.webp"},
  {"id":13,"nombre":"Té de jazmín","categoria":"Combos y bebidas","precio":30,"stock":20,"imagen":"img/te-de-jazmin.webp"},
  {"id":14,"nombre":"Limonada","categoria":"Combos y bebidas","precio":35,"stock":20,"imagen":"img/limonada.webp"},
  {"id":15,"nombre":"Galletas de la fortuna (3)","categoria":"Combos y bebidas","precio":15,"stock":20,"imagen":"img/galletas-de-la-fortuna.webp"}

]


def vista_ssr(request):
    """
    Vista con Renderizado en Servidor (SSR).

    request: el objeto que representa la petición que hizo el navegador.

    render() hace tres cosas:
      1) toma la plantilla 'catalogo/catalogo_ssr.html'
      2) le inyecta el diccionario de "contexto" (aquí: la lista de productos)
      3) devuelve el HTML final, YA CON LOS DATOS DENTRO, listo para el navegador.

    Por eso es "servidor": el HTML que llega al navegador ya trae escritos
    los nombres y precios. Si haces clic derecho > "Ver código fuente de la
    página" verás los productos en el HTML, aunque JavaScript esté desactivado.
    Compáralo con la vista CSR de la Parte B, donde el HTML llega vacío y es
    JavaScript quien dibuja los productos DESPUÉS, ya en el navegador.
    """
    contexto = {"productos": PRODUCTOS}
    return render(request, 'catalogo/catalogo_ssr.html', contexto)