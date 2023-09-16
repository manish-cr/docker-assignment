Things to do:
- [x] Add decorators on customer.py
- [] complete `docker-compose.yaml`
- [] complete `user_dockerfile`
- [] In order to get the cron job working, the cron table on the user container needs to be updated. One
approach is to
    - Modify sample_crontable.txt to run upload.py every day at 2359hrs.
    - Copy this modified file into the container.
    - Use crontab on the container to load the file into the cron table.
    - You don’t have to modify the time/timezone on the containers.`