Things to do:
- [x] Add decorators on customer.py
- [x] complete `docker-compose.yaml`
- [x] complete `user_dockerfile` and `flask_dockerfile`
- [] In order to get the cron job working, the cron table on the user container needs to be updated. One
approach is to
    - Modify sample_crontable.txt to run upload.py every day at 2359hrs.[x]
    - Copy this modified file into the container. [x]
    - Use crontab on the container to load the file into the cron table. *Not sure about this*
    - You don’t have to modify the time/timezone on the containers.