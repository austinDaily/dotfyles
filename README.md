# Dotfyles - A CLI Dotfile Manager
Dotfyles is a command-line tool that scans your Home directory for your important config files (or dotfiles), creates a dedicated directory and git repo for them, and pushes this repository to your GitHub account, **all with one command**. This makes it easy to back up, restore, and share your configuration files across different systems.

## Features
- **Automatic Collection of Dotfiles**: Gathers common configuration files from your home directory.
- **GitHub Integration**: Uses GitHub’s CLI for authentication
- **Symbolic Linking**: Creates symbolic links to the original files, ensuring that your configurations stay in sync.
- **Customizable**: Extend the list of dotfiles as needed to meet your setup requirements.

## Installation

### Prerequisites
- Python3
- Git
- GitHub CLI
```bash
sudo apt install gh
gh auth login
```
```bash
sudo dnf install gh
gh auth login
```
```bash
sudo pacman -S github-cli
gh auth login
```

### Install
From your Home directory, run:
```bash
gh repo clone austinDaily/dotfyles
```

### Usage
```bash
cd ~/dotfyles
dotfyles --init
```
This command will create a git repo in your Home directory called "myDotfyles", scan your Home directory for important configuration files/dirs, copy/symlink them to the "myDotfyles" repo, stage and commit them to Git, and finally push them to your GitHub.
