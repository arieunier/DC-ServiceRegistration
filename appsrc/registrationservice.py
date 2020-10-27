import ujson
from libs import logs, queuer, rabbitmq_utils, config, rediscache, sfapi, postgres, utils
LOGGER = logs.LOGGER

SERVICE_NAME='registrationservice'


def treatMessage(dictValue):
    LOGGER.info(dictValue)
    if (dictValue['PublishExternally'] == True):
        postgres.insertServiceDefinition(dictValue)
    LOGGER.info(" [x] Finished id=%r" % (dictValue))

# create a function which is called on incoming messages
def genericCallback(ch, method, properties, body):
    try:
        treatMessage(ujson.loads(body))
    except Exception as e:
        import traceback
        traceback.print_exc()
        LOGGER.error(e.__str__())


if __name__ == "__main__":
    queuer.initQueuer()
    queuer.listenToTopic(config.SUBSCRIBE_CHANNEL, 
    {
        config.QUEUING_KAFKA : treatMessage,
        config.QUEUING_CLOUDAMQP : genericCallback,
    })

