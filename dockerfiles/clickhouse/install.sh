export DEBIAN_FRONTEND=noninteractive

apt update
apt install -y apt-transport-https ca-certificates curl gnupg

echo 'fetching gpg'
curl -fsSL 'https://packages.clickhouse.com/rpm/lts/repodata/repomd.xml.key' | gpg --dearmor -o /usr/share/keyrings/clickhouse-keyring.gpg

ARCH=$(dpkg --print-architecture)

echo 'adding source'
echo "deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg arch=${ARCH}] https://packages.clickhouse.com/deb stable main" | tee /etc/apt/sources.list.d/clickhouse.list

apt update

apt install -y clickhouse-server clickhouse-client
