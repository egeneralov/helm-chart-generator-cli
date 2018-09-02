# Helm Chart Generator

Command-line client and python library for [Helm Chart Generator API](https://github.com/egeneralov/helm-chart-generator-api).

## QuickStart

  docker run -d --name hcg --rm -p 8080:8080 egeneralov/helm-chart-generator
  pip3 install git+https://github.com/egeneralov/helm-chart-generator-cli
  # print url to get chart
  hcg --endpoint 127.0.0.1:8080 --host app.domain.com --port 8080 --version 3.2.1 --image user/app --tag 3.2.1
  # or save to current directory
  hcg --endpoint 127.0.0.1:8080 --host app.domain.com --port 8080 --version 3.2.1 --image user/app --tag 3.2.1 --save

## Options

- endpoint: running egeneralov/helm-chart-generator
- host: ingress host
- port: your application port
- version: like 0.0.0
- image: registry.domain.com/path/to/image
- tag: latest
- save: save chart to current directory
