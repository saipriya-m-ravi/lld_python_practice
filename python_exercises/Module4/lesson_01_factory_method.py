"""
Lesson 4.1 - Factory Method

Step 1: Add a third notifier type, PushSender.
Step 2: Implement create_notifier() as the OCP-friendly REGISTRY version
        (a dict mapping channel -> class), not an if/elif chain.
Step 3: Prove OCP holds -- add a fourth channel, "slack", by only
        adding a class + one registry entry, touching nothing else.
"""

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str):
        ...


class EmailSender(NotificationSender):
    def send(self, message: str):
        print(f"[EMAIL] {message}")


class SMSSender(NotificationSender):
    def send(self, message: str):
        print(f"[SMS] {message}")


# TODO: PushSender(NotificationSender) -- prints f"[PUSH] {message}"
class PushSender(NotificationSender):
    def send(self, message: str):
        print(f"[PUSH] {message}")

class SlackSender(NotificationSender):
    def send(self, message: str):
        print(f"[SLACK] {message}")
# ------------------------------------------------------------------
# TODO: create_notifier() -- registry-based factory
#
# 1. Define _NOTIFIER_REGISTRY: dict[str, type[NotificationSender]]
#    mapping "email" -> EmailSender, "sms" -> SMSSender, "push" -> PushSender
# 2. def create_notifier(channel: str) -> NotificationSender:
#    - if channel not in the registry, raise ValueError(f"Unknown channel: {channel}")
#    - otherwise return _NOTIFIER_REGISTRY[channel]() (note the () -- you're
#      instantiating the class, not returning the class itself)
_NOTIFIER_REGISTRY : dict[str, type[NotificationSender]] = {
    "email" : EmailSender,
    "sms": SMSSender,
    "push": PushSender,
    "slack": SlackSender
}
def create_notifier(channel: str) -> NotificationSender:
    if channel not in _NOTIFIER_REGISTRY:
        raise ValueError(f"Unknown channel: {channel}")
    return _NOTIFIER_REGISTRY[channel]()
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# TODO: prove OCP -- add a SlackSender(NotificationSender) here
# (prints f"[SLACK] {message}"), and register it as "slack" in
# _NOTIFIER_REGISTRY. create_notifier's own code should need ZERO changes.
# ------------------------------------------------------------------


if __name__ == "__main__":
    for channel in ["email", "sms", "push", "slack"]:
        notifier = create_notifier(channel)
        notifier.send(f"hello via {channel}")

    # TODO: also try create_notifier("carrier_pigeon") in a try/except,
    #       confirm you get a clear ValueError
    try:
        notifier = create_notifier("carrier_pigeon")
    except ValueError as e:
        print(e)
    
