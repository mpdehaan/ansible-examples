About
=====

This is a simple intro to ansible playbooks.  Read more at
http://ansible.github.com.

This is a basic example that shows how to configure a monitoring
server and all also make sure various nodes are monitored.  This is
a multi-node playbook so we'll make sure all nodes are monitorable,
then we'll execute some steps on one particular monitoring server.

To use this example, first install ansible.  Since it's a new project,
installing from git isn't a bad idea.  Follow the instructions on
ansible.github.com to do this.

When ready, read the files in this repo.

Should you wish to execute them, the syntax is simple:

  * ansible-playbook monitoring.yml

This example is more or less just illustrative, so you may wish
to make changes to adapt the configuration to your environment.
Some things like iptables and yum setup aren't included.

Upgrades to this example can be taken as github pull requests.


