get_admin_token() {
    access_token=$(curl -X POST -s \
        -d "grant_type=password"\
        -d "client_id=admin-cli" \
        -d "username=admin" \
        -d "password=admin" \
        http://localhost:8080/realms/master/protocol/openid-connect/token | jq -r .access_token)
    echo $access_token
}