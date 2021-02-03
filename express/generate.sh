#!/bin/sh

project_name=""

print_divider() {
  echo "==========================================="
}

check_project_home_dir() {
  printf "Checking if projects directory exists in home directory..."
  if [ -d $HOME/Projects ]; then
    echo " Success"
    create_project_dir
  else
    echo "Projects subdirectory does not exist! Exiting..."
    exit 1
  fi
}

create_project_dir() {
  print_divider
  while [ -z $project_name ]; do
    printf "Project name (no spaces): "
    read project_name
  done
  if [ ! -d $HOME/Projects/$project_name ]; then
    cd $HOME/Projects
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
}

build_project() {
  cd $HOME/Projects/$project_name
  if [ "$PWD" = "$HOME/Projects/$project_name" ]; then
    echo "Follow the Yarn prompts where necessary..."
    print_divider
    yarnpkg init;
    print_divider
    printf "Creating index.js..."
    touch index.js
    echo " Done"
    printf "Installing Express and Nodemon..."
    yarnpkg add express nodemon;
    echo " Done"
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
check_project_home_dir
