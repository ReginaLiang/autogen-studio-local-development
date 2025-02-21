import boto3
from boto3.dynamodb.conditions import Key
from typing import Dict, List, Optional

class DynamoDBManager:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
        self.agent_weave_table = self.dynamodb.Table('AgentWeave-test-Global')

    def get_agent(self, user_id: str, agent_id: str) -> Optional[Dict]:
        response = self.agent_weave_table.get_item(
            Key={'user_id': user_id, 'agent_id': agent_id}
        )
        return response.get('Item')

    def list_agents(self, user_id: str) -> List[Dict]:
        response = self.agent_weave_table.query(
            IndexName="GIdxS1",  # Specify the GSI name
            KeyConditionExpression=Key('GIdxS1').eq(f"autogen#agent#{user_id}")  # Query by GIdxS1
        )
        return response.get('Items', [])

    def create_agent(self, agent_data: Dict) -> bool:
        self.agent_weave_table.put_item(Item=agent_data)
        return True

    def delete_agent(self, user_id: str, agent_id: str) -> bool:
        self.agent_weave_table.delete_item(
            Key={'user_id': user_id, 'agent_id': agent_id}
        )
        return True

    def link_model(self, agent_id: str, model_id: str) -> bool:
        self.agent_weave_table.put_item(
            Item={'agent_id': agent_id, 'model_id': model_id}
        )
        return True