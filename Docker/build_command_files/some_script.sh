for file in $(find . -type f ! -name ".*"); do
    echo ""
    echo "\n=====File: $file====="
    cat $file
    echo ""
done
