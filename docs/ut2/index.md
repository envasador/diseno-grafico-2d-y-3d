# UT2 Gráficos y animación 2D

En esta unidad das el salto de diseñar un personaje a hacerlo funcionar dentro de un juego. Un sprite tiene que respetar un tamaño concreto, encajar en una rejilla, exportarse en un formato que el motor entienda y, sobre todo, moverse: respirar cuando el jugador suelta el mando, andar cuando se desplaza y atacar cuando pulsa un botón. Todo eso con muy pocos píxeles, donde cada uno cuenta.

Trabajaremos sobre todo con pixel art, porque es el estilo 2D que mejor enseña a tomar decisiones: con tan poca resolución no hay forma de esconder un problema de forma, de color o de timing.

Esta unidad desarrolla el **RA3**: diseña elementos gráficos y animaciones en 2D teniendo en cuenta las características de los personajes.

!!! concept "Fase de concept"
    Antes de abrir el editor de pixel art necesitas tener resuelto el diseño de tu personaje a nivel de concept. Para esta unidad prepara:

    - Una hoja de [siluetas](../concept/siluetas.md) a tamaño real de sprite. Lo que funciona a tamaño de ilustración puede ser ilegible a 32 píxeles, así que la comprobación se hace a la escala final.
    - Una [paleta](../concept/color.md) limitada para el personaje, coherente con la del mundo que definiste en tu [biblia de arte](../concept/biblia-de-arte.md).
    - Un [model sheet](../concept/hojas-de-produccion.md#model-sheet) sencillo y una [hoja de poses](../concept/hojas-de-produccion.md#hojas-de-expresiones-y-de-poses) con las poses clave de cada animación. Esas poses serán tus fotogramas clave.
    - Un moodboard de movimiento: capturas o GIFs de animaciones que te gusten, para analizar su timing.

    Todo esto se añade a tu biblia de arte como capítulo de la UT2.

## Apartados

| Apartado | Contenido |
|---|---|
| [UT2.1 El arte 2D en videojuegos](01-arte-2d.md) | Estilos 2D y tipos de animación |
| [UT2.2 Programas para pixel art](02-programas-pixel-art.md) | Qué herramienta usar y para qué |
| [UT2.3 Tamaño de la imagen](03-tamano-de-la-imagen.md) | Resolución, nivel de detalle y dimensiones recomendadas |
| [UT2.4 Tiles y sprite sheets](04-tiles-y-sprite-sheets.md) | Tilesets, frames y potencias de dos |
| [UT2.5 Principios de animación](05-principios-de-animacion.md) | Fotogramas clave, interpolaciones, timing, squash y stretch |
| [UT2.6 Animación de espera](06-animacion-de-espera.md) | Idle y waiting |
| [UT2.7 Walking cycle](07-walking-cycle.md) | La receta de un ciclo de andar de 6 frames |
| [UT2.8 Animación de ataque](08-animacion-de-ataque.md) | Anticipación, golpe, final y retroceso; easing |
| [UT2.9 Escenarios 2D](09-escenarios-2d.md) | Tilemaps, parallax y perspectiva |
