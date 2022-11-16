#!/usr/bin/env bash

config_dir="$HOME/.config"

scripts_dir="$(echo $USER_SCRIPTS_DIRECTORY)"
if [ -z $scripts_dir ]; then
  echo "USER_SCRIPTS_DIRECTORY not set. Aborting."
  return 1
else
  echo "User scripts: $scripts_dir"
fi

# Alacritty
if test -L "$config_dir/alacritty"; then
  echo "alacritty symlink already exists"
else
  ln -s "$(pwd)/alacritty" "$config_dir"
  echo "alacritty symlink created"
fi

# Qtile
if test -L "$config_dir/qtile"; then
  echo "qtile symlink already exists"
else
  ln -s "$(pwd)/qtile" "$config_dir"
  echo "qtile symlink created"
fi

# Neovim
if test -L "$config_dir/nvim"; then
  echo "nvim symlink already exists"
else
  ln -s "$(pwd)/nvim" "$config_dir"
  echo "nvim symlink created"
fi

# Rofi
if test -L "$config_dir/rofi"; then
  echo "rofi symlink already exists"
else
  ln -s "$(pwd)/nvim" "$config_dir"
  echo "rofi symlink created"
fi

# Scripts
if test -L "$scripts_dir"; then
  echo "scripts symlink already exists"
else
  ln -s "$(pwd)/scripts" "$HOME/.local/share"
  echo "scripts symlink created"
fi

