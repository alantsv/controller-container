Controladores Embutidos Containers
==================================

## Controlador

### Floodlight

[Floodlight Web Site](http://www.projectfloodlight.org/floodlight/)

## Conteiners

### LXC

[LXC Web Site](https://linuxcontainers.org/lxc/introduction/)

### Docker

[Docker Web Site](https://www.docker.com/)

### LXD

[LXD Web Site](https://linuxcontainers.org/lxd/introduction/)

### OpenVZ

[OpenVZ Wiki](https://openvz.org/Main_Page)

### lmctfy

[lmctfy Repositório no Github](https://github.com/google/lmctfy)

## Objetivo

## Como funciona?

Docker:
``` bash
  sudo docker run -p 8080:8080 -p 6653:6653 floodlight-docker --cpus=2
```
Topologia:
``` bash
  sudo mn --custom controller-container/topo-Nsw-2host.py --topo lineartopo --controller=remote,ip=<ip-container>,port=6653
```
