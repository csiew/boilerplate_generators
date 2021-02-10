import os
import subprocess
import json
from globals import *
from generator import Generator


class ExpressGenerator(Generator):
  def __init__(self, config, properties, flags):
    Generator.__init__(self, 'express', config, properties, flags)
    self.project_path = ''
  
  def generate_index_js(self) -> bool:
    index_template_content = None

    # Read index.js template file
    try:
      index_template = open('/'.join([PROGRAM_PATH, 'templates', 'express', 'index.js']), 'r')
      index_template_content = index_template.read()
    except:
      print("Unable to read template")
      os.rmdir(self.project_path)
      return False

    # Generate index.js
    try:
      f_index = open(os.path.join(self.project_path, 'index.js'), 'w')
      f_index.write(index_template_content)
      f_index.close()
      print("[GENERATED] index.js")
    except:
      print("Unable to write index file")
      return False
    
    return True
  
  def project_init(self) -> bool:
    package_json_content = None

    # Initialise Node project
    proc_yarn_init = subprocess.Popen(["npm", "init", "-y"])
    proc_yarn_init.wait()

    # Customise project
    if os.path.exists(os.path.join(self.project_path, 'package.json')):
      # Install default packages
      pkg_install_cmd = ["npm", "install", "express"]
      for pkg_flag_key, pkg_flag_value in FRAMEWORK_PACKAGE_FLAGS['express'].items():
        if pkg_flag_key in self.flags:
          pkg_install_cmd.append(pkg_flag_value)
      proc_pkg_install = subprocess.Popen(pkg_install_cmd)
      proc_pkg_install.wait()

      # TODO: Deposit README instructions for completing setup of express-session

      # Install additional packages
      if '--install-packages' in self.flags:
        pkg_install_cmd = ["npm", "install"]
        for pkg_name in self.flags['--install-packages']:
          pkg_install_cmd.append(pkg_name)
        print(pkg_install_cmd)
        proc_pkg_install_additional = subprocess.Popen(pkg_install_cmd)
        proc_pkg_install_additional.wait()

      # Add scripts
      with open(os.path.join(self.project_path, 'package.json'), 'r') as f_package_json:
        package_json_content = json.load(f_package_json)
        package_json_content['type'] = 'module'
        if '--use-nodemon' in self.flags:
          package_json_content['scripts'] = {
            "start": "node ./index.js",
            "dev": "nodemon index.js"
          }
      f_package_json.close()

      # Write back to package.json
      with open(os.path.join(self.project_path, 'package.json'), 'w') as f_package_json:
        f_package_json.write(json.dumps(package_json_content))
      f_package_json.close()
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
    
    try:
      os.mkdir(self.project_path)
      print("[GENERATED] Project directory")
    except:
      print("Unable to create project directory")
      exit(1)
    os.chdir(self.project_path)

    if self.generate_index_js() == False:
      exit(1)
    if self.project_init() == False:
      exit(1)
    
    print("Express project template generated")
    print("Done")
    
    exit(0)
