import os
import subprocess
import json
from globals import *
from generator import Generator


class ReactGenerator(Generator):
  def __init__(self, config, properties, flags):
    Generator.__init__(self, 'react', config, properties, flags)
    self.project_path = ''
  
  def project_init(self) -> bool:
    if os.path.exists(self.project_path):
      print("Project directory already exists")
      return False
    os.chdir(self.config['properties']['projects_directory'])

    # Initialise Node project
    proc_npx_init = subprocess.Popen(["npx", "create-react-app", self.properties['name']])
    proc_npx_init.wait()

    # Validate project exists
    # Change directory to project directory
    if not os.path.exists(self.project_path):
      print("Project not generated")
      return False
    os.chdir(self.project_path)

    # Customise project
    if os.path.exists(os.path.join(self.project_path, 'package.json')):
      # Install default packages
      pkg_install_cmd = ["yarnpkg", "add"]
      for pkg_flag_key, pkg_flag_value in FRAMEWORK_PACKAGE_FLAGS['react'].items():
        if pkg_flag_key in self.flags:
          pkg_install_cmd.append(pkg_flag_value)
          if pkg_flag_key == '--use-material-ui' and pkg_flag_value == 'icons':
            pkg_install_cmd.append('@material-ui/icons')
      if len(pkg_install_cmd) > 2:
        proc_pkg_install = subprocess.Popen(pkg_install_cmd)
        proc_pkg_install.wait()

      # Install additional packages
      if '--install-packages' in self.flags:
        pkg_install_cmd = ["yarnpkg", "add"]
        for pkg_name in self.flags['--install-packages']:
          pkg_install_cmd.append(pkg_name)
        print(pkg_install_cmd)
        proc_pkg_install_additional = subprocess.Popen(pkg_install_cmd)
        proc_pkg_install_additional.wait()

      # TODO: Replace App.js with template that uses router components
      # os.chdir(os.path.join(self.project_path, 'src'))
    else:
      print("Unable to find package.json")
      return False
    return True
  
  def main(self) -> int:
    if '--ping' in self.flags:
      print("Debug mode exits before project directory creation")
      exit(0)

    # Validate project properties
    if len(self.properties['name']) == 0:
      print("Project name is empty")
      exit(1)
    try:
      self.project_path = self.config['properties']['projects_directory'] + '/' + self.properties['name']
      if os.path.exists(self.project_path):
        print("Project directory already exists")
        exit(1)
    except:
      print("Project configuration or properties unreadable")
      exit(1)

    # Build project
    if not os.path.exists(self.config['properties']['projects_directory']):
      print("Unable to find projects directory")
      exit(1)

    if self.project_init() == False:
      exit(1)
    
    print("Express project template generated")
    print("Done")
    
    exit(0)
