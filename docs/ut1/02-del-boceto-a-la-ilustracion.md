# UT1.2 Del boceto a la ilustración

Manejar el programa te permite ejecutar una idea, pero lo que hace que una ilustración funcione se decide antes: cómo construyes las formas, qué proporciones eliges, dónde colocas el horizonte de un escenario. En este apartado repasamos esos fundamentos y después los juntamos en un recorrido completo en Affinity, del boceto a la imagen exportada.

## Construir con formas simples

Cualquier cosa que dibujes (un personaje, un árbol, una nave) se puede descomponer en esferas, cajas, cilindros y conos. Empezar por ahí te obliga a pensar en el volumen y la proporción antes que en el detalle, que es donde se suelen esconder los errores. Un dragón es un cilindro que se estrecha (cuello y cola), una esfera (la cabeza) y dos triángulos (las alas); cuando esas masas funcionan, el detalle se coloca encima sin esfuerzo.

Esta forma de trabajar encaja con el vectorial, porque esas formas básicas son literalmente las primeras capas de tu archivo. Y conecta con dos herramientas de concept que ya conoces: las [siluetas](../concept/siluetas.md), que comprueban si el personaje se reconoce en negro, y el [lenguaje de formas](../concept/thumbnails.md), que decide qué transmite (círculos amables, cuadrados sólidos, triángulos peligrosos).

## Proporciones

La unidad de medida clásica de un personaje es su propia cabeza. Una figura realista mide entre siete y ocho cabezas, y cuantas menos mide, más joven, tierna o cómica parece. Elegir la proporción es una decisión de estilo, y una vez tomada hay que mantenerla en todo el juego.

| Proporción | Sensación | Dónde la ves |
|---|---|---|
| 7-8 cabezas | Realista, adulta | Juegos de acción y aventura realistas |
| 4-6 cabezas | Estilizada, versátil | Muchos juegos de aventura y plataformas |
| 2-3 cabezas (chibi) | Tierna, cómica | Juegos de móvil y RPG en pixel art |

Si tu personaje va a acabar como un sprite pequeño en la UT2, las proporciones chibi tienen además un motivo práctico: con la cabeza grande, la cara y la expresión se leen con muy pocos píxeles.

## Pose y expresión

Un personaje de juego se mueve, así que su diseño tiene que funcionar en acción. La herramienta básica es la **línea de acción**, una curva que atraviesa el cuerpo de la cabeza a los pies y marca la dirección de la pose. Si esa línea es recta, la pose resulta rígida; si tiene una curva clara, transmite energía. Dibújala primero y construye la figura encima con formas simples, marcando las articulaciones (hombros, codos, caderas, rodillas) con círculos.

La expresión sigue la misma lógica de simplificar: cejas, ojos y boca cuentan casi toda la emoción. Una hoja con cinco o seis expresiones del mismo personaje es la mejor comprobación de que su cara funciona, y tienes el formato en [hojas de expresiones y de poses](../concept/hojas-de-produccion.md#hojas-de-expresiones-y-de-poses).

## Escenarios: perspectiva y planos

En un escenario, la primera decisión es dónde va la **línea del horizonte**, porque coincide con la altura de los ojos de quien mira. Lo que queda por encima se ve desde abajo y lo que queda por debajo se ve desde arriba. A partir de ahí, las líneas que se alejan convergen en puntos de fuga.

| Perspectiva | Cómo funciona | Cuándo usarla |
|---|---|---|
| Un punto de fuga | Las líneas de profundidad van a un único punto | Pasillos, caminos, interiores vistos de frente |
| Dos puntos de fuga | Se ven dos caras del objeto, cada una hacia su punto | Edificios y calles vistos en esquina |
| Tres puntos de fuga | Se añade un punto arriba o abajo | Vistas muy picadas o contrapicadas |
| Isométrica | Las paralelas nunca convergen | Juegos de estrategia, simulación y mucho pixel art |

La isométrica merece una nota porque la vas a volver a ver en la UT2. En ella los objetos mantienen su tamaño con la distancia, así que cualquier pieza puede colocarse en cualquier punto de la rejilla y encajar con las demás, que es justo lo que necesita un juego construido con piezas repetidas. En pixel art se suele usar una variante en la que las líneas avanzan dos píxeles en horizontal por cada uno que suben, porque así los bordes quedan limpios.

Además de la perspectiva, un escenario se lee por **planos**: primer plano, plano medio (donde suele estar la acción) y fondo. Cuanto más lejos está algo, menos contraste y detalle tiene y más se acerca al color del cielo. Es la perspectiva atmosférica, la forma más barata de dar profundidad a una ilustración; en [Color y luz](../concept/color.md) tienes cómo elegir esos valores.

## Composición

Cuando juntas personaje y escenario, la composición decide qué se mira primero. Tres recursos cubren casi todos los casos: colocar el punto de interés cerca de uno de los cruces de la regla de los tercios en lugar de en el centro exacto, aprovechar las líneas del escenario (un camino, una pared, una rama) para llevar la mirada hacia él y reservar el mayor contraste de la imagen para ese punto. Todo esto se decide en los [thumbnails](../concept/thumbnails.md), antes de abrir el archivo definitivo.

## El recorrido completo en Affinity

Con los fundamentos claros, así avanza una ilustración de principio a fin. Tómalo como un orden de trabajo flexible: cada ilustración te pedirá detenerte más en una fase u otra.

1. **Boceto.** En el estudio Pixel, en una capa aparte, dibuja el boceto a partir del thumbnail elegido. Bájale la opacidad y bloquéala para que te sirva de guía.
2. **Formas.** En el estudio Vector, construye encima las masas principales con formas básicas y booleanas, cada pieza en su capa y con su nombre. Rellénalo todo de negro un momento para comprobar la silueta.
3. **Contornos.** Ajusta las curvas con la herramienta Nodo o redibuja con la Pluma las piezas que lo necesiten.
4. **Color base.** Aplica colores planos de tu paleta. Si la guardas como paleta del documento, cambiar un tono más adelante es inmediato.
5. **Luz y sombra.** Crea capas de sombra y de luz recortadas dentro de cada pieza y prueba modos de fusión: Multiplicar para las sombras, Pantalla o Superponer para las luces.
6. **Escenario.** Monta el fondo por planos, con menos contraste y detalle cuanto más lejos, y añade una sombra de contacto que ancle al personaje al suelo.
7. **Revisión y exportación.** Mira la imagen en pequeño para comprobar que se lee, ordena y agrupa las capas, guarda el `.af` y exporta en el formato que pide el destino.

## Para practicar

Estos ejercicios son cortos y te sirven para soltarte con el programa antes de empezar tus ilustraciones:

- Elige un objeto de tu mesa (una grapadora, una taza, unos auriculares) y redibújalo en Affinity solo con formas básicas y operaciones booleanas, sin usar la pluma. Te obliga a ver las masas antes que el detalle.
- Dibuja el mismo personaje sencillo con tres cabezas de altura y con siete. Compara qué transmite cada versión y cuál encajaría con el juego que tienes en mente.
- Compón un escenario pequeño en tres planos usando solo tres grises (claro, medio y oscuro) y decide dónde va el punto de interés. Si se entiende en gris, funcionará en color.

## Lo que te llevas de este apartado

Una buena ilustración se decide antes de abrir el programa: formas simples, una proporción elegida a propósito y un escenario con el horizonte y los planos claros. En Affinity ese orden se traduce en boceto, formas, color plano y luz, con cada cosa en su capa para poder cambiarla.
