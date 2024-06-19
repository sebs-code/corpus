# Docker Cheat Sheet

****

**docker system prune [OPTIONS]**

Remove all unused containers, networks, images (both dangling and unused), and optionally, volumes.


    -a, --all		Remove all unused images not just dangling ones
    
    --filter Provide filter values (e.g. label=<key>=<value>)
    
    -f, --force		Do not prompt for confirmation
    
    --volumes		Prune anonymous volumes

****

**docker-compose down [OPTIONS]**


    --rmi type              Remove images. Type must be one of:
                              'all': Remove all images used by any service.
                              'local': Remove only images that don't have a
                              custom tag set by the `image` field.
    -v, --volumes           Remove named volumes declared in the `volumes`
                            section of the Compose file and anonymous volumes
                            attached to containers.
    --remove-orphans        Remove containers for services not defined in the
                            Compose file
    -t, --timeout TIMEOUT   Specify a shutdown timeout in seconds.
                            (default: 10)

****

