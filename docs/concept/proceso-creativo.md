# Concept · El proceso creativo

Mucha gente se imagina el arte conceptual como una persona inspirada que se sienta y dibuja el diseño definitivo a la primera. En un estudio funciona al revés: el concept es **un proceso ordenado** que empieza por leer un encargo y termina con documentos que otra persona puede usar para producir. La inspiración ayuda, pero lo que hace que un diseño funcione es **haber recorrido todas las fases sin saltarte ninguna**.

Este proceso es el que vas a repetir en todas las unidades del curso. Lo que produces al final cambia (un sprite, un modelo, una escena iluminada), las fases no.

## El brief: qué te están pidiendo

Todo empieza con el **brief**, el documento que describe el encargo. Responde a las preguntas básicas: qué tipo de juego es, en qué mundo ocurre, quién es el personaje o qué función tiene el objeto, para qué plataforma se hace y quién lo va a jugar. También suele incluir **restricciones técnicas**, como el tamaño del sprite, el número de frames o el presupuesto de polígonos.

Lee el brief entero antes de abrir ningún programa y subraya dos cosas: **lo que es obligatorio y lo que queda abierto**. Lo obligatorio no se discute (si el sprite es de 32×32, es de 32×32). Lo abierto es tu espacio creativo, y es donde vas a demostrar criterio. Si algo no está claro, **se pregunta en esta fase**; descubrir un malentendido cuando el asset ya está terminado es la forma más cara de equivocarse.

Si el encargo es un personaje, apunta también su papel en la historia, su personalidad y el mundo del que viene: época, clima, tecnología. Y hazte una pregunta que el brief casi nunca escribe: **qué tiene que contar el diseño**. Imagina que te piden un soldado que vive en el desierto. Le pones "ropa futurista" y listo, ¿verdad? Pues no tan rápido. ¿Dónde guarda el agua? ¿Cómo se protege del sol? ¿Puede correr por la arena con todo eso encima? Cuando la silueta, los materiales y el desgaste responden a esas preguntas, **el personaje parece vivir en ese desierto**. Cuando no, parece que está de visita.

## Referencias y moodboard

Nadie diseña desde cero. Antes de dibujar, buscas material: fotografías reales, otros juegos, películas, ilustración, arquitectura, texturas. Lo que buscas al recopilar es **ampliar tu vocabulario visual**, y cuantas más referencias de calidad tengas, más opciones propias vas a poder generar.

Las referencias se organizan en un **[moodboard](moodboard.md)**, que fija la atmósfera y el estilo que buscas. En la práctica, la investigación y el moodboard ocurren a la vez: encuentras una imagen, la colocas, y al verla junto a las otras te das cuenta de qué te falta buscar.

## Exploración: muchas ideas rápidas

Con el moodboard delante, empiezas a dibujar, y la clave de esta fase es **la cantidad**. Haces muchas [siluetas](siluetas.md) y [thumbnails](thumbnails.md) pequeños, rápidos y sin detalle, para probar variaciones: más alto, más bajo, con capa, con armadura, con un arma a dos manos. Si haces tres bocetos, te vas a quedar con uno de ellos por falta de alternativas. Si haces treinta, vas a encontrar dos o tres que funcionan de verdad.

**No te enamores de la primera idea.** Suele ser la más obvia, la que se le habría ocurrido a cualquiera.

## Desarrollo: elegir y refinar

De la exploración salen unos pocos candidatos, y ahora toca desarrollarlos: definir proporciones, probar [color](color.md), añadir los detalles que cuentan algo del personaje o del objeto. Aquí también **compruebas que el diseño funciona en el juego**. Un personaje precioso a tamaño de ilustración puede ser ilegible a 32 píxeles; una armadura muy compleja puede ser imposible de modelar con el presupuesto del proyecto.

¿Y cómo sabes si un candidato es mejor que otro? Hazle **cuatro preguntas**:

| Pregunta | Qué compruebas | Un ejemplo |
|---|---|---|
| Función: ¿para qué existe? | Que el diseño sirve para lo que hace | Una mochila de exploración tiene que cargar equipo y aguantar el barro |
| Narrativa: ¿qué cuenta? | Que habla del mundo o de su historia | Un remiendo, un arañazo o una insignia dicen por dónde ha pasado |
| Legibilidad: ¿se entiende rápido? | Que se reconoce de un vistazo y a distancia | Una silueta clara distingue al personaje en plena pelea |
| Coherencia: ¿encaja en el mundo? | Que materiales, tecnología y colores responden al tono del juego | Una espada láser en un pueblo medieval necesita una excusa muy buena |

Si un diseño falla en alguna, ya sabes por dónde atacarlo. Si pasa las cuatro, tienes un candidato serio. Y a veces ninguno gana del todo: entonces lo mejor es **combinar lo bueno de varios**, la silueta de uno con la paleta de otro.

En escenarios y estructuras complicadas hay un truco muy de estudio: montar **un bloque 3D sencillo**, sacarle una captura con el encuadre que quieres y pintar encima. La perspectiva te la regala el programa.

### En qué orden se trabaja

El error más típico de esta fase es lanzarse al detalle demasiado pronto. Te pasas dos horas con las hebillas del cinturón y entonces descubres que la pose no funciona. Adiós, hebillas. **Detallar pronto hace carísimo corregir**, así que sigue este orden:

1. Idea y función.
2. Silueta y composición.
3. Valores: luz, sombra y contraste, todavía en grises.
4. Color.
5. Materiales y detalle final.

Fíjate en el paso 3. Antes de elegir un solo color, mira la imagen en blanco y negro. ¿Dónde se va la mirada primero? ¿La figura se separa del fondo? ¿Se entiende la escala? **Si en grises no funciona, el color no la va a rescatar** (lo tienes contado en [Color y luz](color.md)). Después llegan los [color keys](color.md#color-keys-y-color-script), que deciden la hora del día, la temperatura y la emoción de la imagen.

El acabado depende del uso. Una imagen de ambiente puede ser suelta y pictórica. Una hoja para que alguien modele en 3D necesita vistas limpias y notas de construcción. **Pule hasta donde lo necesite quien lo va a usar**, y ni un píxel más.

Esta fase es **iterativa**: dibujas, lo enseñas, recibes comentarios, ajustas y vuelves a dibujar.

## Revisión y feedback

**Ningún diseño se aprueba en solitario.** En un estudio se revisa con la dirección de arte, con diseño y con programación, porque cada uno mira cosas distintas: si encaja con el estilo, si comunica lo que la mecánica necesita, si es viable técnicamente. En clase haremos lo mismo con revisiones entre compañeros y conmigo.

Recibir feedback es una habilidad que se entrena. Cuando alguien te dice que algo no funciona, lo útil es preguntar qué ha visto y por qué, y **separar el problema que detecta de la solución que propone**. Muchas veces el problema es real y la solución que te sugieren no es la mejor.

## Finalización: documentos para producción

Cuando el diseño está aprobado, lo preparas para que otra persona pueda producirlo. Eso significa **[hojas de producción](hojas-de-produccion.md)**: vistas desde varios ángulos, poses clave, paleta con valores exactos, notas sobre materiales. Todo acaba en tu [biblia de arte](biblia-de-arte.md).

La prueba de que has terminado bien es sencilla: **si alguien del equipo puede producir tu asset sin tener que preguntarte nada**, tu concept está listo.

| Fase | Pregunta que responde | Lo que entregas |
|---|---|---|
| Brief | ¿Qué me piden y con qué límites? | Brief leído y dudas resueltas |
| Referencias y moodboard | ¿Cómo se siente este mundo? | Moodboard |
| Exploración | ¿Qué opciones hay? | Siluetas y thumbnails |
| Desarrollo | ¿Cuál funciona mejor y por qué? | Diseños refinados con color |
| Revisión | ¿Funciona para el juego y el equipo? | Cambios aplicados |
| Finalización | ¿Puede otra persona producirlo? | Hojas de producción y biblia de arte |

## Un encargo de principio a fin

Vamos a recorrer todo el proceso con un encargo concreto: *diseña una biblioteca submarina abandonada para un juego de aventuras*.

**Brief.** Lo obligatorio: es un escenario que se explora y dentro hay un objetivo que encontrar. Lo abierto: casi todo lo demás. Te piden que se sienta antigua, misteriosa y con ganas de que la recorras.

**Referencias.** Bibliotecas históricas, barcos hundidos, arrecifes de coral, animales bioluminiscentes, arquitectura naval. Casi nada de videojuegos, y el moodboard ya huele a salitre.

**Exploración.** Quince thumbnails en grises: salas alargadas, salas redondas, entrada por arriba, entrada por un túnel, luz desde una grieta, luz desde un pez linterna del tamaño de un autobús.

**Desarrollo.** Gana una sala circular con una gran cúpula rota, y pasa las cuatro preguntas: tiene rutas que se pueden recorrer, la cúpula cuenta que algo la golpeó, la forma se lee de un vistazo y encaja con el resto del juego. En valores, el haz de luz entra por la cúpula y lleva la mirada directa a un libro iluminado, que es el objetivo. En color, azules profundos y verdes apagados, con una luz cálida solo sobre el libro.

**Revisión.** Diseño de niveles pide ensanchar una ruta de acceso, y alguien comenta que el libro se pierde entre tanta estantería. Se ensancha el paso y se baja el contraste de las estanterías cercanas.

**Finalización.** Hojas con las estanterías modulares, las zonas derrumbadas, los materiales y una figura del personaje al lado para la escala. Todo a la biblia de arte.

Fíjate en el libro iluminado: aparece en los thumbnails, en los valores, en el color y en la revisión. **Una buena idea atraviesa todas las fases**, y cada fase la hace un poco más clara.
