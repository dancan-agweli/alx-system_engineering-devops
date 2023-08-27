# Define a class to configure SSH client
class ssh_client_config {

  # Ensure the SSH client configuration file exists
  file { '/etc/ssh/ssh_config':
    ensure => present,
  }

  # Configure SSH client to use the private key ~/.ssh/school
  file_line { 'Set Identity File':
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school',
    match  => '^#?\s*IdentityFile',
    after  => '^#?\s*Host \*',
    notify => Service['ssh'],
  }

  # Configure SSH client to refuse password authentication
  file_line { 'Disable Password Authentication':
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
    match  => '^#?\s*PasswordAuthentication',
    after  => '^#?\s*Host \*',
    notify => Service['ssh'],
  }
}

# Apply the SSH client configuration class
include ssh_client_config

