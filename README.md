# hadoop-cli

Installs David Streever's hadoop-cli (https://github.com/dstreev/hadoop-cli)

[![Build Status](https://travis-ci.org/rgibert/ansible-role-hadoop-cli.svg?branch=master)](https://travis-ci.org/rgibert/ansible-role-hadoop-cli)
[![GitHub issues](https://img.shields.io/github/issues/rgibert/ansible-role-hadoop-cli.svg)](https://github.com/rgibert/ansible-role-hadoop-cli/issues)
[![GitHub forks](https://img.shields.io/github/forks/rgibert/ansible-role-hadoop-cli.svg)](https://github.com/rgibert/ansible-role-hadoop-cli/network)
[![GitHub stars](https://img.shields.io/github/stars/rgibert/ansible-role-hadoop-cli.svg)](https://github.com/rgibert/ansible-role-hadoop-cli/stargazers)
[![GitHub license](https://img.shields.io/github/license/rgibert/ansible-role-hadoop-cli.svg)](https://github.com/rgibert/ansible-role-hadoop-cli/blob/master/LICENSE)

## Requirements

- Hadoop cluster(s)

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| hadoop_cli_dl_checksum | sha256:bbdad2b455bf8af3e1bdc62e8e69f41dbf5b86347310d05c7ff3db34ca649bb5 | SHA256 checksum for download |
| hadoop_cli_dl_uri | https://github.com/dstreev/hadoop-cli/releases/download/{{ hadoop_cli_version }}.{{ hadoop_cli_hadoop_version }}-bin/hadoop-cli-{{ hadoop_cli_version }}-SNAPSHOT-{{ hadoop_cli_hadoop_version }}.tar.gz | URI to download the binary from |
| hadoop_cli_group | root | Group to own the install |
| hadoop_cli_hadoop_version | 2.7 | Hadoop version for the hadoop-cli |
| hadoop_cli_install_path | /usr/local/share/hadoop-cli-{{ hadoop_cli_version }}.{{ hadoop_cli_hadoop_version }} | Path to install to |
| hadoop_cli_jdk_version | 11 | JDK version to use |
| hadoop_cli_user | root | User to own the install |
| hadoop_cli_version | 1.0.7 | hadoop-cli version to use |

## Dependencies

- rgibert.openjdk_jdk

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: rgibert.hadoop_cli
```

## License

GPLv3

## Author Information

Richard Gibert
[richard@gibert.ca](mailto:richard@gibert.ca)
[https://richard.gibert.ca](https://richard.gibert.ca/)
