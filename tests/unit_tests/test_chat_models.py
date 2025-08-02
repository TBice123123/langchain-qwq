"""Test chat model integration."""

from typing import Type

from dotenv import load_dotenv
from langchain_tests.unit_tests import ChatModelUnitTests

from langchain_qwq.chat_models import ChatQwen, ChatQwQ

load_dotenv()


class TestChatQwQUnit(ChatModelUnitTests):
    @property
    def chat_model_class(self) -> Type[ChatQwQ]:
        return ChatQwQ

    @property
    def chat_model_params(self) -> dict:
        # These should be parameters used to initialize your integration for testing
        return {
            "model": "qwq-plus",
            "temperature": 0,
        }


class TestChatQwenUnit(ChatModelUnitTests):
    @property
    def chat_model_class(self) -> Type[ChatQwen]:
        return ChatQwen

    @property
    def chat_model_params(self) -> dict:
        # These should be parameters used to initialize your integration for testing
        return {
            "model": "qwen-plus-latest",
            "temperature": 0,
        }
