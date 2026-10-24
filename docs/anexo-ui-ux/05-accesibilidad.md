# Anexo A.5 Accesibilidad

Aproximadamente **uno de cada doce hombres** y una de cada doscientas mujeres tiene algún tipo de daltonismo. Si en tu clase hay quince chicos, lo más probable es que al menos uno vea tu barra de vida roja y tu barra de energía verde **casi del mismo color**. Y eso es solo la vista. Hay jugadores sordos, jugadores que no pueden mantener un botón pulsado mucho rato, jugadores que necesitan más tiempo para leer, y jugadores que simplemente están jugando con un bebé dormido al lado y el volumen a cero.

Diseñar con accesibilidad significa **pensar en todos ellos desde el principio**. Y tiene un efecto secundario muy agradable: casi todo lo que se hace para un grupo concreto termina usándolo muchísima más gente. Los subtítulos son el mejor ejemplo: se pensaron para personas sordas, y hoy los activa un montón de gente que oye perfectamente.

## Visión

La regla de oro ya la viste en el [apartado A.1](01-ui-y-ux.md): **el color nunca debe ser la única pista**. Si los enemigos peligrosos son rojos y los débiles verdes, haz que además tengan una forma o un icono distinto. Si una opción del menú está desactivada, que se note por algo más que por el gris.

Además de eso, las opciones más habituales son el **tamaño del texto** (con un mínimo cómodo de partida; las guías de Xbox piden 26 píxeles en consola y 18 en PC sobre una pantalla de 1920×1080), el **tamaño del HUD**, los **modos para daltonismo** (que cambian la paleta de los elementos importantes) y un **fondo detrás de los subtítulos** para que se lean sobre cualquier escena. El **contraste** entre texto y fondo es otra de las claves: un texto gris claro sobre un cielo nublado se lee muy bien en Figma y fatal en el juego.

!!! example "Haz la prueba"
    Busca en la comunidad de Figma un plugin de simulación de daltonismo (con "color blind" aparecen varios) y pásalo por tu paleta o por el mockup de tu HUD. ¿Se siguen distinguiendo todos los elementos importantes? Si dos se confunden, cambia algo más que el color.

## Audición

Lo mínimo son **subtítulos para los diálogos**, y bien hechos: con un tamaño que se pueda ajustar, con fondo, y con **el nombre de quien habla**, porque si no, es imposible saber de quién es cada frase cuando el personaje está fuera de plano.

El paso siguiente es **subtitular también los sonidos importantes** ("[pasos acercándose]", "[explosión a lo lejos]") e incluso **mostrarlos en pantalla**. *Fortnite* tiene una opción para visualizar los efectos de sonido: unos indicadores alrededor del centro de la pantalla te dicen de dónde vienen los disparos, los pasos o los cofres. Recuerda lo que viste en el [apartado A.2](02-hud-y-tipos-de-interfaz.md): **un aviso que solo se oye no existe** para quien no lo puede oír.

## Control y movimiento

Aquí la opción más importante es poder **reasignar los controles**: que cada jugador ponga cada acción en el botón que le resulte cómodo. Detrás vienen otras muy sencillas de implementar y que cambian mucho la experiencia: convertir las acciones de **mantener pulsado en acciones de pulsar una vez**, reducir o quitar las secuencias de pulsar un botón muy rápido, y ajustar la **sensibilidad y las zonas muertas** de los sticks.

*The Last of Us Part II* (Naughty Dog, 2020) se convirtió en la referencia del sector al lanzarse con **más de sesenta opciones de accesibilidad**, desde la reasignación completa de controles hasta un modo de lectura de pantalla y avisos sonoros para jugar sin ver. Si quieres hacerte una idea de hasta dónde se puede llegar, su lista de opciones es una lectura muy recomendable.

## Dificultad y comprensión

No todo el mundo juega al mismo nivel, y no todo el mundo procesa la información a la misma velocidad. Un juego accesible permite **ajustar la dificultad** o, mejor todavía, ajustar **partes concretas** de ella. El caso más citado es el **modo asistido de *Celeste***: puedes bajar la velocidad del juego, darte resistencia infinita para escalar o incluso volverte invencible. El juego sigue siendo el mismo, y nadie te obliga a usarlo, pero **quien lo necesita puede llegar al final**.

En el lado de la interfaz, ayuda mucho que los **tutoriales se puedan volver a consultar**, que el **objetivo actual esté siempre accesible** (para quien deja el juego una semana y vuelve sin acordarse de nada) y que los textos sean **cortos y claros**.

## El libro blanco de accesibilidad de AEVI y Fundación ONCE

En 2023, la Asociación Española del Videojuego (AEVI) y la Fundación ONCE publicaron el [Libro blanco de accesibilidad para desarrolladores](https://www.aevi.org.es/web/wp-content/uploads/2023/06/libro_blanco_de_accesibilidad_para_desarrolladores_digital2023_acf.pdf), una guía gratuita, en español y pensada para estudios de cualquier tamaño, del triple A al indie de dos personas. Se apoya en la norma europea de accesibilidad para productos tecnológicos (la EN 301 549), y es probablemente **la mejor puerta de entrada al tema** que tienes en tu idioma.

Lo primero que propone es un cambio de mirada. En lugar de hablar de tipos de discapacidad, habla de **perfiles funcionales**, es decir, de **cómo usa cada persona la tecnología**: con visión parcial o sin visión, con audición parcial o sin audición, con dificultad moderada o severa para manipular el mando o hacer fuerza, con dificultad para la comprensión, para distinguir colores o para hablar. Da igual el motivo: alguien que juega con el volumen a cero tiene, en ese momento, el mismo perfil que alguien con audición nula.

Después recoge **61 medidas de accesibilidad**, cada una en una ficha con su descripción, los perfiles a los que ayuda (y para cuáles es imprescindible) y **cómo implementarla**. Las clasifica de una a cinco estrellas según lo **difícil que es implementarlas**. La buena noticia está en el reparto: **28 de las 61 medidas son de una sola estrella**, es decir, las más sencillas. Y muchas de ellas son decisiones de diseño de interfaz:

- **Iconos representativos** (una estrella): los iconos que acompañan a los textos tienen que entenderse por sí solos.
- **Tipografía alternativa de fácil lectura** (una estrella): poder cambiar a una fuente de palo seco (sans serif) más legible, por ejemplo para personas con dislexia.
- **Duración de las notificaciones** (una estrella): que el jugador pueda decidir cuánto tiempo se quedan los avisos en pantalla.
- **Efectos repetidos** (una estrella): poder desactivar destellos y luces estroboscópicas.
- **Información con códigos de color** (dos estrellas): nada importante puede depender solo del color. El ejemplo del libro es estupendo para un artista: **pociones de distinto color que además llevan objetos distintos dentro**, o texturas diferentes.
- **Tamaño de letra** y **subtítulos** configurables (dos estrellas), con la advertencia de que el tamaño mínimo y máximo de los textos hay que decidirlo **desde la fase de diseño**, para que la maquetación aguante los dos extremos.
- **Personalización del HUD** (tres estrellas): escala, fondo, color, parpadeo. Su consejo de implementación es puro diseño: **al plantear el HUD, contempla desde el principio todas sus variantes**.

Al final incluye unas **tablas de autoevaluación** por perfil, donde marcas cada medida como "cumple", "no cumple" o "no aplica". Y si quieres ver cómo se aplica todo esto a juegos reales, el portal [Ga11y: videojuegos accesibles](https://ga11y.fundaciononce.es/) de la Fundación ONCE (se pronuncia "gali") analiza la accesibilidad de juegos comerciales con esa misma metodología.

!!! example "Haz la prueba"
    Elige un juego al que juegues y pásale la tabla de autoevaluación de un perfil del libro blanco (la de visión parcial o la de dificultad para ver colores son buenas para empezar). ¿Cuántas medidas cumple? Después mira las de una estrella que no cumple: casi todas se habrían resuelto con una decisión tomada en el diseño de la interfaz.

## Las guías de la industria

Además del libro blanco, hay otras guías muy completas y gratuitas que usa toda la industria, y te ahorran buena parte del trabajo.

| Guía | Qué tiene |
|---|---|
| [Libro blanco de accesibilidad para desarrolladores](https://www.aevi.org.es/web/wp-content/uploads/2023/06/libro_blanco_de_accesibilidad_para_desarrolladores_digital2023_acf.pdf) | 61 medidas en español, clasificadas por dificultad de implementación, con perfiles funcionales y tablas de autoevaluación (AEVI y Fundación ONCE) |
| [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/) | Recomendaciones organizadas en tres niveles (básico, intermedio y avanzado), con ejemplos de juegos reales |
| [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/guidelines) | Las guías de Microsoft, con medidas concretas como los tamaños mínimos de texto |
| [Can I Play That?](https://caniplaythat.com/) | Análisis de juegos desde el punto de vista de la accesibilidad, escritos por jugadores con discapacidad |

Si solo vas a mirar una, empieza por **el libro blanco**, que está en español y ordena las medidas de más fácil a más difícil, o por el **nivel básico de Game Accessibility Guidelines**. Casi todo lo que hay ahí cuesta poco de implementar, y a menudo basta con **tenerlo en cuenta al diseñar** para no tener que rehacer nada después.
