# Anexo A.1 La UI y la UX de un juego

Dos siglas que se usan casi siempre juntas y que conviene separar desde el principio. La **UI** (User Interface, interfaz de usuario) es **lo que ves y tocas**: los botones, las barras, los iconos, los textos, los menús. La **UX** (User Experience, experiencia de usuario) es **lo que te pasa al usarlo**: si encuentras lo que buscas, si entiendes lo que está ocurriendo, si te frustras o ni te enteras de que había una interfaz.

Un ejemplo para que se vea la diferencia. La barra de vida es UI. Darte cuenta **a tiempo** de que te quedan dos golpes, y huir, es UX. Puedes tener una barra de vida preciosa (buena UI) colocada en una esquina donde nadie mira en pleno combate (mala UX). El jugador no va a pensar "qué barra tan bonita". Va a pensar "¿y por qué me he muerto?".

<iframe width="560" height="315" src="https://www.youtube.com/embed/sc3h5JXtIzw" title="So You Wanna Make Games?? Episode 9: User Interface Design, de Riot Games" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

*[So You Wanna Make Games?? Episode 9: User Interface Design](https://www.youtube.com/watch?v=sc3h5JXtIzw), de Riot Games (en inglés, con subtítulos). Cuenta cómo trabajan juntos los equipos de UI y UX en un estudio grande. © Riot Games; uso con fines educativos.*

## En qué se diferencia de la interfaz de una app

En la app de tu banco, **la interfaz es el producto**: entras, haces una transferencia y sales. Toda tu atención está en los botones. En un juego pasa lo contrario: **la interfaz compite con el juego por tu atención**. Mientras lees la munición hay un enemigo acercándose, y cada décima de segundo que pasas mirando una esquina es una décima que no miras la acción.

De ahí sale la idea que vas a ver repetida en todo el anexo: **la mejor interfaz de juego es la que se lee de un vistazo y no estorba**. Y cuando el juego se pausa (en un inventario, en un menú de opciones), la cosa cambia, porque entonces sí tienes la atención del jugador y puedes permitirte mostrar más.

## Las capas de información

Una forma muy práctica de ordenar todo lo que un juego tiene que contar es separarlo en **tres capas según su urgencia**.

La primera es la **información crítica**, la que el jugador necesita en todo momento para no morir o no perderse: la vida, la munición, a veces un minimapa. Tiene que leerse **en un instante** y estar siempre en el mismo sitio. En *Hollow Knight*, las máscaras de vida y el recipiente de alma están arriba a la izquierda durante toda la partida, y en una pelea difícil los miras sin pensar.

La segunda es la **información contextual**, la que aparece cuando hace falta y desaparece después: "Has conseguido un objeto", un aviso de misión, el botón que tienes que pulsar para abrir una puerta. **Si estuviera siempre en pantalla, sería ruido.**

La tercera es la **gestión con el juego en pausa**: inventario, mapa completo, árbol de habilidades, opciones. Aquí el jugador ya no está esquivando nada, así que **cabe más densidad**, más texto y estructuras más complejas.

!!! example "Haz la prueba"
    Coge una captura de un juego al que juegues y apunta todo lo que aparece en pantalla que no sea el mundo del juego. Clasifica cada elemento en una de las tres capas. Si hay algo que está siempre visible y que solo miras de vez en cuando, ya has encontrado un candidato a pasar a la segunda capa.

## Las piezas de una interfaz

Por complicada que parezca una interfaz, casi siempre está hecha con las mismas piezas: **botones, barras** (de vida, de energía, de progreso), **iconos, paneles** (los fondos sobre los que va el contenido), **textos** y **tooltips** (los recuadros que explican qué hace algo cuando lo seleccionas).

Lo que diferencia a una pieza de interfaz de una ilustración es que **tiene estados**. Un botón son en realidad varios dibujos: cómo se ve normalmente, cómo se ve cuando está seleccionado, cómo se ve en el momento de pulsarlo y cómo se ve cuando no se puede usar. Si te olvidas de alguno, el programador se lo inventará (y no te va a gustar).

| Estado | Qué le dice al jugador |
|---|---|
| Normal | "Estoy aquí y puedes usarme" |
| Seleccionado (foco) | "Si pulsas ahora, me activas a mí" |
| Pulsado | "Recibido, ya estoy haciendo lo que me has pedido" |
| Desactivado | "Ahora mismo no puedes usarme" (y conviene que se entienda por qué) |

Hay un detalle que separa la UI de juegos de la web: **con un mando no hay ratón**, así que no existe el "pasar por encima". El jugador se mueve de botón en botón con la cruceta o el stick, y **el estado de foco tiene que verse muchísimo**, porque es la única forma de saber dónde estás. Un foco que solo cambia un poco el tono del botón es una invitación a pulsar lo que no querías.

## Color, tipografía e iconos

El **color** es la forma más rápida de comunicar un estado. Hay códigos que los jugadores ya traen aprendidos: el rojo para la vida y el peligro, el verde para lo positivo, el amarillo para lo que pide atención. Los colores de rareza del botín que popularizó *World of Warcraft* (gris, blanco, verde, azul, morado y naranja, de menos a más valioso) se usan hoy en cientos de juegos distintos. Puedes aprovechar esos códigos o romperlos, pero **si los rompes, que sea a propósito**.

Eso sí: **el color nunca debe ser la única pista**. Una parte importante de los jugadores tiene algún tipo de daltonismo (lo verás con más detalle en el apartado de [accesibilidad](05-accesibilidad.md)), así que acompaña el color con una forma, un icono o un texto.

La **tipografía** tiene que leerse en las peores condiciones posibles: en una tele a dos metros del sofá, en una consola portátil o en un móvil al sol. Como referencia, las guías de accesibilidad de Xbox piden que el texto normal mida **al menos 26 píxeles de alto en consola y 18 en PC**, contando sobre una pantalla de 1920×1080 píxeles (lo que se suele llamar 1080p). El truco habitual para no renunciar al estilo es **separar los usos**: una fuente con mucha personalidad para títulos y textos grandes, y una muy legible para todo lo demás. Una fuente gótica preciosa queda de maravilla en "Game Over"; en la descripción de una espada, a 18 píxeles, se convierte en un jeroglífico.

Los **iconos** tienen que reconocerse sin leer el texto que los acompaña, y eso solo se comprueba de una manera: **mirándolos a su tamaño real**. Igual que en el pixel art (lo verás en la UT2), un icono que se ve perfecto con el zoom al 800 % puede ser una mancha ilegible al 100 %.

## Consistencia y coherencia

Son dos palabras que se parecen mucho y que se refieren a cosas distintas.

La **consistencia** va de funcionamiento: **lo mismo se hace siempre de la misma manera**. Si el botón de confirmar está a la derecha en un menú, está a la derecha en todos. Si el rojo significa daño en el HUD, no puede significar "objeto nuevo" en el inventario. Cada excepción obliga al jugador a pararse a pensar.

La **coherencia** va de estilo: **toda la interfaz parece del mismo juego que el resto del juego**. Los menús de *Persona 5* son un ejemplo famoso: recortes, ángulos imposibles, rojo y negro. Encajan tan bien con el tono del juego que cuesta imaginarlo con otra interfaz. Para conseguirla, **aplica a la interfaz las reglas que ya tienes en tu biblia de arte**: la misma paleta, las mismas formas y el mismo acabado.
