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

## Las guías de la industria

Hay guías muy completas y gratuitas que usa toda la industria, y te ahorran buena parte del trabajo.

| Guía | Qué tiene |
|---|---|
| [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/) | Recomendaciones organizadas en tres niveles (básico, intermedio y avanzado), con ejemplos de juegos reales |
| [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/guidelines) | Las guías de Microsoft, con medidas concretas como los tamaños mínimos de texto |
| [Can I Play That?](https://caniplaythat.com/) | Análisis de juegos desde el punto de vista de la accesibilidad, escritos por jugadores con discapacidad |

Si solo vas a mirar una, empieza por el **nivel básico de Game Accessibility Guidelines**. Casi todo lo que hay ahí cuesta poco de implementar, y a menudo basta con **tenerlo en cuenta al diseñar** para no tener que rehacer nada después.
