
if [ -f /docker/dockitnow ]
then
  cd /docker

#This section is not needed for this server.
##  scp /docker/eagle_eye.jar docker@172.31.16.14:/docker/
##  scp /docker/eagle_eye.jar docker@172.31.16.13:/docker/
##  scp /docker/dockitnow docker@172.31.16.13:/docker/
##  scp /docker/dockitnow docker@172.31.16.14:/docker/
  rm /docker/dockitnow



  docker build -t bmccord/eagle_eye .

  #----Uncomment to save image to tar file
#  docker save bmccord/eagle_eye > eagle_eye_docker.tar
   sleep 60


  /bin/docker stop $(docker ps | grep -v CONTAINER | awk '{print $1}' )
  /bin/docker rm $(docker ps -a -q)
  /bin/docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
  /bin/docker run -d -h `hostname` -p 8080:8080 bmccord/eagle_eye


##maybe later echo "Jar file updated"  | /bin/mail -s "Docker File Updated due to jar file update" tozaltin@etcc.com,bmccord@etcc.com,gmayfield@etcc.com,nkim@etcc.com,bjestis@etcc.com,dching@etcc.com,amoseley@etcc.com,bice@etcc.com,jmccord@etcc.com
echo "This is the email alert for CNN Test Environment docker image refresh!
Please, go to http://ec2-52-73-180-0.compute-1.amazonaws.com:8080 to verify/QA changes" | /bin/mail -s "CNN Test Environment Docker Image Changed!" tozaltin@etcc.com,dagonzalez@etcc.com
else
echo no new jar file yet


fi


