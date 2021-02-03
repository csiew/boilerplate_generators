#!/bin/sh

project_name=""

print_divider() {
  echo "==========================================="
}

create_project_dir() {
  echo "Node/Express boilerplate generator"
  print_divider
  while [ -z $project_name ]; do
    echo "Project name (no spaces):"
    read project_name
  done
  if [ -d ~/Projects ]; then
    if [ ! -d $HOME/Projects/$project_name ]; then
      cd ~/Projects
      mkdir $project_name
      if [ -d $project_name ]; then
        echo "Created directory: $project_target_dir"
        build_project
      else
        echo "Failed to create project directory! Exiting..."
        exit 1
      fi
    else
      echo "Project directory already exists! Exiting..."
      exit 1
    fi
  else
    if [ -d ~/Projects ]; then
      echo "Projects sub-directory exists in home directory"
    fi
  fi
}

build_project() {
  cd $HOME/Projects/$project_name
  if [ "$PWD" = "$HOME/Projects/$project_name" ]; then
    echo "Follow the Yarn prompts where necessary..."
    print_divider
    yarnpkg init;
    print_divider
    echo "Creating index.js...\n"
    touch index.js
    echo "\tDone"
    echo "Installing Express and Nodemon...\n"
    yarnpkg add express nodemon;
    echo "\tDone"
    if [ -e $HOME/Projects/$project_name/package.json ]; then
      package_json_pointer=$HOME/Projects/$project_name/package.json
      updated_package_json=`jq '. += {"type": "module", "scripts": {"start": "node ./index.js", "dev": "nodemon index.js"}}' $HOME/Projects/$project_name/package.json`
      echo "$updated_package_json" > "$package_json_pointer"
      print_divider
      echo "Project generation complete!"
      print_divider
      exit 0
    else
      echo "Cannot find package.json file! Exiting..."
      exit 1
    fi
  else
    echo "Cannot navigate to project directory! Exiting..."
    exit 1
  fi
}

if [ ! -e /usr/bin/yarnpkg ]; then
  echo "Yarn not installed! Exiting..."
  exit 1
fi
if [ ! -e /usr/bin/jq ]; then
  echo "jq not installed! Exiting..."
  exit 1
fi
create_project_dir
