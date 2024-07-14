# Running gitlab

Here is my experience in running gitlab server for tests to try it locally.

Use following command to run gitlab localy in docker.

```bash
docker run 
    --detach 
    --hostname gitlab.example.com
    --publish 443:443 --publish 80:80 --publish 22:22
    --name gitlab   
    --restart always   
    gitlab/gitlab-ce:latest
```

For some reasons previous command usully don't allow to turn gitlab up you need to run.

```bash
docker exec -it gitlab update-permissions
docker restart gitlab
```

Then you need to configre root user - you'll be able to enter your gitlab.

```bash
docker exec -it gitlab gitlab-rails console
```

After waiting for some time enter following script:

```ruby
user = User.find_by(username: 'root')
user.password = 'turbo_super'
user.password_confirmation = 'turbo_super'
user.save!
exit
```

So now you can access your git lab using credentials user - `root`, password - `turbo_super`.