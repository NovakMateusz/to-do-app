# Token manager

### Generating SSL certificates
```shell script
mkdir certs
cd certs
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```