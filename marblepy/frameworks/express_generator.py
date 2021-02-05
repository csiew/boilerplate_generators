import os
from generator import Generator


class ExpressGenerator(Generator):
  def __init__(self, config, properties, flags):
    Generator.__init__(self, 'express', properties, flags)
    self.config = config
    self.project_path = ''
  
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
    if os.path.exists(self.config['properties']['projects_directory']):
      try:
        os.mkdir(self.project_path)
      except:
        print("Unable to create project directory")
        exit(1)
      os.chdir(self.project_path)
      os.system("touch hello_world.txt")
      os.system("echo 'Hello world!' > hello_world.txt")
    else:
      print("Unable to find projects directory")
      exit(1)
    
    exit(0)