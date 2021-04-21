import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

# There's no need to have two test cases for a user, since the user name and
# home directory will be the same no matter what distro of linux we're using.
# But it's a neat example of how to customize tests for different distros.


def test_ansible_user(host):
    os = host.system_info.distribution

    if os == 'debian':
        user = host.user('ansible')
        assert user.exists
        assert user.home == '/home/ansible'
        assert user.group == 'ansible'

    elif os == 'redhat':
        user = host.user('ansible')
        assert user.exists
        assert user.home == '/home/ansible'
        assert user.group == 'ansible'
