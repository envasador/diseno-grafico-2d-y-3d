# Anexo A.7 Hoja de ruta: la interfaz como en un estudio

En un estudio de videojuegos nadie abre Figma y empieza a dibujar botones bonitos. La interfaz pasa por una serie de fases, cada una con su entregable, y en cada fase intervienen personas distintas: diseño de juego, UX, UI art y programación. Esta hoja de ruta sigue **ese mismo proceso**, tal y como lo cuentan profesionales que diseñan y programan interfaces de juegos (tienes las fuentes al final), para que lo recorras con la interfaz de tu propio juego.

En un estudio grande cada fase la lleva una persona distinta. En uno pequeño, como en tu caso, **una misma persona hace de todo**: hoy eres diseñador de UX, mañana artista de UI y pasado programador. Ve cambiándote el sombrero.

Como el resto del anexo, **no se evalúa por separado** y es orientativa: **haz lo que puedas en cada fase, a tu nivel**. Lo importante es que recorras el proceso en orden y que cada fase te deje su entregable, aunque sea sencillo.

## Antes de empezar

Elige **el juego del proyecto en el que estés trabajando** (o el de tu equipo, o el de una jam) y trabaja todo en **un archivo de Figma**, con una página por fase. Si ya tienes la [biblia de arte](../concept/biblia-de-arte.md) de ese juego, la interfaz va a salir de ella.

## Las herramientas

En la industria, **Figma** se usa sobre todo en las fases de diseño: flujos, wireframes, prototipos, mockups y guías de estilo. Es colaborativo, tiene componentes y variantes, y diseño, arte y programación pueden comentar sobre el mismo archivo. Pero no es la única herramienta ni la última:

- **Figma (fases 1 a 6).** El inventario, el moodboard, el diagrama de flujo, los wireframes con su *layout grid* de 8 px, el prototipo navegable (pestaña *Prototype*), los mockups, la guía de estilo con **variables y estilos de texto**, y el kit de UI con **componentes, variantes y Auto Layout**. Los anclajes del HUD se prueban con las **constraints** de cada elemento.
- **Affinity, Photoshop o Aseprite (fase 6).** Las piezas con más acabado (marcos ornamentados, texturas, iconos pintados o interfaces en pixel art) suelen salir de las mismas herramientas que el resto del arte del juego, porque tienen que encajar con él. Después se colocan en Figma para montar las pantallas.
- **Figma también anima (fases 6 y 7).** Con **Smart Animate**, Figma anima el paso de una variante a otra: el botón que se ilumina al recibir el foco, el que se hunde al pulsarlo o la barra de vida que baja. Desde 2026 tiene además **Figma Motion**, un modo con línea de tiempo y fotogramas clave para animaciones más elaboradas (está en beta y puede que aún no te aparezca). Lo que animes en Figma no entra directamente en el motor: sirve para **enseñar cómo debe moverse** la interfaz, en un vídeo o un GIF, y luego la animación se vuelve a hacer en Unity o Godot.
- **After Effects o Rive (opcional).** Las herramientas de animación que se usan en muchos estudios. Rive tiene la ventaja de que sus animaciones pueden entrar en el motor tal cual.
- **El motor (fases 4, 7 y 8).** Unity, Godot o Unreal. Lo que diseñas en Figma no se exporta como código: **se vuelve a montar dentro del motor**, y ahí es donde de verdad se prueba.

Resumiendo: **Figma sirve para decidir y el motor para construir.** Todo lo que defines en Figma (jerarquía, estados, anclajes, nombres de las piezas) es justo la información que necesita quien monte la interfaz, aunque esa persona seas tú.

## Qué hace cada perfil

En un estudio, la interfaz pasa por tres perfiles distintos. Conviene que sepas qué hace cada uno, porque en cada fase de la ruta verás quién la lleva.

| | Diseñador de UX | Artista de UI | Programador de UI |
|---|---|---|---|
| **Se pregunta** | ¿El jugador entiende lo que pasa y encuentra lo que busca? | ¿Se ve bien y parece del mismo juego? | ¿Funciona en el motor, con datos reales y en cualquier pantalla? |
| **Trabaja con** | Diseño de juego, investigación y QA | Dirección de arte y UX | UX, UI art y el resto de programación |
| **Fases donde más pesa** | Requisitos, investigación, flujos, wireframes y pruebas | Dirección visual, guía de estilo, assets y animación | Prototipo en el motor, integración y ajustes finales |
| **Entrega** | Flujos de pantallas, wireframes, prototipos e informes de pruebas | Mockups, guía de estilo, kit de UI, iconos y referencias de movimiento | Las pantallas montadas en el motor y conectadas a los datos del juego |
| **Herramientas** | Papel, pizarra y Figma | Figma, Photoshop, Illustrator, After Effects o Rive | Unity, Unreal o Godot y su sistema de UI |

Dos matices importantes. El primero: **las fronteras son borrosas**. Ben Humphreys es programador de UI, pero empieza preguntando a diseño y dibujando wireframes en papel, que en teoría es trabajo de UX. Y las ofertas de empleo de artista de UI piden también wireframes, flujos y prototipos. En la práctica, cada perfil hace un poco del trabajo de los otros dos.

El segundo: **en un estudio pequeño es una sola persona**. Humphreys cuenta que en su estudio a menudo no hay diseñador de UX ni de UI dedicado, y que ese papel lo cubren él y el director de arte. Es tu caso en los proyectos del curso: vas a llevar los tres perfiles a la vez.

## Fase 1. Requisitos: qué necesita saber el jugador

**En un estudio:** antes de dibujar nada, quien diseña la interfaz se sienta con diseño de juego y pregunta. Qué información necesita el jugador, qué es prioritario, qué puede pasar a la vez (¿se puede estar envenenado y quemado al mismo tiempo?), en qué plataformas sale el juego y a qué idiomas se va a traducir. Ben Humphreys, programador de UI en Brace Yourself Games, lo resume diciendo que al principio su trabajo es "muy de texto".

**Tu entregable:** un **documento de requisitos** de una página con el género, la plataforma, el control (mando, ratón o táctil) y la lista de información que necesita el jugador. Conviértelo en la **tabla de inventario** de [De Figma al motor](06-de-figma-al-motor.md#haz-inventario-de-la-informacion): datos en las filas, momentos del juego en las columnas.

## Fase 2. Investigación y referencias

**En un estudio:** se analizan los juegos del mismo género (qué funciona, de qué se quejan los jugadores) y se monta un moodboard de interfaces. El equipo de *No Love Lost* reunió capturas de juegos, películas y series para fijar la dirección visual de su HUD antes de hacer ningún mockup.

**Tu entregable:** un **moodboard de interfaces** de tu género (la [Game UI Database](https://www.gameuidatabase.com/) es perfecta para esto) y el **análisis de dos capturas**: cada elemento clasificado en una de las [tres capas](01-ui-y-ux.md#las-capas-de-informacion) y en uno de los [cuatro tipos](02-hud-y-tipos-de-interfaz.md), respondiendo a las dos preguntas: ¿existe en la historia del juego? ¿Está en la escena o pegado a la pantalla?

## Fase 3. Flujos y wireframes

**En un estudio:** se dibuja primero **el flujo**, es decir, cómo se pasa de una pantalla a otra (menú principal, opciones, partida, pausa), y después cada pantalla en **wireframe de baja fidelidad**, a veces en papel o en una pizarra. Humphreys empieza siempre por lo más difícil: la interfaz que tiene que explicar una mecánica nueva o el bucle principal del juego.

**Tu entregable:** el **diagrama de flujo** de pantallas de tu juego (cajas y flechas en Figma) y los **wireframes en gris** del HUD en exploración, el HUD en combate y el menú de pausa, en un marco de 1920×1080 con la [safe area](04-reticula-safe-area-y-escalado.md#la-safe-area) marcada. Haz la **prueba de los cinco segundos** con alguien de clase.

## Fase 4. Prototipo gris

**En un estudio:** antes de invertir en arte final, se prueba la interfaz **lo antes posible** y con el arte más tosco posible, en blanco y negro para que nadie la confunda con la definitiva. El objetivo es usarla mucho y descubrir pronto lo que no funciona. Según Humphreys, la respuesta a "¿esto funciona?" es casi siempre que no, y por eso se itera.

**Tu entregable:** un **prototipo navegable en Figma** con tus wireframes: los botones del menú llevan a sus pantallas y vuelven. Si te manejas con el motor, puedes montar el HUD gris directamente en Unity o en Godot, que es lo que hacen muchos estudios.

## Fase 5. Dirección visual y guía de estilo

**En un estudio:** en paralelo, UI art explora el estilo (tipografía, texturas, estilo de los botones) con mockups de alta fidelidad, y el equipo elige una dirección. Después se recoge en una **guía de estilo** con los componentes estándar: botones, títulos, paneles. Una regla muy habitual es **limitar las opciones** para que todo sea consistente, por ejemplo con solo tres tamaños de texto (título, subtítulo y cuerpo).

**Tu entregable:** **dos o tres mockups** de una misma pantalla con estilos distintos, sacados de tu biblia de arte, y la **guía de estilo de UI** de la dirección elegida: colores de estado (vida, peligro, foco, desactivado), los tres tamaños de texto con su mínimo legible y el lenguaje de formas de los paneles. Recuerda la regla de la [accesibilidad](05-accesibilidad.md): el color nunca va solo.

## Fase 6. Assets y componentes de UI

**En un estudio:** UI art produce las piezas: iconos, tipografía, menús, elementos del HUD y notificaciones, con todos sus estados y listas para el motor.

**Tu entregable:** el **kit de UI** en Figma: un **botón con sus cuatro estados** (normal, foco, pulsado y desactivado) que crezca con el texto, la **barra de vida** y, si tu juego tiene diálogos, el **cuadro de diálogo** pensado para [9-slice](04-reticula-safe-area-y-escalado.md#paneles-que-se-estiran-9-slice). Con el kit, monta las pantallas definitivas del HUD y del menú de pausa, y comprueba los anclajes en 21:9 y 16:10.

Si llegas, anima los estados del botón con **Smart Animate** (normal, foco y pulsado) y comprueba cómo se siente en el modo *Present*. Entre 100 y 200 milisegundos suele ser suficiente: una interfaz que tarda en reaccionar parece rota, por bonita que sea la animación (es el [umbral de Doherty](03-leyes-de-ux.md#umbral-de-doherty)).

## Fase 7. Integración en el motor

**En un estudio:** las piezas aprobadas se llevan al motor, se prueban dentro del juego y ahí se añaden las animaciones, los efectos y los ajustes píxel a píxel. Lo que en el mockup parecía perfecto a menudo se mueve después de verlo jugando: en *No Love Lost*, la barra de vida acabó pasando del centro a la esquina inferior izquierda para dejar libre el centro de la pantalla.

**Tu entregable:** las piezas **exportadas con [nombres sistemáticos](06-de-figma-al-motor.md#prepara-los-assets-para-el-motor)**, las medidas de las esquinas de las piezas 9-slice y una **referencia de movimiento**: un vídeo o GIF corto, hecho en Figma, que enseñe cómo se mueve tu interfaz (el foco de los botones, la barra de vida al recibir daño, la entrada del menú de pausa). Es lo que en un estudio se entrega a quien implementa la interfaz para que sepa qué tiene que reproducir. Si llegas, el HUD montado en Unity o en Godot con sus anclajes.

## Fase 8. Prueba con jugadores e iteración

**En un estudio:** la interfaz se prueba con personas que juegan sin que nadie les explique nada (playtests y pruebas de usabilidad), y se corrige lo que se descubre. La iteración no es una fase final: está presente en todo el proceso.

**Tu entregable:** una **sesión de prueba** con alguien de clase que use tu prototipo o tu juego sin explicaciones. Apunta dónde mira, dónde duda y qué pulsa por error, y anota **tres cambios** que harías. Si llegas, aplícalos. Aprovecha para revisar la accesibilidad: simulador de daltonismo, tamaño mínimo del texto y tres medidas de una estrella del [libro blanco](05-accesibilidad.md#el-libro-blanco-de-accesibilidad-de-aevi-y-fundacion-once).

## Resumen de la ruta

| Fase | Quién la lleva en un estudio | Herramienta | Tu entregable |
|---|---|---|---|
| 1. Requisitos | Diseño de juego y UX | Documento o Figma | Documento de requisitos e inventario de información |
| 2. Investigación | UX y UI art | Figma | Moodboard de interfaces y análisis de dos capturas |
| 3. Flujos y wireframes | UX (o diseño de juego) | Papel y Figma | Diagrama de flujo y wireframes en gris |
| 4. Prototipo gris | UX y programación de UI | Figma (o el motor) | Prototipo navegable |
| 5. Dirección visual | UI art y dirección de arte | Figma | Mockups de estilo y guía de estilo de UI |
| 6. Assets | UI art | Figma (con Smart Animate), Affinity o Aseprite | Kit de UI y pantallas definitivas |
| 7. Integración | Programación de UI | El motor (y Figma para la referencia de movimiento) | Piezas exportadas, referencia de movimiento (y HUD en el motor) |
| 8. Prueba e iteración | Todo el equipo | El prototipo o el juego | Notas de la prueba y cambios |

## Dónde lo guardas

Todo va al mismo archivo de Figma, con una página por fase y en el mismo orden. Si tu proyecto tiene interfaz, **añade la guía de estilo (fase 5) y las pantallas definitivas (fase 6) a la biblia de arte** de ese proyecto. Es una pieza de portfolio muy valorada, porque enseña algo que piden todas las ofertas de UI artist: wireframes, flujos, prototipos, guía de estilo y assets, todo en el orden en que se trabaja.

## Fuentes

- Ben Humphreys (programador de UI en Brace Yourself Games), [Creating UI for games](https://cbgamedev.substack.com/p/003-creating-ui-for-games-with-ben).
- Nora Leca (diseñadora de UX en un estudio AAA de juegos para móvil), [Creating space for UX in game development](https://uxdesign.cc/creating-space-for-ux-in-game-development-13a0eef6aa5b).
- Rat Loop Games, [Vital transmissions: designing No Love Lost's HUD](https://ratloopgamescanada.com/dev-blog/vital-transmissions-designing-no-love-losts-hud).
- Pixune, [UI/UX design pipeline for game interfaces](https://pixune.com/blog/ui-ux-design-pipeline/).
- Responsabilidades habituales en las ofertas de empleo de UI artist en estudios de videojuegos (wireframes, flujos, prototipos interactivos, mockups, assets, guías de estilo e integración en el motor).
