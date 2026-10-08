# UT1.2 Del boceto a la ilustración

¿Te ha pasado alguna vez que dibujas algo con todo el cuidado del mundo, te pasas una hora con los detalles y al final hay algo que no funciona, pero no sabes qué? **Casi siempre el problema está debajo**: una proporción rara, una pose sin fuerza, un horizonte mal colocado. Y los detalles, por bonitos que sean, solo lo disimulan.

Por eso este apartado va de **lo que se decide antes de afinar**: cómo construyes las formas, qué proporciones eliges, dónde pones el horizonte. Y al final lo juntamos todo en un recorrido completo en Affinity, del boceto a la imagen exportada.

## Construir con formas simples

Cualquier cosa que dibujes (un personaje, un árbol, una nave espacial) se puede reducir a **esferas, cajas, cilindros y conos**. Empezar por ahí te obliga a pensar en **el volumen y en la proporción** antes de entretenerte con el detalle, que es justo donde se esconden los errores.

Un dragón, por ejemplo, es un cilindro que se va estrechando (cuello y cola), una esfera (la cabeza) y dos triángulos (las alas). Cuando esas masas funcionan, **el detalle casi se coloca solo**.

Para verlo en acción, Seba Guidobono dibuja en este vídeo varios personajes y objetos **partiendo solo de formas básicas** y añadiendo detalle encima, capa a capa. Fíjate en cuánto tiempo pasa con las formas antes de dibujar un solo detalle: ahí está el truco. Y después haz la prueba con algo que tengas delante (una taza, una silla, tu mochila) antes de pasar a tu personaje.

<iframe width="560" height="315" src="https://www.youtube.com/embed/epfmqEQ4mfQ" title="El secreto para dibujar bien: las formas básicas, de Seba Guidobono" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

*[El secreto para dibujar bien. Las formas básicas](https://www.youtube.com/watch?v=epfmqEQ4mfQ), de Seba Guidobono. © de su autor; uso con fines educativos.*

Además, esta forma de trabajar encaja de maravilla con el vectorial, porque esas formas básicas son literalmente las primeras capas de tu archivo. Y enlaza con dos herramientas de concept que ya conoces: las [siluetas](../concept/siluetas.md), para comprobar si el personaje se reconoce en negro, y el [lenguaje de formas](../concept/thumbnails.md), que decide qué transmite (círculos amables, cuadrados sólidos, triángulos peligrosos).

Si te cuesta pasar de la silueta en negro al personaje dibujado, repasa el **sistema de boceto por módulos** de JS Linares que tienes en la página de [siluetas](../concept/siluetas.md#como-disenar-desde-la-silueta). La parte [de la mancha al dibujo](https://www.youtube.com/watch?v=n4E35sQ1whQ&t=623s) es justo el paso que vas a dar aquí: de masas simples a un personaje con estructura.

## Proporciones

La regla de medir de un personaje es **su propia cabeza**. Una figura realista mide **entre siete y ocho cabezas**, y cuantas menos mide, más joven, más tierna o más cómica parece. Elegir la proporción es una **decisión de estilo**, y una vez tomada toca **ser coherente con ella en todo el juego**.

| Proporción | Sensación | Dónde la ves |
|---|---|---|
| 7-8 cabezas | Realista, adulta | Juegos de acción y aventura realistas |
| 4-6 cabezas | Estilizada, versátil | Muchos juegos de aventura y plataformas |
| 2-3 cabezas (chibi) | Tierna, cómica | Juegos de móvil y RPG en pixel art |

Un detalle para cuando llegues a la UT2: si tu personaje va a acabar convertido en un sprite pequeñito, las proporciones chibi tienen además un motivo muy práctico. Con la cabeza grande, **la cara y la expresión se leen con cuatro píxeles**.

## Pose y expresión

Un personaje de juego se pasa la vida corriendo, saltando y pegando, así que **su diseño tiene que aguantar en movimiento**. Aquí la herramienta estrella es la **línea de acción**: una curva que atraviesa el cuerpo de la cabeza a los pies y marca hacia dónde va la pose. Si esa línea es recta, el personaje parece estar esperando el autobús, aunque en teoría esté dando un salto mortal. Si tiene una curva clara, **transmite energía**. Dibújala primero y construye la figura encima con formas simples, marcando hombros, codos, caderas y rodillas con círculos.

Con la expresión pasa lo mismo: **simplifica**. **Cejas, ojos y boca cuentan casi toda la emoción.** La mejor prueba de que la cara de tu personaje funciona es dibujarle cinco o seis expresiones distintas; tienes el formato en [hojas de expresiones y de poses](../concept/hojas-de-produccion.md#hojas-de-expresiones-y-de-poses).

## Escenarios: perspectiva y planos

En un escenario, lo primero que decides es dónde va la **línea del horizonte**, porque **está a la altura de los ojos de quien mira**. Lo que queda por encima lo ves desde abajo, y lo que queda por debajo, desde arriba. Si colocas el horizonte bajo, todo parecerá enorme. Si lo subes, verás la escena desde arriba, como en un juego de estrategia.

A partir de ahí, las líneas que se alejan van a parar a **puntos de fuga**:

| Perspectiva | Cómo funciona | Cuándo usarla |
|---|---|---|
| Un punto de fuga | Las líneas de profundidad van a un único punto | Pasillos, caminos, interiores vistos de frente |
| Dos puntos de fuga | Se ven dos caras del objeto, cada una hacia su punto | Edificios y calles vistos en esquina |
| Tres puntos de fuga | Se añade un punto arriba o abajo | Vistas muy picadas o contrapicadas |
| Isométrica | Las paralelas nunca convergen | Juegos de estrategia, simulación y mucho pixel art |

La **isométrica** merece que nos paremos un momento, porque te la vas a volver a encontrar en la UT2. En ella las cosas mantienen su tamaño aunque estén lejos, así que **cualquier pieza encaja en cualquier punto de la rejilla**. Justo lo que necesita un juego construido a base de piezas repetidas. En pixel art se usa una variante en la que las líneas avanzan **dos píxeles en horizontal por cada uno que suben**, porque así los bordes quedan limpios y sin dientes raros.

Además de la perspectiva, un escenario se lee por **planos**: primer plano, plano medio (donde suele pasar la acción) y fondo. Fíjate en cualquier paisaje de montaña: cuanto más lejos está algo, menos contraste tiene, menos detalle y más se parece al color del cielo. Es la **perspectiva atmosférica**, y es el truco más barato que existe para dar profundidad a una ilustración. En [Color y luz](../concept/color.md) tienes cómo elegir esos valores.

## Composición

Cuando juntas personaje y escenario, **la composición decide qué se mira primero**. Con tres recursos resuelves casi cualquier imagen:

- Coloca el punto de interés cerca de uno de los cruces de la **regla de los tercios**, en lugar de plantarlo en el centro exacto.
- Aprovecha las líneas del escenario (un camino, una pared, una rama) para **llevar la mirada hasta él**.
- Reserva para ese punto **el mayor contraste de toda la imagen**.

Todo esto se decide en los [thumbnails](../concept/thumbnails.md), antes de abrir el archivo bueno. **Es mucho más barato equivocarse en un dibujo del tamaño de una uña.**

## El recorrido completo en Affinity

Con los fundamentos claros, así avanza una ilustración de principio a fin. Tómalo como un **orden de trabajo flexible**: cada ilustración te pedirá quedarte más en una fase u otra.

1. **Boceto.** En el estudio Pixel, en una capa aparte, dibuja el boceto a partir del thumbnail que elegiste. Bájale la opacidad y bloquéala para que te sirva de guía.
2. **Formas.** En el estudio Vector, construye encima las masas principales con formas básicas y booleanas, cada pieza en su capa y con su nombre. Rellénalo todo de negro un momento: si la silueta se lee, vas bien.
3. **Contornos.** Afina las curvas con la herramienta Nodo o redibuja con la Pluma las piezas que lo pidan.
4. **Color base.** Pon colores planos de tu paleta. Si la guardas como paleta del documento, cambiar un tono más adelante es cosa de segundos.
5. **Luz y sombra.** Crea capas de sombra y de luz recortadas dentro de cada pieza y juega con los modos de fusión: Multiplicar para las sombras, Pantalla o Superponer para las luces.
6. **Escenario.** Monta el fondo por planos, con menos contraste y detalle cuanto más lejos, y añade una sombra de contacto bajo los pies para que el personaje no parezca flotar.
7. **Revisión y exportación.** Mira la imagen en pequeño para comprobar que se lee, ordena y agrupa las capas, guarda el `.af` y exporta en el formato que pide el destino.

## Para practicar

Tres ejercicios cortos para soltar la mano con el programa antes de meterte con tus ilustraciones:

- Coge un objeto de tu mesa (una grapadora, una taza, unos auriculares) y redibújalo en Affinity solo con formas básicas y operaciones booleanas. La pluma, prohibida. Verás cómo empiezas a ver las masas antes que el detalle.
- Dibuja el mismo personaje sencillo con tres cabezas de altura y con siete. ¿Qué te cuenta cada versión? ¿Cuál encajaría con el juego que tienes en mente?
- Compón un escenario pequeño en tres planos usando solo tres grises (claro, medio y oscuro) y decide dónde va el punto de interés. **Si se entiende en gris, funcionará en color.**

Y si quieres seguir practicando por tu cuenta, ten a mano el canal de **[Aleks Font](https://www.youtube.com/@AleksFont)**. Alex y Aida son ilustradores profesionales y suben cada semana un tutorial sobre lo mismo que acabas de ver: **anatomía, perspectiva, color, paisaje y composición**. Cuando un dibujo se te atasque (unas manos que no salen, un escenario que no tiene profundidad), busca el tema en su canal antes de rendirte. Lo más probable es que tengan un vídeo justo sobre eso.
