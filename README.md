# Helm Chart Generator

Command-line client and python library for [Helm Chart Generator API](https://github.com/egeneralov/helm-chart-generator-api).

## QuickStart

    docker run -d --name hcg --rm -p 8080:8080 egeneralov/helm-chart-generator
    pip3 install git+https://github.com/egeneralov/helm-chart-generator-cli
    echo 'print url to get chart'
    hcg --endpoint 127.0.0.1:8080 --host app.domain.com --port 8080 --version 3.2.1 --image user/app --tag 3.2.1
    echo 'or save to current directory'
    hcg --endpoint 127.0.0.1:8080 --host app.domain.com --port 8080 --version 3.2.1 --image user/app --tag 3.2.1 --save

## Options

- endpoint: running egeneralov/helm-chart-generator
- host: ingress host
- port: your application port
- version: like 0.0.0
- image: registry.domain.com/path/to/image
- tag: latest
- save: save chart to current directory

## Python-way

    from hcg import helmGeneratorClient
    chart = helmGeneratorClient(
      endpoint = 'http://178.128.193.32:1234',
      host = 'my.app.domain.com',
      version = '1.2.3',
      image = 'registry.domain.com/group/project',
      imageTag = 'latest',
      port = 8080
    )
    chart.filename == 'my.app.domain.com-1.2.3.tgz'
    chart.download()
    tgz = chart.archive
