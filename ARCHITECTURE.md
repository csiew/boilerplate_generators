# Architecture
Marble will be divided into backend and frontend applications. The backend application is a Python CLI application that accepts arguments. The frontend application is an Electron application that calls the backend application.

## Backend application
`marblepy` is a Python CLI application that follows object-oriented programming conventions (as much as Python could possibly offer).

### main.py
The main body of the application sits in `main.py`. It parses user arguments and performs the project generation. Project generation is a combination of usage of the `os`, `sys`, and `subprocess` libraries to perform file system operations and perform shell commands. This may include calling a Node package manager like `npm` or `yarn`.

### Generator
A generator object (defined in `generator.py`) accepts an `id`, the user config (`config`), project properties (`properties`), and CLI flags (`flags`).

Generator implementations live in the `frameworks` directory.

Implementations of the generator class, for example `express_generator.py`, create the project directory, perform the actual project generation (i.e. performing an `npm init` or `yarn init`), and installs additional packages.

The Express option provides a template `index.js` file, which is copied from the `marblepy` directory to the project directory. Other frameworks and options, such as for React with `react-router-dom` will require the generator to manipulate the `npm`/`yarn` generated project files to support routing.
