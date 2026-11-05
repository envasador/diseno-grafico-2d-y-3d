# UT2.2 Programas para pixel art

Técnicamente puedes hacer pixel art con cualquier programa que te deje pintar un píxel. Sí, incluido el Paint de Windows. Otra cosa es que quieras sufrir. Un programa pensado para pixel art te da rejillas de tiles, previsualización de la animación en tiempo real, paletas indexadas y exportación directa a sprite sheet, y eso se traduce en **horas ahorradas**.

Así que la pregunta interesante es otra: **qué herramienta encaja con cada parte del trabajo**.

## Programas de escritorio

**Aseprite** es **el estándar del pixel art para videojuegos**, el que vas a ver en casi todos los tutoriales. Está pensado exclusivamente para esto, organiza el trabajo en capas y grupos, tiene una línea de tiempo muy cómoda para animar, previsualización en bucle, **onion skin** (ver los frames anterior y siguiente en transparencia) y exporta sprite sheets con un clic. Funciona en Windows, macOS y Linux. Es de pago, aunque su código está disponible y se puede compilar gratuitamente; también existe LibreSprite, una versión libre basada en una versión antigua.

**Pyxel Edit** es más sencillo e intuitivo, y destaca en un punto concreto: **el trabajo con tiles**. Todo en él gira alrededor de la rejilla, así que es muy cómodo para construir tilesets y para animar en una tira de frames. Es barato y tiene una versión gratuita antigua. Sus limitaciones son que no agrupa capas y que no está disponible para Linux.

Hay alternativas gratuitas que merece la pena conocer: **Pixelorama** (libre y multiplataforma, muy completo) y **Piskel** (funciona en el navegador, ideal para empezar o para pruebas rápidas).

Por último, puedes usar programas de ilustración generalistas como **Photoshop** o **Affinity**. Ninguno está pensado para pixel art, pero los dos sirven si configuras bien el lápiz y **desactivas el suavizado**, y tienen la ventaja de que seguramente ya los sabes usar (Affinity lo conoces de la UT1 y además es gratuito). En Affinity, por ejemplo, el estudio **Pixel** tiene la herramienta **Pincel de píxeles**, que pinta píxeles enteros, y con la rejilla ajustada a 1 px controlas cada punto. A cambio, ninguno de los dos tiene una línea de tiempo cómoda para animar ni exporta sprite sheets por sí solo, así que te rinden más en fondos, escenarios y retoques que en animación.

| Programa | A favor | En contra | Plataformas |
|---|---|---|---|
| Aseprite | Exclusivo para pixel art, capas y grupos, animación y exportación excelentes | Complejidad intermedia, de pago | Windows, macOS, Linux |
| Pyxel Edit | Muy sencillo, editor de tiles, versión de pago muy barata | No agrupa capas | Windows, macOS |
| Pixelorama | Libre y gratuito, animación y tiles | Menos pulido que Aseprite | Windows, macOS, Linux, web |
| Piskel | Gratuito y en el navegador | Muy básico para proyectos grandes | Web |
| Photoshop | Archivos pesados, capas y efectos avanzados, probablemente ya lo conoces | Complejo, caro, no es exclusivo de pixel art | Windows, macOS |
| Affinity | Gratuito, capas y efectos avanzados, ya lo conoces de la UT1 | Sin línea de tiempo para animar, no es exclusivo de pixel art | Windows, macOS |

## Aplicaciones móviles

Existen aplicaciones como **Pixel Studio**, **Pixly** o **Pixel Station** que te permiten pixelar desde el móvil o la tableta. Son más completas de lo que parece y casi todas gratuitas, así que están genial para practicar en el autobús o bocetar una idea antes de que se te olvide. Para un trabajo serio se hacen incómodas: **úsalas como cuaderno de bocetos y termina en el ordenador**.

## Un flujo habitual

En un proyecto real nadie se casa con un único programa: **cada tarea se hace con el que mejor la resuelve**. Un flujo muy común es este:

1. **Personajes y objetos** en un editor de pixel art (Pyxel Edit o Aseprite), donde controlas cada píxel.
2. **Animaciones y tilesets** en el mismo editor, aprovechando su línea de tiempo y su rejilla.
3. **Escenarios y efectos** en un programa de ilustración (Affinity o Photoshop), donde componer fondos grandes, pintar degradados de cielo o preparar capas de parallax es más cómodo.

Las explicaciones de clase se hacen con **Pyxel Edit**, porque su rejilla de tiles hace muy visibles los conceptos de esta unidad. Puedes trabajar con otra herramienta siempre que **exporte PNG y sprite sheets con todos los frames del mismo tamaño**.
