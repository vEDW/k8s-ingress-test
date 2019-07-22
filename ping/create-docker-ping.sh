
docker build -t ping:0.1 .
docker tag ping:0.1 harbor.corp.local/ingress-test/ping:0.1
docker push harbor.corp.local/ingress-test/ping:0.1