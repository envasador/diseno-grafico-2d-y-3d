# Anexo A.3 Leyes de UX aplicadas a juegos

Las llamadas "leyes de UX" son **observaciones sobre cómo percibimos, decidimos y recordamos**, casi todas sacadas de la psicología experimental de mediados del siglo XX. El diseñador Jon Yablonski las recopiló en la web [Laws of UX](https://lawsofux.com/), y desde entonces se citan en cualquier curso de diseño de interfaces.

Antes de empezar, una advertencia: llamarlas "leyes" es un poco exagerado. Son **tendencias que se cumplen casi siempre**, con mucha menos exactitud que una fórmula de física. Úsalas como una lista de preguntas que hacerle a tu interfaz. Aquí tienes las que más juego dan en un videojuego, empezando por las más intuitivas.

## Ley de Hick

William Hick y Ray Hyman comprobaron en los años cincuenta que **el tiempo que tardamos en decidir crece con el número de opciones**. El detalle interesante es cómo crece: cada vez más despacio. Pasar de 2 a 4 opciones cuesta lo mismo que pasar de 4 a 8, o de 8 a 16. Es decir, **cada vez que duplicas las opciones, añades el mismo "paso" de tiempo**.

En un juego de acción, ese paso es justo lo que no tienes. Por eso los **menús radiales de armas** suelen limitarse a unas ocho casillas, y por eso los árboles de habilidades se dividen en **ramas y niveles que se desbloquean poco a poco**. En lugar de enfrentarte a cincuenta habilidades de golpe, eliges entre tres ramas, y dentro de cada rama entre unas pocas opciones.

En un juego de gestión con el tiempo en pausa la presión es mucho menor, y una pantalla con muchas opciones es perfectamente aceptable. **Lo que importa es cuánto tiempo tiene el jugador para decidir.**

!!! example "Haz la prueba"
    Abre el menú principal de tres juegos distintos y cuenta las opciones. Después piensa en cuál de ellos llegas antes a jugar. Casi siempre gana el que tiene "Continuar" como primera opción, ya seleccionada.

## Ley de Fitts

Paul Fitts demostró en 1954 que **el tiempo que tardamos en llegar a un objetivo depende de lo lejos que está y de lo grande que es**. Un botón grande y cerca se pulsa enseguida; uno pequeño y lejos obliga a frenar y apuntar.

Donde más se nota es con **ratón y pantalla táctil**. En un juego de móvil, los botones de acción van grandes y donde caen los pulgares. Las guías de Apple y de Google piden que cualquier elemento táctil mida **como mínimo 44 o 48 unidades de lado**, unas unidades que se ajustan a la densidad de cada pantalla y que vienen a ser el tamaño de la yema de un dedo. Con ratón hay un truco precioso: **las esquinas y los bordes de la pantalla** son objetivos "infinitos", porque el cursor se para ahí aunque te pases. No es casualidad que tantos juegos de estrategia pongan sus paneles pegados a los bordes.

Con **mando** la ley se traduce de otra forma: la "distancia" pasa a ser **el número de pulsaciones** que necesitas para llegar a una opción. Las opciones que más se usan tienen que estar a una o dos pulsaciones. Y aquí los menús radiales vuelven a ganar, porque con el stick **todas las opciones están a la misma distancia** del centro.

## Ley de Jakob

Jakob Nielsen la formuló pensando en la web: la gente pasa la mayor parte de su tiempo en otras webs, así que **espera que la tuya funcione como las demás**. En los juegos ocurre exactamente lo mismo. El jugador llega a tu juego con cientos de horas de otros juegos encima, y trae aprendido que el menú de pausa está en el botón de opciones, que en PC se mueve uno con WASD y que se salta con la barra espaciadora.

Romper esas convenciones tiene un coste. Un ejemplo real: durante años, en Japón el botón de confirmar de PlayStation era el círculo y el de cancelar la equis, justo al revés que en Europa y América. Cuando PlayStation 5 unificó la equis como "confirmar" en todo el mundo, a muchos jugadores japoneses les costó acostumbrarse y se pasaron una temporada **cancelando cosas que querían aceptar**.

Puedes innovar, claro, pero **cada cambio respecto a lo habitual tiene que aportar algo** que compense el rato de confusión. Y que, si cambias los controles, conviene dejar que el jugador los reasigne.

## Efecto Von Restorff

La psiquiatra Hedwig von Restorff observó en 1933 que, en una lista de elementos parecidos, **recordamos mucho mejor el que es distinto**. En diseño se usa al revés: si quieres que algo se vea, **hazlo diferente de lo que lo rodea**.

Los juegos lo usan constantemente. El objeto legendario brilla en naranja entre un montón de botín gris. La puerta que puedes abrir tiene un marco más claro que las demás. Los salientes a los que puedes trepar llevan una mancha de **pintura amarilla**, una solución tan extendida que en 2023, con el remake de *Resident Evil 4*, se convirtió en un debate enorme entre jugadores: unos la veían como una ayuda imprescindible y otros como un insulto a su inteligencia.

La trampa de esta ley es evidente: **si todo destaca, nada destaca**. Un HUD donde todo parpadea es tan ilegible como uno donde nada lo hace.

## Ley de proximidad

Viene de la psicología de la Gestalt, la misma que explica por qué ves formas en las nubes. **Los elementos que están cerca unos de otros se perciben como un grupo**, aunque sean distintos.

En una interfaz, eso te permite **ordenar sin necesidad de líneas ni recuadros**. La vida y el escudo van juntos porque se leen a la vez. En un inventario, los consumibles en un bloque, las armas en otro y los materiales en un tercero, con un poco más de espacio entre bloques que entre objetos. Y al revés: si pones juntas dos cosas que no tienen nada que ver, el jugador **va a suponer que están relacionadas**.

## Carga cognitiva y ley de Miller

Seguro que has oído que podemos retener "siete cosas, más o menos dos". Viene de un artículo de George Miller de 1956, y es probablemente la idea de psicología más citada (y peor citada) del diseño. Investigaciones posteriores, como las de Nelson Cowan, rebajan la cifra a unas **cuatro cosas a la vez**. Lo importante es que **la memoria de trabajo es muy pequeña** y que se llena enseguida.

En un juego, esa memoria ya está ocupada con lo que pasa en pantalla: dónde está el enemigo, cuándo va a atacar, por dónde huir. El HUD tiene que pedir lo mínimo. En un juego de lucha como *Street Fighter 6*, lo que vigilas en plena pelea se reduce a **tu vida, la del rival y tus barras de energía**, y todo lo demás pasa a un segundo plano.

La técnica más útil para aligerar esa carga es **agrupar** (en inglés, chunking): cuatro iconos sueltos cuestan más de leer que un único bloque con cuatro iconos ordenados. Por eso esta ley y la de proximidad trabajan juntas.

## Ley de Tesler

Larry Tesler, que trabajó en Xerox y en Apple, defendía que **todo sistema tiene una cantidad de complejidad que no se puede eliminar**. Lo único que puedes decidir es **quién carga con ella**: el juego o el jugador.

Un botón de "ordenar inventario" es un ejemplo perfecto. La complejidad de ordenar cuarenta objetos sigue ahí, pero ahora la asume el juego. Los juegos de estrategia como la saga *Civilization* hacen algo parecido a lo largo del tiempo: **presentan sus sistemas poco a poco**, con consejeros que te explican cada uno cuando lo necesitas, en lugar de enseñarte todos en la primera partida.

Cuando diseñes una pantalla complicada, pregúntate **qué parte de ese trabajo podría hacer el juego por el jugador**.

## Umbral de Doherty

En 1982, Walter Doherty y Ahrvind Thadani, dos investigadores de IBM, comprobaron que **cuando un sistema responde en menos de unos 400 milisegundos**, la gente trabaja más rápido y más concentrada. Por encima de ese tiempo, empieza a notarse la espera y se pierde el ritmo.

En un juego, la interfaz tiene que **responder al instante a cada pulsación**: el botón cambia de estado, suena un clic, algo se mueve. Si una acción va a tardar (cargar una partida, conectarse a un servidor), **enséñalo**: una animación, una barra de progreso, un icono girando. Lo peor que le puede pasar a un jugador es pulsar un botón y no saber si el juego le ha hecho caso. Así es como se acaba pulsando cinco veces y comprando cinco pociones.

## Resumen de las leyes

| Ley | Qué dice | Ejemplo en un juego |
|---|---|---|
| Hick | Más opciones, más tiempo para decidir | Menús radiales de pocas casillas, árboles de habilidades por ramas |
| Fitts | Lo grande y cercano se alcanza antes | Botones táctiles grandes, opciones frecuentes a una pulsación |
| Jakob | Se espera lo que ya se conoce | Convenciones de controles de cada plataforma y género |
| Von Restorff | Lo diferente destaca | Colores de rareza del botín, pintura amarilla en los salientes |
| Proximidad | Lo cercano se lee como un grupo | Vida y escudo juntos, inventario por bloques |
| Carga cognitiva | La memoria de trabajo es pequeña | HUD de un juego de lucha reducido a lo esencial |
| Tesler | La complejidad se reparte entre juego y jugador | Botón de ordenar inventario, sistemas que se presentan poco a poco |
| Doherty | La respuesta tiene que ser inmediata | Feedback en cada pulsación, indicadores de carga |
