# Concept · Color y luz

Pinta el mismo personaje dos veces: una iluminado por un sol de mediodía y otra por la luz azulada de la luna. El dibujo es idéntico y, sin embargo, cuentan historias distintas. El color es de las herramientas más potentes que tienes para transmitir emoción, y también de las más fáciles de usar mal, porque cualquier combinación "se ve bien" en un asset suelto y falla cuando lo pones junto al resto del juego.

## El valor va antes que el color

Antes de elegir tonos conviene entender el valor: lo claro o lo oscuro que es un color. Es lo que hace que una imagen se lea. Si conviertes tu concept a escala de grises y todo queda en un gris medio uniforme, el color no lo va a arreglar.

Por eso muchos artistas resuelven primero la imagen en grises (lo viste en los [thumbnails](thumbnails.md)) y colorean después. Un truco útil mientras trabajas: ten una capa de ajuste en blanco y negro que puedas activar para comprobar el valor en cualquier momento.

## La paleta

La paleta es el conjunto limitado de colores con el que trabaja un proyecto. Limitarla es precisamente lo que le da coherencia: si cada artista elige sus colores libremente, el juego se fragmenta.

Al construirla piensa en tres cosas. La **armonía**: colores que funcionan juntos (análogos, complementarios, tríadas). La **temperatura**: los cálidos se acercan al espectador y transmiten energía o confort; los fríos se alejan y transmiten calma, distancia o amenaza. Y la **saturación**: los colores muy saturados atraen la mirada, así que resérvalos para lo importante.

En pixel art la paleta es todavía más importante, porque trabajas con muy pocos colores y cada uno se nota. Es habitual partir de paletas ya probadas (Lospec tiene un catálogo enorme) y adaptarlas al proyecto.

## Color con función

En un juego el color también da información. Guía la mirada hacia lo que importa (el objeto interactivo, la salida, el punto débil del enemigo). Diferencia facciones y tipos de enemigo. Comunica estado: daño, veneno, poder activo. Y separa planos: lo jugable suele tener más contraste y saturación que el fondo.

Cuidado con depender solo del color para transmitir información crítica. Una parte de los jugadores tiene algún tipo de daltonismo, así que refuerza lo importante también con forma, valor o iconografía.

## La luz dentro del concept

La luz define la hora del día, la atmósfera y el tono emocional de una escena. En el concept te interesan tres decisiones:

- **La fuente.** Sol, luna, antorcha, pantalla, magia. Condiciona todo lo demás.
- **La dirección.** La luz lateral da drama y textura, la frontal aplana, la luz desde abajo inquieta y el contraluz crea siluetas.
- **El color de la luz.** La luz dorada del atardecer transmite calidez o nostalgia; la luz azul, frío o misterio. Las sombras suelen tomar el color complementario de la luz.

## Color keys y color script

Un **color key** es un thumbnail en color que fija la paleta y la luz de una escena o un momento concreto. Se pinta sin detalle, porque solo sirve para decidir la atmósfera. Se hacen varios para comparar (la misma escena al amanecer, a mediodía y de noche) y se elige uno.

Un **color script** es la secuencia de color keys de todo un juego o de un nivel, colocados en orden. Permite ver de un vistazo cómo evoluciona la emoción: dónde el juego se vuelve frío y opresivo, dónde recupera la calidez. Pixar lo popularizó en cine, y en videojuegos se usa para planificar la progresión visual de los niveles.

En la **UT4** vas a usar color keys como referencia para configurar la iluminación de tu escena 3D, y compararás el render con tu key para ver si has conseguido la atmósfera que buscabas.
