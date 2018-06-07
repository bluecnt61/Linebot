rsync -azL -P --delete -e "ssh -i macbookpro.pem" --exclude=development.log --exclude=.git* /Users/lyzhao/PycharmProjects/LineBot/ ubuntu@ec2-52-33-33-91.us-west-2.compute.amazonaws.com:~/LineBot
