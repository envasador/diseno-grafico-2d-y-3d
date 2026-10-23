# Anexo A.6 De Figma al motor

Hasta aquí has visto qué tiene que hacer una interfaz, qué tipos hay y qué reglas conviene respetar. Este apartado va de **cómo se trabaja**: los pasos para pasar de "mi juego necesita un HUD" a una interfaz funcionando en Unity o en Godot.

Lo que vas a leer está ordenado en pasos, pero en la práctica **se solapan y se repiten**. Mientras haces los wireframes descubres un dato que te faltaba en el inventario; al probar en el motor te das cuenta de que un icono no se lee y vuelves a Figma. Es lo normal, y es la misma forma de trabajar que ya conoces del [proceso creativo](../concept/proceso-creativo.md).

## Haz inventario de la información

Antes de dibujar nada, apunta **todo lo que el jugador necesita saber y en qué momento lo necesita**. Una tabla sencilla basta: en las filas, cada dato (vida, munición, objetivo, dinero, mapa…); en las columnas, los momentos del juego (explorando, en combate, en un diálogo, en pausa). Marca en cada casilla si ese dato hace falta ahí.

Esa tabla te dice casi sola en qué [capa](01-ui-y-ux.md) va cada cosa. Lo que hace falta en todas las columnas es información crítica. Lo que solo hace falta en una es contextual o va a un menú. Y lo que no hace falta en ninguna (pasa más de lo que parece) **no debería estar en la interfaz**.

## Reúne referencias del género

Igual que hiciste en el [moodboard](../concept/moodboard.md), reúne en Figma **capturas de interfaces de juegos del mismo género** que el tuyo. Agrúpalas por temas: HUD en combate, menús de pausa, inventarios, pantallas de título. Apunta al lado de cada una qué te funciona y qué no.

Esto sirve para dos cosas. Por un lado, para descubrir **qué convenciones espera el jugador** (la [ley de Jakob](03-leyes-de-ux.md) en acción): si todos los juegos de tu género ponen la vida arriba a la izquierda, hay un motivo. Por otro, para encontrar **ideas que nadie del género está usando** y que podrías aprovechar.

La web [Game UI Database](https://www.gameuidatabase.com/) tiene miles de capturas de interfaces organizadas por juego, por tipo de pantalla y por elemento. Es una mina para esta fase.

## Wireframes en gris

Un **wireframe** es un boceto de la pantalla **solo con cajas grises y texto**, sin colores, sin estilo y sin ilustraciones. Se hace así a propósito: si no hay estilo, solo puedes juzgar **dónde está cada cosa, qué tamaño tiene y qué se lee primero**, que es justo lo que hay que decidir en este momento.

Haz los wireframes en Figma sobre un marco de **1920×1080 con la [safe area](04-reticula-safe-area-y-escalado.md) marcada**, y haz uno por cada pantalla y cada estado importante: HUD en exploración, HUD en combate, menú de pausa, inventario. Un buen truco es colocar debajo **una captura del juego** (o de un juego parecido, si todavía no tienes el tuyo) para ver cómo convive la interfaz con la acción.

!!! example "Haz la prueba"
    Enseña tu wireframe del HUD a alguien durante cinco segundos y quítaselo. Pregúntale dónde estaba la vida y cuánta munición quedaba. Si no lo sabe, la jerarquía todavía no funciona, y es mucho mejor descubrirlo ahora, con cajas grises, que cuando ya tengas todo dibujado.

## Aplica el estilo de la biblia de arte

Con la estructura decidida, toca vestirla, y el estilo ya lo tienes: **la interfaz sale de tu [biblia de arte](../concept/biblia-de-arte.md)**. La misma paleta (con los colores de estado bien elegidos), el mismo lenguaje de formas (si tus personajes son redondeados, los botones probablemente también) y el mismo acabado (pixel art, vector, pintado a mano).

Cuando lo tengas claro, **añade a tu biblia de arte un capítulo de interfaz** con sus reglas: tipografías y tamaños, colores de cada estado, márgenes, cómo son los iconos. Igual que con los personajes, la idea es que cualquier persona pueda dibujar un botón nuevo **y que parezca del mismo juego**.

## Componentes y estados en Figma

En Figma, cada pieza que se repite (un botón, una casilla de inventario, una barra) debería ser un **componente**. Así, cuando cambies el componente principal, cambian todas sus copias a la vez. Y los distintos estados de cada pieza (normal, seleccionado, pulsado, desactivado) se organizan como **variantes** del mismo componente.

Esto tiene una ventaja que se agradece mucho al final: **te obliga a dibujar todos los estados**. Un botón con una sola variante en Figma es un botón al que le faltan tres dibujos.

Un detalle más que conviene prever: **los textos cambian de longitud al traducirse**. Una frase en alemán puede ocupar bastante más que en español, así que deja aire en los botones y en los paneles, o diseña paneles que se puedan estirar con la técnica de [9-slice](04-reticula-safe-area-y-escalado.md).

## Prepara los assets para el motor

Cuando el diseño esté cerrado, toca **exportar las piezas por separado** para que el programador (o tú) las monte en el motor. Unas cuantas costumbres te van a ahorrar disgustos:

- **Exporta en PNG con transparencia** y al tamaño al que se van a ver con la resolución de referencia. Para pixel art, exporta al tamaño original, sin ampliar.
- **Nombra los archivos de forma sistemática**, con el tipo de pieza, su nombre y su estado: `ui_boton_jugar_normal.png`, `ui_boton_jugar_seleccionado.png`. Dentro de un mes habrá ochenta archivos en la carpeta.
- **Marca qué piezas son 9-slice** y dónde van sus cortes.
- **Comprueba la licencia de las fuentes.** Una fuente gratuita para uso personal no se puede usar en un juego que se publica. Las de [Google Fonts](https://fonts.google.com/) tienen licencias abiertas que lo permiten.
- **Apunta las medidas y los anclajes** de cada elemento: a qué esquina va atado y a cuántos píxeles del borde.

En Affinity y en Figma, las **porciones** (slices, en inglés) te permiten marcar cada pieza una vez y exportarlas todas de golpe, tal como viste en la [UT1](../ut1/01-ilustrar-con-affinity.md).

## Prueba en el motor y ajusta

Un mockup (la imagen de cómo quedará la pantalla terminada) es una imagen quieta. Hasta que no ves la interfaz **con el juego en marcha**, con explosiones detrás y el personaje moviéndose, no sabes si funciona. Por eso el último paso (que en realidad se repite muchas veces) es **montarla en el motor y probarla jugando**.

Pídele a alguien que juegue sin que le expliques nada, y **míralo jugar sin intervenir**. Fíjate en dónde mira, en qué momentos duda y en qué botones pulsa por error. Al terminar, unas pocas preguntas sencillas dan mucha información: ¿encontraste lo que necesitabas sin dejar de mirar la acción? ¿Hubo algún momento en que la interfaz te tapó algo? ¿Te perdiste en algún menú?

Y luego, de vuelta a Figma. **Cada vuelta del ciclo hace la interfaz un poco mejor**, y es así como trabajan los estudios de verdad: diseñar, probar, corregir y volver a probar.
