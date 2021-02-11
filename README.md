# Marble
> **NOTE:** Marble is under active development. The frontend, `marble-vue` is still a work in progress. Please try `marblepy` if you want to actually generate a project!

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

Examples:
```
python3 marblepy/main.py express todo-list-app
python3 marblepy/main.py express todo-list-app --use-nodemon
python3 marblepy/main.py express todo-list-app --use-nodemon --use-express-session --install-packages marked ejs
```

### Flags
| Framework | Flag | Value | Description |
|-----|-----|-----|-----|
| *Node projects (Express, React, Vue, etc)* | `--install-packages`      | *Package names (space separated)* | Install additional packages. |
| `express` | `--use-nodemon`           | *none*  | Install and enable `nodemon` for automatic runtime restarts when making changes to source code. |
|           | `--use-express-session`   | *none*  | Install `express-session` to enable login sessions for your app. |
| `react`   | `--use-react-router-dom`  | *none*  | Install and enable `react-router-dom`. |
|           | `--use-material-ui`       | *none*  | Install `@material-ui/core` for Material UI. |
|           |                           | `icons` | Install `@material-ui/icons` for Material UI icons. |

## Roadmap
### Framework support
> **NOTE:** Support for packages other than those that could be enabled using flags has not been implemented yet.
- [x] Express (+ Mocha test framework option) [***In progress***]
- [ ] Vue (+ router option)
- [x] React (+ router option) [***In progress***]
- [ ] Electron
- [ ] Spring framework (with Maven or Gradle)

### Features
- [x] Switch to generic generator script; run child script or JSON file for each project type.
- [ ] Consolidate all generators into menu-based tool.
- [ ] ~~Ncurses (TUI) menu.~~
- [x] Optional project name and directory path parameters.
- [ ] Predefined package config metadata (e.g. author, license, etc).
- [ ] Flag to toggle router packages when initialising frontend projects.
- [ ] Flag or optional parameter for automatic `git` repository initialisation.