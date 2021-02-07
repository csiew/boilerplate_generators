import os
import sys
import numpy
import json
from globals import *
from generator import Generator
from frameworks.express_generator import ExpressGenerator
from frameworks.react_generator import ReactGenerator


class App:
  def __init__(self):
    self.config = {}
    self.framework = ''
    self.properties = {
      'name': ''
    }
    self.flags = {}
  
  def check_dependencies(self):
    # TODO: Remove platform check when implementing support for other platforms
    if sys.platform != "linux":
      print("Support for macOS and Windows is coming soon")
      exit(1)
    
    for dep_name, dep_path in DEPENDENCIES.items():
      try:
        if not os.path.exists(dep_path[sys.platform]):
          print("Dependency not met: " + dep_name)
          exit(1)
      except:
        print("Could not determine system platform")
        exit(1)
  
  def check_config_path(self):
    if os.path.exists(CONFIG_PATH):
      with open(CONFIG_PATH, "r") as user_prefs:
        self.config = json.load(user_prefs)
        projects_directory_props = self.config['properties']['projects_directory']
        if (projects_directory_props.startswith('$HOME', 0)):
          self.config['properties']['projects_directory'] = os.getenv('HOME') + projects_directory_props[len('$HOME'):]
          print("New project directory will be generated in: " + self.config['properties']['projects_directory'])
      user_prefs.close()
    else:
      print("Config file not found at: " + CONFIG_PATH)
      exit(1)
  
  def print_usage(self):
    print("Usage: /usr/bin/python3 marble.py [framework] [project name] [...flags]")
  
  def is_valid_framework(self, framework_arg) -> bool:
    return FRAMEWORKS.__contains__(framework_arg)
  
  def process_flags(self, flag_args):
    last_flag_template = {
      'flag': '',
      'arg_count': 0
    }
    if len(flag_args) > 0:
      last_flag = {
        'flag': '',
        'arg_count': 0
      }
      for arg in flag_args:
        if (arg.startswith('--', 0)):
          # Reset flag parameter check when seeing new flag
          last_flag = last_flag_template.copy()
          self.flags[arg] = []
          # Check if flag is expecting values
          # If so, prepare to read in flag parameter values
          if (arg in FLAGS['general'] and FLAGS['general'][arg] != 0) or (arg in FLAGS['frameworks'][self.framework] and FLAGS['frameworks'][self.framework][arg] != 0):
            last_flag['flag'] = arg
            if arg in FLAGS['general'] and FLAGS['general'][arg] != 0:
              last_flag['arg_count'] = FLAGS['general'][arg]
            elif arg in FLAGS['frameworks'][self.framework] and FLAGS['frameworks'][self.framework][arg] != 0:
              last_flag['arg_count'] = FLAGS['frameworks'][self.framework][arg]
        else:
          # Append flag parameter values
          if len(last_flag['flag']) > 0 and last_flag['flag'] in self.flags:
            self.flags[last_flag['flag']].append(arg)
            # If expecting parameters, reduce parameters-to-expect count
            if last_flag['arg_count'] > 0:
              last_flag['arg_count'] -= 1
              # Stop checking for parameters for this flag when reaching 0
              if last_flag['arg_count'] == 0:
                last_flag = last_flag_template.copy()
          else:
            # Orphan parameter detected
            pass
    return
  
  def generate_config(self):
    print("Generating Marble configuration in: " + CONFIG_PATH)
    try:
      config_template = open(os.path.join(PROGRAM_PATH, 'templates', 'marble.config.json'), 'r')
      config_template_content = config_template.read()
      config_template.close()
    except:
      print("Unable to read default configuration template")
      exit(1)
    
    try:
      config_target = open(CONFIG_PATH, 'w+')
      config_target.write(config_template_content)
      config_target.close()
    except:
      print("Unable to generate configuration file")
      exit(1)
    
    print("Done")
    exit(0)

  def main(self) -> int:
    self.check_dependencies()
    self.check_config_path()
    if len(sys.argv) == 2:
      if sys.argv[1] == '--generate-config':
        if not os.path.exists(CONFIG_PATH):
          exit(self.generate_config())
        else:
          print("Existing Marble configuration exists in: " + CONFIG_PATH)
          print("Do you want to overwrite it with the default configuration file?")
          overwrite_decision = input("[y/N]: ")
          if overwrite_decision.lower().startswith('y'):
            exit(self.generate_config())
          else:
            exit(0)
      else:
        self.print_usage()
        exit(1)
    elif len(sys.argv) >= 3:
      # Get framework option
      if self.is_valid_framework(sys.argv[1]) == True:
        self.framework = sys.argv[1]
      else:
        print("Framework not supported: " + sys.argv[1])
        print("Supported frameworks:")
        for framework in FRAMEWORKS:
          print(" - " + framework)
        self.print_usage()
        exit(1)
      
      # Get project name
      if sys.argv[2].startswith('--', 0):
        print("Invalid project name: do not start with dashes")
        exit(1)
      self.properties['name'] = sys.argv[2]

      # Get project build options via flags
      flag_args = numpy.array(sys.argv[1:])
      self.process_flags(flag_args)
      if self.framework == 'express':
        exit(ExpressGenerator(self.config, self.properties, self.flags).main())
      elif self.framework == 'react':
        exit(ReactGenerator(self.config, self.properties, self.flags).main())
    else:
      self.print_usage()
      exit(1)
    exit(0)


if __name__ == '__main__':
  exit(App().main())
