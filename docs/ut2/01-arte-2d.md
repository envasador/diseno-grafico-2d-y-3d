# UT2.1 El arte 2D en videojuegos

*Celeste*, *Hollow Knight* y *Cuphead* son juegos en dos dimensiones que salieron con pocos años de diferencia, y no se parecen en nada. El 2D es mucho más que el estilo de los juegos antiguos: agrupa técnicas muy distintas, cada una con su forma de dibujar, de animar y de producir. Antes de ponerte a pixelar conviene que conozcas el mapa completo, porque la técnica que elijas condiciona todo el trabajo posterior.

## Tres formas de hacer arte 2D

El **pixel art** construye las imágenes colocando cada píxel de forma deliberada, con una resolución y una paleta limitadas a propósito. Es el estilo de *Celeste*, *Stardew Valley* o *Dead Cells*. Parece sencillo por su aspecto retro, pero es muy exigente: con tan pocos píxeles, un solo punto mal colocado cambia la expresión de una cara. Se anima dibujando cada frame.

El **arte vectorial** define las formas con curvas matemáticas en lugar de píxeles, así que se puede escalar a cualquier tamaño sin perder calidad. Produce imágenes limpias, de colores planos, muy habituales en juegos móviles y casuales. Encaja muy bien con la animación por piezas y por huesos.

El **arte pintado a mano** (hand-drawn) usa técnicas de ilustración digital para conseguir un acabado de dibujo o pintura tradicional. *Hollow Knight* y *Cuphead* son los ejemplos clásicos. Permite el mayor nivel de detalle y expresividad, a cambio de un proceso de producción mucho más lento.

| Técnica | Ventaja principal | Coste principal | Herramientas habituales |
|---|---|---|---|
| Pixel art | Lectura clara y estética muy reconocible | Cada frame se dibuja a mano | Aseprite, Pyxel Edit |
| Vectorial | Escalable y fácil de animar por piezas | Puede resultar frío si no se estiliza | Affinity Designer, Illustrator, Inkscape |
| Pintado a mano | Máxima expresividad y detalle | Producción lenta, archivos pesados | Photoshop, Krita, Clip Studio Paint |

## Tres formas de animar en 2D

La **animación frame a frame** dibuja cada fotograma por separado, como en los dibujos animados clásicos. Es la técnica natural del pixel art y del arte pintado a mano. Da el control total sobre el movimiento, y también es la más laboriosa: cada frame es un dibujo nuevo.

La **animación cut-out** divide al personaje en piezas (cabeza, torso, brazos, piernas) que se mueven como si fueran una marioneta de recortes, rotando y desplazando cada parte. Es rápida de producir y muy habitual con arte vectorial.

La **animación esquelética** (skeletal animation) va un paso más allá: coloca un esqueleto de huesos dentro del personaje y las piezas del dibujo se deforman siguiendo esos huesos. Es la misma idea que el rigging en 3D, aplicada a imágenes 2D. Herramientas como Spine o los sistemas de animación 2D de Unity y Godot trabajan así. Permite reutilizar animaciones y conseguir movimientos muy suaves con pocos dibujos.

En esta unidad trabajaremos frame a frame, porque es la técnica que mejor enseña los [principios de animación](05-principios-de-animacion.md). Lo que aprendas sobre poses clave y timing te servirá igual cuando animes con huesos en 2D o en 3D.

## Qué vas a producir

Un personaje 2D jugable necesita, como mínimo, un sprite base, una animación de espera, un ciclo de andar y una acción principal (un ataque, un salto). Todo eso se exporta como sprite sheets que el motor recorta y reproduce. Además, el personaje necesita un mundo, que en 2D se construye con tilesets y fondos por capas.

Ese es el recorrido de esta unidad: herramientas, tamaño, tiles y sprite sheets, principios de animación, las tres animaciones básicas y, al final, el escenario.

## Lo que te llevas

El arte 2D agrupa técnicas muy distintas (pixel art, vectorial y pintado a mano), y cada una tiene su forma natural de animarse. Elegir técnica es elegir un proceso de producción, así que la decisión se toma pensando en el estilo que buscas y en el tiempo que tienes.
