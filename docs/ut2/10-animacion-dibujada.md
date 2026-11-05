# UT2.10 Animación dibujada

Llevas toda la unidad contando píxeles. Pero a lo mejor el juego que tienes en la cabeza se parece más a *Hollow Knight* que a *Celeste*: trazo de dibujo, formas suaves, nada de rejilla. ¿Hay que empezar de cero?

Para nada. **Casi todo lo que has visto sirve tal cual**: las poses clave, el timing, el idle, el walking cycle, los cuatro estados del ataque, los sprite sheets y el parallax. Lo que cambia es **la herramienta, el tamaño, lo que cuesta cada frame y la forma de montar el escenario**. En este apartado verás esas diferencias usando *Hollow Knight* como ejemplo, porque lo hizo un equipo diminuto (casi todo el arte salió de una sola persona, Ari Gibson) y aun así es uno de los juegos dibujados más bonitos que hay.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2IfLmc9ZHt8" title="Análisis del estilo artístico de Hollow Knight, de The Superforge" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

El vídeo está en inglés (puedes activar los subtítulos traducidos) y analiza **cómo el estilo de *Hollow Knight* está al servicio del juego**: por qué los personajes son tan simples, cómo se usa el color para separar zonas y cómo se integra todo con el sonido.

## Cómo está hecho Hollow Knight

Team Cherry dibujó **todo el arte y la animación a mano en Photoshop**, frame a frame, y lo guardó como **PNG normales y corrientes** que después montaba en Unity. Nada de trucos raros: los mismos sprites que vas a exportar tú. Ni siquiera la luz es real. La mayoría de brillos y penumbras son **formas suaves y semitransparentes dibujadas encima**, que dan la sensación de luz sin que el motor tenga que calcular nada.

<figure markdown>
![Idle de un personaje de Hollow Knight](https://images.squarespace-cdn.com/content/v1/606d4deb4db8c15ea53b3624/1619052826263-J027H0HTVKG7DP4GJZ4E/idle.gif){ loading=lazy }
<figcaption>Un idle dibujado frame a frame: pocos dibujos, formas muy limpias y el movimiento justo para que el personaje esté vivo. © Team Cherry, imagen enlazada desde su <a href="https://www.teamcherry.com.au/introducing-hollow-knight">blog</a>. Uso con fines educativos.</figcaption>
</figure>

En [su blog](https://www.teamcherry.com.au/introducing-hollow-knight) cuentan que eligieron un estilo **casi monocromo a propósito**: al quitar detalle, cada enemigo, personaje y escenario nuevo se producía mucho más deprisa, y eso les permitió llenar el mundo de bichos distintos. Y en unos comentarios que recoge [80 Level](https://80.lv/articles/breakdown-hollow-knights-art-style), uno de sus desarrolladores explicaba que **el número de frames de cada animación lo marcó el presupuesto**, y que la mayoría de ataques son **un único frame de tajo seguido de su continuación**. Si vienes de la [animación de ataque](08-animacion-de-ataque.md), eso te suena: anticipación corta, golpe instantáneo y que el final haga el resto.

## Diseñar un personaje que puedas animar

En pixel art el tamaño te obliga a simplificar. Dibujando no hay nada que te frene, y ahí está la trampa: **cada detalle que añades al diseño lo vas a redibujar en cada frame de cada animación**. Esa capa con cinco pliegues y tres hebillas que tan bien quedaba en la ilustración se convierte, multiplicada por cuarenta frames, en tu peor enemigo.

Fíjate en [Hornet](https://hollowknight.wiki/w/File:Hornet_(Hollow_Knight).png) o en el propio protagonista: **silueta muy marcada, colores planos y casi ningún detalle interior**. Se reconocen en un vistazo, en movimiento y a tamaño pequeño, que es justo lo que trabajaste en las [siluetas](../concept/siluetas.md) del concept.

<figure markdown>
![Bichos infectados de Hollow Knight](https://images.squarespace-cdn.com/content/v1/606d4deb4db8c15ea53b3624/1619052813236-DNRUCQVI9NGCJYSGIR5R/infected_bugs.gif){ loading=lazy }
<figcaption>Enemigos distintos con el mismo lenguaje de formas sencillas: así se puede producir mucha variedad sin morir en el intento. © Team Cherry, imagen enlazada desde su <a href="https://www.teamcherry.com.au/introducing-hollow-knight">blog</a>. Uso con fines educativos.</figcaption>
</figure>

Haz la prueba con tu personaje: **tápale los ojos al diseño y mira solo la mancha**. Si se entiende qué es y hacia dónde mira, se puede animar. Si necesita sus detalles para leerse, simplifícalo antes de dibujar el primer frame.

## El proceso de un frame dibujado

Un frame de pixel art lo vas puliendo píxel a píxel. Un frame dibujado **pasa por varias fases**, y lo importante es el orden en que las recorres:

1. **Rough.** Un boceto rápido y suelto de la pose, sin preocuparte por la línea.
2. **Limpieza.** Repasas el rough con una línea limpia en una capa nueva (o directamente con manchas de color, si tu estilo no lleva contorno).
3. **Color plano.** Rellenas cada zona con su color base.
4. **Luz y sombra.** Solo lo justo. En un estilo como el de *Hollow Knight*, casi nada.

El truco está en **animar la acción completa en rough antes de limpiar un solo frame**. Igual que con los [fotogramas clave](05-principios-de-animacion.md#fotogramas-clave), reproduces los borradores, compruebas que la acción y el timing funcionan y solo entonces pasas a limpio. Limpiar un frame precioso que luego descubres que sobraba es de las cosas más tristes que le pueden pasar a un animador.

Si quieres ver cómo de sueltos pueden ser esos primeros dibujos, el museo ACMI de Melbourne expuso [los cuadernos de desarrollo de Hollow Knight](https://www.acmi.net.au/works/99982--hollow-knight-paper-sketchbook-a5-moleskine-red-cover/) de Ari Gibson: **todo empezó en un Moleskine**.

## Animar a unos y a doses

En animación tradicional se habla de animar **a unos** cuando cada dibujo dura un fotograma y **a doses** cuando cada dibujo se mantiene dos fotogramas seguidos. A 24 fotogramas por segundo, animar a doses significa **12 dibujos por segundo en lugar de 24**. Es decir, la mitad de trabajo.

¿Se nota? Mucho menos de lo que crees. La mayor parte de la animación clásica se hizo a doses, y en un videojuego el efecto es todavía más suave porque el ojo está pendiente de jugar. Reserva los unos para los momentos muy rápidos (un tajo, un impacto) y anima el resto a doses o incluso a treses.

En el motor esto se traduce en algo que ya conoces del [timing](05-principios-de-animacion.md#timing): **no todos los frames tienen que durar lo mismo**. Dibuja menos y deja que cada dibujo aguante en pantalla el tiempo que necesita.

| Forma de animar | Dibujos por segundo (a 24 fps) | Cuándo usarla |
|---|---|---|
| A unos | 24 | Movimientos muy rápidos o muy suaves, en momentos puntuales |
| A doses | 12 | La opción por defecto para casi todo |
| A treses | 8 | Idles, gestos tranquilos, personajes de fondo |

## Que el personaje no cambie de un frame a otro

En pixel art la rejilla te sujeta: si la cabeza mide 8 píxeles, mide 8 en todos los frames. Dibujando a mano no hay rejilla, y es facilísimo que **el personaje engorde, encoja o cambie de proporciones** entre un frame y el siguiente sin que te des cuenta hasta que lo reproduces (y entonces tiembla como un flan).

Para evitarlo tienes dos aliados. El primero es tu [model sheet](../concept/hojas-de-produccion.md#model-sheet), que aquí pasa de ser recomendable a **imprescindible**: tenlo siempre abierto al lado. El segundo es el **papel cebolla (onion skin)**, que te muestra en transparencia el frame anterior y el siguiente para comparar tamaños mientras dibujas. Y otra vez, cuanto más sencillo es el diseño, más fácil es mantenerlo estable.

## Escenarios por capas

Los escenarios de *Hollow Knight* **se montan colocando piezas dibujadas** (rocas, columnas, raíces, plantas) en capas a distintas profundidades. Nada encaja en una rejilla, y por eso no se nota la repetición. Como esas capas viven en un espacio con profundidad, al mover la cámara cada una se desplaza a su ritmo y el [parallax](09-escenarios-2d.md#fondos-y-parallax) sale solo.

<figure markdown>
![Escena atmosférica de Hollow Knight](https://images.squarespace-cdn.com/content/v1/606d4deb4db8c15ea53b3624/1619052859725-2QOOV2LX2JMOHJ4ZRFM3/atmospheric_example_01_banner.gif){ loading=lazy }
<figcaption>Capas de piezas dibujadas, niebla y partículas: la profundidad sale de apilar planos, sin ningún tile a la vista. © Team Cherry, imagen enlazada desde su <a href="https://www.teamcherry.com.au/introducing-hollow-knight">blog</a>. Uso con fines educativos.</figcaption>
</figure>

Ahora bien, el personaje necesita un suelo por el que andar y unas paredes con las que chocar, y eso **sigue siendo un conjunto de piezas que se repiten**. Tienes dos caminos. El primero es un **tileset dibujado**: las mismas reglas de [tilesets](09-escenarios-2d.md#tilesets-construir-con-piezas) que ya conoces (que encaje, que cubra todos los casos, con variantes), pero con piezas más grandes y trazo de dibujo. El segundo, en Unity, es el paquete **2D Sprite Shape**, que repite una textura dibujada a lo largo de una curva que trazas en el editor. Es muy cómodo para suelos orgánicos con cuestas y bordes irregulares. Sobre esa base jugable colocas la decoración libremente, en capas por delante y por detrás.

## Qué cambia respecto al pixel art

| Aspecto | Pixel art | Animación dibujada |
|---|---|---|
| Herramienta | Editor de pixel art (Aseprite, Pyxel Edit) | Programa de dibujo con línea de tiempo (Krita, Clip Studio Paint) |
| Tamaño | Lienzo pequeño y fijo, en potencias de dos | Se dibuja más grande y se reduce al exportar |
| Coste de cada frame | Bajo o medio | Alto: cada frame pasa por rough, limpieza y color |
| Número de frames | Pocos frames bien elegidos | Todavía menos, animando a doses o a treses |
| Consistencia | La rejilla la garantiza | Depende del model sheet y del papel cebolla |
| Escenario | Tileset en rejilla y fondos por capas | Base jugable con tiles o Sprite Shape y decoración libre en capas |
| Exportación | Sprite sheet en PNG | Sprite sheet en PNG (igual) |
