# UT2.5 Principios de animación

Puedes tener todos los frames de una animación perfectamente dibujados y que, al reproducirla, parezca rígida, lenta o sin vida. Frustrante, ¿verdad? La buena noticia es que **casi nunca es culpa del dibujo**. Lo que hace que un movimiento convenza depende de unas pocas decisiones: **qué poses eliges, cuántos frames pones entre ellas y cuánto dura cada una**.

Los animadores de Disney recopilaron hace décadas doce principios de animación. Aquí vas a ver **los cuatro que más vas a usar en pixel art**, y lo haremos con la animación más humilde que existe: una pelota que bota. Si consigues que una pelota tenga vida, lo tienes casi todo.

## Fotogramas clave

Los **fotogramas clave (keyframes)** son los frames más descriptivos de una animación, las poses que cuentan qué está pasando. En una pelota que bota son tres: arriba, abajo tocando el suelo y arriba otra vez. En un puñetazo, el brazo recogido y el brazo extendido.

La regla es que, encadenando solo los fotogramas clave, **la animación ya tiene que entenderse**. Si con las poses clave no se lee la acción, añadir frames intermedios no lo va a arreglar.

<figure markdown>
![Fotogramas clave de una pelota que bota](../assets/ut2/keyframes.png){ loading=lazy }
<figcaption>Solo con los fotogramas clave la acción ya se entiende, aunque todavía salta de golpe. Uso con fines educativos.</figcaption>
</figure>

Por eso **siempre, siempre, se empieza por aquí**. Dibuja las poses clave, reprodúcelas y comprueba que la acción se entiende antes de seguir. Esas poses salen directamente de tu [hoja de poses](../concept/hojas-de-produccion.md#hojas-de-expresiones-y-de-poses) del concept.

## Interpolaciones

Las **interpolaciones (inbetweens)** son los frames que se dibujan entre dos fotogramas clave para que el ojo perciba el movimiento como continuo. Con solo las poses clave, la pelota aparece arriba y de repente abajo. Con interpolaciones, recorre el camino.

<figure markdown>
![Fotogramas clave con interpolaciones intermedias](../assets/ut2/interpolaciones.png){ loading=lazy }
<figcaption>Las interpolaciones rellenan el camino entre poses clave y hacen que el movimiento sea fluido. Uso con fines educativos.</figcaption>
</figure>

¿Cuántas interpolaciones pongo? Depende de la fluidez que quieras y del tiempo que tengas. Más frames dan un movimiento más suave, pero multiplican el trabajo. Y aquí va un secreto del pixel art: **pocos frames bien elegidos suelen resultar más expresivos que muchos**.

## Timing

El **timing** es el tiempo que tarda un elemento en realizar una acción, y es lo que **le da peso, emoción e intención**. Haz la prueba: la misma pelota, con el mismo dibujo, parece de goma o de plomo solo con cambiar cuánto tarda en caer y en subir.

El timing se controla de dos formas: **con el número de frames y con la duración de cada frame**. En pixel art es muy habitual no dar la misma duración a todos. **Las poses importantes se mantienen más tiempo** y los frames de transición pasan rápido.

<figure markdown>
![Distribución del timing en una animación](../assets/ut2/timing.png){ loading=lazy }
<figcaption>Con el timing decides cuánto dura cada tramo del movimiento: dónde se acumulan los frames y dónde se separan. Uso con fines educativos.</figcaption>
</figure>

En la pelota, fíjate en el espaciado: cerca de la parte alta los frames están muy juntos (la pelota frena, se queda casi quieta y empieza a caer) y cerca del suelo están muy separados (va rápida). Ese cambio de espaciado es **lo que el ojo interpreta como gravedad**.

## Squash, stretch y motion blur

El **squash** (aplastamiento) y el **stretch** (estiramiento) son deformaciones que aplicas a la forma de un objeto mientras se mueve. La pelota se estira cuando cae deprisa y se aplasta al chocar con el suelo. Sirven para expresar flexibilidad, velocidad e impacto, y hacen que los elementos animados dejen de parecer rígidos.

Hay una regla que no puedes saltarte: **el volumen se conserva**. Si la pelota se aplasta en vertical, se ensancha en horizontal, como un globo de agua cuando lo apoyas en la mesa. Si solo la achatas, parecerá que encoge.

<figure markdown>
![Squash al tocar el suelo y stretch durante la caída](../assets/ut2/squash-stretch.png){ loading=lazy }
<figcaption>Squash al impactar y stretch en la caída. Son frames que por separado parecen "raros", y es lo normal. Uso con fines educativos.</figcaption>
</figure>

El **motion blur** (desenfoque de movimiento) es el efecto que representa un objeto que se mueve tan deprisa que deja un rastro. En pixel art **se dibuja a mano**: una estela, una forma alargada o varias copias superpuestas del objeto. Se usa en movimientos bruscos o veloces, como un golpe de espada, y combinado con stretch resulta muy eficaz.

Vistos sueltos, estos frames parecen dibujos mal hechos. Reproducidos a velocidad, **son los que dan vida a la animación**. Pausa cualquier película de animación en mitad de un movimiento rápido y verás personajes deformados de maneras imposibles (y a veces bastante ridículas). Ahí está el truco.

| Principio | Qué controla | Pregunta para comprobarlo |
|---|---|---|
| Fotogramas clave | Qué pasa | ¿Se entiende la acción solo con las poses clave? |
| Interpolaciones | Fluidez | ¿El movimiento es continuo o salta? |
| Timing | Peso e intención | ¿Pesa lo que tiene que pesar? |
| Squash, stretch y motion blur | Flexibilidad, velocidad e impacto | ¿Se siente la velocidad y el golpe? |
