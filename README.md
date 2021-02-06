# Marble
> **NOTE:** Marble is under active development. It currently only supports creating Express projects using a shell script. See the `marblepy` directory for progress on the *unified version* of Marble that will support numerous frameworks.

Marble is a tool to generate templates for numerous types of projects (mostly web development). These will create the project directory, setup the build environment, and install packages/libraries.

The generators are currently intended for use on Linux only (it relies on UNIX shell tools like jq). Compatibility with macOS and Windows to be implemented and tested at a later date.

## Usage

### Generate configuration file
A configuration file is necessary to determine where your projects are generated in. Options like preferred package manager and default packages are not implemented yet.

```
python3 marblepy/main.py --generate-config
```

### Generate a project
General format for project generation:
```
python3 marblepy/main.py [framework] [project_name] [...flags]
```

Example:
```
python3 marblepy/main.py express todo-list-app --use-nodemon
```

## Currently supported project types
- Express

## TODO

### Future project types
- [ ] Express (+ Mocha test framework option)
- [ ] Vue (+ router option)
- [ ] React (+ router option)
- [ ] Electron
- [ ] Spring framework (with Maven or Gradle)

### Features
- [ ] Switch to generic generator script; run child script or JSON file for each project type.
- [ ] Consolidate all generators into menu-based tool.
- [ ] Ncurses (TUI) menu.
- [ ] Optional project name and directory path parameters.
- [ ] Predefined package config metadata (e.g. author, license, etc).
- [ ] Flag to toggle router packages when initialising frontend projects.
- [ ] Flag or optional parameter for automatic `git` repository initialisation.