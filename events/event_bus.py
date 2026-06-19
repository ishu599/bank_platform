from collections import defaultdict


class EventBus:

    def __init__(self):

        self.subscribers = defaultdict(list)

    def subscribe(

        self,

        event_name,

        callback

    ):

        self.subscribers[

            event_name

        ].append(

            callback

        )

    def publish(

        self,

        event_name,

        data

    ):

        callbacks = self.subscribers[

            event_name

        ]

        for callback in callbacks:

            callback(data)
