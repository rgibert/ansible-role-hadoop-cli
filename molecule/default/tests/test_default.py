import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_installed(host):
    assert host.file(
        '/usr/local/share/hadoop-cli-1.0.7.2.7/hadoop-cli-2.7/hadoopcli'
    ).exists
    assert host.file('/usr/local/bin/hadoop-cli').exists
