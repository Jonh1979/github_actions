# Plantilla para desarrollo guiado por pruebas en Python

Proyecto base para crear aplicaciones siguiendo la metodología TDD

## Instrucciones

1. Crea un nuevo repositorio a partir de la plantilla.
1. Crea un entorno virtual con la herramienta `pipenv`. Ejecuta estos comandos en la raíz del proyecto:
   ```bash
   $ pip install --user pipenv ### Instala la herramienta pipenv en el entorno del usuario
   $ mkdir .venv ### Opcional: Crea el entorno virtual dentro del proyecto
   $ pipenv install
   ```
   El comando `pipenv install` crea el entorno virtual e instala las dependencias definidas en el fichero `Pipfile`.
1. Accede al entorno virtual:
   ```bash
   $ pipenv shell
   ```
1. Ejecuta las pruebas:
   ```bash
   $ pytest tests
   ```

## Integración continua

- Añade un flujo de trabajo de GitHub Actions para validar las pruebas
- Crea las pruebas en el directorio  `tests/`. Los archivos deben empezar con el nombre `test_`.

## Referencias

- [GitHub Actions: About continuous integration](https://docs.github.com/es/actions/automating-builds-and-tests/about-continuous-integration)
- [GitHub Actions: Building and testing Python](https://docs.github.com/es/actions/automating-builds-and-tests/building-and-testing-python)
- [PyTest With GitHub Actions](https://blog.dennisokeeffe.com/blog/2021-08-08-pytest-with-github-actions)
- [Documentación del framework `pytest` para la realización de pruebas en Python](https://docs.pytest.org/)
