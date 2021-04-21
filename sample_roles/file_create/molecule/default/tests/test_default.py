import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ansible_file(host):
    f = host.file('/tmp/Ansible/AnsibleWasHere.txt')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
