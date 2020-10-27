APPNAME=$1
export PYTHONPATH=.:./libs/:./appsrc/:./pyutils
# logs
export LOG_LEVEL=DEBUG

export CLOUDAMQP_APIKEY=`heroku config:get CLOUDAMQP_APIKEY  --app $APPNAME`
export CLOUDAMQP_URL=`heroku config:get CLOUDAMQP_URL  --app $APPNAME`

export DATABASE_URL=`heroku config:get DATABASE_URL  --app $APPNAME`
