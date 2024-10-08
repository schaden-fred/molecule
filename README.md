# molecule
Self-contained development and testing environment for Ansible roles and playbooks.  Creates a Centos 7 VM in Vagrant/VirtualBox.  Installs Docker and Molecule.  Pulls down your Ansible repo.  Includes example role(s) and test(s).
NOTE: This code has not been maintained since 2021, and will need to be updated in order to function with the current versions of Vagrant/Docker/Molecule

## Setup
Edit each Vagrantfile, and find the section marked "Create local clone of Ansible repo"
Edit the path(s) to your Ansible repo(s) here.  They will be cloned to the development machine when you run Vagrant.

## Running the VM
You must have VirtualBox and Vagrant installed.  Change to the vm/centos7  or cd vm/centos8 directory, depending on if you want a Centos7 or Centos8 development box.

vagrant up

## Connecting to the VM

Your public ssh key in ~/.ssh/id_rsa will be copied to the VM, and port 2200 on your computer will be forwarded to port 22 on the VM.  Use any client to ssh to 127.0.0.1 on port 2200 as user 'vagrant'

Alternately, you can use Vagrant's ssh function.  From the command line, in the vm directory:
```sh
vagrant ssh  
```

## Molecule Quickstart
Molecule provides a local environment for Ansible testing.  You can write playbooks, run them on multiple docker containers at the same time, and perform unit tests quickly.  Once you're satisfied with the results, you can commit them to your repo.

To learn more about Molecule, visit https://molecule.readthedocs.io/en/stable/getting-started.html
