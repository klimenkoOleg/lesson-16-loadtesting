# lesson-16-loadtesting


Application uses read through cache:
![Architecture](https://github.com/klimenkoOleg/otus-cache-kuber/blob/master/OTUS%20Architect%20Course.png?raw=true)




# Установка и настройка

1. Создаем namespace для приложения:<br>
    kubectl create namespace products-namespace
    kubectl config use-context products-namespace

2. Для установки приложения через Helm chary запускаем install.sh  <br>
    *  Используйте uninstall.sh для удаления приложения из Kubernetes.

3. Создать namespace для продуктового приложения<br>
    kubectl create namespace oklimenko-loadtest<br>
    kubectl config set-context --current --namespace=oklimenko-loadtest

4. Запустиь install.sh  из корня репозитория<br>Используя Helm чарты сделает следующее:
    * создаст приложение
    * установит Redis
    * установит PostgreSQL
    * зальет тестовые данные - 100к строк
    
5. Для мониторинга - развернем Prometheus и nginx в отдельнмо namespace

    kubectl create namespace monitoring<br>
    helm install prom stable/prometheus-operator -f monitoring/prometheus.yaml -n monitoring<br>
    
    Проверить статус установки:<br>
    kubectl --namespace monitoring get pods -l "release=prom"<br>
    
    Hint: default user/password for grafana is: user: admin password: prom-operator<br>

6. Развернем Ingress<br>
    kubectl create namespace ingress<br>
    helm install ing stable/nginx-ingress -f ingress/nginx-ingress.yaml -n ingress

7. Grafana
    Запускаем графану и импортируем в нее дашборд с основными графиками:
    kubectl port-forward -n monitoring service/prom-grafana 9000:80

8. Locust
    Устанавливаем locust:

    pip install locust

9. Нагрузка и графики

    Выполняем нагрузку (запуск из корня репо):
    
    locust -f locustfile.py --headless -u 100000 -r 10 --run-time 10m --host http://arch.homework --step-load --step-users 25 --step-time 15s






# Dependencies / other projects:

Products App create using Java Spring Boot froom this repo: https://github.com/klimenkoOleg/arch-cache-products

Docker image for this App is here: https://hub.docker.com/r/oklimenko/products-cached

