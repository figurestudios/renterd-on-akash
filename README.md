# renterd on Akash

## Testing

We will be using the GUI example from [renterd_gui.yml](https://github.com/figurestudios/renterd-on-akash/blob/main/renterd_gui.yml) to give us a web interface for easy testing of Sia's renterd software on Akash.

On the left side off the screen close to the bottom, you can click on the wallet icon and then press "Receive" to get your address. Using this address, you can request funds from the [testnet](https://zen.sia.tech/faucet) to be able to form contracts and pay for storage.

Like [this workshop](https://github.com/SiaFoundation/renterd/wiki/Workshop#configuration) shows, configuration can be done using API requests but depending on how it is done it may need to be done differently. Over the internet will require you to use the full URI instead of localhost, along with the external port which random unless you are using IP leases. From another service would require you to instead of using http*:9880*, you would have to specify service_name:9880*. From the same service, their example should work.

We can now press the plane icon to go to "Autopilot" and for each field either enter the recommended values or write a fitting number (e.g., 1 TiB for the estimates). For testing purposes, you can go to "Configuration" and change the both the Min shards and Total shards to 1, meaning that you will only need one contract formed to store files. For production use 10/30 can be recommended.

Now, as soon as you have contracts formed, you can upload/download files manually or with API, along with the other functionality in renterd.

## Examples

## API Usage

### Uploading

Change `yourpassword`, URI, port, and foo.txt from this command:
```
curl -u :yourpassword -H "Content-Type: application/octet-stream" -X PUT http://URI:port/api/worker/objects/foo.txt --data-binary '@foo.txt'
```

### Downloading

Change `yourpassword`, URI, port, and foo.txt from this command:
```
curl -u :yourpassword http://URI:port/api/worker/objects/foo.txt
```

### More

A good place to start is [api.sia.tech](https://api.sia.tech/renterd).

## Building and pushing your own Docker Image on testnet

```
git clone https://github.com/SiaFoundation/renterd
cd renterd
docker build -t username/renterd:latest -f docker/Dockerfile.testnet .
docker push username/renterd:latest
```

##  Backing up and restoring

Connect using Shell and run these commands to extract your `db.sqlite` file to a FTP server:
```
apt-get update
apt-get install ftp
ftp FTP_SERVER -P 21
put /data/db/db.sqlite database
```

With a variation of API requests, you can also extract information piece by piece if the Shell stops working:

Change `yourpassword`, URI, and port from these commands:
```
curl -u :yourpassword http://URI:port/api/bus/contracts/active --output hostdb.db

curl -u :yourpassword http://URI:port/api/bus/objects/ | jq -r '.entries[] | .name' | while read name; do curl -u :yourpassword "http://URI:port/api/bus/objects$name" --output "$name"; done
```

Restoring has not yet been attempted, but both FTP and wget can be used with Shell and in the worst case scenario, the image can be re-deployed.
