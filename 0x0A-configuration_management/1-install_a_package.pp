#!/usr/bin/pup
# Install a specific version of flask (2.1.0) from pip3
package {'flask':
	ensure	=> '2.1.0',
	provide	=> 'pip3'
}

