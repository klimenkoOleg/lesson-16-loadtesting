# otus-cache-kuber

Application uses read through cache:
![Architecture](https://github.com/klimenkoOleg/otus-cache-kuber/blob/master/OTUS%20Architect%20Course.png?raw=true)



# Installation

1. Use any namespace, for example products-namespace:
kubectl create namespace products-namespace
kubectl config use-context products-namespace

2. Use install.sh to install application to Kubernetes (uses Helm charts)

3. Use uninstall.sh to uninstall the app from Kubernetes.


# Dependencies / other projects:

Products App create using Java Spring Boot froom this repo: https://github.com/klimenkoOleg/arch-cache-products

Docker image for this App is here: https://hub.docker.com/r/oklimenko/products-cached

