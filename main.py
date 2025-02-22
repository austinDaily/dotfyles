import argparse
import os
import shutil
import subprocess

# Create the CLI argument parser 
parser = argparse.ArgumentParser(description='Initialize the project')
parser.add_argument('--init', action='store_true', help='Initialize the project')
args = parser.parse_args()


# If the --init flag is passed, run the initialization code
if args.init:
    print('Creating the "myDotfyles" directory...')

    # Create the "myDotfyles" directory in users Home directory
    os.makedirs(os.path.expanduser('~/myDotfyles'), exist_ok=True)
    print('Done!')

    # Intitialize the git repository in the "myDotfyles" directory
    print('Initializing the git repository...')
    os.system('cd ~/myDotfyles && git init > /dev/null 2>&1')
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
    #print('Checking if config files exist...')
    #for config in configs:
    #    if os.path.exists(os.path.expanduser(f'~/{config}')):
    #        print(f'Found {config}')
    #    else:
    #        print(f'{config} not found')
    #print('Done!')


    # For the configs that were found, copy (for files) or symlink (for directories) them to the "myDotfyles" dir
    print('Copying/symlinking the config files...')
    for config in configs:
        if os.path.exists(os.path.expanduser(f'~/{config}')):
            if os.path.isfile(os.path.expanduser(f'~/{config}')):
                os.system(f'cp ~/{config} ~/myDotfyles/')
            else:
                os.system(f'ln -s ~/{config} ~/myDotfyles/')
    print('Done!')

    
    # Add/stage the copied/symlinked files to the git repository
    print('Staging the config files to the git repo...')
    os.system('cd ~/myDotfyles && git add . > /dev/null 2>&1')
    print('Done!')

    # Commit the staged files
    print('Committing the config files...')
    os.system('cd ~/myDotfyles && git commit -m "Initial commit" > /dev/null 2>&1')
    print('Done!')

    # Make sure the GH CLI is installed and the user is logged in.
    # If not, prompt the user to install the GH CLI and log in.
    # If the GH CLI is installed and the user is logged in, create a new repo called "myDotfyles"
    # and push the local repo to the remote repo
    print('Checking if the GH CLI is installed...')
    gh_installed = shutil.which('gh')
    if gh_installed:
        print('GH CLI is installed!')
        print('Checking if the user is logged in...')
        gh_login = subprocess.run(['gh', 'auth', 'status'], stdout=subprocess.PIPE)
        if 'Logged in to github.com' in gh_login.stdout.decode('utf-8'):
            print('User is logged in!')
            print('Creating the remote repo...')
            os.system('cd ~/myDotfyles && gh repo create myDotfyles --public > /dev/null 2>&1')
            print('Done!')
            print('Pushing the local repo to the remote repo...')
            os.system('cd ~/myDotfyles && git push origin master > /dev/null 2>&1')
            print('Done!')
        else:
            print('User is not logged in. Please run "gh auth login" to log in.')
    else:
        print('GH CLI is not installed. Please install it from https://cli.github.com/')
    

    



