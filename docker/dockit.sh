#!/bin/bash

date

if [ -f /home/tolga/eagle_eye.jar ]
  then
  mv  /home/tolga/eagle_eye.jar /docker/
  sleep 20
  echo dockit > /docker/dockitnow
  echo dockit starts

  else
  echo nothing to dock

fi

