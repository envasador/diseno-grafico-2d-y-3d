# UT4.1 Iluminación

Haz una prueba rápida. Coge una linterna, apaga la luz de la habitación y alumbra tu cara desde abajo, a lo película de miedo. Ahora ilumínala desde arriba y un poco de lado. Es la misma cara, y en un caso das miedo y en el otro pareces el protagonista de un anuncio. La luz decide cómo se siente una escena más que casi cualquier otra cosa.

En un juego, además, la luz tiene otro coste: el del ordenador. Cada luz y cada sombra hay que calcularlas, así que aquí vas a aprender a iluminar bien y a iluminar barato.

## Los cuatro tipos de luz de Blender

Las luces se añaden como cualquier objeto, con Mayús + A > Light. Blender tiene cuatro, y cada una imita una fuente de luz del mundo real:

| Tipo | Cómo emite | Qué imita |
|---|---|---|
| Point | En todas direcciones desde un punto | Una bombilla, una vela, una antorcha |
| Spot | En un cono desde un punto | Una linterna, un foco de escenario, una farola |
| Area | Desde una superficie (rectangular o circular) | Una ventana, un panel de luz, luz suave de estudio |
| Sun | Rayos paralelos desde infinitamente lejos | El sol (su posición no importa, solo su dirección) |

Lo de Sun merece una aclaración, porque despista mucho al principio: da igual dónde coloques la luz en la escena, solo cuenta hacia dónde apunta. Es lógico, porque el sol está tan lejos que ilumina igual toda tu escena.

## Las propiedades que vas a tocar

Selecciona una luz y ve a la pestaña de la bombilla en el panel Propiedades. Aunque cada tipo tiene las suyas, hay tres que vas a tocar siempre:

- **Power** (o **Strength** en el Sun): la intensidad. Las luces Point, Spot y Area se miden en vatios, como las bombillas de verdad.
- **Color**: el color de la luz. Casi nunca es blanco puro: el sol de la tarde es anaranjado, la luna es azulada y una antorcha tira a rojo.
- **Radius** o **Size**: el tamaño de la fuente de luz. Esta es la que más sorprende. Una luz pequeña da sombras nítidas y duras; una luz grande da sombras suaves y difusas. Piensa en el sol de mediodía (pequeño en el cielo, sombras marcadas) frente a un día nublado (todo el cielo ilumina, casi no hay sombras).

En las Spot tienes además **Spot Size**, que abre o cierra el cono, y **Blend**, que decide si el borde del círculo de luz es nítido o se difumina.

## La iluminación de tres puntos

Si no sabes por dónde empezar a iluminar algo, empieza por aquí. Es el esquema clásico del cine y la fotografía, y funciona casi siempre:

1. **Luz principal** (key light): la que manda. Suele ir a un lado de la cámara y algo elevada, y es la que dibuja las sombras.
2. **Luz de relleno** (fill light): más suave y menos intensa, en el lado contrario. Su trabajo es aclarar las sombras de la principal para que no queden negras del todo.
3. **Contraluz** (back light o rim light): detrás del sujeto, apuntando hacia la cámara. Dibuja un borde de luz alrededor de la silueta y la despega del fondo.

¿Te acuerdas de la comprobación de silueta de Concept? El contraluz es tu mejor aliado para que el personaje se lea sobre cualquier fondo.

Y un consejo de oro: enciende las luces de una en una. Coloca la principal sola y no añadas la siguiente hasta que te guste lo que hace. Si lo enciendes todo a la vez, no sabrás qué luz está haciendo qué.

## Sombras y oclusión ambiental

Las **sombras** son las que pegan los objetos al suelo. Sin ellas, todo parece flotar. Cada luz tiene su casilla de Shadow en sus propiedades, y en juegos se piensa bien cuáles la llevan activada, porque cada luz que proyecta sombras cuesta rendimiento.

La **oclusión ambiental** (ambient occlusion, AO) es algo más sutil: el oscurecimiento suave que aparece en rincones, grietas y en los sitios donde dos objetos se tocan, porque ahí llega menos luz rebotada. Fíjate en la esquina de tu habitación donde se juntan dos paredes y el techo: está un poco más oscura aunque nada le haga sombra directamente. Eso es oclusión ambiental.

En Blender depende del motor de render. **Cycles** la calcula de forma natural, porque simula cómo rebota la luz de verdad. **EEVEE**, el motor en tiempo real (el más parecido a lo que hace un motor de juego), la aproxima, y en las versiones actuales la incluye dentro de su cálculo de iluminación, con los ajustes en la pestaña de propiedades de render.

## La luz del entorno

Además de las luces que colocas, hay una luz que lo envuelve todo: el **World**, el mundo que rodea la escena. Por defecto es un gris oscuro, y por eso las primeras escenas se ven tan apagadas.

Puedes darle un color (azulado para un exterior de día, por ejemplo) o, mucho mejor, cargar una **imagen HDRI**: una foto panorámica de 360 grados que ilumina la escena como lo haría ese lugar real. Con un HDRI de un bosque al atardecer, tu escena se ilumina como un bosque al atardecer. En Poly Haven tienes cientos gratuitos.

## De Blender al motor: luz estática y dinámica

Todo lo anterior sirve para renderizar en Blender. En un motor de juego hay que tomar además una decisión muy importante sobre cada luz:

| | Luz estática (baked) | Luz dinámica |
|---|---|---|
| Cómo funciona | Se calcula una vez y se guarda en texturas (lightmaps) | Se calcula en cada fotograma |
| Coste en el juego | Casi nulo | Alto, sobre todo con sombras |
| Calidad | Muy alta, con rebotes y sombras suaves | Más limitada |
| Limitación | No cambia: si mueves algo, la luz no lo sigue | Reacciona a todo lo que se mueve |
| Úsala para | Escenarios, arquitectura, todo lo que no se mueve | Personajes, linternas, explosiones, ciclos de día y noche |

Lo habitual es mezclarlas: el escenario con luz horneada, que queda preciosa y no cuesta nada, y unas pocas luces dinámicas para lo que se mueve. Esa mezcla, y cómo se configura en el motor, la trabajarás en el proyecto de la cinemática.

## Para practicar

- Ilumina la misma esfera o busto con cuatro esquemas: solo luz principal, principal y relleno, tres puntos completos, y solo contraluz. Haz un render de cada uno y compáralos.
- Coloca un personaje o un prop en una escena y prueba tres HDRI distintos (un día soleado, un interior y una noche). Fíjate en cuánto cambia la sensación sin tocar ni una luz.
- Recrea con luces el ambiente de uno de tus color keys y pon el render al lado del key. ¿Qué se parece y qué no?
