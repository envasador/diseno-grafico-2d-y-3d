# UT2.9 Escenarios 2D

Tu personaje ya respira, anda y ataca, pero todavía flota en un fondo transparente. Necesita un mundo, y en 2D ese mundo se construye de una forma muy particular: con piezas pequeñas que se repiten para formar el suelo y las paredes, y con capas que se mueven a distintas velocidades para simular profundidad. En este apartado verás cómo se planifican los dos, y qué decisiones de perspectiva tienes que tomar antes de dibujar la primera pieza.

## Primero, la perspectiva

Antes de dibujar un solo tile tienes que decidir desde dónde mira la cámara, porque cambia la forma de dibujar cada elemento del escenario. En 2D hay cuatro vistas principales:

| Vista | Cómo se ve el mundo | Ejemplos |
|---|---|---|
| Lateral (side view) | De perfil, con gravedad hacia abajo | *Celeste*, *Hollow Knight*, *Dead Cells* |
| Cenital (top-down) | Desde arriba, casi en planta | *Hotline Miami*, juegos clásicos de naves |
| Tres cuartos (3/4) | Desde arriba y ligeramente de frente: ves el techo y la fachada | *Stardew Valley*, *The Legend of Zelda: A Link to the Past* |
| Isométrica | En diagonal, con ángulos fijos, sin punto de fuga | *Hades*, *Into the Breach* |

Personaje y escenario tienen que compartir vista. Un personaje dibujado de perfil sobre un suelo en tres cuartos rompe la ilusión al instante.

La vista isométrica tiene una particularidad en pixel art: sus líneas se construyen con una proporción de dos píxeles en horizontal por uno en vertical, que es la que produce diagonales limpias sin dientes de sierra.

## Tilesets: construir con piezas

Ya viste en [tiles y sprite sheets](04-tiles-y-sprite-sheets.md) que un tileset es un conjunto de piezas de escenario dibujadas en una rejilla. Diseñar uno bueno tiene tres retos.

El primero es que **las piezas encajen**. Un tile de suelo tiene que poder repetirse a izquierda y derecha sin que se vea la costura. Para comprobarlo, colócalo en una rejilla de tres por tres copias y busca cualquier línea o patrón que delate la repetición.

El segundo es **cubrir todos los casos**. Un bloque de tierra necesita pieza central, bordes superior e inferior, laterales, cuatro esquinas exteriores y cuatro interiores. Si falta alguna, el diseñador de niveles no podrá cerrar ciertas formas. Los motores tienen sistemas de autotiling (las reglas de tiles en Unity, los terrains de Godot) que eligen automáticamente la pieza correcta según sus vecinas, pero necesitan que todas estén dibujadas.

El tercero es **evitar la monotonía**. Si el mismo tile de hierba se repite doscientas veces, el ojo detecta el patrón enseguida. Dibuja dos o tres variantes de las piezas más frecuentes (una con una piedra, otra con una flor) y mézclalas.

## Montar el nivel

Los tiles se colocan con un editor de mapas. Puedes usar **Tiled**, un editor gratuito que exporta mapas a casi cualquier motor, o los editores integrados: **Tilemap** en Unity y **TileMapLayer** en Godot. En todos, el flujo es parecido: cargas el tileset, defines el tamaño del tile y pintas el nivel con las piezas como si fueran pinceles.

Organiza el mapa en capas separadas. Una capa para el suelo y las paredes con las que el personaje colisiona, otra para la decoración que queda detrás, otra para la que queda delante. Esa separación facilita que programación configure las colisiones y te permite cambiar la decoración sin tocar lo jugable.

## Fondos y parallax

Lo que queda detrás del nivel jugable (el cielo, las montañas, la ciudad lejana) no suele construirse con tiles. Se pinta como ilustraciones grandes, a menudo en un programa de ilustración, divididas en capas según su distancia.

El **parallax scrolling** aprovecha esas capas: cuando la cámara se mueve, cada capa se desplaza a una velocidad distinta. Las lejanas se mueven muy despacio y las cercanas más deprisa, exactamente como cuando miras por la ventanilla de un tren. Con tres o cuatro capas ya se consigue una sensación de profundidad muy convincente.

Al pintar las capas de parallax ten en cuenta tres cosas:

- **Perspectiva atmosférica.** Cuanto más lejos está una capa, menos contraste, menos saturación y más se acerca al color del cielo.
- **Continuidad horizontal.** Las capas que se repiten al desplazarse tienen que enlazar por los lados sin costura, igual que los tiles.
- **Jerarquía con lo jugable.** El fondo nunca debe competir con el primer plano. Si el jugador duda de si una plataforma es suelo o decoración, el fondo tiene demasiado contraste.

## La fase de concept del escenario

Los escenarios también pasan por concept antes de producirse. Unos [thumbnails](../concept/thumbnails.md) de composición te ayudan a decidir cuántas capas de profundidad tendrá la escena, un [color key](../concept/color.md#color-keys-y-color-script) fija la paleta y la atmósfera, y una [hoja de entornos](../concept/hojas-de-produccion.md#hojas-de-props-y-de-entornos) con las piezas del tileset y el personaje al lado para comparar escala evita sorpresas al montar el nivel.

## Lo que te llevas

Un escenario 2D empieza por decidir la perspectiva, que tiene que coincidir con la del personaje. Lo jugable se construye con tilesets que encajan, cubren todos los casos y tienen variantes; lo lejano se pinta en capas de parallax que pierden contraste con la distancia y nunca compiten con el primer plano.
