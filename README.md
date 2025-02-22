# Dotfyles - A CLI Dotfile Manager
Dotfyles is a command-line tool that scans your Home directory for your important config files (or dotfiles), creates a dedicated directory and git repo for them, and pushes this repository to your GitHub account, **all with one command**. This makes it easy to back up, restore, and share your configuration files across different systems.

## Features
- **Automatic Collection of Dotfiles**: Gathers common configuration files from your home directory.
- **GitHub Integration**: Uses GitHub’s Device Flow for authentication and pushes the collected dotfiles to your GitHub repository.
- **Symbolic Linking**: Creates symbolic links to the original files, ensuring that your configurations stay in sync.
- **Customizable**: Extend the list of dotfiles as needed to meet your setup requirements.

## Installation

### Prerequisites
- Python3
- Git
- A GitHub account.
- Make sure your GitHub account does not already contain a repo called "myDotfyles", as this program will overwrite it.

### Usage
```bash
dotfyles init
```
This command will create a git repo in your Home directory called "myDotfyles", scan your Home directory for important configuration files/dirs, copy/symlink them to the "myDotfyles" repo, stage and commit them to Git, and finally push them to your GitHub.
