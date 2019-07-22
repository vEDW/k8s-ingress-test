
docker build -t pong:0.1 .
docker tag pong:0.1 harbor.corp.local/ingress-test/pong:0.1
docker push harbor.corp.local/ingress-test/pong:0.1
