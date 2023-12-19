# Requirements
* [Python 3.11+](https://www.python.org/downloads/) 
* Ability to follow instructions.



# Setup - Docker
> This is recommended for better security & resource control.
### Installing Docker
[Visit Docker](https://docs.docker.com/engine/install/) and select the OS that matches best then follow the installation guide.

If you are new to Docker and want to do the quickest install possible, use [Install using the convenience script](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script).

### Launching Container
TO BE CONINUED

# Setup - Linux
> Should be supported with any OS that supports [Python 3.11+](https://www.python.org/downloads/) 

TO BE CONTINUED

# Setup - Windows
> Make sure you have [Python 3.11+](https://www.python.org/downloads/) installed.

TO BE CONTINUED

# Networking
## Production Ports
* Database
    * TCP 3555

* Website
    * TCP 80

## Development Ports
* Database
    * TCP 8081

* Website
    * TCP 8080


# Python CLI Args
> All arguments available with src/main.py.

### Managing the database.
* database ...
    * development

        Launches database using development data and changes to the development API port.
    * production
    * wipe