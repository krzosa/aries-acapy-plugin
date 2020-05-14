from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from marshmallow import fields
from ..message_types import QUERY, PROTOCOL_PACKAGE

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.query_handler.QueryHandler"


class Query(AgentMessage):
    class Meta:
        handler_class = HANDLER_CLASS
        message_type = QUERY
        schema_class = "QuerySchema"

    def __init__(self, *, query: str = None, comment: str = None, **kwargs):
        super(Query, self).__init__(**kwargs)
        self.query = query
        self.comment = comment


class QuerySchema(AgentMessageSchema):
    class Meta:
        model_class = Query

    query = fields.Str(required=False)
    comment = fields.Str(required=False)
