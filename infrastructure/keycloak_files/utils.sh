get_admin_token() {
    echo $(curl -X POST -s \
        -d "grant_type=password"\
        -d "client_id=admin-cli" \
        -d "username=admin" \
        -d "password=admin" \
        http://localhost:8080/realms/master/protocol/openid-connect/token)
}

get_admin_user() {
    # Get the information of admin user
    # you can optionally pass the access token
    # otherwise the new session will be created
    local access_token=${1:-$(get_admin_token | jq -r .access_token)}
    echo $(
        curl -X GET -s \
            -H "authorization: Bearer $access_token" \
            http://localhost:8080/admin/realms/master/users?username=admin | jq .[0]
    )
}