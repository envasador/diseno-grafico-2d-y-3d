# UT2.4 Tiles y sprite sheets

Abre Pyxel Edit por primera vez y lo primero que verás es una rejilla de casillas. Y la vas a seguir viendo por todas partes, porque en este programa todo gira alrededor de ella. Cada casilla es un tile, y entender para qué sirve es la llave de casi todo lo que harás en esta unidad: **con tiles construyes escenarios y con tiles construyes animaciones**.

## Qué es un tile

Un tile es **una celda de tamaño fijo dentro de una rejilla**, y en ella se dibuja. Según lo que dibujes, ese tile servirá para una de dos cosas muy distintas: **formar parte de un escenario o ser un fotograma de una animación**.

## Tiles para crear tilesets

Un **tileset** es un documento donde dibujas piezas de escenario **como si fueran las piezas de un Lego**: suelo, pared, esquina, borde, un trozo de agua. Cada pieza ocupa una celda de la rejilla, un tile. Después, en el motor o en un editor de niveles, esas piezas se colocan una junto a otra para construir mapas completos.

<figure markdown>
![Tileset y el escenario montado con sus piezas](../assets/ut2/tileset.png){ loading=lazy }
<figcaption>Cada pieza del tileset ocupa un tile. Combinándolas se construye el escenario. Tileset © de su autor. Uso con fines educativos.</figcaption>
</figure>

La ventaja es enorme: **con unas pocas decenas de tiles bien diseñados montas niveles gigantes**, el juego ocupa menos memoria y cambiar un nivel es tan fácil como mover piezas. ¿La pega? Que los tiles **tienen que encajar entre sí sin que se noten las costuras**, y eso tiene su truco. Lo verás con calma en [escenarios 2D](09-escenarios-2d.md).

## Tiles para crear animaciones

En animación, un tile **funciona igual que un fotograma (frame)** en cine, o que cada hoja de esos cuadernos que pasabas rápido con el pulgar para ver moverse un dibujo. Cada celda contiene una pose del personaje, y al reproducirlas seguidas aparece el movimiento.

<figure markdown>
![Un tile equivale a un frame de una película](../assets/ut2/tile-frame.png){ loading=lazy }
<figcaption>Tile = frame. Cada fila de la rejilla guarda una animación distinta del mismo personaje. Sprites © de sus respectivos autores. Uso con fines educativos.</figcaption>
</figure>

Mientras trabajas, el programa te deja previsualizar esos frames en bucle, y puedes exportar el resultado como un **GIF animado** para enseñarlo. Para el motor del juego, en cambio, lo que se exporta es un sprite sheet.

## Qué es un sprite sheet

Un sprite sheet es **una única imagen** (normalmente un PNG con transparencia) que contiene **todos los frames de una animación, o de varias**, colocados en una rejilla. El motor **carga esa imagen una sola vez** y va mostrando cada trozo en orden. Es mucho más eficiente que cargar un archivo por frame.

<figure markdown>
![Frames de una animación exportados como sprite sheet](../assets/ut2/spritesheet.png){ loading=lazy }
<figcaption>Al exportar todos los frames de una animación obtienes un sprite sheet en PNG. Sprites de <i>Scott Pilgrim vs. the World: The Game</i> © Ubisoft. Uso con fines educativos.</figcaption>
</figure>

Para que el motor pueda recortar el sprite sheet correctamente, todos los frames tienen que cumplir una condición: **tener exactamente el mismo tamaño**. Si un frame es más ancho porque el personaje extiende la espada, el tamaño de todos los frames tiene que crecer hasta ese ancho. El motor divide la imagen en celdas iguales y no sabe hacer otra cosa. No le pidas imaginación.

<figure markdown>
![Todos los frames de una animación comparten tamaño](../assets/ut2/frames-mismo-tamano.png){ loading=lazy }
<figcaption>Todos los tiles o frames de una animación comparten el mismo tamaño. Sprites de <i>Scott Pilgrim vs. the World: The Game</i> © Ubisoft. Uso con fines educativos.</figcaption>
</figure>

## Por qué potencias de dos

Las dimensiones más recomendadas para tiles y frames son potencias de dos: 16, 32, 64, 128, 256, 512, 1024. El motivo es **técnico**. Las tarjetas gráficas gestionan las texturas de forma más eficiente cuando sus dimensiones son potencias de dos, y los motores y herramientas de empaquetado (Unity, Godot, TexturePacker) están optimizados para esos tamaños. Además, las potencias de dos **se dividen entre sí sin restos**: un tile de 16 cabe exactamente dos veces en uno de 32, lo que hace que personajes y escenarios encajen en la misma rejilla.

¿Y si tu personaje ocupa 33×21 píxeles, que no es potencia de nada? Pues eliges **la potencia de dos inmediatamente superior que lo contenga** (aquí, 64×64, porque 33 ya no cabe en 32) y colocas el personaje dentro **dejando margen**. Ese margen te hará falta cuando el personaje se mueva, extienda los brazos o blanda un arma.

<figure markdown>
![Adaptar un sprite de 33x21 a un frame de 64x64](../assets/ut2/potencia-de-dos.png){ loading=lazy }
<figcaption>Un sprite de 33×21 no encaja en ninguna potencia de dos: se coloca dentro de un frame de 64×64. Sprites © de sus respectivos autores. Uso con fines educativos.</figcaption>
</figure>

Un consejo que te ahorrará rehacer trabajo: decide el tamaño del frame pensando en **la pose más grande** de todas las animaciones del personaje (normalmente el ataque) y usa ese tamaño para todas. Así todas sus animaciones comparten rejilla y el personaje no "salta" al cambiar de una a otra.

## Exportar para el motor

Antes de darle a exportar, repasa esta lista. Cada punto viene de un error que alguien cometió antes que tú:

- Formato **PNG** con transparencia, nunca JPG (la compresión con pérdida destroza el pixel art).
- Todos los frames del **mismo tamaño**, sin separaciones irregulares entre ellos.
- El **punto de apoyo** (los pies del personaje) en la misma posición en todos los frames, para que no parezca que flota o se hunde.
- Un **nombre de archivo** que indique personaje, animación y tamaño de frame, por ejemplo `caballero_walk_64x64.png`.
