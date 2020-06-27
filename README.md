# lesson-16-loadtesting


Application uses read through cache:
![Architecture](https://github.com/klimenkoOleg/otus-cache-kuber/blob/master/OTUS%20Architect%20Course.png?raw=true)




# Installation

1. Use any namespace, for example products-namespace:
kubectl create namespace products-namespace
kubectl config use-context products-namespace

2. Use install.sh to install application to Kubernetes (uses Helm charts)

3. Use uninstall.sh to uninstall the app from Kubernetes.

# Load testing

1. Создать namespace для продуктового приложения
kubectl create namespace oklimenko-loadtest
kubectl config set-context --current --namespace=oklimenko-loadtest

2. Запустиь install.sh  из корня репозитория
Используя Helm чарты сделает следующее:
* создаст приложение
* установит Redis
* установит PostgreSQL
* зальет тестовые данные - 100к строк

3. Для мониторинга - развернем Prometheus и nginx в отдельнмо namespace

kubectl create namespace oklimenko-monitoring
helm install prom stable/prometheus-operator -f monitoring/prometheus.yaml -n oklimenko-monitoring

kubectl create namespace oklimenko-ingress
helm install ing stable/nginx-ingress -f ingress/nginx-ingress.yaml -n ingress

4. Grafana

Запускаем графану и импортируем в нее дашборд с основными графиками

kubectl port-forward -n monitoring service/prom-grafana 9000:80


5. locust

Устанавливаем locust

pip install locust


6. Нагрузка и графики

locust -f locustfile.py --headless -u 100000 -r 10 --run-time 10m --host http://arch.homework --step-load --step-users 25 --step-time 15s






# Dependencies / other projects:

Products App create using Java Spring Boot froom this repo: https://github.com/klimenkoOleg/arch-cache-products

Docker image for this App is here: https://hub.docker.com/r/oklimenko/products-cached

