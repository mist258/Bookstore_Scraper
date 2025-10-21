from src.rmq.extensions import RPCTaskConsumer
from src.rmq.spiders import TaskBaseSpider
from src.rmq.utils import TaskObserver


class TaskToSingleResultSpider(TaskBaseSpider):
    name = "single"

    def __init__(self, *args, **kwargs):
        super(TaskToSingleResultSpider, self).__init__(*args, **kwargs)
        self.processing_tasks = TaskObserver()
        self.completion_strategy = RPCTaskConsumer.CompletionStrategies.WEAK_ITEMS_BASED
