# Anexo A.4 Retícula, safe area y escalado

Diseñas un HUD precioso en Figma, a 1920×1080, con el minimapa pegadito a la esquina. Lo pruebas en una tele y el minimapa aparece cortado. Lo pruebas en un monitor panorámico y queda flotando a medio camino del borde. Lo pruebas en un móvil y la cámara frontal se come la barra de vida. Acabas de toparte con el problema menos glamuroso (y más frecuente) de la UI de juegos: **la pantalla del jugador nunca es la tuya**.

Este apartado va de las tres herramientas que lo resuelven: **la retícula** para ordenar, **la safe area** para no perder nada por los bordes y **el escalado** para que todo se adapte a cualquier pantalla.

## La retícula

Una retícula (o grid) es **una estructura invisible de líneas y medidas** sobre la que colocas los elementos. El jugador no la ve, pero nota cuando no está: los márgenes cambian de una pantalla a otra, los botones no se alinean y todo tiene un aire de "casi".

### Sistema de 8 puntos

La forma más extendida de trabajar es que **todas las medidas sean múltiplos de 8**: un botón de 48 píxeles de alto, un margen de 16, un espacio de 24 entre bloques. Para los ajustes finos (el hueco entre un icono y su texto) se permite bajar a 4.

¿Por qué 8? Porque se divide limpiamente entre 2 y entre 4, lo que facilita escalar sin medios píxeles, y porque **las resoluciones más habituales son múltiplos de 8**: 1920×1080 son 240×135 bloques de 8, y 1280×720 son 160×90. Pero la razón más práctica es otra: **te ahorra decisiones**. En lugar de dudar entre un margen de 13 o de 15 píxeles, eliges entre 8, 16 o 24, y todo queda proporcionado casi sin pensar.

Si tu juego es de **pixel art**, la retícula manda todavía más, y la marca la resolución base del juego. Un juego que se dibuja a 320×180 píxeles y se amplía seis veces para llenar una pantalla de 1920×1080 tiene que diseñar su interfaz **a 320×180**, con los mismos píxeles gordos que el resto del juego. Una interfaz con píxeles más finos que los personajes se nota a la legua, porque el ojo compara el tamaño de los píxeles sin que nadie se lo pida. A ese defecto se le llama **mixel** (de *mixed pixels*, píxeles mezclados), y es de los que más delatan un pixel art poco cuidado.

### Tipos de retícula

Según lo que tenga que organizar cada pantalla, te conviene una estructura u otra. La retícula de **columnas** divide la pantalla en franjas verticales y funciona muy bien en menús de opciones y pantallas con texto. La retícula **modular** divide el espacio en casillas iguales, y es la de los inventarios: el maletín de *Resident Evil 4*, donde cada objeto ocupa un número de casillas según su tamaño, es el caso más famoso, porque **la propia retícula se convierte en mecánica**. Y hay pantallas donde lo que manda es la importancia de cada elemento, como el enorme árbol de habilidades pasivas de *Path of Exile*; ahí se trabaja con una estructura más libre, **jerárquica**, donde lo importante es más grande o está más al centro.

| Retícula | Cómo organiza | Dónde se usa |
|---|---|---|
| Columnas | Franjas verticales del mismo ancho | Menús de opciones, pantallas de texto, tiendas |
| Modular | Casillas iguales en filas y columnas | Inventarios, selección de personaje, mapas por casillas |
| Jerárquica | Tamaño y posición según la importancia | Árboles de habilidades, pantallas de título |

Lo normal es que un mismo juego **use varias**: el HUD con el sistema de 8 puntos, las opciones en columnas y el inventario en módulos. Lo que tienen que compartir son **los márgenes y las medidas base**.

## La safe area

Durante décadas, los televisores **recortaban un poco los bordes de la imagen** (se llamaba overscan). Hoy la mayoría ya no lo hacen por defecto, pero muchos siguen haciéndolo según el modo de imagen, y además los juegos se ven en proyectores, en monitores de todas las formas y en móviles con **cámaras en la pantalla y esquinas redondeadas**.

La solución es definir una **safe area** (zona segura): un rectángulo un poco más pequeño que la pantalla dentro del cual va **toda la información importante**. Fuera de ella solo dejas lo que puede perderse sin problema, como el fondo o una viñeta decorativa. Un margen de **en torno al 5 % por cada lado** es un buen punto de partida (unos 96 píxeles a izquierda y derecha y unos 54 arriba y abajo en una pantalla de 1920×1080). Muchos juegos de consola dejan además que el jugador **ajuste ese margen** en las opciones, con la típica pantalla de "mueve las esquinas hasta que se vean".

En móvil, los motores te dan el dato directamente: en Unity, por ejemplo, `Screen.safeArea` te devuelve el rectángulo que el sistema operativo garantiza que se ve entero.

<!-- Imagen pendiente: pantalla de ajuste de safe area de algún juego de consola -->

## El escalado

Diseñas para una resolución, pero el juego se va a ver en muchas. La forma de trabajar habitual es elegir una **resolución de referencia** (hoy casi siempre 1920×1080) y diseñar todo ahí. Después, el motor **escala la interfaz** para que ocupe lo mismo en proporción en cualquier otra pantalla: en una de 3840×2160 (4K) todo se dibuja al doble, y en una de 1280×720, a dos tercios.

Eso resuelve el tamaño, pero no la forma. Una pantalla puede ser **16:9** (la mayoría de televisores y monitores), **16:10** (muchos portátiles y la Steam Deck, con 1280×800), **21:9** (los monitores panorámicos) o la de un móvil en horizontal, todavía más alargada. Para que la interfaz sobreviva a eso existen los **anclajes**: cada elemento se "ata" a una esquina, a un borde o al centro de la pantalla. El minimapa anclado arriba a la derecha **sigue arriba a la derecha** en un monitor panorámico, en lugar de quedarse flotando donde estaba en 16:9.

En Unity, el componente **Canvas Scaler** (con el modo *Scale With Screen Size*) o los **Panel Settings** de UI Toolkit se encargan del escalado, y los anclajes se definen en cada elemento. En Godot, el modo de **stretch** del proyecto y los anclajes de los nodos `Control` hacen lo mismo.

!!! example "Haz la prueba"
    En Figma, crea tres marcos: uno de 1920×1080, otro de 2560×1080 (21:9) y otro de 1280×800 (16:10). Coloca en el primero un HUD sencillo con su safe area. Después pásalo a los otros dos decidiendo a qué esquina o borde está anclado cada elemento. ¿Hay algo que no sabías dónde poner? Ese elemento necesitaba un anclaje y no lo tenía.

## Paneles que se estiran: 9-slice

Un último problema muy práctico. Dibujas un panel con las esquinas decoradas y un borde de dos píxeles. Funciona perfecto a 300×200, pero cuando el texto es más largo y el panel se estira a 600×200, **las esquinas se deforman** y el borde engorda.

La técnica que lo resuelve se llama **9-slice** (o nine-patch): divides la imagen en **nueve trozos** con dos líneas horizontales y dos verticales. Las cuatro esquinas no se estiran nunca, los bordes se estiran solo a lo largo y el centro se estira en las dos direcciones. Con una sola imagen pequeña tienes paneles, botones y bocadillos de diálogo de cualquier tamaño.

<!-- Imagen pendiente: esquema de un panel dividido en nueve partes (9-slice) -->

En Unity se definen los bordes del sprite en el **Sprite Editor**; en Godot, el nodo **NinePatchRect** hace el trabajo. Así que, cuando dibujes los paneles de tu interfaz, piensa desde el principio **qué parte se puede estirar y cuál no**: es mucho más fácil dibujarlo así que arreglarlo después.
