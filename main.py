import argparse
import os

# Create the CLI argument parser 
parser = argparse.ArgumentParser(description='Initialize the project')
parser.add_argument('--init', action='store_true', help='Initialize the project')
args = parser.parse_args()


# If the --init flag is passed, run the initialization code
if args.init:
    print('Creating the "dotfyles" directory...')

    # Create the "dotfyles" directory in users Home directory
    os.makedirs(os.path.expanduser('~/dotfyles'), exist_ok=True)
    print('Done!')

    # Intitialize the git repository in the "dotfyles" directory
    print('Initializing the git repository...')
    os.system('cd ~/dotfyles && git init > /dev/null 2>&1')
    print('Done!')

    # List of config files and/or directories the program should search for
    configs = [
         ".bashrc", 
	     ".bash_profile", 
	     ".zshrc", 
         ".profile", 
         ".fish/config.fish", 
         ".config/fish/", 
         ".vimrc", 
         ".config/nvim/", 
         ".emacs.d/init.el", 
         ".config/helix/", 
         ".tmux.conf", 
         ".zellij/", 
         ".config/wezterm/", 
         ".wezterm.lua", 
         ".config/alacritty/", 
         ".alacritty.yml", 
         ".config/kitty/", 
         ".config/starship.toml", 
         ".config/i3/", 
         ".config/sway/", 
         ".config/hypr/", 
         ".config/xfce4/", 
         ".gitconfig", 
         ".gitignore_global", 
         ".config/ranger/", 
         ".config/picom.conf", 
         ".config/dunst/", 
         ".config/rofi", 
         ".config/swaylock", 
         ".ssh/config/", 
         ".config/gtk-3.0/", 
        ]
    
    # Check if the configs exist in the users Home directory
    print('Checking if config files exist...')
    for config in configs:
        if os.path.exists(os.path.expanduser(f'~/{config}')):
            print(f'Found {config}')
        else:
            print(f'{config} not found')
    print('Done!')


    # For the configs that were found, copy (for files) or symlink (for directories) them to the "dotfyles" dir
    print('Copying/symlinking the config files...')
    for config in configs:
        if os.path.exists(os.path.expanduser(f'~/{config}')):
            if os.path.isfile(os.path.expanduser(f'~/{config}')):
                os.system(f'cp ~/{config} ~/dotfyles/')
            else:
                os.system(f'ln -s ~/{config} ~/dotfyles/')
    print('Done!')

    
    # Add/stage the copied/symlinked files to the git repository
    print('Staging the config files to the git repo...')
    os.system('cd ~/dotfyles && git add . > /dev/null 2>&1')
    print('Done!')

    # Commit the staged files
    print('Committing the config files...')
    os.system('cd ~/dotfyles && git commit -m "Initial commit" > /dev/null 2>&1')
    print('Done!')
