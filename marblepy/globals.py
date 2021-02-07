import os


PROGRAM_PATH = '/'.join([os.getcwd(), 'marblepy'])

DEPENDENCIES = {
  'jq': {
    'linux': '/usr/bin/jq'
  },
  'yarn': {
    'linux': '/usr/bin/yarnpkg'
  }
}

CONFIG_PATH = os.getenv('HOME') + '/.config/marble.config.json'
FRAMEWORKS = ['express', 'react']

'''
Flag code:
-1  Expecting indefinite number of values
0   Not expecting value
>0  Expecting fixed number of values
'''
FLAGS = {
  'general': {
    '--ping': 0,    # Test flag that skips directory generation
    '--debug': 0,
    '--install-packages': -1
  },
  'frameworks': {
    'express': {
      '--use-nodemon': 0,
      '--use-express-session': 0
    },
    'react': {
      '--use-react-router-dom': 0,
      '--use-material-ui': 1
    }
  }
}

FRAMEWORK_PACKAGE_FLAGS = {
  'express': {
    '--use-nodemon': 'nodemon',
    '--use-express-session': 'express-session'
  },
  'react': {
    '--use-router': 'react-router-dom',
    '--use-material-ui': '@material-ui/core'
  }
}
