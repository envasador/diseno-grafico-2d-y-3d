# Anexo A.2 El HUD y los tipos de interfaz

El término **HUD** viene de la aviación. Un head-up display proyecta los datos de vuelo en un cristal delante del piloto, para que pueda leerlos **sin bajar la cabeza** hacia los instrumentos. Los videojuegos se quedaron con el nombre y con la idea: el HUD es **la información que ves mientras juegas**, sin salir de la acción.

Conviene no confundirlo con la UI en general. El menú principal, el inventario o la pantalla de opciones son interfaz, pero no son HUD. **El HUD es solo la parte que convive con el juego en marcha**: la vida, la munición, el minimapa, el contador de monedas, el aviso de "pulsa X para abrir".

<iframe width="560" height="315" src="https://www.youtube.com/embed/aHn_SsVBYAc" title="¿Qué es el HUD y cómo se utiliza? Diseño de Videojuegos, de Yisus XIII" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

*[¿Qué es el HUD y cómo se utiliza? Diseño de Videojuegos](https://www.youtube.com/watch?v=aHn_SsVBYAc), de Yisus XIII. Un repaso corto con ejemplos de HUD que funcionan y de HUD que no. © de su autor; uso con fines educativos.*

## Dos preguntas para clasificar cualquier interfaz

En 2009, Erik Fagerholt y Magnus Lorentzon publicaron un estudio sobre interfaces de shooters en primera persona que se ha convertido en la referencia para hablar de este tema. Su idea es muy sencilla: **cualquier elemento de interfaz se clasifica respondiendo a dos preguntas**.

La primera: **¿existe dentro de la historia del juego?** Es decir, ¿lo vería el personaje si fuera una persona real dentro de ese mundo? La segunda: **¿está dentro del espacio 3D de la escena?** Es decir, ¿ocupa un lugar en el escenario, con su perspectiva y su profundidad, o está pegado a la pantalla como una pegatina?

Con dos preguntas de sí o no salen cuatro combinaciones, y cada una es un tipo de interfaz.

| | Está en el espacio de la escena | No está en el espacio de la escena |
|---|---|---|
| **Existe en la historia** | Diegética | Meta |
| **No existe en la historia** | Espacial | No diegética |

<figure>
<img src="https://eu-images.contentstack.com/v3/assets/blt740a130ae3c5d529/blt412f241f1ca11183/650ebbd21c5c32ab3258970a/terminology.gif" alt="Esquema de los cuatro tipos de interfaz según Fagerholt y Lorentzon" loading="lazy" referrerpolicy="no-referrer">
<figcaption>El esquema original de los cuatro tipos de interfaz. Imagen: Fagerholt y Lorentzon, <i>Beyond the HUD</i> (Chalmers University of Technology, 2009), publicada en <a href="https://www.gamedeveloper.com/design/game-ui-discoveries-what-players-want">Game Developer</a>. © de sus autores; uso con fines educativos.</figcaption>
</figure>

La palabra **diegético** viene del cine y de la teoría literaria: es todo lo que pertenece al mundo de la historia. La música que suena en la radio de una escena es diegética (los personajes la oyen); la banda sonora que suena por encima no lo es (solo la oyes tú).

## Interfaz no diegética

Es la de toda la vida: **elementos dibujados encima de la imagen que solo ve el jugador**. Los corazones de Zelda, el contador de monedas de Mario, la posición en la carrera. El personaje no sabe que tiene una barra de vida flotando en la esquina.

En *Mario Kart 8 Deluxe* la posición, el objeto que llevas, las vueltas y el minimapa ocupan las esquinas y **dejan libre el centro**, que es donde está la carretera. Los iconos son grandes y de colores muy saturados para que se lean a 150 km/h y con tres caparazones rojos persiguiéndote.

*Blasphemous* (The Game Kitchen, un estudio de Sevilla) muestra cómo una interfaz no diegética puede tener mucha personalidad. En la parte superior de la pantalla tienes la **barra roja de vida**, la **barra azul de Fervor** (la energía para las habilidades), los **Frascos Biliares** que te curan y el contador de **Lágrimas de Expiación** (la moneda del juego), todo enmarcado con ornamentación barroca que **sale directamente del arte del juego**. No forma parte del mundo, pero se nota que pertenece a él.

<!-- Imagen pendiente: captura del HUD de Blasphemous con su crédito -->

Su gran ventaja es la **claridad**: puedes ponerla donde quieras, al tamaño que quieras y con el contraste que haga falta. Además es la más fácil de adaptar para jugadores con necesidades distintas, porque cambiar su tamaño o su color no afecta al mundo del juego.

## Interfaz diegética

Aquí la información **forma parte del mundo** y el personaje la ve igual que tú. El ejemplo de manual es *Dead Space*: la vida de Isaac aparece como una **columna de luces en la espalda de su traje**, la munición se proyecta en un pequeño holograma **sobre el propio arma** y el inventario se abre como una **pantalla holográfica delante del personaje**. Ese último detalle tiene truco: como el inventario existe dentro del juego, **el juego no se pausa** mientras lo miras, y un necromorfo puede alcanzarte mientras eliges qué botiquín usar.

<!-- Imagen pendiente: captura de Isaac de espaldas con la barra de vida en el traje (Dead Space) -->

*Metro 2033* lleva la idea más lejos. El reloj de pulsera del protagonista te dice cuánto le queda al filtro de la máscara de gas y tiene un indicador que se enciende cuando estás iluminado (y, por tanto, cuando te pueden ver). En *Far Cry 2*, para consultar el mapa, el personaje **saca un mapa de papel y lo sostiene en la mano** mientras sigue caminando. En *Silent Hill 2*, la radio que lleva James empieza a soltar estática cuando hay un monstruo cerca, y la linterna define literalmente lo que puedes ver.

La interfaz diegética **sumerge muchísimo**, pero tiene un precio: es **más difícil de leer** (tienes que interpretar la luz de un traje en lugar de leer un número) y **más difícil de adaptar**. Si un jugador necesita la vida más grande, no puedes hacerle la espalda de Isaac el doble de ancha.

## Interfaz espacial

Elementos que **están colocados en el escenario 3D, pero que el personaje no vería**. Existen para ayudarte a ti, aunque respeten la perspectiva y la profundidad de la escena.

En *Left 4 Dead*, tus compañeros aparecen **con un contorno de color a través de las paredes** para que no os separéis. En *Splinter Cell: Conviction*, los objetivos de la misión se **proyectan como texto sobre las paredes** del escenario. Y en muchísimos juegos de acción ves la barra de vida de cada enemigo flotando sobre su cabeza, o los números de daño saltando desde el punto donde has golpeado.

Es una solución muy útil cuando la información **tiene que ver con un lugar concreto del mundo**: dónde está un objeto, a quién le queda poca vida, por dónde se va. Su riesgo es llenar el escenario de cosas flotando hasta que deja de verse el escenario.

## Interfaz meta

La más curiosa de las cuatro: **información que pertenece a la historia, pero que se muestra sobre la pantalla** en lugar de dentro del escenario. El ejemplo más conocido es el de los shooters como *Call of Duty*: cuando te hieren, **los bordes de la pantalla se llenan de sangre** y la imagen se vuelve más roja cuanto peor estás. El daño es real dentro de la historia (el personaje está herido), pero la sangre está pegada a la cámara.

Otro ejemplo, de nuevo en *Metro 2033*: cuando la máscara de gas se daña, **ves el cristal agrietado delante de la imagen**. La máscara existe en el mundo, pero la vives como una capa sobre la pantalla.

<!-- Imagen pendiente: captura con el cristal de la máscara agrietado (Metro 2033 o Metro Exodus) -->

La interfaz meta es muy buena para **transmitir sensaciones** (dolor, mareo, poco oxígeno) y bastante mala para transmitir **datos exactos**. Nadie sabe cuántos puntos de vida le quedan mirando cuánta sangre hay en los bordes.

## Juegos que mezclan varios tipos

Muy pocos juegos usan un solo tipo. En *The Legend of Zelda: Breath of the Wild*, los corazones y la resistencia son no diegéticos, pero el mapa y el inventario se consultan en la **tableta sheikah**, un objeto que Link lleva encima. Además, el juego tiene un **modo de HUD reducido** que esconde casi todo para que mires el paisaje y no las esquinas.

*Ghost of Tsushima* tiene una solución preciosa para la navegación: en lugar de una flecha o un punto en el minimapa, **el viento sopla hacia tu objetivo** y mueve la hierba, los árboles y la ropa de Jin en esa dirección. Lo que en otro juego sería un icono aquí es parte del paisaje.

<!-- Imagen pendiente: captura del viento guía de Ghost of Tsushima -->

La pregunta útil, por tanto, es **qué tipo de interfaz conviene a cada dato**. La vida en un juego de lucha tiene que ser no diegética y enorme, porque se consulta cada segundo. La dirección hacia el objetivo en un juego de exploración puede ser diegética, porque se consulta con calma y a cambio te deja mirar el mundo.

!!! example "Haz la prueba"
    Elige una captura de un juego que conozcas bien y clasifica cada elemento de interfaz en uno de los cuatro tipos, respondiendo a las dos preguntas. Después escoge uno de esos elementos y piensa cómo sería si fuera de otro tipo: ¿cómo mostrarías la munición de forma diegética en ese juego? ¿Qué ganaría y qué perdería?

## Interfaz de sonido y vibración

La interfaz también **se oye y se siente**. Son canales que no compiten con la vista, y por eso son tan valiosos cuando la pantalla va llena.

En *Resident Evil 2* (la versión de 2019), los **pasos de Mr. X** te dicen que viene a por ti y desde dónde mucho antes de que lo veas. En *Hellblade: Senua's Sacrifice*, las voces que oye la protagonista te **avisan de los ataques que llegan por la espalda**. Y prácticamente todos los juegos usan un sonido de alarma cuando la vida está muy baja.

La **vibración del mando** (lo que se llama respuesta háptica) también comunica: un golpe fuerte, el retroceso de un arma, la textura del suelo. Con mandos como el DualSense de PlayStation 5 puede ser muy precisa: en *Astro's Playroom* notas la diferencia entre caminar sobre arena, sobre hielo o sobre metal.

Estos canales tienen la misma pega que la interfaz diegética: **no todo el mundo puede percibirlos**. Un aviso que solo se oye no existe para un jugador sordo o para alguien que juega sin volumen en el autobús. Por eso los juegos cuidados **duplican la información importante en otro canal**, como verás en el apartado de [accesibilidad](05-accesibilidad.md).

## Cuándo esconder el HUD

Un HUD no tiene por qué estar siempre entero en pantalla. Muchos juegos usan un **HUD dinámico**: la barra de vida aparece cuando recibes daño y se desvanece cuando te recuperas; la munición aparece cuando disparas o recargas. Así la pantalla queda limpia la mayor parte del tiempo y **la interfaz aparece justo cuando tiene algo que decir**.

En las cinemáticas, en los momentos de contemplación o en los juegos de terror, esconder el HUD ayuda a la atmósfera. Lo que conviene casi siempre es **dejar que el jugador decida**: una opción para mostrar el HUD completo, uno reducido o ninguno cuesta poco y deja contentos tanto a quien quiere ver todos los datos como a quien quiere hacer capturas del paisaje.
