# Diagramas del curso

Todas las imágenes de `docs/assets/ut2` y `docs/assets/concept` se generan con estos scripts. Son originales (mascota y diagramas dibujados por código), así que no hay dudas de derechos.

Para regenerarlas después de cambiar algo:

```bash
cd herramientas/diagramas
python3 diagramas.py
```

- `sprites.py`: la mascota del curso, sus poses (idle, walking cycle, ataque) y utilidades de pixel art.
- `diagramas.py`: una función por diagrama. Cada una guarda un SVG en `docs/assets`.
