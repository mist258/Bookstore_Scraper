from src.rmq.extensions import RPCTaskConsumer
from src.rmq.spiders import TaskBaseSpider
from src.rmq.utils import TaskObserver


class TaskToMultipleResultsSpider(TaskBaseSpider):
    name = "multiple"

    def __init__(self, *args, **kwargs):
        super(TaskToMultipleResultsSpider, self).__init__(*args, **kwargs)
        self.processing_tasks = TaskObserver()
        self.completion_strategy = RPCTaskConsumer.CompletionStrategies.REQUESTS_BASED
