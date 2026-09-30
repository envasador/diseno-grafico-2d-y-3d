# UT2.1 El arte 2D en videojuegos

Pon una captura de *Celeste* al lado de una de *Hollow Knight* y otra de *Cuphead*. Los tres son juegos en 2D, salieron con pocos años de diferencia... y no se parecen en nada. Si alguna vez has pensado que el 2D es "lo de los juegos antiguos", aquí tienes la prueba de lo contrario: bajo esa etiqueta caben técnicas muy distintas, cada una con su forma de dibujar, de animar y de producir.

Antes de ponerte a pixelar conviene que tengas el mapa completo, porque la técnica que elijas va a marcar todo lo que venga después.

## Tres formas de hacer arte 2D

El **pixel art** construye las imágenes colocando cada píxel de forma deliberada, con una resolución y una paleta limitadas a propósito. Es el estilo de *Celeste*, *Stardew Valley* o *Dead Cells*. Por su aspecto retro parece sencillo, y es justo al revés: con tan pocos píxeles, mover un solo punto cambia la expresión de una cara. Se anima dibujando cada frame.

El **arte vectorial** define las formas con curvas matemáticas en lugar de píxeles, así que se puede escalar a cualquier tamaño sin perder calidad. Produce imágenes limpias, de colores planos, muy habituales en juegos móviles y casuales. Encaja muy bien con la animación por piezas y por huesos.

El **arte pintado a mano** (hand-drawn) usa técnicas de ilustración digital para conseguir un acabado de dibujo o pintura tradicional. *Hollow Knight* y *Cuphead* son los ejemplos clásicos. Permite el mayor nivel de detalle y expresividad, y lo paga con una producción mucho más lenta (en *Cuphead* se dibujó a mano cada fotograma, y se nota).

| Técnica | Ventaja principal | Coste principal | Herramientas habituales |
|---|---|---|---|
| Pixel art | Lectura clara y estética muy reconocible | Cada frame se dibuja a mano | Aseprite, Pyxel Edit |
| Vectorial | Escalable y fácil de animar por piezas | Puede resultar frío si no se estiliza | Affinity, Illustrator, Inkscape |
| Pintado a mano | Máxima expresividad y detalle | Producción lenta, archivos pesados | Photoshop, Krita, Clip Studio Paint |

## Tres formas de animar en 2D

La **animación frame a frame** dibuja cada fotograma por separado, como en los dibujos animados clásicos. Es la técnica natural del pixel art y del arte pintado a mano. Te da el control total sobre el movimiento, y también es la más laboriosa: cada frame es un dibujo nuevo.

La **animación cut-out** divide al personaje en piezas (cabeza, torso, brazos, piernas) que se mueven como una marioneta de recortes de cartulina, rotando y desplazando cada parte. Es rápida de producir y muy habitual con arte vectorial.

La **animación esquelética** (skeletal animation) va un paso más allá: coloca un esqueleto de huesos dentro del personaje y las piezas del dibujo se deforman siguiendo esos huesos. Es la misma idea que el rigging en 3D, aplicada a imágenes 2D. Herramientas como Spine o los sistemas de animación 2D de Unity y Godot trabajan así. Permite reutilizar animaciones y conseguir movimientos muy suaves con pocos dibujos.

En esta unidad vamos a trabajar frame a frame, porque es la técnica que mejor enseña los [principios de animación](05-principios-de-animacion.md). Y lo que aprendas aquí sobre poses clave y timing no se tira: te servirá igual cuando animes con huesos, en 2D o en 3D.

## Qué vas a producir

¿Qué necesita, como mínimo, un personaje 2D para ser jugable? Un sprite base, una animación de espera, un ciclo de andar y una acción principal (un ataque, un salto). Todo eso se exporta como sprite sheets que el motor recorta y reproduce. Y como un personaje sin mundo se aburre bastante, también necesita un escenario, que en 2D se construye con tilesets y fondos por capas.

Ese es exactamente el recorrido de esta unidad: herramientas, tamaño, tiles y sprite sheets, principios de animación, las tres animaciones básicas y, para cerrar, el escenario.
